import streamlit as st
from utils.styles import apply_ceritajiwa_styles, card
from utils.auth import require_role, get_user, logout_user

st.set_page_config(page_title="Dashboard - Cerita Jiwa", page_icon="📋", layout="wide")
apply_ceritajiwa_styles()
require_role(["peserta", "admin", "trainer"])

user = get_user()

with st.sidebar:
    st.markdown(f"""
    <div style="text-align:center; padding:10px 0;">
        <p style="color:white; font-size:16px; font-weight:700; margin:0;">{user['nama']}</p>
        <p style="color:rgba(255,255,255,0.6); font-size:12px; margin:4px 0 0 0;">{user['email']}</p>
    </div>
    <hr style="border-color:rgba(255,255,255,0.15);">
    """, unsafe_allow_html=True)
    if st.button("🏠 Dashboard", use_container_width=True):
        st.rerun()
    if st.button("📝 Asesmen", use_container_width=True):
        st.switch_page("pages/04_Asesmen.py")
    if st.button("📋 Ujian", use_container_width=True):
        st.switch_page("pages/05_Ujian.py")
    if st.button("📜 Sertifikat", use_container_width=True):
        st.switch_page("pages/06_Sertifikat.py")
    st.markdown("<hr style='border-color:rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
    if st.button("🚪 Logout", use_container_width=True):
        logout_user()
        st.switch_page("app.py")

st.title("Dashboard Peserta")
st.markdown(f"Selamat datang, **{user['nama']}**!")

if st.session_state.get("is_first_login", False):
    st.warning("⚠️ Ini adalah login pertama Anda. Silakan ganti password untuk keamanan.")
    with st.form("change_password"):
        new_pass = st.text_input("Password Baru", type="password")
        confirm_pass = st.text_input("Konfirmasi Password", type="password")
        if st.form_submit_button("Simpan Password", type="primary"):
            if new_pass != confirm_pass:
                st.error("Password tidak cocok!")
            elif len(new_pass) < 6:
                st.error("Password minimal 6 karakter!")
            else:
                st.session_state.is_first_login = False
                st.success("Password berhasil diubah!")
                st.rerun()

st.subheader("Sertifikasi Saya")
col1, col2 = st.columns(2)

with col1:
    card("CERC", "Certified Emotional Regulation Coach<br>Batch: Agustus 2026", "active")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📝 Mulai Asesmen", use_container_width=True):
            st.switch_page("pages/04_Asesmen.py")
    with c2:
        if st.button("📋 Mulai Ujian", use_container_width=True):
            st.switch_page("pages/05_Ujian.py")

with col2:
    card("CMBC", "Certified Money Behavior Coach", "locked")
    st.link_button("💳 Beli di Mayar", "https://app.mayar.id", use_container_width=True)

st.divider()
st.info("""
**Jadwal Hari Ini:**
- 📝 Asesmen: 08:00 WIB
- 📚 Training: 09:00 - 16:00 WIB
- 📋 Ujian: 16:00 WIB
""")
