import streamlit as st
import plotly.graph_objects as go
from utils.styles import apply_ceritajiwa_styles
from utils.auth import require_akses, get_peserta, clear_akses

st.set_page_config(page_title="Trainer - Cerita Jiwa", page_icon="👨‍🏫", layout="wide")
apply_ceritajiwa_styles()

# Trainer bisa pakai kode akses trainer atau langsung akses (untuk demo)
if not st.session_state.get("kode_akses"):
    st.warning("Halaman Trainer. Masukkan kode akses trainer.")
    kode = st.text_input("Kode Trainer", placeholder="TRAINER-001")
    if st.button("Masuk"):
        if kode.upper() == "TRAINER-001":
            from utils.auth import set_akses
            set_akses("TRAINER-001", "Trainer", "All", "All")
            st.rerun()
        else:
            st.error("Kode trainer tidak valid.")
    st.stop()

peserta = get_peserta()

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Trainer Panel</p>", unsafe_allow_html=True)
    if st.button("🚪 Logout", use_container_width=True, key="logout_trainer"):
        clear_akses()
        st.switch_page("app.py")

st.title("👨‍🏫 Dashboard Trainer")

st.subheader("📊 Status Peserta Hari Ini")
st.dataframe({
    "Nama": ["Budi S.", "Ani R.", "Citra D.", "Dedi K.", "Eka L."],
    "Kode": ["CERC-AGT-001", "CERC-AGT-002", "CERC-AGT-003", "CERC-AGT-004", "CERC-AGT-005"],
    "Login": ["✅", "✅", "❌", "✅", "✅"],
    "Asesmen": ["✅ Done", "⏳ Progress", "—", "✅ Done", "✅ Done"],
    "Ujian": ["—", "—", "—", "—", "—"],
    "Nilai": ["—", "—", "—", "—", "—"]
}, use_container_width=True)

st.divider()

st.subheader("🔍 Lihat Hasil Asesmen Peserta")
peserta_pilihan = st.selectbox("Pilih Peserta", ["Budi S.", "Ani R.", "Dedi K.", "Eka L."])

if peserta_pilihan:
    st.info(f"Report Asesmen: {peserta_pilihan}")

    fig = go.Figure(go.Bar(
        x=['Stress Mgmt', 'EQ', 'Empati', 'Regulasi', 'Resilience'],
        y=[65, 78, 70, 82, 68],
        marker_color='#344A61',
        text=[65, 78, 70, 82, 68],
        textposition='outside'
    ))
    fig.update_layout(title="Skor Kompetensi", yaxis_range=[0,100])
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Skor Tertinggi", "82", "Regulasi Emosi")
    with col2:
        st.metric("Skor Terendah", "65", "Stress Management")

    st.download_button("📥 Download Report PDF", b"Mock", f"asesmen_{peserta_pilihan.replace(' ', '_')}.pdf")
