import streamlit as st

def init_session():
    defaults = {
        "training_id": None,
        "training_kode": None,
        "training_nama": None,
        "training_perusahaan": None,
        "training_sertifikasi": None,
        "training_batch": None,
        "peserta_nama": None,
        "peserta_email": None,
        "asesmen_done": False,
        "ujian_attempts": 0,
        "current_nilai": 0,
        "admin_logged_in": False,
        "trainer_logged_in": False,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def set_training_session(training_id, kode, nama, perusahaan, sertifikasi, batch):
    st.session_state.training_id = training_id
    st.session_state.training_kode = kode
    st.session_state.training_nama = nama
    st.session_state.training_perusahaan = perusahaan
    st.session_state.training_sertifikasi = sertifikasi
    st.session_state.training_batch = batch

def set_peserta(nama, email):
    st.session_state.peserta_nama = nama
    st.session_state.peserta_email = email

def clear_training_session():
    for k in ["training_id", "training_kode", "training_nama", "training_perusahaan",
              "training_sertifikasi", "training_batch", "peserta_nama", "peserta_email",
              "asesmen_done", "ujian_attempts", "current_nilai"]:
        st.session_state[k] = None if k not in ["ujian_attempts", "current_nilai"] else 0
    st.session_state.asesmen_done = False

def clear_all():
    for k in ["training_id", "training_kode", "training_nama", "training_perusahaan",
              "training_sertifikasi", "training_batch", "peserta_nama", "peserta_email",
              "asesmen_done", "ujian_attempts", "current_nilai",
              "admin_logged_in", "trainer_logged_in"]:
        st.session_state[k] = None if k not in ["ujian_attempts", "current_nilai"] else 0
    st.session_state.asesmen_done = False

def is_training_set():
    return st.session_state.training_id is not None

def is_peserta_set():
    return st.session_state.peserta_nama is not None

def is_admin_logged_in():
    return st.session_state.admin_logged_in

def is_trainer_logged_in():
    return st.session_state.trainer_logged_in

def get_training():
    return {
        "id": st.session_state.training_id,
        "kode": st.session_state.training_kode,
        "nama": st.session_state.training_nama,
        "perusahaan": st.session_state.training_perusahaan,
        "sertifikasi": st.session_state.training_sertifikasi,
        "batch": st.session_state.training_batch,
    }

def get_peserta():
    return {
        "nama": st.session_state.peserta_nama,
        "email": st.session_state.peserta_email,
    }

def require_training():
    if not is_training_set():
        st.warning("Silakan pilih training dan masukkan kode akses.")
        st.page_link("app.py", label="← Kembali ke Beranda")
        st.stop()

def require_peserta():
    require_training()
    if not is_peserta_set():
        st.warning("Silakan isi nama dan email.")
        st.stop()

def require_admin():
    if not is_admin_logged_in():
        st.warning("Silakan login sebagai Admin.")
        st.page_link("app.py", label="← Kembali")
        st.stop()

def require_trainer():
    if not is_trainer_logged_in():
        st.warning("Silakan login sebagai Trainer.")
        st.page_link("app.py", label="← Kembali")
        st.stop()

# ===== MOCK DATABASE: TRAININGS (per perusahaan/batch) =====
# Nanti diganti query ke Supabase
MOCK_TRAININGS = {
    "TR-CERC-001": {
        "kode_akses": "CERC-AGT-001",
        "nama_training": "CERC Batch Agustus 2026",
        "perusahaan": "PT Maju Jaya",
        "sertifikasi": "CERC",
        "batch": "Agustus 2026",
        "tanggal": "2026-08-15",
        "status": "aktif",
    },
    "TR-CERC-002": {
        "kode_akses": "CERC-SEP-001",
        "nama_training": "CERC Batch September 2026",
        "perusahaan": "PT Sejahtera",
        "sertifikasi": "CERC",
        "batch": "September 2026",
        "tanggal": "2026-09-20",
        "status": "aktif",
    },
    "TR-CMBC-001": {
        "kode_akses": "CMBC-OKT-001",
        "nama_training": "CMBC Batch Oktober 2026",
        "perusahaan": "PT Sukses Abadi",
        "sertifikasi": "CMBC",
        "batch": "Oktober 2026",
        "tanggal": "2026-10-10",
        "status": "aktif",
    },
}

def get_trainings_list():
    """Return list of trainings for dropdown."""
    return [(k, f"{v['sertifikasi']} - {v['perusahaan']} - {v['batch']}") for k, v in MOCK_TRAININGS.items()]

def verifikasi_kode_akses(training_id, kode_input):
    """Verifikasi kode akses untuk training tertentu."""
    kode_input = kode_input.strip().upper()
    training = MOCK_TRAININGS.get(training_id)
    if training and training["kode_akses"] == kode_input:
        return training
    return None
