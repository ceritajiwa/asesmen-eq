import hmac

import streamlit as st

_TRAINING_KEYS = [
    "training_id", "training_kode", "training_nama", "training_perusahaan",
    "training_sertifikasi", "training_batch", "training_instrumen",
]
_PESERTA_KEYS = ["peserta_nama", "peserta_email"]


def init_session():
    defaults = {
        **{k: None for k in _TRAINING_KEYS + _PESERTA_KEYS},
        "asesmen_done": False, "ujian_attempts": 0, "current_nilai": 0,
        "admin_logged_in": False, "trainer_logged_in": False,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def set_training_session(t: dict):
    st.session_state.training_id = t["id"]
    st.session_state.training_kode = t["kode_akses"]
    st.session_state.training_nama = t["nama"]
    st.session_state.training_perusahaan = t["perusahaan"]
    st.session_state.training_sertifikasi = t["sertifikasi"]
    st.session_state.training_batch = t["batch"]
    st.session_state.training_instrumen = t.get("instrumen") or []


def set_peserta(nama, email):
    st.session_state.peserta_nama = nama.strip()
    st.session_state.peserta_email = email.strip().lower()


def clear_training_session():
    for k in _TRAINING_KEYS + _PESERTA_KEYS:
        st.session_state[k] = None
    st.session_state.asesmen_done = False
    st.session_state.pop("asesmen_hasil", None)
    for k in [k for k in st.session_state.keys() if str(k).startswith(("as_", "uj_"))]:
        del st.session_state[k]
    st.session_state.ujian_attempts = 0
    st.session_state.current_nilai = 0


def is_training_set():
    return st.session_state.get("training_id") is not None


def is_peserta_set():
    return st.session_state.get("peserta_nama") is not None


def is_admin_logged_in():
    return bool(st.session_state.get("admin_logged_in"))


def is_trainer_logged_in():
    return bool(st.session_state.get("trainer_logged_in"))


def get_training():
    return {
        "id": st.session_state.training_id, "kode": st.session_state.training_kode,
        "nama": st.session_state.training_nama, "perusahaan": st.session_state.training_perusahaan,
        "sertifikasi": st.session_state.training_sertifikasi, "batch": st.session_state.training_batch,
        "instrumen": st.session_state.get("training_instrumen") or [],
    }


def get_peserta():
    return {"nama": st.session_state.peserta_nama, "email": st.session_state.peserta_email}


def check_password(input_pw: str, secret_name: str, fallback_secret: str | None = None) -> bool | None:
    """True/False hasil cek. None kalau password belum diatur di Secrets.
    Password TIDAK ada di kode, hanya di Secrets Streamlit."""
    expected = st.secrets.get(secret_name, "")
    if not expected and fallback_secret:
        expected = st.secrets.get(fallback_secret, "")
    if not expected:
        return None
    return hmac.compare_digest(str(input_pw), str(expected))
