import streamlit as st

from cjlib.db import (INST_MAP, DatabaseError, ambil_training, cari_respondent, get_enabled,
                      jawaban_respondent, simpan_asesmen)
from cjlib.hasil import show_result
from cjlib.styles import esc, footer, page_header
from cjlib.ui import peserta_sidebar, require_peserta_gate, show_db_error, subjudul
from scoring import compute_dim_scores, responses_to_answers

training, peserta = require_peserta_gate("📝 Asesmen")
peserta_sidebar("asesmen")

page_header("📝 Asesmen EQ & Emotional Regulation", subjudul(training, peserta))

# Data training terbaru (supaya pilihan instrumen dari Admin langsung terbaca)
try:
    tr = ambil_training(training["id"]) or {}
    sudah = cari_respondent(training["id"], peserta["email"])
except Exception as e:  # noqa: BLE001
    show_db_error(DatabaseError(str(e)))
    st.stop()

# ---------------- Sudah pernah mengisi: langsung tampilkan hasil ----------------
if sudah:
    if st.session_state.pop("asesmen_baru_kirim", False):
        st.success("Terima kasih, jawaban Anda sudah tersimpan. Berikut hasil asesmen Anda.")
    else:
        st.info("Email ini sudah mengisi asesmen untuk training ini. Berikut hasil Anda.")
    try:
        scores = compute_dim_scores(responses_to_answers(jawaban_respondent(sudah["id"])))
    except Exception as e:  # noqa: BLE001
        show_db_error(DatabaseError(str(e)))
        st.stop()
    if scores:
        show_result(sudah["full_name"], tr.get("name", training["nama"]), sudah.get("department"),
                    sudah.get("job_level"), scores, key="asesmen")
    else:
        st.warning("Data jawaban belum lengkap. Silakan hubungi admin.")
    footer()
    st.stop()

# ---------------- Form asesmen (semua soal satu halaman, tidak reload sampai submit) ----------------
insts = [INST_MAP[k] for k in get_enabled(tr)]
total_q = sum(len(i["items"]) for i in insts)

st.caption("Isi seluruh pernyataan dengan jujur sesuai kondisi Anda saat ini. Tidak ada jawaban benar atau salah.")
st.markdown(
    f"<div class='cj-card' style='padding:14px 20px;'>Training ini menggunakan <b>{len(insts)} asesmen</b> "
    f"dengan total <b>{total_q} pernyataan</b>. Semuanya ada di halaman ini, cukup scroll ke bawah. "
    f"Jawaban baru dikirim setelah tombol <b>Kirim &amp; Lihat Hasil</b> ditekan.</div>",
    unsafe_allow_html=True,
)

with st.form("form_asesmen", border=False):
    with st.container(border=True, key="card_datadiri"):
        st.subheader("Data Diri")
        c1, c2 = st.columns(2)
        dept = c1.text_input("Departemen")
        job_level = c2.selectbox("Level jabatan", ["Individual Contributor / Staff", "Supervisor / Team Lead",
                                                   "Manager ke atas", "Lainnya"])

    for inst in insts:
        with st.container(border=True, key=f"card_inst_{inst['key']}"):
            st.subheader(inst["name"])
            st.markdown(f"<p class='cj-sub' style='margin-top:-4px;'>{esc(inst['intro'])}</p>", unsafe_allow_html=True)
            for it in inst["items"]:
                kunci = f"as_{inst['key']}_{it['n']}"
                if inst.get("mcq"):
                    if it.get("img"):
                        st.markdown(f"**{it['n']}.** Pilih gambar yang tepat:")
                        st.image(it["img"], width=520)
                        st.radio("Jawaban", it["opts"], key=kunci, index=None, horizontal=True,
                                 label_visibility="collapsed")
                    else:
                        st.radio(f"**{it['n']}.** {it['text']}", it["opts"], key=kunci, index=None)
                else:
                    st.radio(f"**{it['n']}.** {it['text']}", [s[1] for s in inst["scale"]], key=kunci, index=None)

    kirim = st.form_submit_button("✅ Kirim & Lihat Hasil", type="primary", width="stretch")

if kirim:
    answers, kosong = {}, []
    for inst in insts:
        for it in inst["items"]:
            val = st.session_state.get(f"as_{inst['key']}_{it['n']}")
            if val is None:
                kosong.append(f"{inst['key']} no. {it['n']}")
                continue
            if inst.get("mcq"):
                answers[(inst["key"], it["n"])] = it["opts"].index(val)
            else:
                answers[(inst["key"], it["n"])] = {lbl: num for num, lbl in inst["scale"]}[val]

    if kosong:
        contoh = ", ".join(kosong[:8]) + (" dan lainnya" if len(kosong) > 8 else "")
        st.error(f"Masih ada {len(kosong)} pernyataan yang belum dijawab ({contoh}). "
                 "Jawaban yang sudah diisi tetap ada, silakan scroll ke atas untuk melengkapi.")
    else:
        try:
            if cari_respondent(training["id"], peserta["email"]):
                st.rerun()  # sudah tersimpan (misalnya tombol tertekan dua kali)
            simpan_asesmen(training["id"], peserta["nama"], peserta["email"], dept, job_level, answers)
        except Exception as e:  # noqa: BLE001
            st.error(f"Gagal menyimpan jawaban: {e}")
            st.stop()
        st.session_state["asesmen_baru_kirim"] = True
        st.rerun()  # halaman dimuat ulang dan otomatis menampilkan hasil

footer()
