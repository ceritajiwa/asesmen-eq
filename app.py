import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session

st.set_page_config(page_title="Cerita Jiwa Training Center", page_icon="🧠", layout="wide", initial_sidebar_state="collapsed")
apply_ceritajiwa_styles()
init_session()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/logo_dark.png", width=180)
    st.markdown("<h1 style='text-align:center; margin-top:8px; color:#344A61;'>Cerita Jiwa</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#6D6F71; font-size:18px;'>Training Center</p>", unsafe_allow_html=True)

st.divider()
st.markdown("<h3 style='text-align:center; color:#344A61;'>Menu</h3>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("📝 Asesmen", use_container_width=True, key="menu_asesmen"):
        st.switch_page("pages/01_Asesmen.py")
    if st.button("🎓 Training", use_container_width=True, key="menu_training"):
        st.switch_page("pages/02_Training.py")
    if st.button("📋 Ujian", use_container_width=True, key="menu_ujian"):
        st.switch_page("pages/03_Ujian.py")
with c2:
    if st.button("📜 Sertifikat", use_container_width=True, key="menu_sertifikat"):
        st.switch_page("pages/04_Sertifikat.py")
    if st.button("🔍 Cek Sertifikasi", use_container_width=True, key="menu_verifikasi"):
        st.switch_page("pages/05_Verifikasi.py")
with c3:
    if st.button("⚙️ Admin", use_container_width=True, key="menu_admin"):
        st.switch_page("pages/06_Admin.py")
    if st.button("👨‍🏫 Trainer / BEI", use_container_width=True, key="menu_trainer"):
        st.switch_page("pages/07_Trainer.py")

st.divider()
st.markdown("<div style='text-align:center; padding: 20px 0;'><h2 style='color:#344A61;'>Sertifikasi Profesional untuk Kesehatan Mental</h2><p style='color:#6D6F71; font-size:18px;'>CERC | CMBC | CPSC | CPPC | CRWC | CCTC</p></div>", unsafe_allow_html=True)

sertifikasi = [
    ("CERC", "Certified Emotional Regulation Coach", "Mengelola emosi dengan bijak"),
    ("CMBC", "Certified Money Behavior Coach", "Memahami perilaku finansial"),
    ("CPSC", "Certified Psychology of Sales Coach", "Psikologi dalam penjualan"),
    ("CPPC", "Certified Positive Parenting Coach", "Parenting yang positif"),
    ("CRWC", "Certified Relationship Wellbeing Coach", "Kesehatan relasi"),
    ("CCTC", "Certified Complex Trauma Coach", "Penanganan trauma kompleks"),
]
cols = st.columns(3)
for i, (kode, nama, desk) in enumerate(sertifikasi):
    with cols[i % 3]:
        st.markdown(f"<div style='background:white; border-radius:16px; padding:24px; box-shadow:0 2px 12px rgba(52,74,97,0.06); border:1px solid #EEF0F4; margin-bottom:16px;'><h3 style='margin-top:0; color:#344A61;'>{kode}</h3><p style='font-weight:600; color:#344A61;'>{nama}</p><p style='color:#6D6F71; font-size:14px;'>{desk}</p></div>", unsafe_allow_html=True)

st.divider()
st.markdown("<p style='text-align:center; color:#6D6F71;'>© 2026 Cerita Jiwa Training Center</p>", unsafe_allow_html=True)
