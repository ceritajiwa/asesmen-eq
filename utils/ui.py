"""Komponen yang dipakai bersama oleh halaman peserta (Asesmen, Training, Ujian, Sertifikat)."""
import re

import streamlit as st

from utils.auth import (
    clear_training_session, get_peserta, get_training, is_peserta_set,
    is_training_set, set_peserta, set_training_session,
)
from utils.db import DatabaseError, get_trainings, training_label, verifikasi_kode_akses
from utils.styles import esc, footer, page_header
from utils.supabase_client import SupabaseNotConfigured

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def show_db_error(e: Exception):
    if isinstance(e, SupabaseNotConfigured):
        st.error(str(e))
    else:
        st.error("Tidak bisa mengambil data dari database. Coba muat ulang halaman, "
                 "atau hubungi admin kalau masih bermasalah.")
        with st.expander("Detail teknis (untuk admin)"):
            st.code(str(e))


def _narrow():
    """Kolom tengah supaya form login tidak terlalu lebar di layar besar."""
    _, mid, _ = st.columns([1, 2, 1])
    return mid


def _form_kode_akses(page_title: str):
    with _narrow():
        st.image("assets/logo_dark.png", width=96)
        page_header(page_title, "Pilih training lalu masukkan kode akses dari trainer.", eyebrow="Langkah 1 dari 2")

        try:
            trainings = get_trainings(only_active=True)
        except (DatabaseError, SupabaseNotConfigured) as e:
            show_db_error(e)
            st.stop()

        if not trainings:
            st.info("Belum ada training yang dibuka saat ini.")
            st.stop()

        options = {t["id"]: training_label(t) for t in trainings}
        with st.form("form_kode_akses", border=True):
            selected = st.selectbox("Pilih Training", options=list(options.keys()),
                                    format_func=lambda x: options[x])
            kode = st.text_input("Kode Akses", placeholder="Masukkan kode dari trainer")
            submit = st.form_submit_button("Masuk", type="primary", width="stretch")

        if submit:
            if not kode.strip():
                st.error("Kode akses wajib diisi.")
            else:
                try:
                    data = verifikasi_kode_akses(selected, kode)
                except DatabaseError as e:
                    show_db_error(e)
                    st.stop()
                if data:
                    set_training_session(data)
                    st.rerun()
                else:
                    st.error("Kode akses tidak cocok untuk training ini. Cek lagi huruf dan angkanya, ya.")
    footer()
    st.stop()


def _form_peserta(page_title: str):
    training = get_training()
    detail = " · ".join(x for x in [training.get("perusahaan"), f"Batch {training['batch']}" if training.get("batch") else ""] if x)
    with _narrow():
        st.image("assets/logo_dark.png", width=96)
        page_header(page_title, eyebrow="Langkah 2 dari 2")
        st.markdown(
            f"<div class='cj-card' style='padding:16px 20px;'>"
            f"<p style='margin:0; font-weight:800; color:#344A61;'>{esc(training['nama'])}</p>"
            + (f"<p style='margin:2px 0 0; color:#6D6F71;'>{esc(detail)}</p>" if detail else "") +
            f"</div>",
            unsafe_allow_html=True,
        )
        with st.form("form_peserta", border=True):
            nama = st.text_input("Nama Lengkap", help="Tulis sesuai nama yang ingin dicetak di sertifikat.")
            email = st.text_input("Email")
            submit = st.form_submit_button("Lanjutkan", type="primary", width="stretch")
        if submit:
            if not nama.strip() or not email.strip():
                st.error("Nama dan email wajib diisi.")
            elif not EMAIL_RE.match(email.strip()):
                st.error("Format email belum benar.")
            else:
                set_peserta(nama, email)
                st.rerun()
        if st.button("← Ganti training", key="ganti_training"):
            clear_training_session()
            st.rerun()
    footer()
    st.stop()


def subjudul(training: dict, peserta: dict) -> str:
    """Baris keterangan di bawah judul halaman: nama peserta · perusahaan · batch (yang kosong dilewati)."""
    bagian = [peserta.get("nama"), training.get("perusahaan"),
              f"Batch {training['batch']}" if training.get("batch") else None]
    if not training.get("perusahaan"):
        bagian.insert(1, training.get("nama"))
    return " · ".join(str(b) for b in bagian if b)


def require_peserta_gate(page_title: str):
    """Tampilkan form kode akses / data peserta kalau belum lengkap.
    Kalau sudah lengkap, kembalikan (training, peserta)."""
    if not is_training_set():
        _form_kode_akses(page_title)
    if not is_peserta_set():
        _form_peserta(page_title)
    return get_training(), get_peserta()


def peserta_sidebar(page_key: str):
    training, peserta = get_training(), get_peserta()
    with st.sidebar:
        st.markdown(
            f"<div style='padding:6px 0 4px;'>"
            f"<p style='font-size:16px; font-weight:800; margin:0;'>{esc(peserta['nama'])}</p>"
            f"<p style='opacity:.7; font-size:12px; margin:2px 0 0;'>{esc(training['nama'])}</p>"
            f"<p style='opacity:.7; font-size:12px; margin:0;'>Kode: {esc(training['kode'])}</p>"
            f"</div><hr>",
            unsafe_allow_html=True,
        )
        if st.button("🚪 Keluar", width="stretch", key=f"keluar_{page_key}"):
            clear_training_session()
            st.switch_page("views/beranda.py")
