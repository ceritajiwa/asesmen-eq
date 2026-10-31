import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session, set_akses, verifikasi_kode, clear_akses

st.set_page_config(
    page_title="Cerita Jiwa Training Center",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_ceritajiwa_styles()
init_session()

# Kalau sudah punya akses, langsung ke dashboard
if st.session_state.kode_akses:
    st.switch_page("pages/03_Dashboard.py")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/logo_dark.png", width=180)
    st.markdown("<h1 style='text-align:center; margin-top:8px; color:#344A61;'>Cerita Jiwa</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#6D6F71; font-size:18px;'>Training Center</p>", unsafe_allow_html=True)

st.divider()

# KODE AKSES INPUT
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align:center; padding: 20px 0;">
        <h3 style="color:#344A61;">Masukkan Kode Akses</h3>
        <p style="color:#6D6F71;">Kode akses diberikan oleh trainer saat training dimulai.</p>
    </div>
    """, unsafe_allow_html=True)
    
    kode = st.text_input("Kode Akses", placeholder="Contoh: CERC-AGT-001", label_visibility="collapsed")
    
    if st.button("Masuk", type="primary", use_container_width=True):
        if not kode:
            st.error("Kode akses wajib diisi.")
        else:
            data = verifikasi_kode(kode)
            if data:
                set_akses(kode.strip().upper(), data["nama"], data["sertifikasi"], data["batch"])
                st.success(f"Selamat datang, {data['nama']}!")
                st.switch_page("pages/03_Dashboard.py")
            else:
                st.error("Kode akses tidak valid. Silakan cek kembali atau hubungi trainer.")
    
    st.divider()
    st.page_link("pages/07_Verifikasi.py", label="🔍 Cek Sertifikasi (Publik)")
    st.link_button("💬 Hubungi Admin via WhatsApp", "https://wa.me/6281234567890", use_container_width=True)

st.divider()

# INFO SERTIFIKASI
st.markdown("""
<div style="text-align:center; padding: 20px 0;">
    <h2 style="color:#344A61;">Sertifikasi Profesional untuk Kesehatan Mental</h2>
</div>
""", unsafe_allow_html=True)

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
        st.markdown(f"""
        <div style="background:white; border-radius:16px; padding:24px; 
                    box-shadow:0 2px 12px rgba(52,74,97,0.06); 
                    border:1px solid #EEF0F4; margin-bottom:16px;">
            <h3 style="margin-top:0; color:#344A61;">{kode}</h3>
            <p style="font-weight:600; color:#344A61;">{nama}</p>
            <p style="color:#6D6F71; font-size:14px;">{desk}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.markdown("<p style='text-align:center; color:#6D6F71;'>© 2026 Cerita Jiwa Training Center</p>", unsafe_allow_html=True)
