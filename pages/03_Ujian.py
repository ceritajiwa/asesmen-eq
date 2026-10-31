
import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session, is_training_set, is_peserta_set, set_training_session, set_peserta, get_training, get_peserta, verifikasi_kode_akses, get_trainings_list, clear_training_session

st.set_page_config(page_title="📋 Ujian - Cerita Jiwa", layout="wide")
apply_ceritajiwa_styles()
init_session()

if not is_training_set():
    st.image("assets/logo_dark.png", width=120)
    st.title("📋 Ujian")
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
    st.title("📋 Ujian")
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
    if st.button("🏠 Beranda", use_container_width=True, key="ujian_home"):
        st.switch_page("app.py")
    if st.button("📝 Asesmen", use_container_width=True, key="ujian_asesmen"):
        st.switch_page("pages/01_Asesmen.py")
    if st.button("🎓 Training", use_container_width=True, key="ujian_training"):
        st.switch_page("pages/02_Training.py")
    if st.button("📜 Sertifikat", use_container_width=True, key="ujian_sertifikat"):
        st.switch_page("pages/04_Sertifikat.py")
    st.markdown("<hr style='border-color:rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
    if st.button("🚪 Keluar", use_container_width=True, key="keluar_ujian"):
        clear_training_session()
        st.switch_page("app.py")

st.title(f"📋 Ujian {training['sertifikasi']}")
st.caption(f"{peserta['nama']} | {training['perusahaan']} | Batch: {training['batch']}")

col1, col2 = st.columns([3, 1])
with col2: st.metric("⏱️ Sisa Waktu", "45:00")

st.progress(0, text="Soal 1 dari 20")
soal_list = [
    ("Dalam teknik active listening, hal yang paling penting adalah...", ["Memberi saran cepat", "Menunjukkan empati", "Mengalihkan pembicaraan", "Mengkritik perasaan klien"], 1),
    ("Apa tujuan utama dari emotional regulation?", ["Menekan emosi", "Mengelola emosi secara konstruktif", "Menghindari konflik", "Bersikap netral"], 1),
    ("Teknik grounding paling efektif dilakukan saat...", ["Santai", "Sedang panik/cemas", "Sedang tidur", "Sedang makan"], 1),
]
jawaban = []
for i, (pertanyaan, opsi, benar) in enumerate(soal_list):
    st.subheader(f"Soal {i+1}")
    j = st.radio(pertanyaan, opsi, key=f"soal_ujian_{i}")
    jawaban.append(opsi.index(j))
st.progress(15, text="Soal 3 dari 20")
c1, c2, c3 = st.columns(3)
with c1: st.button("← Sebelumnya", disabled=True, key="btn_prev")
with c2: st.button("🚩 Ragu-ragu", key="btn_doubt")
with c3: st.button("Selanjutnya →", key="btn_next")
st.divider()
if st.button("✅ Submit Ujian", type="primary", key="btn_submit_ujian"):
    nilai = 85
    st.session_state.ujian_attempts += 1
    st.session_state.current_nilai = nilai
    if nilai >= 80:
        st.success(f"🎉 Selamat! Anda lulus dengan nilai {nilai}!")
        st.balloons()
        st.markdown(f"🏷️ Running Key: **{training['sertifikasi']}-2026-000089**")
    else:
        st.warning(f"Nilai Anda: {nilai}. Belum memenuhi (minimum 80).")
        st.info(f"Percobaan ke-{st.session_state.ujian_attempts}. Silakan ulangi.")
        if st.button("🔄 Ulangi Ujian", type="primary", key="btn_retry"):
            st.rerun()
