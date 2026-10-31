import pandas as pd
import streamlit as st

from utils.db import DatabaseError, format_tanggal, riwayat_ujian
from utils.styles import footer, page_header
from utils.ui import peserta_sidebar, require_peserta_gate, show_db_error

training, peserta = require_peserta_gate("📜 Sertifikat")
peserta_sidebar("sertifikat")

sert = str(training["sertifikasi"] or "CJ")
page_header("📜 Hasil & Sertifikat", f"{training['nama']} · {peserta['nama']}")

try:
    riwayat = riwayat_ujian(training["id"], peserta["email"])
except DatabaseError as e:
    riwayat = []
    show_db_error(e)

lulus = [r for r in riwayat if r.get("passed")]

with st.container(border=True, key="card_sertifikat_1"):
    c1, c2, c3 = st.columns(3)
    if lulus:
        c1.metric("Status", "LULUS")
        c2.metric("Nilai", lulus[0].get("score", "-"))
        c3.metric("Tanggal Lulus", format_tanggal(lulus[0].get("created_at")))
        col1, col2 = st.columns(2)
        with col1:
            st.download_button("📥 Download Sertifikat PDF", b"Mock PDF", f"sertifikat_{sert.lower()}.pdf",
                               type="primary", width="stretch")
        with col2:
            st.download_button("🏅 Download Badge", b"Mock PNG", f"badge_{sert.lower()}.png", width="stretch")
    else:
        c1.metric("Status", "BELUM LULUS" if riwayat else "BELUM UJIAN")
        c2.metric("Jumlah Percobaan", len(riwayat))
        c3.metric("Nilai Tertinggi", max((r.get("score") or 0) for r in riwayat) if riwayat else "-")
        st.info("Sertifikat bisa diunduh setelah lulus ujian (nilai minimum 80).")

st.subheader("📊 Riwayat Ujian")
if riwayat:
    st.dataframe(
        pd.DataFrame([{
            "Percobaan": i + 1,
            "Nilai": r.get("score"),
            "Jawaban Benar": r.get("correct"),
            "Status": "✅ Lulus" if r.get("passed") else "❌ Belum lulus",
            "Waktu": format_tanggal(r.get("created_at"), with_time=True),
        } for i, r in enumerate(riwayat)]),
        hide_index=True, width="stretch",
    )
else:
    st.caption(f"Belum ada data ujian untuk email {peserta['email']} di training ini.")

st.subheader("📝 Report Asesmen")
st.download_button("📥 Download Report Asesmen", b"Mock PDF", f"asesmen_{sert.lower()}_report.pdf", width="stretch")

footer()
