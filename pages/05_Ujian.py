import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import require_role, get_user

st.set_page_config(page_title="Ujian - Cerita Jiwa", page_icon="📋", layout="wide")
apply_ceritajiwa_styles()
require_role(["peserta", "admin", "trainer"])

user = get_user()

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Menu</p>", unsafe_allow_html=True)
    if st.button("← Dashboard", use_container_width=True):
        st.switch_page("pages/03_Dashboard.py")

st.title("📋 Ujian CERC")
st.markdown("Certified Emotional Regulation Coach")

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
    j = st.radio(pertanyaan, opsi, key=f"soal_{i}")
    jawaban.append(opsi.index(j))

st.progress(15, text="Soal 3 dari 20")

c1, c2, c3 = st.columns(3)
with c1:
    st.button("← Sebelumnya", disabled=True)
with c2:
    st.button("🚩 Ragu-ragu")
with c3:
    st.button("Selanjutnya →")

st.divider()

if st.button("✅ Submit Ujian", type="primary"):
    nilai = 85
    st.session_state.ujian_attempts += 1
    st.session_state.current_nilai = nilai

    if nilai >= 80:
        st.success(f"🎉 Selamat! Anda lulus dengan nilai {nilai}!")
        st.balloons()
        st.markdown("""
        **Sertifikat & Badge telah dikirim ke email Anda.**

        🏷️ Running Key: **CERC-2026-000089**
        """)
        st.session_state.sertifikasi_list[0]["status"] = "lulus"
    else:
        st.warning(f"Nilai Anda: {nilai}. Belum memenuhi (minimum 80).")
        st.info(f"Percobaan ke-{st.session_state.ujian_attempts}. Anda bisa mengulang kapan saja.")
        if st.button("🔄 Ulangi Ujian", type="primary"):
            st.rerun()
