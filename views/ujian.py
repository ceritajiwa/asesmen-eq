import streamlit as st

from utils.styles import footer, page_header
from utils.ui import peserta_sidebar, require_peserta_gate, subjudul

training, peserta = require_peserta_gate("📋 Ujian")
peserta_sidebar("ujian")

col1, col2 = st.columns([3, 1])
with col1:
    page_header(f"📋 Ujian {training['sertifikasi'] or ''}",
                subjudul(training, peserta))
with col2:
    st.metric("⏱️ Sisa Waktu", "45:00")

st.progress(0, text="Soal 1 dari 20")
soal_list = [
    ("Dalam teknik active listening, hal yang paling penting adalah...", ["Memberi saran cepat", "Menunjukkan empati", "Mengalihkan pembicaraan", "Mengkritik perasaan klien"], 1),
    ("Apa tujuan utama dari emotional regulation?", ["Menekan emosi", "Mengelola emosi secara konstruktif", "Menghindari konflik", "Bersikap netral"], 1),
    ("Teknik grounding paling efektif dilakukan saat...", ["Santai", "Sedang panik/cemas", "Sedang tidur", "Sedang makan"], 1),
]
jawaban = []
for i, (pertanyaan, opsi, benar) in enumerate(soal_list):
    with st.container(border=True, key=f"card_soal_{i}"):
        st.subheader(f"Soal {i + 1}")
        j = st.radio(pertanyaan, opsi, key=f"soal_ujian_{i}")
        jawaban.append(opsi.index(j))
st.progress(15, text="Soal 3 dari 20")

c1, c2, c3 = st.columns(3)
with c1:
    st.button("← Sebelumnya", disabled=True, key="btn_prev", width="stretch")
with c2:
    st.button("🚩 Ragu-ragu", key="btn_doubt", width="stretch")
with c3:
    st.button("Selanjutnya →", key="btn_next", width="stretch")

st.divider()
if st.button("✅ Submit Ujian", type="primary", key="btn_submit_ujian"):
    nilai = 85
    st.session_state.ujian_attempts += 1
    st.session_state.current_nilai = nilai
    if nilai >= 80:
        st.success(f"🎉 Selamat! Anda lulus dengan nilai {nilai}!")
        st.balloons()
        st.markdown(f"🏷️ Running Key: **{training['sertifikasi']}-2026-000089**")
    else:
        st.warning(f"Nilai Anda: {nilai}. Belum memenuhi (minimum 80).")
        st.info(f"Percobaan ke-{st.session_state.ujian_attempts}. Silakan ulangi.")

footer()
