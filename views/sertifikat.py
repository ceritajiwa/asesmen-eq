import pandas as pd
import streamlit as st

from cjlib import pdf
from cjlib.db import (DatabaseError, cari_respondent, format_tanggal, jawaban_respondent, judul_paket,
                      nomor_sertifikat, riwayat_ujian)
from cjlib.hasil import pdf_individu
from cjlib.styles import footer, page_header
from cjlib.ui import peserta_sidebar, require_peserta_gate, show_db_error
from scoring import compute_dim_scores, responses_to_answers

training, peserta = require_peserta_gate("📜 Sertifikat")
peserta_sidebar("sertifikat")

page_header("📜 Hasil & Sertifikat", f"{training['nama']} · {peserta['nama']}")
nama_file = peserta["nama"].replace(" ", "_")

try:
    riwayat = riwayat_ujian(training["id"], peserta["email"])
except DatabaseError as e:
    riwayat = []
    show_db_error(e)

# Kelulusan pertama per paket ujian
lulus_per_paket = {}
for r in riwayat:
    if r.get("passed") and r.get("package") not in lulus_per_paket:
        lulus_per_paket[r.get("package")] = r

if lulus_per_paket:
    for paket, att in lulus_per_paket.items():
        nomor = nomor_sertifikat(att, training.get("sertifikasi"))
        tanggal = format_tanggal(att.get("created_at"))
        with st.container(border=True, key=f"card_sertifikat_{paket}"):
            st.markdown(f"**{judul_paket(paket) or 'Ujian Sertifikasi'}**")
            c1, c2, c3 = st.columns(3)
            c1.metric("Status", "LULUS")
            c2.metric("No. Sertifikat", nomor)
            c3.metric("Tanggal Lulus", tanggal)
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    "📥 Download Sertifikat PDF",
                    data=pdf.sertifikat(peserta["nama"],
                                        pdf.judul_program(paket or training.get("sertifikasi"),
                                                          judul_paket(paket) or training["nama"]),
                                        nomor, tanggal),
                    file_name=f"sertifikat_{(paket or 'cj').lower()}_{nama_file}.pdf", mime="application/pdf",
                    type="primary", width="stretch", key=f"dl_sert_{paket}")
            with col2:
                st.download_button(
                    "🏅 Download Badge",
                    data=pdf.badge_png(paket or "CJ", peserta["nama"], nomor),
                    file_name=f"badge_{(paket or 'cj').lower()}_{nama_file}.png", mime="image/png",
                    width="stretch", key=f"dl_badge_{paket}")
else:
    with st.container(border=True, key="card_sertifikat_none"):
        c1, c2, c3 = st.columns(3)
        c1.metric("Status", "BELUM LULUS" if riwayat else "BELUM UJIAN")
        c2.metric("Jumlah Percobaan", len(riwayat))
        c3.metric("Nilai Tertinggi", max((r.get("score") or 0) for r in riwayat) if riwayat else "-")
        st.info("Sertifikat bisa diunduh setelah lulus ujian di menu 📋 Ujian.")

st.subheader("📊 Riwayat Ujian")
if riwayat:
    st.dataframe(
        pd.DataFrame([{
            "Percobaan": i + 1,
            "Paket": r.get("package") or "-",
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
    resp = cari_respondent(training["id"], peserta["email"])
    scores = compute_dim_scores(responses_to_answers(jawaban_respondent(resp["id"]))) if resp else {}
except Exception as e:  # noqa: BLE001
    resp, scores = None, {}
    show_db_error(DatabaseError(str(e)))

if resp and scores:
    st.download_button("📥 Download Report Asesmen",
                       data=pdf_individu(resp["full_name"], training["nama"], resp.get("department"),
                                         resp.get("job_level"), scores),
                       file_name=f"Hasil_Asesmen_{nama_file}.pdf", mime="application/pdf", width="stretch")
else:
    st.caption("Report asesmen tersedia setelah asesmen diisi di menu 📝 Asesmen.")

footer()
