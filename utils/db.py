"""
Akses data training & kode akses dari Supabase.

>>> SESUAIKAN BAGIAN "PEMETAAN TABEL" DI BAWAH DENGAN STRUKTUR SUPABASE ANDA <<<
Kiri  = nama yang dipakai di dalam aplikasi (jangan diubah)
Kanan = nama kolom yang sebenarnya di tabel Supabase
"""
import hmac
import secrets
import string

import streamlit as st

from utils.supabase_client import get_supabase

# ============================ PEMETAAN TABEL ============================
TRAINING_TABLE = "trainings"

COL = {
    "id": "id",
    "kode_akses": "kode_akses",
    "nama": "nama_training",
    "perusahaan": "perusahaan",
    "sertifikasi": "sertifikasi",
    "batch": "batch",
    "tanggal": "tanggal",
    "status": "status",
}

# Nilai kolom status yang dianggap "boleh dipakai login peserta"
STATUS_AKTIF = "aktif"
STATUS_NONAKTIF = "nonaktif"
# =======================================================================

SERTIFIKASI_LIST = ["CERC", "CMBC", "CPSC", "CPPC", "CRWC", "CCTC"]


class DatabaseError(Exception):
    pass


def _normalize(row: dict) -> dict:
    """Ubah 1 baris Supabase ke format standar aplikasi."""
    return {key: row.get(col) for key, col in COL.items()}


def _is_aktif(status) -> bool:
    return str(status or "").strip().lower() in (STATUS_AKTIF, "active", "true", "1")


def normalize_kode(kode: str) -> str:
    return (kode or "").strip().upper()


@st.cache_data(ttl=60, show_spinner=False)
def get_trainings(only_active: bool = True) -> list[dict]:
    """Daftar training dari database (di-cache 60 detik)."""
    try:
        res = (
            get_supabase()
            .table(TRAINING_TABLE)
            .select("*")
            .order(COL["tanggal"], desc=True)
            .execute()
        )
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    rows = [_normalize(r) for r in (res.data or [])]
    if only_active:
        rows = [r for r in rows if _is_aktif(r["status"])]
    return rows


def training_label(t: dict) -> str:
    parts = [t.get("sertifikasi"), t.get("perusahaan"), t.get("batch")]
    return " - ".join(str(p) for p in parts if p)


def verifikasi_kode_akses(training_id, kode_input: str) -> dict | None:
    """Cek kode akses langsung ke database (tanpa cache, supaya perubahan kode langsung berlaku)."""
    kode_input = normalize_kode(kode_input)
    if not kode_input:
        return None
    try:
        res = (
            get_supabase()
            .table(TRAINING_TABLE)
            .select("*")
            .eq(COL["id"], training_id)
            .limit(1)
            .execute()
        )
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    if not res.data:
        return None
    t = _normalize(res.data[0])
    if not _is_aktif(t["status"]):
        return None
    if hmac.compare_digest(normalize_kode(t["kode_akses"]).encode(), kode_input.encode()):
        return t
    return None


def _kode_sudah_ada(kode: str) -> bool:
    res = (
        get_supabase()
        .table(TRAINING_TABLE)
        .select(COL["id"])
        .eq(COL["kode_akses"], kode)
        .limit(1)
        .execute()
    )
    return bool(res.data)


def generate_kode_akses(sertifikasi: str, batch: str) -> str:
    """Format: CERC-AGU-4821. Dicek dulu supaya tidak dobel di database."""
    prefix_batch = "".join(ch for ch in (batch or "").upper() if ch.isalpha())[:3] or "TRN"
    for _ in range(20):
        angka = "".join(secrets.choice(string.digits) for _ in range(4))
        kode = f"{sertifikasi}-{prefix_batch}-{angka}"
        if not _kode_sudah_ada(kode):
            return kode
    raise DatabaseError("Gagal membuat kode akses unik, coba lagi.")


def create_training(sertifikasi, perusahaan, batch, tanggal, nama_training=None) -> dict:
    try:
        kode = generate_kode_akses(sertifikasi, batch)
        payload = {
            COL["kode_akses"]: kode,
            COL["nama"]: nama_training or f"{sertifikasi} Batch {batch}",
            COL["perusahaan"]: perusahaan,
            COL["sertifikasi"]: sertifikasi,
            COL["batch"]: batch,
            COL["tanggal"]: str(tanggal) if tanggal else None,
            COL["status"]: STATUS_AKTIF,
        }
        res = get_supabase().table(TRAINING_TABLE).insert(payload).execute()
    except DatabaseError:
        raise
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    get_trainings.clear()
    return _normalize(res.data[0]) if res.data else _normalize(payload)


def set_training_status(training_id, aktif: bool) -> None:
    try:
        (
            get_supabase()
            .table(TRAINING_TABLE)
            .update({COL["status"]: STATUS_AKTIF if aktif else STATUS_NONAKTIF})
            .eq(COL["id"], training_id)
            .execute()
        )
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    get_trainings.clear()
