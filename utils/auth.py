import streamlit as st

def init_session():
    defaults = {
        "kode_akses": None,
        "nama_peserta": None,
        "sertifikasi": None,
        "batch": None,
        "asesmen_done": False,
        "ujian_attempts": 0,
        "current_nilai": 0,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def set_akses(kode, nama, sertifikasi, batch):
    st.session_state.kode_akses = kode
    st.session_state.nama_peserta = nama
    st.session_state.sertifikasi = sertifikasi
    st.session_state.batch = batch

def clear_akses():
    keys = ["kode_akses", "nama_peserta", "sertifikasi", "batch", 
            "asesmen_done", "ujian_attempts", "current_nilai"]
    for k in keys:
        if k in st.session_state:
            del st.session_state[k]
    init_session()

def is_akses_valid():
    return st.session_state.kode_akses is not None

def require_akses():
    if not is_akses_valid():
        st.warning("Silakan masukkan kode akses terlebih dahulu.")
        st.page_link("app.py", label="← Kembali ke Halaman Utama")
        st.stop()

def get_peserta():
    return {
        "kode": st.session_state.kode_akses,
        "nama": st.session_state.nama_peserta,
        "sertifikasi": st.session_state.sertifikasi,
        "batch": st.session_state.batch,
    }

# Mock database kode akses
# Nanti diganti dengan query ke Supabase
MOCK_KODE_DATABASE = {
    "CERC-AGT-001": {"nama": "Budi Santoso", "sertifikasi": "CERC", "batch": "Agustus 2026"},
    "CERC-AGT-002": {"nama": "Ani Rahayu", "sertifikasi": "CERC", "batch": "Agustus 2026"},
    "CERC-AGT-003": {"nama": "Citra Dewi", "sertifikasi": "CERC", "batch": "Agustus 2026"},
    "CMBC-SEP-001": {"nama": "Dedi Kurniawan", "sertifikasi": "CMBC", "batch": "September 2026"},
}

def verifikasi_kode(kode):
    """Verifikasi kode akses. Return dict peserta atau None."""
    kode = kode.strip().upper()
    return MOCK_KODE_DATABASE.get(kode)
