import json
from datetime import datetime

import streamlit as st

from bei import BEI_PROMPTS, _struct_table, bei_participant_pdf, bei_radar_png, fetch_bei, structure_bei
from cjlib.auth import check_password, is_trainer_logged_in
from cjlib.db import fetch_respondents, fetch_trainings_raw, sb as _sb
from cjlib.styles import footer, page_header


def _jloads(v):
    if not v:
        return None
    if isinstance(v, (dict, list)):
        return v
    return json.loads(v)


# ---------------- Login ----------------
if not is_trainer_logged_in():
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.image("assets/logo_dark.png", width=96)
        page_header("👨‍🏫 Trainer / BEI Panel", "Masukkan password trainer.")
        with st.form("form_trainer_login", border=True):
            password = st.text_input("Password Trainer", type="password")
            submit = st.form_submit_button("Masuk", type="primary", width="stretch")
        if submit:
            ok = check_password(password, "TRAINER_PASSWORD", fallback_secret="ADMIN_PASSWORD")
            if ok is None:
                st.error("TRAINER_PASSWORD / ADMIN_PASSWORD belum diatur di Secrets Streamlit.")
            elif ok:
                st.session_state.trainer_logged_in = True
                st.rerun()
            else:
                st.error("Password salah.")
    footer()
    st.stop()

with st.sidebar:
    st.markdown("<p style='font-weight:800; margin:6px 0 0;'>Trainer Panel</p><hr>", unsafe_allow_html=True)
    if st.button("🚪 Logout", width="stretch", key="logout_trainer"):
        st.session_state.trainer_logged_in = False
        st.switch_page("views/beranda.py")

sb = _sb()

page_header("👨‍🏫 Trainer / BEI: Catatan Sesi Konseling")
st.caption("Isi narasi sesi sesuai panduan pertanyaan. AI akan menyusun hasil dalam bentuk tabel "
           "terstruktur untuk peserta dan perusahaan.")
trainings = fetch_trainings_raw()
if not trainings:
    st.warning("Belum ada training terdaftar.")
    st.stop()
tname = st.selectbox("Perusahaan / Training", [t["name"] for t in trainings], key="bei_t")
training = next(t for t in trainings if t["name"] == tname)

# muat sesi lama ke form (harus sebelum widget dirender)
if "bei_load" in st.session_state:
    _ld = st.session_state.pop("bei_load")
    st.session_state["bei_existing"] = "-- peserta baru --"
    st.session_state["bei_pname"] = _ld["participant"]
    st.session_state["bei_counselor"] = _ld["counselor"]
    for _k, _t, _ in BEI_PROMPTS:
        st.session_state[f"bei_{_k}"] = (_ld["narratives"] or {}).get(_k, "")
    st.session_state["bei_loaded_id"] = _ld["id"]
    st.info(f"Sesi {_ld['participant']} dimuat ke form. Proses ulang dengan AI, lalu simpan "
            f"-> hasil diperbarui pada sesi yang sama.")
    st.rerun()

resps = fetch_respondents(training["id"])

c1, c2 = st.columns(2)
existing = c1.selectbox("Pilih peserta (yang sudah pernah asesmen)", ["-- peserta baru --"] + [r["full_name"] for r in resps], key="bei_existing")
if existing == "-- peserta baru --":
    p_name = c2.text_input("Nama peserta", key="bei_pname")
else:
    p_name = existing
counselor = st.text_input("Nama konselor / trainer", key="bei_counselor")

st.divider()
st.subheader("Panduan Pertanyaan Sesi")
narratives = {}
for key, title, hint in BEI_PROMPTS:
    with st.expander(f"**{title}**"):
        st.caption(hint)
        narratives[key] = st.text_area("Catatan", key=f"bei_{key}", height=110, label_visibility="collapsed")

if st.button("💾 Simpan & Proses dengan AI", type="primary", width="stretch"):
    if not p_name.strip() or not counselor.strip():
        st.error("Nama peserta dan konselor wajib diisi.")
    elif not any(str(v).strip() for v in narratives.values()):
        st.error("Isi minimal salah satu bagian narasi.")
    else:
        with st.spinner("Menyimpan dan memproses dengan AI..."):
            api_key = st.secrets.get("GEMINI_API_KEY", None)
            structured = structure_bei(narratives, api_key, st.secrets.get("GROQ_API_KEY", None))
            _lid = st.session_state.pop("bei_loaded_id", None)
            try:
                if _lid:
                    sb.table("bei_sessions").update(
                        dict(narratives=narratives, structured=structured)).eq("id", _lid).execute()
                else:
                    sb.table("bei_sessions").insert(dict(
                        training_id=training["id"], participant_name=p_name.strip(),
                        counselor_name=counselor.strip(),
                        narratives=narratives,
                        structured=structured)).execute()
            except Exception as ex:
                st.error("Gagal menyimpan sesi ke database. Kemungkinan tabel bei_sessions "
                         "belum dibuat - jalankan migrasi SQL (lihat panduan) lalu coba lagi. "
                         f"Detail: {ex}")
                st.stop()
        st.success("Sesi tersimpan.")
        st.session_state["bei_last"] = (p_name.strip(), dict(narratives), structured)
        st.session_state["bei_last_tanggal"] = datetime.now().strftime("%Y-%m-%d")
        st.rerun()

