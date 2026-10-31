import streamlit as st

from cjlib.db import simpan_ujian
from cjlib.styles import esc, footer, page_header
from cjlib.ui import peserta_sidebar, require_peserta_gate, subjudul
from questions import EXAM_PACKAGES

training, peserta = require_peserta_gate("📋 Ujian")
peserta_sidebar("ujian")

page_header("📋 Ujian Sertifikasi", subjudul(training, peserta))

# ---------------- Pilih paket ----------------
pkg_keys = list(EXAM_PACKAGES.keys())
default_pkg = training.get("sertifikasi") if training.get("sertifikasi") in EXAM_PACKAGES else pkg_keys[0]
if "exam_result" not in st.session_state and "exam_retry" not in st.session_state:
    pkg_key = st.selectbox("Pilih Paket Ujian", pkg_keys, index=pkg_keys.index(default_pkg),
                           format_func=lambda k: EXAM_PACKAGES[k]["title"], key="exam_pkg")
else:
    pkg_key = (st.session_state.get("exam_result") or st.session_state.get("exam_retry"))["pkg"]
pkg = EXAM_PACKAGES[pkg_key]
SOAL = pkg["questions"]
N = len(SOAL)
LULUS = pkg["passing"]
SESI = pkg["sessions"]


def _opsi(q):
    return [f"{chr(65 + i)}. {o}" for i, o in enumerate(q["opts"])]


def _render_soal(daftar, prefix):
    """Semua soal dikelompokkan per sesi, tampil terbuka (tanpa expander)."""
    per_sesi = {}
    for q in daftar:
        per_sesi.setdefault(int(q["session"]), []).append(q)
    for s in sorted(per_sesi):
        qs = per_sesi[s]
        with st.container(border=True, key=f"card_{prefix}_sesi_{s}"):
            st.subheader(SESI.get(str(s), f"Sesi {s}"))
            for q in qs:
                st.radio(f"**{q['n']}.** {q['q']}", _opsi(q), key=f"{prefix}_{pkg_key}_{q['n']}", index=None)


def _kumpulkan(daftar, prefix):
    jawaban = {}
    for q in daftar:
        v = st.session_state.get(f"{prefix}_{pkg_key}_{q['n']}")
        if v is not None:
            jawaban[q["n"]] = ord(v[0]) - 65
    return jawaban


def _simpan(benar):
    nilai = round(benar / N * 100)
    lulus = nilai >= LULUS
    try:
        simpan_ujian(training["id"], peserta["nama"], peserta["email"], benar, nilai, lulus, pkg_key)
    except Exception as e:  # noqa: BLE001
        st.warning(f"Nilai belum tersimpan ke database: {e}")
    return nilai, lulus


# ---------------- Hasil ujian ----------------
if "exam_result" in st.session_state:
    r = st.session_state["exam_result"]
    c1, c2, c3 = st.columns(3)
    c1.metric("Nilai", f"{r['score']}")
    c2.metric("Benar", f"{r['correct']} / {N}")
    c3.metric("Status", "LULUS ✅" if r["passed"] else "BELUM LULUS ❌")
    if r["passed"]:
        st.success(f"Selamat, **{peserta['nama']}**! Anda dinyatakan LULUS {pkg['title']}. "
                   "Sertifikat bisa diunduh di menu 📜 Sertifikat.")
        if not r.get("balon"):
            st.balloons()
            r["balon"] = True
    else:
        st.error(f"Nilai Anda {r['score']}, belum mencapai {LULUS}. Pelajari kembali materinya, "
                 "lalu ulangi ujian. Boleh mengulang tanpa batas.")

    salah = [q["n"] for q in SOAL if r["answers"].get(q["n"]) != q["key"]]
    cc1, cc2, cc3 = st.columns(3)
    if not r["passed"] and salah:
        if cc1.button(f"🎯 Ulangi {len(salah)} Soal Salah", type="primary", width="stretch"):
            st.session_state["exam_retry"] = dict(pkg=pkg_key, wrong=salah, keep=r["correct"], prev=dict(r["answers"]))
            del st.session_state["exam_result"]
            st.rerun()
    if cc2.button(f"🔁 Ulang Semua ({N} Soal)", width="stretch"):
        del st.session_state["exam_result"]
        for q in SOAL:
            st.session_state.pop(f"uj_{pkg_key}_{q['n']}", None)
        st.rerun()
    if cc3.button("Selesai", width="stretch"):
        del st.session_state["exam_result"]
        st.switch_page("views/sertifikat.py" if r["passed"] else "views/beranda.py")

    st.divider()
    st.subheader("📋 Review Jawaban")
    for q in SOAL:
        ua = r["answers"].get(q["n"])
        ok = ua == q["key"]
        st.markdown(f"**{q['n']}. {'✅' if ok else '❌'}** {esc(q['q'])}")
        for i, opt in enumerate(q["opts"]):
            mark = ""
            if i == q["key"]:
                mark = "  ✅ **(jawaban benar)**"
            elif ua is not None and i == ua:
                mark = "  ❌ **(jawaban Anda)**"
            st.markdown(f"- {chr(65 + i)}. {opt}{mark}")
    footer()
    st.stop()

