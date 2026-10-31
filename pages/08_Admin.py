import streamlit as st
import pandas as pd
from utils.styles import apply_ceritajiwa_styles
from utils.auth import require_akses, get_peserta, clear_akses, MOCK_KODE_DATABASE

st.set_page_config(page_title="Admin - Cerita Jiwa", page_icon="⚙️", layout="wide")
apply_ceritajiwa_styles()

# Admin bisa pakai kode akses admin atau langsung akses (untuk demo)
if not st.session_state.get("kode_akses"):
    st.warning("Halaman Admin. Masukkan kode akses admin.")
    kode = st.text_input("Kode Admin", placeholder="ADMIN-001")
    if st.button("Masuk"):
        if kode.upper() == "ADMIN-001":
            from utils.auth import set_akses
            set_akses("ADMIN-001", "Admin", "Admin", "All")
            st.rerun()
        else:
            st.error("Kode admin tidak valid.")
    st.stop()

peserta = get_peserta()

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Admin Panel</p>", unsafe_allow_html=True)
    if st.button("🚪 Logout", use_container_width=True, key="logout_admin"):
        clear_akses()
        st.switch_page("app.py")

st.title("⚙️ Dashboard Admin")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Peserta", str(len(MOCK_KODE_DATABASE)))
c2.metric("Menunggu Verifikasi", "0")
c3.metric("Aktif", str(len(MOCK_KODE_DATABASE)))
c4.metric("Lulus", "0")

st.divider()

st.subheader("📤 Upload Peserta Batch")
uploaded = st.file_uploader("Upload CSV (kolom: nama, email, wa, sertifikasi, batch)", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df, use_container_width=True)
    if st.button("💾 Simpan ke Database", type="primary"):
        st.success(f"✅ {len(df)} peserta berhasil ditambahkan!")

st.divider()

st.subheader("📋 Daftar Kode Akses")

data_table = []
for kode, info in MOCK_KODE_DATABASE.items():
    data_table.append({
        "Kode Akses": kode,
        "Nama": info["nama"],
        "Sertifikasi": info["sertifikasi"],
        "Batch": info["batch"]
    })

st.dataframe(data_table, use_container_width=True)

st.divider()
st.subheader("➕ Generate Kode Akses Baru")
col1, col2, col3 = st.columns(3)
with col1:
    sert = st.selectbox("Sertifikasi", ["CERC", "CMBC", "CPSC", "CPPC", "CRWC", "CCTC"])
with col2:
    batch = st.text_input("Batch", "Agustus 2026")
with col3:
    jumlah = st.number_input("Jumlah", min_value=1, max_value=50, value=10)

if st.button("Generate Kode", type="primary"):
    st.success(f"✅ {jumlah} kode akses berhasil dibuat untuk {sert} - {batch}!")
    for i in range(1, jumlah + 1):
        st.code(f"{sert}-{batch[:3].upper()}-{i:03d}", language=None)
