"""
Akses data Supabase untuk aplikasi Cerita Jiwa Training Center.

Struktur yang dipakai (schema public):
  trainings      : id (uuid), name, access_code, created_at, enabled_instruments
  respondents    : id, training_id, full_name, email, department, job_level, created_at
  exam_attempts  : id, training_id, full_name, email, correct, score, passed, created_at, package

Aturan kode akses:
  - Training dianggap TERBUKA kalau kolom access_code terisi.
  - Training TERTUTUP kalau access_code kosong (NULL), tidak muncul di pilihan peserta.
"""
import hmac
import re
import secrets
import string
from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st

from utils.supabase_client import get_supabase

TRAINING_TABLE = "trainings"
RESPONDENT_TABLE = "respondents"
EXAM_TABLE = "exam_attempts"

SERTIFIKASI_LIST = ["CERC", "CMBC", "CPSC", "CPPC", "CRWC", "CCTC"]
WIB = ZoneInfo("Asia/Jakarta")


class DatabaseError(Exception):
    pass


# ----------------------------------------------------------------------------
# Helper
# ----------------------------------------------------------------------------
def normalize_kode(kode) -> str:
    return (kode or "").strip().upper()


def _parse_waktu(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).astimezone(WIB)
    except ValueError:
        return None


def format_tanggal(value, with_time=False) -> str:
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
             "Agustus", "September", "Oktober", "November", "Desember"]
    dt = _parse_waktu(value)
    if not dt:
        return "-"
    teks = f"{dt.day} {bulan[dt.month - 1]} {dt.year}"
    return f"{teks}, {dt:%H:%M}" if with_time else teks


def _tebak_sertifikasi(nama: str) -> str:
    """Ambil kode sertifikasi dari nama training, misal 'CERC - PT Maju Jaya' -> 'CERC'."""
    upper = (nama or "").upper()
    for kode in SERTIFIKASI_LIST:
        if re.search(rf"\b{kode}\b", upper):
            return kode
    return ""


def _normalize(row: dict) -> dict:
    """Ubah 1 baris tabel trainings ke format yang dipakai halaman-halaman aplikasi.
    Kalau nama training ditulis 'SERTIFIKASI - PERUSAHAAN - BATCH' (format dari menu Admin),
    perusahaan & batch ikut terbaca. Kalau formatnya lain, cukup nama training saja yang tampil."""
    nama = row.get("name") or ""
    bagian = [b.strip() for b in nama.split(" - ")]
    perusahaan = bagian[1] if len(bagian) >= 3 else ""
    batch = bagian[2] if len(bagian) >= 3 else ""
    return {
        "id": row.get("id"),
        "nama": nama,
        "kode_akses": row.get("access_code"),
        "sertifikasi": _tebak_sertifikasi(nama),
        "perusahaan": perusahaan,
        "batch": batch,
        "tanggal": row.get("created_at"),
        "aktif": bool(normalize_kode(row.get("access_code"))),
    }


# ----------------------------------------------------------------------------
# Trainings
# ----------------------------------------------------------------------------
@st.cache_data(ttl=60, show_spinner=False)
def get_trainings(only_active: bool = True) -> list[dict]:
    try:
        res = (
            get_supabase().table(TRAINING_TABLE)
            .select("id, name, access_code, created_at")
            .order("created_at", desc=True)
            .execute()
        )
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    rows = [_normalize(r) for r in (res.data or [])]
    return [r for r in rows if r["aktif"]] if only_active else rows


def training_label(t: dict) -> str:
    return t.get("nama") or "(tanpa nama)"


def verifikasi_kode_akses(training_id, kode_input: str) -> dict | None:
    """Dicek langsung ke database (tanpa cache) supaya kode yang baru diganti langsung berlaku."""
    kode_input = normalize_kode(kode_input)
    if not kode_input:
        return None
    try:
        res = (
            get_supabase().table(TRAINING_TABLE)
            .select("id, name, access_code, created_at")
            .eq("id", training_id).limit(1).execute()
        )
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    if not res.data:
        return None
    t = _normalize(res.data[0])
    if t["aktif"] and hmac.compare_digest(normalize_kode(t["kode_akses"]).encode(), kode_input.encode()):
        return t
    return None


def _kode_sudah_ada(kode: str) -> bool:
    res = get_supabase().table(TRAINING_TABLE).select("id").eq("access_code", kode).limit(1).execute()
    return bool(res.data)


def generate_kode_akses(sertifikasi: str = "", batch: str = "") -> str:
    """Format: CERC-AGU-4821. Dicek dulu supaya tidak dobel di database."""
    prefix = sertifikasi or "CJ"
    huruf = "".join(ch for ch in (batch or "").upper() if ch.isalpha())[:3]
    for _ in range(20):
        tengah = huruf or "".join(secrets.choice(string.ascii_uppercase) for _ in range(3))
        angka = "".join(secrets.choice(string.digits) for _ in range(4))
        kode = f"{prefix}-{tengah}-{angka}"
        if not _kode_sudah_ada(kode):
            return kode
    raise DatabaseError("Gagal membuat kode akses unik, coba lagi.")


def create_training(sertifikasi: str, perusahaan: str, batch: str) -> dict:
    nama = f"{sertifikasi} - {perusahaan} - {batch}"
    try:
        kode = generate_kode_akses(sertifikasi, batch)
        res = get_supabase().table(TRAINING_TABLE).insert({"name": nama, "access_code": kode}).execute()
    except DatabaseError:
        raise
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    get_trainings.clear()
    return _normalize(res.data[0]) if res.data else {"nama": nama, "kode_akses": kode}


def set_kode_akses(training: dict, buka: bool) -> str | None:
    """buka=True  -> buat kode akses baru (menggantikan kode lama).
    buka=False -> hapus kode akses, training tertutup untuk peserta."""
    try:
        kode = generate_kode_akses(training.get("sertifikasi"), training.get("batch")) if buka else None
        get_supabase().table(TRAINING_TABLE).update({"access_code": kode}).eq("id", training["id"]).execute()
    except DatabaseError:
        raise
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    get_trainings.clear()
    return kode


# ----------------------------------------------------------------------------
# Statistik & riwayat (hanya membaca)
# ----------------------------------------------------------------------------
@st.cache_data(ttl=60, show_spinner=False)
def hitung_statistik() -> dict:
    """Total peserta (respondents) & jumlah peserta lulus (exam_attempts.passed). None kalau gagal dibaca."""
    hasil = {"peserta": None, "lulus": None}
    sb = get_supabase()
    try:
        res = sb.table(RESPONDENT_TABLE).select("id", count="exact").limit(1).execute()
        hasil["peserta"] = res.count
    except Exception:  # noqa: BLE001
        pass
    try:
        res = sb.table(EXAM_TABLE).select("training_id, email").eq("passed", True).execute()
        hasil["lulus"] = len({(r["training_id"], (r["email"] or "").lower()) for r in (res.data or [])})
    except Exception:  # noqa: BLE001
        pass
    return hasil


def riwayat_ujian(training_id, email: str) -> list[dict]:
    try:
        res = (
            get_supabase().table(EXAM_TABLE)
            .select("score, correct, passed, created_at, package")
            .eq("training_id", training_id)
            .ilike("email", (email or "").strip())
            .order("created_at")
            .execute()
        )
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    return res.data or []
