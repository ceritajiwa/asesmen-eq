import plotly.graph_objects as go
import streamlit as st

from cjlib import pdf
from cjlib.db import DatabaseError, simpan_asesmen
from cjlib.konten import hitung_hasil_asesmen, instrumen_untuk, skala_item, skor_item
from cjlib.styles import esc, footer, page_header
from cjlib.ui import peserta_sidebar, require_peserta_gate, show_db_error, subjudul

training, peserta = require_peserta_gate("📝 Asesmen")
peserta_sidebar("asesmen")

page_header(f"📝 Asesmen {training['sertifikasi'] or ''}", subjudul(training, peserta))

instrumen_list, belum_ada = instrumen_untuk(training)
mode_demo = any(ins.get("demo") for _, ins in instrumen_list)
total_soal = sum(len(ins["items"]) for _, ins in instrumen_list)

if belum_ada:
    st.warning("Instrumen berikut sudah dipilih admin tapi soalnya belum dimasukkan ke aplikasi: "
               + ", ".join(f"**{n}**" for n in belum_ada))
if mode_demo:
    st.info("Ini **soal contoh**. Hasilnya bisa dilihat dan diunduh, tapi tidak disimpan ke database.")

st.caption(f"Ada {total_soal} pertanyaan. Semua ada di halaman ini, cukup scroll ke bawah. "
           "Jawaban baru dikirim setelah tombol **Submit Asesmen** ditekan.")

# ---------------- Semua soal dalam satu form (tidak reload sampai submit) ----------------
with st.form("form_asesmen", border=False):
    nomor = 0
    for nama_ins, ins in instrumen_list:
        dimensi_terakhir = None
        with st.container(border=True, key=f"card_ins_{nama_ins}"):
            st.subheader(ins["judul"])
            for i, item in enumerate(ins["items"]):
                nomor += 1
                if item.get("dimensi") and item["dimensi"] != dimensi_terakhir:
                    dimensi_terakhir = item["dimensi"]
                    st.markdown(f"<p class='cj-eyebrow' style='margin-top:12px;'>{esc(dimensi_terakhir)}</p>",
                                unsafe_allow_html=True)
                st.radio(f"{nomor}. {item['teks']}", skala_item(ins, item), index=None,
                         key=f"as_{nama_ins}_{i}", horizontal=True)
    kirim = st.form_submit_button("Submit Asesmen", type="primary", width="stretch")

if kirim:
    jawaban, detail, kosong = [], [], []
    nomor = 0
    for nama_ins, ins in instrumen_list:
        for i, item in enumerate(ins["items"]):
            nomor += 1
            pilihan = st.session_state.get(f"as_{nama_ins}_{i}")
            if pilihan is None:
                kosong.append(nomor)
                continue
            idx = skala_item(ins, item).index(pilihan)
            jawaban.append({"instrument": nama_ins, "item_n": i + 1, "score": skor_item(ins, item, idx)})
            detail.append({"teks": item["teks"], "jawaban": pilihan})

    if kosong:
        st.error(f"Masih ada {len(kosong)} pertanyaan yang belum dijawab: nomor "
                 + ", ".join(map(str, kosong)) + ". Jawaban yang sudah diisi tetap ada di halaman ini.")
    else:
        if not mode_demo:
            try:
                simpan_asesmen(training["id"], peserta["nama"], peserta["email"], jawaban)
            except DatabaseError as e:
                show_db_error(e)
                st.stop()
        st.session_state.asesmen_done = True
        st.session_state.asesmen_hasil = {
            "hasil": hitung_hasil_asesmen(instrumen_list, jawaban), "detail": detail,
        }

# ---------------- Hasil ----------------
hasil_simpan = st.session_state.get("asesmen_hasil")
if hasil_simpan:
    hasil = hasil_simpan["hasil"]
    st.success("✅ Asesmen selesai!" + ("" if mode_demo else " Jawaban sudah tersimpan."))
    kategori = [h["dimensi"] for h in hasil]
    nilai = [h["skor"] for h in hasil]
    c1, c2 = st.columns(2)
    if len(hasil) >= 3:
        with c1:
            fig = go.Figure(data=go.Scatterpolar(
                r=nilai + [nilai[0]], theta=kategori + [kategori[0]], fill="toself",
                fillcolor="rgba(52,74,97,0.25)", line=dict(color="#344A61", width=2.5)))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False,
                              title="Profil Kompetensi Emosional")
            st.plotly_chart(fig, width="stretch")
    with (c2 if len(hasil) >= 3 else c1):
        fig2 = go.Figure(go.Bar(x=kategori, y=nilai, marker_color="#344A61", text=nilai, textposition="outside"))
        fig2.update_layout(title="Skor per Dimensi (0-100)", yaxis_range=[0, 110])
        st.plotly_chart(fig2, width="stretch")

    st.download_button(
        "📥 Download Report PDF",
        data=pdf.laporan_asesmen(training, peserta, hasil, hasil_simpan["detail"]),
        file_name=f"asesmen_{(training['sertifikasi'] or 'cj').lower()}_{peserta['nama'].replace(' ', '_')}.pdf",
        mime="application/pdf", type="primary",
    )
    st.info("💡 Simpan report ini untuk dibahas saat sesi training.")

footer()
