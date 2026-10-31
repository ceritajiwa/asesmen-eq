import streamlit as st
import pandas as pd
from utils.styles import apply_ceritajiwa_styles
from utils.auth import require_role, logout_user

st.set_page_config(page_title="Admin - Cerita Jiwa", page_icon="⚙️", layout="wide")
apply_ceritajiwa_styles()
require_role(["admin"])

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Admin Panel</p>", unsafe_allow_html=True)
    if st.button("🚪 Logout", use_container_width=True, key="logout_admin"):
        logout_user()
        st.switch_page("app.py")

st.title("⚙️ Dashboard Admin")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Peserta", "45")
c2.metric("Menunggu Verifikasi", "5")
c3.metric("Aktif", "32")
c4.metric("Lulus", "8")

st.divider()

st.subheader("📤 Upload Peserta Batch")
uploaded = st.file_uploader("Upload CSV (kolom: nama, email, wa, sertifikasi, batch)", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df, use_container_width=True)
    if st.button("💾 Simpan ke Database", type="primary"):
        st.success(f"✅ {len(df)} peserta berhasil ditambahkan! Password default: 123456")

st.divider()

st.subheader("📋 Daftar Peserta")
st.dataframe({
    "Nama": ["Budi S.", "Ani R.", "Citra D.", "Dedi K.", "Eka L."],
    "Email": ["budi@gmail.com", "ani@gmail.com", "citra@gmail.com", "dedi@gmail.com", "eka@gmail.com"],
    "Sertifikasi": ["CERC", "CERC", "CMBC", "CERC", "CPSC"],
    "Batch": ["Agustus 2026", "Agustus 2026", "Sept 2026", "Agustus 2026", "Okt 2026"],
    "Status": ["Aktif", "Aktif", "Pending", "Lulus", "Aktif"],
    "Ujian": ["⏳ -", "⏳ -", "—", "✅ 85", "⏳ -"],
    "Asesmen": ["✅ Done", "⏳ On Progress", "—", "✅ Done", "✅ Done"]
}, use_container_width=True)
