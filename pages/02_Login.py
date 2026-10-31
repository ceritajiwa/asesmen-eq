import streamlit as st
from utils.styles import apply_ceritajiwa_styles
from utils.auth import login_user, init_session

st.set_page_config(page_title="Login - Cerita Jiwa", page_icon="🔐", layout="centered")
apply_ceritajiwa_styles()
init_session()

st.image("assets/logo_dark.png", width=100)
st.title("Login")
st.markdown("Masuk ke akun ujian & asesmen Anda")

email = st.text_input("Email", placeholder="nama@email.com")
password = st.text_input("Password", type="password", placeholder="123456")

col1, col2 = st.columns(2)
with col1:
    if st.button("Login", type="primary", use_container_width=True):
        if not email or not password:
            st.error("Email dan password wajib diisi")
        else:
            if email == "admin@ceritajiwa.id" and password == "admin123":
                login_user(email, "Admin", "admin")
                st.success("Login berhasil!")
                st.switch_page("pages/08_Admin.py")
            elif email == "trainer@ceritajiwa.id" and password == "trainer123":
                login_user(email, "Trainer", "trainer")
                st.success("Login berhasil!")
                st.switch_page("pages/09_Trainer.py")
            else:
                login_user(email, "Peserta", "peserta",
                          sertifikasi_list=[{"kode":"CERC","nama":"Certified Emotional Regulation Coach","status":"aktif"}],
                          is_first_login=(password == "123456"))
                st.success("Login berhasil!")
                st.switch_page("pages/03_Dashboard.py")

with col2:
    if st.button("Kembali", use_container_width=True):
        st.switch_page("app.py")

st.info("Belum punya akun? Hubungi admin untuk pendaftaran.")
