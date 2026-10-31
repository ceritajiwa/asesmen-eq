import base64
from pathlib import Path

import streamlit as st

from cjlib.styles import esc, footer

# ---------- Hero ----------
_logo = base64.b64encode(Path("assets/logo_dark.png").read_bytes()).decode()
st.markdown(
    f"<div style='text-align:center;'><img src='data:image/png;base64,{_logo}' "
    f"alt='Cerita Jiwa' style='width:200px; max-width:60%;'></div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div style='text-align:center; margin-top:-8px;'>"
    "<p class='cj-eyebrow' style='margin-bottom:6px;'>Training Center</p>"
    "<h2 style='margin:0 0 6px;'>Sertifikasi Profesional untuk Kesehatan Mental</h2>"
    "<p style='color:#6D6F71; font-size:17px; margin:0;'>Asesmen, training, ujian, sampai sertifikat dalam satu tempat.</p>"
    "</div>",
    unsafe_allow_html=True,
)
st.write("")

# ---------- Menu (sama seperti sebelumnya) ----------
with st.container(key="menu_beranda"):
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📝 Asesmen", width="stretch", key="menu_asesmen"):
            st.switch_page("views/asesmen.py")
        if st.button("🎓 Training", width="stretch", key="menu_training"):
            st.switch_page("views/training.py")
        if st.button("📋 Ujian", width="stretch", key="menu_ujian"):
            st.switch_page("views/ujian.py")
    with c2:
        if st.button("📜 Sertifikat", width="stretch", key="menu_sertifikat"):
            st.switch_page("views/sertifikat.py")
        if st.button("🔍 Cek Sertifikasi", width="stretch", key="menu_verifikasi"):
            st.switch_page("views/verifikasi.py")
    with c3:
        if st.button("⚙️ Admin", width="stretch", key="menu_admin"):
            st.switch_page("views/admin.py")
        if st.button("👨‍🏫 Trainer / BEI", width="stretch", key="menu_trainer"):
            st.switch_page("views/trainer.py")

st.divider()

# ---------- Program sertifikasi ----------
st.markdown(
    "<div style='text-align:center; margin-bottom:18px;'>"
    "<h3 style='margin:0;'>Program Sertifikasi</h3>"
    "<p style='color:#6D6F71; margin:4px 0 0;'>CERC | CMBC | CPSC | CPPC | CRWC | CCTC</p>"
    "</div>",
    unsafe_allow_html=True,
)

sertifikasi = [
    ("CERC", "Certified Emotional Regulation Coach", "Mengelola emosi dengan bijak"),
    ("CMBC", "Certified Money Behavior Coach", "Memahami perilaku finansial"),
    ("CPSC", "Certified Psychology of Sales Coach", "Psikologi dalam penjualan"),
    ("CPPC", "Certified Positive Parenting Coach", "Parenting yang positif"),
    ("CRWC", "Certified Relationship Wellbeing Coach", "Kesehatan relasi"),
    ("CCTC", "Certified Complex Trauma Coach", "Penanganan trauma kompleks"),
]
for row in range(0, len(sertifikasi), 3):
    cols = st.columns(3)
    for col, (kode, nama, desk) in zip(cols, sertifikasi[row:row + 3]):
        with col:
            st.markdown(
                f"<div class='cj-card cj-cert'><p class='kode'>{esc(kode)}</p>"
                f"<p class='nama'>{esc(nama)}</p><p class='desk'>{esc(desk)}</p></div>",
                unsafe_allow_html=True,
            )

footer()
