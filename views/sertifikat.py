import streamlit as st

from utils.styles import footer, page_header
from utils.ui import peserta_sidebar, require_peserta_gate

training, peserta = require_peserta_gate("📜 Sertifikat")
peserta_sidebar("sertifikat")

sert = str(training["sertifikasi"])
page_header("📜 Hasil & Sertifikat", f"{sert} · {peserta['nama']}")

with st.container(border=True, key="card_sertifikat_1"):
    c1, c2, c3 = st.columns(3)
    c1.metric("Status", "LULUS")
    c2.metric("Running Key", f"{sert}-2026-000089")
    c3.metric("Tanggal Lulus", "15 Agustus 2026")
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("📥 Download Sertifikat PDF", b"Mock PDF", f"sertifikat_{sert.lower()}.pdf",
                           type="primary", width="stretch")
    with col2:
        st.download_button("🏅 Download Badge", b"Mock PNG", f"badge_{sert.lower()}.png", width="stretch")

st.subheader("📊 Riwayat Ujian")
st.dataframe(
    {"Percobaan": [1, 2, 3], "Nilai": [65, 72, 85], "Status": ["❌ Gagal", "❌ Gagal", "✅ Lulus"],
     "Waktu": ["16:05", "16:25", "16:45"]},
    hide_index=True, width="stretch",
)

st.subheader("📝 Report Asesmen")
st.download_button("📥 Download Report Asesmen", b"Mock PDF", f"asesmen_{sert.lower()}_report.pdf", width="stretch")

footer()
