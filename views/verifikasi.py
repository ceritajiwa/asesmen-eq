import streamlit as st

from utils.db import SERTIFIKASI_LIST
from utils.styles import esc, footer, page_header

_, mid, _ = st.columns([1, 2, 1])
with mid:
    st.image("assets/logo_dark.png", width=96)
    page_header("🔍 Verifikasi Sertifikasi", "Cek keaslian sertifikasi Cerita Jiwa.")

    with st.form("form_verifikasi", border=True):
        sertifikasi = st.selectbox("Pilih Sertifikasi", SERTIFIKASI_LIST)
        cari = st.text_input("Masukkan Nama Lengkap atau Running Key", placeholder="Contoh: Budi Santoso")
        submit = st.form_submit_button("Cari", type="primary", width="stretch")

    if submit:
        if cari.strip():
            st.success("✅ Sertifikat Terverifikasi")
            st.markdown(
                f"""
            <div style="background:#F0FAF8; border:1.5px solid #9ED3CC; border-radius:16px; padding:22px 24px;">
                <h4 style="color:#2E7D74 !important; margin-top:0;">Data Lulusan</h4>
                <p><strong>Nama:</strong> Budi Santoso</p>
                <p><strong>Sertifikasi:</strong> {esc(sertifikasi)}</p>
                <p><strong>Running Key:</strong> {esc(sertifikasi)}-2026-000089</p>
                <p><strong>Tanggal Lulus:</strong> 15 Agustus 2026</p>
                <p style="margin-bottom:0;"><strong>Status:</strong> <span style="color:#2E7D74; font-weight:800;">Aktif</span></p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.error("Masukkan nama atau running key")

footer()
