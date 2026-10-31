import streamlit as st

from cjlib.db import SERTIFIKASI_LIST, DatabaseError, cari_sertifikat
from cjlib.styles import esc, footer, page_header
from cjlib.supabase_client import SupabaseNotConfigured
from cjlib.ui import show_db_error

_, mid, _ = st.columns([1, 2, 1])
with mid:
    st.image("assets/logo_dark.png", width=96)
    page_header("🔍 Verifikasi Sertifikasi", "Cek keaslian sertifikasi Cerita Jiwa.")

    with st.form("form_verifikasi", border=True):
        sertifikasi = st.selectbox("Pilih Sertifikasi", SERTIFIKASI_LIST)
        cari = st.text_input("Masukkan Nama Lengkap atau No. Sertifikat", placeholder="Contoh: Budi Santoso atau CERC-2026-000089")
        submit = st.form_submit_button("Cari", type="primary", width="stretch")

    if submit:
        if len(cari.strip()) < 3:
            st.error("Masukkan minimal 3 huruf nama atau nomor sertifikat.")
        else:
            try:
                hasil = cari_sertifikat(sertifikasi, cari)
            except (DatabaseError, SupabaseNotConfigured) as e:
                show_db_error(e)
                hasil = None
            if hasil == []:
                st.warning("Data sertifikat tidak ditemukan. Cek lagi ejaan nama atau nomor sertifikatnya.")
            for h in hasil or []:
                st.markdown(
                    f"""
                <div style="background:#F0FAF8; border:1.5px solid #9ED3CC; border-radius:16px; padding:22px 24px; margin-bottom:12px;">
                    <h4 style="color:#2E7D74 !important; margin-top:0;">✅ Sertifikat Terverifikasi</h4>
                    <p><strong>Nama:</strong> {esc(h['nama'])}</p>
                    <p><strong>Training:</strong> {esc(h['training'])}</p>
                    <p><strong>No. Sertifikat:</strong> {esc(h['nomor'])}</p>
                    <p style="margin-bottom:0;"><strong>Tanggal Lulus:</strong> {esc(h['tanggal'])}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

footer()
