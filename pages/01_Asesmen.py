
import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session, is_training_set, is_peserta_set, set_training_session, set_peserta, get_training, get_peserta, verifikasi_kode_akses, get_trainings_list, clear_training_session

apply_ceritajiwa_styles()
init_session()

if not is_training_set():
    st.image("assets/logo_dark.png", width=120)
    st.title("📝 Asesmen")
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
    st.title("📝 Asesmen")
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
    st.page_link("pages/01_Asesmen.py", label="📝 Asesmen", disabled=True)
    st.page_link("pages/02_Training.py", label="🎓 Training")
    st.page_link("pages/03_Ujian.py", label="📋 Ujian")
    st.page_link("pages/04_Sertifikat.py", label="📜 Sertifikat")
    if st.button("🚪 Keluar", use_container_width=True, key="keluar_asesmen"):
        clear_training_session()
        st.switch_page("app.py")

st.title(f"📝 Asesmen {training['sertifikasi']}")
st.caption(f"{peserta['nama']} | {training['perusahaan']} | Batch: {training['batch']}")

import plotly.graph_objects as go
progress = st.progress(0, text="Progress: 0%")

st.subheader("Bagian 1: Stress Level & Emotional Awareness")
q1 = st.radio("1. Seberapa sering Anda merasa kewalahan?", ["Tidak pernah", "Jarang", "Kadang", "Sering", "Selalu"], index=2)
q2 = st.radio("2. Seberapa baik Anda mengelola emosi saat marah?", ["Sangat buruk", "Buruk", "Cukup", "Baik", "Sangat baik"], index=2)
q3 = st.radio("3. Seberapa sering Anda menggunakan teknik grounding?", ["Tidak pernah", "Jarang", "Kadang", "Sering", "Selalu"], index=2)

st.subheader("Bagian 2: Emotional Quotient (EQ)")
q4 = st.radio("4. Seberapa mudah Anda mengenali emosi orang lain?", ["Sangat sulit", "Sulit", "Cukup", "Mudah", "Sangat mudah"], index=2)
q5 = st.radio("5. Seberapa sering Anda bereaksi impulsif?", ["Selalu", "Sering", "Kadang", "Jarang", "Tidak pernah"], index=2)

progress.progress(60, text="Progress: 60%")

if st.button("Submit Asesmen", type="primary"):
    st.session_state.asesmen_done = True
    st.success("✅ Asesmen selesai!")
    categories = ['Stress Mgmt', 'Emotional Awareness', 'Impulse Control', 'Empathy', 'Self-Regulation', 'Resilience']
    values = [65, 78, 82, 70, 75, 68]
    fig = go.Figure(data=go.Scatterpolar(r=values+[values[0]], theta=categories+[categories[0]], fill='toself', fillcolor='rgba(52,74,97,0.25)', line=dict(color='#344A61', width=2.5)))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])), showlegend=False, title="Profil Kompetensi Emosional")
    st.plotly_chart(fig, use_container_width=True)
    fig2 = go.Figure(go.Bar(x=categories, y=values, marker_color='#344A61', text=values, textposition='outside'))
    fig2.update_layout(title="Skor per Dimensi", yaxis_range=[0,100])
    st.plotly_chart(fig2, use_container_width=True)
    st.download_button("📥 Download Report PDF", b"Mock PDF", file_name=f"asesmen_{training['sertifikasi'].lower()}_{peserta['nama'].replace(' ','_')}.pdf")
    st.info("💡 Simpan report ini untuk dibahas saat sesi training.")
