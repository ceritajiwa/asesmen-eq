
import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session, is_training_set, is_peserta_set, set_training_session, set_peserta, get_training, get_peserta, verifikasi_kode_akses, get_trainings_list, clear_training_session

apply_ceritajiwa_styles()
init_session()

if not is_training_set():
    st.image("assets/logo_dark.png", width=120)
    st.title("📜 Sertifikat")
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
    st.title("📜 Sertifikat")
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
    if st.button("🏠 Beranda", use_container_width=True, key="sertifikat_home"):
        st.switch_page("app.py")
    if st.button("📝 Asesmen", use_container_width=True, key="sertifikat_asesmen"):
        st.switch_page("pages/01_Asesmen.py")
    if st.button("🎓 Training", use_container_width=True, key="sertifikat_training"):
        st.switch_page("pages/02_Training.py")
    if st.button("📋 Ujian", use_container_width=True, key="sertifikat_ujian"):
        st.switch_page("pages/03_Ujian.py")
    st.markdown("<hr style='border-color:rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
    if st.button("🚪 Keluar", use_container_width=True, key="keluar_sertifikat"):
        clear_training_session()
        st.switch_page("app.py")

st.title("📜 Hasil & Sertifikat")
st.subheader(f"{training['sertifikasi']} - {peserta['nama']}")
st.markdown("Status: ✅ **LULUS**")
st.markdown(f"🏷️ Running Key: **{training['sertifikasi']}-2026-000089**")
st.markdown("📅 Tanggal Lulus: 15 Agustus 2026")
col1, col2 = st.columns(2)
with col1: st.download_button("📥 Download Sertifikat PDF", b"Mock PDF", f"sertifikat_{training['sertifikasi'].lower()}.pdf", use_container_width=True)
with col2: st.download_button("🏅 Download Badge", b"Mock PNG", f"badge_{training['sertifikasi'].lower()}.png", use_container_width=True)
st.divider()
st.subheader("📊 Riwayat Ujian")
st.table({"Percobaan": [1, 2, 3], "Nilai": [65, 72, 85], "Status": ["❌ Gagal", "❌ Gagal", "✅ Lulus"], "Waktu": ["16:05", "16:25", "16:45"]})
st.divider()
st.subheader("📝 Report Asesmen")
st.download_button("📥 Download Report Asesmen", b"Mock PDF", f"asesmen_{training['sertifikasi'].lower()}_report.pdf", use_container_width=True)
