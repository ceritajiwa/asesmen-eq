import pandas as pd
import streamlit as st

from utils.auth import check_password, is_admin_logged_in
from utils.db import (
    SERTIFIKASI_LIST, DatabaseError, create_training, format_tanggal, get_trainings,
    hitung_statistik, set_kode_akses, training_label,
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

aktif = [t for t in semua if t["aktif"]]
stat = hitung_statistik()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Training", len(semua))
c2.metric("Akses Dibuka", len(aktif))
c3.metric("Total Peserta", stat["peserta"] if stat["peserta"] is not None else "-")
c4.metric("Lulus", stat["lulus"] if stat["lulus"] is not None else "-")

st.divider()

# ---------------- Daftar training ----------------
h1, h2 = st.columns([4, 1])
with h1:
    st.subheader("📋 Daftar Training")
with h2:
    if st.button("🔄 Muat ulang", width="stretch"):
        get_trainings.clear()
        hitung_statistik.clear()
        st.rerun()

if semua:
    df = pd.DataFrame([{
        "Nama Training": t["nama"],
        "Sertifikasi": t["sertifikasi"] or "-",
        "Dibuat": format_tanggal(t["tanggal"]),
        "Kode Akses": t["kode_akses"] or "-",
        "Status": "Dibuka" if t["aktif"] else "Ditutup",
    } for t in semua])
    st.dataframe(df, hide_index=True, width="stretch")

    with st.expander("🔑 Atur kode akses training", expanded=bool(st.session_state.get("admin_kode_baru"))):
        st.caption("Training tanpa kode akses tidak muncul di pilihan peserta. "
                   "Membuat kode baru akan menggantikan kode lama, jadi kode lama langsung tidak berlaku.")
        opts = {t["id"]: f"{training_label(t)}  ({'Dibuka' if t['aktif'] else 'Ditutup'})" for t in semua}
        pilih_id = st.selectbox("Training", list(opts.keys()), format_func=lambda x: opts[x], key="kode_pilih")
        pilih = next(t for t in semua if t["id"] == pilih_id)
        b1, b2 = st.columns(2)
        try:
            if b1.button("Buat kode akses baru", type="primary", width="stretch"):
                kode = set_kode_akses(pilih, buka=True)
                st.session_state["admin_kode_baru"] = (pilih["nama"], kode)
                st.rerun()
            if b2.button("Tutup akses (hapus kode)", width="stretch", disabled=not pilih["aktif"]):
                set_kode_akses(pilih, buka=False)
                st.session_state.pop("admin_kode_baru", None)
                st.rerun()
        except DatabaseError as e:
            show_db_error(e)
        if st.session_state.get("admin_kode_baru"):
            nama, kode = st.session_state["admin_kode_baru"]
            st.success(f"Kode akses baru untuk **{nama}**:")
            st.code(kode, language=None)
else:
    st.info("Belum ada training di database.")

st.divider()

# ---------------- Buat training baru ----------------
st.subheader("➕ Buat Training Baru")
with st.form("form_training_baru", border=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        sert = st.selectbox("Sertifikasi", SERTIFIKASI_LIST, key="admin_sert")
    with col2:
        perusahaan = st.text_input("Nama Perusahaan", placeholder="PT Maju Jaya")
    with col3:
        batch = st.text_input("Batch", "Agustus 2026", key="admin_batch")
    st.caption("Nama training akan tersimpan dengan format: SERTIFIKASI - PERUSAHAAN - BATCH")
    simpan = st.form_submit_button("Generate Kode Akses & Simpan", type="primary")

if simpan:
    if not perusahaan.strip() or not batch.strip():
        st.error("Nama perusahaan dan batch wajib diisi.")
    else:
        try:
            baru = create_training(sert, perusahaan.strip(), batch.strip())
            st.success(f"✅ Training **{baru['nama']}** berhasil dibuat dan tersimpan di database!")
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
