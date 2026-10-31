import plotly.graph_objects as go
import streamlit as st

from utils.styles import footer, page_header
from utils.ui import peserta_sidebar, require_peserta_gate, subjudul

training, peserta = require_peserta_gate("📝 Asesmen")
peserta_sidebar("asesmen")

page_header(f"📝 Asesmen {training['sertifikasi'] or ''}",
            subjudul(training, peserta))

progress = st.progress(0, text="Progress: 0%")

with st.container(border=True, key="card_asesmen_1"):
    st.subheader("Bagian 1: Stress Level & Emotional Awareness")
    q1 = st.radio("1. Seberapa sering Anda merasa kewalahan?", ["Tidak pernah", "Jarang", "Kadang", "Sering", "Selalu"], index=2)
    q2 = st.radio("2. Seberapa baik Anda mengelola emosi saat marah?", ["Sangat buruk", "Buruk", "Cukup", "Baik", "Sangat baik"], index=2)
    q3 = st.radio("3. Seberapa sering Anda menggunakan teknik grounding?", ["Tidak pernah", "Jarang", "Kadang", "Sering", "Selalu"], index=2)

with st.container(border=True, key="card_asesmen_2"):
    st.subheader("Bagian 2: Emotional Quotient (EQ)")
    q4 = st.radio("4. Seberapa mudah Anda mengenali emosi orang lain?", ["Sangat sulit", "Sulit", "Cukup", "Mudah", "Sangat mudah"], index=2)
    q5 = st.radio("5. Seberapa sering Anda bereaksi impulsif?", ["Selalu", "Sering", "Kadang", "Jarang", "Tidak pernah"], index=2)

progress.progress(60, text="Progress: 60%")

if st.button("Submit Asesmen", type="primary"):
    st.session_state.asesmen_done = True
    st.success("✅ Asesmen selesai!")
    categories = ["Stress Mgmt", "Emotional Awareness", "Impulse Control", "Empathy", "Self-Regulation", "Resilience"]
    values = [65, 78, 82, 70, 75, 68]
    c1, c2 = st.columns(2)
    with c1:
        fig = go.Figure(data=go.Scatterpolar(
            r=values + [values[0]], theta=categories + [categories[0]], fill="toself",
            fillcolor="rgba(52,74,97,0.25)", line=dict(color="#344A61", width=2.5)))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False,
                          title="Profil Kompetensi Emosional")
        st.plotly_chart(fig, width="stretch")
    with c2:
        fig2 = go.Figure(go.Bar(x=categories, y=values, marker_color="#344A61", text=values, textposition="outside"))
        fig2.update_layout(title="Skor per Dimensi", yaxis_range=[0, 100])
        st.plotly_chart(fig2, width="stretch")
    st.download_button("📥 Download Report PDF", b"Mock PDF",
                       file_name=f"asesmen_{str(training['sertifikasi']).lower()}_{peserta['nama'].replace(' ', '_')}.pdf")
    st.info("💡 Simpan report ini untuk dibahas saat sesi training.")

footer()
