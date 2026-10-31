
import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session, is_training_set, is_peserta_set, set_training_session, set_peserta, get_training, get_peserta, verifikasi_kode_akses, get_trainings_list, clear_training_session

apply_ceritajiwa_styles()
init_session()

if not is_training_set():
    st.image("assets/logo_dark.png", width=120)
    st.title("🎓 Training")
    st.markdown("Pilih training dan masukkan kode akses yang diberikan trainer.")

    trainings = get_trainings_list()
    if not trainings:
        st.error("Belum ada training yang tersedia.")
        st.stop()

    training_options = {tid: label for tid, label in trainings}
    selected = st.selectbox("Pilih Training", options=list(training_options.keys()), format_func=lambda x: training_options[x])
    kode = st.text_input("Kode Akses", placeholder="Contoh: CERC-AGT-001")

    if st.button("Masuk", type="primary"):
        if not kode:
            st.error("Kode akses wajib diisi.")
        else:
            data = verifikasi_kode_akses(selected, kode)
            if data:
                set_training_session(selected, data["kode_akses"], data["nama_training"], data["perusahaan"], data["sertifikasi"], data["batch"])
                st.success("Kode akses valid!")
                st.rerun()
            else:
                st.error("Kode akses tidak valid untuk training ini.")
    st.stop()

if not is_peserta_set():
    st.image("assets/logo_dark.png", width=120)
    st.title("🎓 Training")
    training = get_training()
    st.info(f"Training: **{training['nama']}** | {training['perusahaan']}")

    nama = st.text_input("Nama Lengkap")
    email = st.text_input("Email")
    if st.button("Lanjutkan", type="primary"):
        if not nama or not email:
            st.error("Nama dan email wajib diisi.")
        else:
            set_peserta(nama, email)
            st.rerun()
    st.stop()

training = get_training()
peserta = get_peserta()

with st.sidebar:
    st.markdown(f"<div style='text-align:center; padding:10px 0;'><p style='color:white; font-size:16px; font-weight:700; margin:0;'>{peserta['nama']}</p><p style='color:rgba(255,255,255,0.6); font-size:12px; margin:4px 0 0 0;'>{training['kode']}</p></div><hr style='border-color:rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
    st.page_link("app.py", label="🏠 Beranda")
    st.page_link("pages/01_Asesmen.py", label="📝 Asesmen")
    st.page_link("pages/02_Training.py", label="🎓 Training", disabled=True)
    st.page_link("pages/03_Ujian.py", label="📋 Ujian")
    st.page_link("pages/04_Sertifikat.py", label="📜 Sertifikat")
    if st.button("🚪 Keluar", use_container_width=True, key="keluar_training"):
        clear_training_session()
        st.switch_page("app.py")

st.title(f"🎓 Training {training['sertifikasi']}")
st.caption(f"{peserta['nama']} | {training['perusahaan']} | Batch: {training['batch']}")
st.info("📚 Materi training akan ditampilkan di sini.")
st.markdown("### Jadwal Training Hari Ini\n- **08:00 - 09:00** : Asesmen\n- **09:00 - 12:00** : Sesi Pagi\n- **12:00 - 13:00** : Istirahat\n- **13:00 - 16:00** : Sesi Sore\n- **16:00 - 17:00** : Ujian")
