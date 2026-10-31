import streamlit as st
from utils.styles import apply_ceritajiwa_styles, card
from utils.auth import require_akses, get_peserta, clear_akses

st.set_page_config(page_title="Dashboard - Cerita Jiwa", page_icon="📋", layout="wide")
apply_ceritajiwa_styles()
require_akses()

peserta = get_peserta()

with st.sidebar:
    st.markdown(f"""
    <div style="text-align:center; padding:10px 0;">
        <p style="color:white; font-size:16px; font-weight:700; margin:0;">{peserta['nama']}</p>
        <p style="color:rgba(255,255,255,0.6); font-size:12px; margin:4px 0 0 0;">{peserta['kode']}</p>
    </div>
    <hr style="border-color:rgba(255,255,255,0.15);">
    """, unsafe_allow_html=True)
    
    st.page_link("pages/03_Dashboard.py", label="🏠 Dashboard", disabled=True)
    st.page_link("pages/04_Asesmen.py", label="📝 Asesmen")
    st.page_link("pages/05_Ujian.py", label="📋 Ujian")
    st.page_link("pages/06_Sertifikat.py", label="📜 Sertifikat")
    st.markdown("<hr style='border-color:rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
    if st.button("🚪 Keluar", use_container_width=True, key="keluar_dashboard"):
        clear_akses()
        st.switch_page("app.py")

st.title("Dashboard Peserta")
st.markdown(f"Selamat datang, **{peserta['nama']}**!")
st.caption(f"Sertifikasi: {peserta['sertifikasi']} | Batch: {peserta['batch']}")

st.subheader("Sertifikasi Saya")

col1, col2 = st.columns(2)

with col1:
    card(peserta['sertifikasi'], f"{peserta['sertifikasi']} - Batch: {peserta['batch']}", "active")
    st.page_link("pages/04_Asesmen.py", label="📝 Mulai Asesmen")
    st.page_link("pages/05_Ujian.py", label="📋 Mulai Ujian")

with col2:
    card("Info", "Asesmen: Pukul 08:00 WIB<br>Ujian: Pukul 16:00 WIB<br>Training: 09:00 - 16:00 WIB", "pending")

st.divider()
st.info("""
**Jadwal Hari Ini:**
- 📝 Asesmen: 08:00 WIB
- 📚 Training: 09:00 - 16:00 WIB
- 📋 Ujian: 16:00 WIB

Silakan kerjakan asesmen terlebih dahulu sebelum training dimulai.
""")
