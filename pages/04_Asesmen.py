import streamlit as st
import plotly.graph_objects as go
from utils.styles import apply_ceritajiwa_styles
from utils.auth import require_role, get_user

st.set_page_config(page_title="Asesmen - Cerita Jiwa", page_icon="📝", layout="wide")
apply_ceritajiwa_styles()
require_role(["peserta", "admin", "trainer"])

user = get_user()

with st.sidebar:
    st.markdown("<p style='color:white; font-weight:700;'>Menu</p>", unsafe_allow_html=True)
    st.page_link("pages/03_Dashboard.py", label="🏠 Dashboard")
    st.page_link("pages/04_Asesmen.py", label="📝 Asesmen", disabled=True)
    st.page_link("pages/05_Ujian.py", label="📋 Ujian")
    st.page_link("pages/06_Sertifikat.py", label="📜 Sertifikat")

st.title("📝 Asesmen CERC")
st.markdown("Certified Emotional Regulation Coach")

progress = st.progress(0, text="Progress: 0%")

st.subheader("Bagian 1: Stress Level & Emotional Awareness")

q1 = st.radio("1. Seberapa sering Anda merasa kewalahan dalam 30 hari terakhir?",
              ["Tidak pernah", "Jarang", "Kadang", "Sering", "Selalu"], index=2)

q2 = st.radio("2. Seberapa baik Anda mengelola emosi saat marah?",
              ["Sangat buruk", "Buruk", "Cukup", "Baik", "Sangat baik"], index=2)

q3 = st.radio("3. Seberapa sering Anda menggunakan teknik grounding?",
              ["Tidak pernah", "Jarang", "Kadang", "Sering", "Selalu"], index=2)

st.subheader("Bagian 2: Emotional Quotient (EQ)")

q4 = st.radio("4. Seberapa mudah Anda mengenali emosi orang lain?",
              ["Sangat sulit", "Sulit", "Cukup", "Mudah", "Sangat mudah"], index=2)

q5 = st.radio("5. Seberapa sering Anda bereaksi impulsif?",
              ["Selalu", "Sering", "Kadang", "Jarang", "Tidak pernah"], index=2)

progress.progress(60, text="Progress: 60%")

if st.button("Submit Asesmen", type="primary"):
    st.session_state.asesmen_done = True
    st.success("✅ Asesmen selesai! Berikut hasil Anda:")

    categories = ['Stress Mgmt', 'Emotional Awareness', 'Impulse Control',
                  'Empathy', 'Self-Regulation', 'Resilience']
    values = [65, 78, 82, 70, 75, 68]

    fig = go.Figure(data=go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(52,74,97,0.25)',
        line=dict(color='#344A61', width=2.5)
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        title="Profil Kompetensi Emosional Anda",
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    st.plotly_chart(fig, use_container_width=True)

    fig2 = go.Figure(go.Bar(
        x=categories, y=values,
        marker_color='#344A61',
        text=values, textposition='outside'
    ))
    fig2.update_layout(title="Skor per Dimensi", yaxis_range=[0,100])
    st.plotly_chart(fig2, use_container_width=True)

    st.download_button(
        label="📥 Download Report PDF",
        data=b"Mock PDF Report Content",
        file_name="asesmen_cerc_report.pdf",
        mime="application/pdf"
    )

    st.info("💡 Simpan report ini untuk dibahas saat sesi training hari ini.")
