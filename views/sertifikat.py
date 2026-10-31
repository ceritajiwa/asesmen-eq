import pandas as pd
import streamlit as st

from cjlib import pdf
from cjlib.db import DatabaseError, ambil_jawaban_asesmen, format_tanggal, nomor_sertifikat, riwayat_ujian
from cjlib.konten import hitung_hasil_asesmen, instrumen_untuk
from cjlib.styles import footer, page_header
from cjlib.ui import peserta_sidebar, require_peserta_gate, show_db_error

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
nama_file = peserta["nama"].replace(" ", "_")

with st.container(border=True, key="card_sertifikat_1"):
    c1, c2, c3 = st.columns(3)
    if lulus:
        pertama = lulus[0]
        nomor = nomor_sertifikat(sert, pertama)
        tanggal = format_tanggal(pertama.get("created_at"))
        c1.metric("Status", "LULUS")
        c2.metric("No. Sertifikat", nomor)
        c3.metric("Tanggal Lulus", tanggal)
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "📥 Download Sertifikat PDF",
                data=pdf.sertifikat(peserta["nama"], training["nama"], nomor, tanggal, pertama.get("score")),
                file_name=f"sertifikat_{sert.lower()}_{nama_file}.pdf", mime="application/pdf",
                type="primary", width="stretch")
        with col2:
            st.download_button(
                "🏅 Download Badge",
                data=pdf.badge_png(sert, peserta["nama"], nomor),
                file_name=f"badge_{sert.lower()}_{nama_file}.png", mime="image/png", width="stretch")
    else:
        c1.metric("Status", "BELUM LULUS" if riwayat else "BELUM UJIAN")
        c2.metric("Jumlah Percobaan", len(riwayat))
        c3.metric("Nilai Tertinggi", max((r.get("score") or 0) for r in riwayat) if riwayat else "-")
        st.info("Sertifikat bisa diunduh setelah lulus ujian.")

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
try:
    jawaban = ambil_jawaban_asesmen(training["id"], peserta["email"])
except DatabaseError:
    jawaban = []
instrumen_list, _ = instrumen_untuk(training)
hasil = hitung_hasil_asesmen(instrumen_list, jawaban) if jawaban else []
if not hasil and st.session_state.get("asesmen_hasil"):
    hasil = st.session_state.asesmen_hasil["hasil"]  # hasil asesmen contoh dari sesi ini

if hasil:
    st.download_button("📥 Download Report Asesmen",
                       data=pdf.laporan_asesmen(training, peserta, hasil),
                       file_name=f"asesmen_{sert.lower()}_{nama_file}.pdf", mime="application/pdf",
                       width="stretch")
else:
    st.caption("Report asesmen tersedia setelah asesmen diisi di menu 📝 Asesmen.")

footer()
