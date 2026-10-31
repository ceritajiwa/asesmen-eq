import pandas as pd
import streamlit as st

from utils.auth import check_password, is_admin_logged_in
from utils.db import (
    SERTIFIKASI_LIST, DatabaseError, create_training, get_trainings,
    set_training_status, training_label, _is_aktif,
)
from utils.styles import footer, page_header
from utils.supabase_client import SupabaseNotConfigured
from utils.ui import show_db_error

# ---------------- Login ----------------
if not is_admin_logged_in():
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.image("assets/logo_dark.png", width=96)
        page_header("⚙️ Admin Panel", "Masukkan password admin.")
        with st.form("form_admin_login", border=True):
            password = st.text_input("Password Admin", type="password")
            submit = st.form_submit_button("Masuk", type="primary", width="stretch")
        if submit:
            if not password:
                st.error("Password wajib diisi.")
            else:
                ok = check_password(password, "ADMIN_PASSWORD")
                if ok is None:
                    st.error("ADMIN_PASSWORD belum diatur di Secrets Streamlit.")
                elif ok:
                    st.session_state.admin_logged_in = True
                    st.rerun()
                else:
                    st.error("Password salah.")
    footer()
    st.stop()

with st.sidebar:
    st.markdown("<p style='font-weight:800; margin:6px 0 0;'>Admin Panel</p><hr>", unsafe_allow_html=True)
    if st.button("🚪 Logout", width="stretch", key="logout_admin"):
        st.session_state.admin_logged_in = False
        st.switch_page("views/beranda.py")

page_header("⚙️ Dashboard Admin")

try:
    semua = get_trainings(only_active=False)
except (DatabaseError, SupabaseNotConfigured) as e:
    show_db_error(e)
    st.stop()

aktif = [t for t in semua if _is_aktif(t["status"])]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Training", len(semua))
c2.metric("Aktif", len(aktif))
c3.metric("Total Peserta", "45")
c4.metric("Lulus", "8")

st.divider()

# ---------------- Daftar training ----------------
h1, h2 = st.columns([4, 1])
with h1:
    st.subheader("📋 Daftar Training")
with h2:
    if st.button("🔄 Muat ulang", width="stretch"):
        get_trainings.clear()
        st.rerun()

if semua:
    df = pd.DataFrame([{
        "Nama Training": t["nama"], "Perusahaan": t["perusahaan"], "Sertifikasi": t["sertifikasi"],
        "Batch": t["batch"], "Tanggal": t["tanggal"], "Kode Akses": t["kode_akses"],
        "Status": "Aktif" if _is_aktif(t["status"]) else "Nonaktif",
    } for t in semua])
    st.dataframe(df, hide_index=True, width="stretch")

    with st.expander("Aktifkan / nonaktifkan training"):
        st.caption("Training yang nonaktif tidak muncul di pilihan peserta dan kodenya tidak bisa dipakai login.")
        opts = {t["id"]: f"{training_label(t)}  ({'Aktif' if _is_aktif(t['status']) else 'Nonaktif'})" for t in semua}
        pilih = st.selectbox("Training", list(opts.keys()), format_func=lambda x: opts[x], key="status_pilih")
        b1, b2 = st.columns(2)
        try:
            if b1.button("Aktifkan", width="stretch"):
                set_training_status(pilih, True)
                st.rerun()
            if b2.button("Nonaktifkan", width="stretch"):
                set_training_status(pilih, False)
                st.rerun()
        except DatabaseError as e:
            show_db_error(e)
else:
    st.info("Belum ada training di database.")

st.divider()

# ---------------- Buat training baru ----------------
st.subheader("➕ Buat Training Baru")
with st.form("form_training_baru", border=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        sert = st.selectbox("Sertifikasi", SERTIFIKASI_LIST, key="admin_sert")
        perusahaan = st.text_input("Nama Perusahaan", placeholder="PT Maju Jaya")
    with col2:
        batch = st.text_input("Batch", "Agustus 2026", key="admin_batch")
        tanggal = st.date_input("Tanggal Training")
    with col3:
        jumlah_peserta = st.number_input("Jumlah Peserta", min_value=1, max_value=100, value=20)
    simpan = st.form_submit_button("Generate Kode Akses & Simpan", type="primary")

if simpan:
    if not perusahaan.strip() or not batch.strip():
        st.error("Nama perusahaan dan batch wajib diisi.")
    else:
        try:
            baru = create_training(sert, perusahaan.strip(), batch.strip(), tanggal)
            st.success("✅ Training berhasil dibuat dan tersimpan di database!")
            st.code(f"Kode Akses: {baru['kode_akses']}", language=None)
            st.info("Bagikan kode akses ini ke peserta training tersebut.")
        except DatabaseError as e:
            show_db_error(e)

st.divider()

# ---------------- Upload peserta (masih demo) ----------------
st.subheader("📤 Upload Peserta")
uploaded = st.file_uploader("Upload CSV (kolom: nama, email, wa)", type=["csv"])
if uploaded:
    df_up = pd.read_csv(uploaded)
    st.dataframe(df_up, width="stretch")
    if st.button("💾 Simpan ke Database", type="primary"):
        st.success(f"✅ {len(df_up)} peserta ditambahkan!")

footer()