# ---------------- Mode perbaikan: hanya soal yang salah ----------------
if "exam_retry" in st.session_state:
    rz = st.session_state["exam_retry"]
    rq = [q for q in SOAL if q["n"] in rz["wrong"]]
    st.info(f"🎯 **Mode Perbaikan**: {len(rq)} soal yang sebelumnya salah. "
            f"Benar sebelumnya: {rz['keep']}/{N}. Jawab ulang, lalu kumpulkan.")
    with st.form("form_retry", border=False):
        _render_soal(rq, "retry")
        kirim_r = st.form_submit_button("✅ Kumpulkan Perbaikan", type="primary", width="stretch")
    if kirim_r:
        jr = _kumpulkan(rq, "retry")
        if len(jr) < len(rq):
            st.error(f"Masih ada {len(rq) - len(jr)} soal belum dijawab.")
        else:
            total_benar = rz["keep"] + sum(1 for q in rq if jr.get(q["n"]) == q["key"])
            nilai, lulus = _simpan(total_benar)
            merged = dict(rz["prev"])
            merged.update(jr)
            for q in rq:
                st.session_state.pop(f"retry_{pkg_key}_{q['n']}", None)
            st.session_state["exam_result"] = dict(answers=merged, correct=total_benar, score=nilai,
                                                   passed=lulus, pkg=pkg_key)
            del st.session_state["exam_retry"]
            st.rerun()
    footer()
    st.stop()

# ---------------- Ujian lengkap ----------------
st.caption(f"{N} soal pilihan ganda (studi kasus). Nilai kelulusan **{LULUS}** "
           f"(minimal {round(LULUS / 100 * N)} benar). Boleh mengulang sampai lulus. "
           "Semua soal ada di halaman ini, jawaban baru dikirim setelah tombol **Kumpulkan Jawaban** ditekan.")

with st.form("form_ujian", border=False):
    _render_soal(SOAL, "uj")
    kirim = st.form_submit_button("✅ Kumpulkan Jawaban", type="primary", width="stretch")

if kirim:
    jawaban = _kumpulkan(SOAL, "uj")
    if len(jawaban) < N:
        belum = [str(q["n"]) for q in SOAL if q["n"] not in jawaban]
        st.error(f"Masih ada {len(belum)} soal belum dijawab: nomor {', '.join(belum[:15])}"
                 + (" dan lainnya" if len(belum) > 15 else "") + ". Jawaban yang sudah diisi tetap ada.")
    else:
        benar = sum(1 for q in SOAL if jawaban.get(q["n"]) == q["key"])
        nilai, lulus = _simpan(benar)
        st.session_state["exam_result"] = dict(answers=jawaban, correct=benar, score=nilai, passed=lulus, pkg=pkg_key)
        st.rerun()

footer()
