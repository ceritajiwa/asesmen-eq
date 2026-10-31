import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import require_akses, get_peserta

st.set_page_config(page_title="Sertifikat - Cerita Jiwa", page_icon="📜", layout="wide")
apply_ceritajiwa_styles()
require_akses()

peserta = get_peserta()

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Menu</p>", unsafe_allow_html=True)
    st.page_link("pages/03_Dashboard.py", label="🏠 Dashboard")
    st.page_link("pages/04_Asesmen.py", label="📝 Asesmen")
    st.page_link("pages/05_Ujian.py", label="📋 Ujian")
    st.page_link("pages/06_Sertifikat.py", label="📜 Sertifikat", disabled=True)

st.title("📜 Hasil & Sertifikat")

st.subheader(f"{peserta['sertifikasi']} - {peserta['nama']}")
st.markdown("Status: ✅ **LULUS**")
st.markdown(f"🏷️ Running Key: **{peserta['sertifikasi']}-2026-000089**")
st.markdown("📅 Tanggal Lulus: 15 Agustus 2026")

col1, col2 = st.columns(2)
with col1:
    st.download_button("📥 Download Sertifikat PDF", b"Mock PDF", f"sertifikat_{peserta['sertifikasi'].lower()}.pdf", use_container_width=True)
with col2:
    st.download_button("🏅 Download Badge", b"Mock PNG", f"badge_{peserta['sertifikasi'].lower()}.png", use_container_width=True)

st.divider()
st.subheader("📊 Riwayat Ujian")
st.table({
    "Percobaan": [1, 2, 3],
    "Nilai": [65, 72, 85],
    "Status": ["❌ Gagal", "❌ Gagal", "✅ Lulus"],
    "Waktu": ["16:05", "16:25", "16:45"]
})

st.divider()
st.subheader("📝 Report Asesmen")
st.download_button("📥 Download Report Asesmen", b"Mock PDF", f"asesmen_{peserta['sertifikasi'].lower()}_report.pdf", use_container_width=True)
