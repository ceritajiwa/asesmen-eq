import streamlit as st

def init_session():
    defaults = {
        "user": None,
        "role": None,
        "nama": None,
        "email": None,
        "user_id": None,
        "sertifikasi_list": [],
        "current_sertifikasi": None,
        "asesmen_done": False,
        "ujian_attempts": 0,
        "current_nilai": 0,
        "page": "home",
        "is_first_login": False,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def login_user(email, nama, role, user_id=None, sertifikasi_list=None, is_first_login=False):
    st.session_state.user = email
    st.session_state.email = email
    st.session_state.nama = nama
    st.session_state.role = role
    st.session_state.user_id = user_id or email
    st.session_state.sertifikasi_list = sertifikasi_list or []
    st.session_state.is_first_login = is_first_login

def logout_user():
    keys_to_clear = ["user", "role", "nama", "email", "user_id", 
                     "sertifikasi_list", "current_sertifikasi", 
                     "asesmen_done", "ujian_attempts", "current_nilai", 
                     "page", "is_first_login"]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]
    init_session()

def is_logged_in():
    return st.session_state.user is not None

def get_user():
    return {
        "email": st.session_state.email,
        "nama": st.session_state.nama,
        "role": st.session_state.role,
        "user_id": st.session_state.user_id,
    }

def get_role():
    return st.session_state.role

def require_login():
    if not is_logged_in():
        st.warning("Silakan login terlebih dahulu.")
        st.stop()

def require_role(allowed_roles):
    require_login()
    if st.session_state.role not in allowed_roles:
        st.error("Anda tidak memiliki akses ke halaman ini.")
        st.stop()

def has_sertifikasi(kode):
    for s in st.session_state.sertifikasi_list:
        if s.get("kode") == kode and s.get("status") == "aktif":
            return True
    return False

def get_sertifikasi_status(kode):
    for s in st.session_state.sertifikasi_list:
        if s.get("kode") == kode:
            return s.get("status", "locked")
    return "locked"
