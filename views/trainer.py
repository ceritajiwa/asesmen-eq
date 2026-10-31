import plotly.graph_objects as go
import streamlit as st

from cjlib.auth import check_password, is_trainer_logged_in
from cjlib.styles import footer, page_header

if not is_trainer_logged_in():
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.image("assets/logo_dark.png", width=96)
        page_header("👨‍🏫 Trainer / BEI Panel", "Masukkan password trainer.")
        with st.form("form_trainer_login", border=True):
            password = st.text_input("Password Trainer", type="password")
            submit = st.form_submit_button("Masuk", type="primary", width="stretch")
        if submit:
            if not password:
                st.error("Password wajib diisi.")
            else:
                ok = check_password(password, "TRAINER_PASSWORD", fallback_secret="ADMIN_PASSWORD")
                if ok is None:
                    st.error("TRAINER_PASSWORD belum diatur di Secrets Streamlit.")
                elif ok:
                    st.session_state.trainer_logged_in = True
                    st.rerun()
                else:
                    st.error("Password salah.")
    footer()
    st.stop()

with st.sidebar:
    st.markdown("<p style='font-weight:800; margin:6px 0 0;'>Trainer Panel</p><hr>", unsafe_allow_html=True)
    if st.button("🚪 Logout", width="stretch", key="logout_trainer"):
        st.session_state.trainer_logged_in = False
        st.switch_page("views/beranda.py")

page_header("👨‍🏫 Dashboard Trainer / BEI")

st.subheader("📊 Status Peserta Hari Ini")
st.dataframe({
    "Nama": ["Budi S.", "Ani R.", "Citra D.", "Dedi K.", "Eka L."],
    "Perusahaan": ["PT Maju Jaya", "PT Maju Jaya", "PT Maju Jaya", "PT Sejahtera", "PT Sejahtera"],
    "Training": ["CERC-AGT-001", "CERC-AGT-001", "CERC-AGT-001", "CERC-SEP-001", "CERC-SEP-001"],
    "Asesmen": ["✅ Done", "⏳ Progress", "-", "✅ Done", "✅ Done"],
    "Ujian": ["-", "-", "-", "-", "-"],
    "Nilai": ["-", "-", "-", "-", "-"],
}, hide_index=True, width="stretch")

st.divider()
st.subheader("🔍 Lihat Hasil Asesmen Peserta")
peserta = st.selectbox("Pilih Peserta", ["Budi S.", "Ani R.", "Dedi K.", "Eka L."])

if peserta:
    with st.container(border=True, key="card_trainer_1"):
        st.markdown(f"**Report Asesmen: {peserta}**")
        fig = go.Figure(go.Bar(
            x=["Stress Mgmt", "EQ", "Empati", "Regulasi", "Resilience"],
            y=[65, 78, 70, 82, 68],
            marker_color="#344A61", text=[65, 78, 70, 82, 68], textposition="outside",
        ))
        fig.update_layout(title="Skor Kompetensi", yaxis_range=[0, 100])
        st.plotly_chart(fig, width="stretch")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Skor Tertinggi", "82", "Regulasi Emosi")
        with col2:
            st.metric("Skor Terendah", "65", "Stress Management", delta_color="off")
        st.download_button("📥 Download Report PDF", b"Mock", f"asesmen_{peserta.replace(' ', '_')}.pdf")

footer()
