import streamlit as st
import plotly.graph_objects as go
from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session, is_trainer_logged_in

apply_ceritajiwa_styles()
init_session()

if not is_trainer_logged_in():
    st.image("assets/logo_dark.png", width=120)
    st.title("👨‍🏫 Trainer / BEI Panel")
    st.markdown("Masukkan password trainer.")
    password = st.text_input("Password Trainer", type="password")
    if st.button("Masuk", type="primary"):
        if not password:
            st.error("Password wajib diisi.")
        else:
            trainer_pass = st.secrets.get("TRAINER_PASSWORD", "")
            admin_pass = st.secrets.get("ADMIN_PASSWORD", "asesmencerc12")
            effective = trainer_pass if trainer_pass else admin_pass
            if password == effective:
                st.session_state.trainer_logged_in = True
                st.success("Login trainer berhasil!")
                st.rerun()
            else:
                st.error("Password salah.")
    st.stop()

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Trainer Panel</p>", unsafe_allow_html=True)
    if st.button("🚪 Logout", use_container_width=True, key="logout_trainer"):
        st.session_state.trainer_logged_in = False
        st.switch_page("app.py")

st.title("👨‍🏫 Dashboard Trainer / BEI")

st.subheader("📊 Status Peserta Hari Ini")
st.dataframe({
    "Nama": ["Budi S.", "Ani R.", "Citra D.", "Dedi K.", "Eka L."],
    "Perusahaan": ["PT Maju Jaya", "PT Maju Jaya", "PT Maju Jaya", "PT Sejahtera", "PT Sejahtera"],
    "Training": ["CERC-AGT-001", "CERC-AGT-001", "CERC-AGT-001", "CERC-SEP-001", "CERC-SEP-001"],
    "Asesmen": ["✅ Done", "⏳ Progress", "—", "✅ Done", "✅ Done"],
    "Ujian": ["—", "—", "—", "—", "—"],
    "Nilai": ["—", "—", "—", "—", "—"]
}, use_container_width=True)

st.divider()
st.subheader("🔍 Lihat Hasil Asesmen Peserta")
peserta = st.selectbox("Pilih Peserta", ["Budi S.", "Ani R.", "Dedi K.", "Eka L."])

if peserta:
    st.info(f"Report Asesmen: {peserta}")
    fig = go.Figure(go.Bar(
        x=['Stress Mgmt', 'EQ', 'Empati', 'Regulasi', 'Resilience'],
        y=[65, 78, 70, 82, 68],
        marker_color='#344A61', text=[65, 78, 70, 82, 68], textposition='outside'
    ))
    fig.update_layout(title="Skor Kompetensi", yaxis_range=[0,100])
    st.plotly_chart(fig, use_container_width=True)
    col1, col2 = st.columns(2)
    with col1: st.metric("Skor Tertinggi", "82", "Regulasi Emosi")
    with col2: st.metric("Skor Terendah", "65", "Stress Management")
    st.download_button("📥 Download Report PDF", b"Mock", f"asesmen_{peserta.replace(' ', '_')}.pdf")
