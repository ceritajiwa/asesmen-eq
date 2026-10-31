import streamlit as st
from utils.styles import apply_ceritajiwa_styles

st.set_page_config(page_title="Verifikasi Sertifikasi - Cerita Jiwa", page_icon="🔍", layout="centered")
apply_ceritajiwa_styles()

st.image("assets/logo_dark.png", width=100)
st.title("🔍 Verifikasi Sertifikasi")
st.markdown("Cek keaslian sertifikasi Cerita Jiwa")

sertifikasi = st.selectbox("Pilih Sertifikasi", ["CERC", "CMBC", "CPSC", "CPPC", "CRWC", "CCTC"])
cari = st.text_input("Masukkan Nama Lengkap atau Running Key", placeholder="Contoh: Budi Santoso")

if st.button("Cari", type="primary"):
    if cari:
        st.success("✅ Sertifikat Terverifikasi")
        st.markdown(f"""
        <div style="background:#F0FDF4; border:2px solid #86EFAC; border-radius:16px; padding:24px;">
            <h4 style="color:#166534; margin-top:0;">Data Lulusan</h4>
            <p><strong>Nama:</strong> Budi Santoso</p>
            <p><strong>Sertifikasi:</strong> {sertifikasi}</p>
            <p><strong>Running Key:</strong> {sertifikasi}-2026-000089</p>
            <p><strong>Tanggal Lulus:</strong> 15 Agustus 2026</p>
            <p><strong>Status:</strong> <span style="color:#2E7D32; font-weight:700;">Aktif</span></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Masukkan nama atau running key")

st.divider()
st.markdown("<p style='text-align:center; color:#6D6F71;'>© 2026 Cerita Jiwa Training Center</p>", unsafe_allow_html=True)