if "bei_last" in st.session_state:
    ln, lnar, lstc = st.session_state.pop("bei_last")
    st.divider()
    st.subheader(f"📋 Hasil Terstruktur - {ln}")
    if lstc and lstc.get("_error"):
        st.error("⚠️ AI tidak dapat memproses sesi ini:")
        st.code(lstc["_error"])
        st.info("Narasi sesi TETAP TERSIMPAN di database. Perbaiki penyebab di atas "
                "(paling umum: GEMINI_API_KEY belum/belum benar diisi di Secrets, "
                "atau API Gemini belum diaktifkan untuk key tersebut).")
    elif lstc:
        st.dataframe(_struct_table(lstc), hide_index=True, width="stretch")
    else:
        st.info("Struktur AI kosong. Narasi tetap tersimpan.")
    if lstc and isinstance(lstc.get("skor_visual"), dict) and lstc["skor_visual"]:
        st.image(bei_radar_png(lstc["skor_visual"]), width=380)
    pdf_b = bei_participant_pdf(tname, ln, counselor, lnar, lstc,
                                tanggal=str(st.session_state.get("bei_last_tanggal", "")))
    st.download_button("⬇️ Download PDF Sesi Ini", data=pdf_b,
                       file_name=f"BEI_{ln.replace(' ','_')}.pdf", mime="application/pdf")


st.divider()
st.subheader("📚 Riwayat Sesi Tersimpan")
_sessions_all = fetch_bei(sb, training["id"])
_sessions = [s for s in _sessions_all if s["participant_name"] == p_name] if p_name.strip() else _sessions_all
if not _sessions:
    st.info("Belum ada sesi tersimpan untuk peserta ini." if p_name.strip()
            else "Belum ada sesi tersimpan untuk training ini.")
else:
    st.caption(f"{len(_sessions)} sesi untuk **{p_name}**." if p_name.strip()
               else f"{len(_sessions)} sesi ditemukan (semua peserta).")
    for s in _sessions:
        _stc = _jloads(s.get("structured"))
        _nar = _jloads(s.get("narratives")) or {}
        with st.expander(f"**{s['participant_name']}** - {s.get('counselor_name','-')} "
                         f"({str(s.get('created_at',''))[:10]})"):
            _cc1, _cc2 = st.columns([1, 2])
            if _cc1.button("✏️ Muat ke Form (proses ulang)", key=f"bei_load_{s['id']}"):
                st.session_state["bei_load"] = dict(
                    id=s["id"], participant=s["participant_name"],
                    counselor=s.get("counselor_name", ""), narratives=_nar)
                st.rerun()
            if st.session_state.get("bei_loaded_id") == s["id"]:
                _cc2.info("✓ sesi ini sedang dimuat di form")
            if _stc and _stc.get("_error"):
                st.warning(f"AI: {_stc['_error'][:200]}")
            elif _stc:
                st.dataframe(_struct_table(_stc), hide_index=True, width="stretch")
            st.markdown("**Catatan narasi:**")
            for _k, _t, _ in BEI_PROMPTS:
                _v = (_nar or {}).get(_k, "").strip()
                if _v:
                    st.markdown(f"- **{_t}:** {_v[:300]}")
            if _stc and isinstance(_stc.get("skor_visual"), dict) and _stc["skor_visual"]:
                st.image(bei_radar_png(_stc["skor_visual"]), width=380)
            _pdf = bei_participant_pdf(tname, s["participant_name"],
                                       s.get("counselor_name", "-"), _nar or {}, _stc,
                                       tanggal=str(s.get("created_at", "")))
            st.download_button("⬇️ PDF Sesi Ini", data=_pdf,
                               file_name=f"BEI_{s['participant_name'].replace(' ','_')}_{str(s.get('created_at',''))[:10]}.pdf",
                               mime="application/pdf", key=f"bei_hist_{s['id']}")

footer()
