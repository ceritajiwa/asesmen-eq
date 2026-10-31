"""
Cerita Jiwa Training Center - entrypoint & router.

Semua halaman didaftarkan secara eksplisit di sini lewat st.navigation.
Folder `pages/` TIDAK dipakai lagi (Streamlit mengabaikannya otomatis kalau
st.navigation dipakai), jadi file lama yang tertinggal di repo tidak bisa
bikin error "Multiple Pages specified with URL pathname" lagi.
"""
import streamlit as st

from utils.styles import apply_ceritajiwa_styles
from utils.auth import init_session

st.set_page_config(
    page_title="Cerita Jiwa Training Center",
    page_icon="assets/logo_dark.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_ceritajiwa_styles()
init_session()

pages = [
    st.Page("views/beranda.py", title="Beranda", icon="🏠", url_path="beranda", default=True),
    st.Page("views/asesmen.py", title="Asesmen", icon="📝", url_path="asesmen"),
    st.Page("views/training.py", title="Training", icon="🎓", url_path="training"),
    st.Page("views/ujian.py", title="Ujian", icon="📋", url_path="ujian"),
    st.Page("views/sertifikat.py", title="Sertifikat", icon="📜", url_path="sertifikat"),
    st.Page("views/verifikasi.py", title="Cek Sertifikasi", icon="🔍", url_path="verifikasi"),
    st.Page("views/admin.py", title="Admin", icon="⚙️", url_path="admin"),
    st.Page("views/trainer.py", title="Trainer / BEI", icon="👨‍🏫", url_path="trainer"),
]

st.navigation(pages, position="sidebar").run()
