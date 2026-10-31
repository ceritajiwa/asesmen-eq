import streamlit as st
import pandas as pd
from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session, is_admin_logged_in, MOCK_TRAININGS

apply_ceritajiwa_styles()
init_session()

if not is_admin_logged_in():
    st.image("assets/logo_dark.png", width=120)
    st.title("⚙️ Admin Panel")
    st.markdown("Masukkan password admin.")
    password = st.text_input("Password Admin", type="password")
    if st.button("Masuk", type="primary"):
        if not password:
            st.error("Password wajib diisi.")
        else:
            admin_pass = st.secrets.get("ADMIN_PASSWORD", "asesmencerc12")
            if password == admin_pass:
                st.session_state.admin_logged_in = True
                st.success("Login admin berhasil!")
                st.rerun()
            else:
                st.error("Password salah.")
    st.stop()

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Admin Panel</p>", unsafe_allow_html=True)
    if st.button("🚪 Logout", use_container_width=True, key="logout_admin"):
        st.session_state.admin_logged_in = False
        st.switch_page("app.py")

st.title("⚙️ Dashboard Admin")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Training", str(len(MOCK_TRAININGS)))
c2.metric("Aktif", str(len(MOCK_TRAININGS)))
c3.metric("Total Peserta", "45")
c4.metric("Lulus", "8")

st.divider()

st.subheader("📋 Daftar Training")
data_table = []
for tid, info in MOCK_TRAININGS.items():
    data_table.append({
        "ID": tid, "Nama Training": info["nama_training"], "Perusahaan": info["perusahaan"],
        "Sertifikasi": info["sertifikasi"], "Batch": info["batch"],
        "Kode Akses": info["kode_akses"], "Status": info["status"],
    })
st.dataframe(data_table, use_container_width=True)

st.divider()
st.subheader("➕ Buat Training Baru")
col1, col2, col3 = st.columns(3)
with col1:
    sert = st.selectbox("Sertifikasi", ["CERC", "CMBC", "CPSC", "CPPC", "CRWC", "CCTC"], key="admin_sert")
    perusahaan = st.text_input("Nama Perusahaan", placeholder="PT Maju Jaya")
with col2:
    batch = st.text_input("Batch", "Agustus 2026", key="admin_batch")
    tanggal = st.date_input("Tanggal Training")
with col3:
    jumlah_peserta = st.number_input("Jumlah Peserta", min_value=1, max_value=100, value=20)

if st.button("Generate Kode Akses & Simpan", type="primary"):
    import random
    kode = f"{sert}-{batch[:3].upper()}-{random.randint(100,999)}"
    st.success(f"✅ Training berhasil dibuat!")
    st.code(f"Kode Akses: {kode}", language=None)
    st.info("Simpan kode akses ini dan bagikan ke peserta.")

st.divider()
st.subheader("📤 Upload Peserta")
uploaded = st.file_uploader("Upload CSV (kolom: nama, email, wa)", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df, use_container_width=True)
    if st.button("💾 Simpan ke Database", type="primary"):
        st.success(f"✅ {len(df)} peserta ditambahkan!")
