import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import require_akses, get_peserta

st.set_page_config(page_title="Ujian - Cerita Jiwa", page_icon="📋", layout="wide")
apply_ceritajiwa_styles()
require_akses()

peserta = get_peserta()

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Menu</p>", unsafe_allow_html=True)
    st.page_link("pages/03_Dashboard.py", label="🏠 Dashboard")
    st.page_link("pages/04_Asesmen.py", label="📝 Asesmen")
    st.page_link("pages/05_Ujian.py", label="📋 Ujian", disabled=True)
    st.page_link("pages/06_Sertifikat.py", label="📜 Sertifikat")

st.title(f"📋 Ujian {peserta['sertifikasi']}")
st.markdown(f"Peserta: **{peserta['nama']}** | Batch: {peserta['batch']}")

col1, col2 = st.columns([3, 1])
with col2:
    st.metric("⏱️ Sisa Waktu", "45:00")

st.progress(0, text="Soal 1 dari 20")

soal_list = [
    ("Dalam teknik active listening, hal yang paling penting adalah...",
     ["Memberi saran cepat", "Menunjukkan empati", "Mengalihkan pembicaraan", "Mengkritik perasaan klien"], 1),
    ("Apa tujuan utama dari emotional regulation?",
     ["Menekan emosi", "Mengelola emosi secara konstruktif", "Menghindari konflik", "Bersikap netral"], 1),
    ("Teknik grounding paling efektif dilakukan saat...",
     ["Santai", "Sedang panik/cemas", "Sedang tidur", "Sedang makan"], 1),
]

jawaban = []
for i, (pertanyaan, opsi, benar) in enumerate(soal_list):
    st.subheader(f"Soal {i+1}")
    j = st.radio(pertanyaan, opsi, key=f"soal_ujian_{i}")
    jawaban.append(opsi.index(j))

st.progress(15, text="Soal 3 dari 20")

c1, c2, c3 = st.columns(3)
with c1:
    st.button("← Sebelumnya", disabled=True, key="btn_prev")
with c2:
    st.button("🚩 Ragu-ragu", key="btn_doubt")
with c3:
    st.button("Selanjutnya →", key="btn_next")

st.divider()

if st.button("✅ Submit Ujian", type="primary", key="btn_submit_ujian"):
    nilai = 85
    st.session_state.ujian_attempts += 1
    st.session_state.current_nilai = nilai

    if nilai >= 80:
        st.success(f"🎉 Selamat! Anda lulus dengan nilai {nilai}!")
        st.balloons()
        st.markdown(f"""
        **Sertifikat & Badge telah dikirim ke email Anda.**
        
        🏷️ Running Key: **{peserta['sertifikasi']}-2026-000089**
        """)
    else:
        st.warning(f"Nilai Anda: {nilai}. Belum memenuhi (minimum 80).")
        st.info(f"Percobaan ke-{st.session_state.ujian_attempts}. Anda bisa mengulang kapan saja.")
        if st.button("🔄 Ulangi Ujian", type="primary", key="btn_retry"):
            st.rerun()
