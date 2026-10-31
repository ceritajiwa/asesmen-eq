"""
Akses Supabase untuk aplikasi Cerita Jiwa Training Center.

Aturan (sama seperti aplikasi asli):
  - trainings.access_code kosong  -> training PUBLIK, peserta tidak perlu kode.
  - trainings.access_code terisi  -> peserta wajib memasukkan kode itu.
  - trainings.enabled_instruments -> JSON list kunci instrumen, contoh ["PSS","MBI"].
                                      Kosong = semua instrumen.
"""
import hmac
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st

from cjlib.supabase_client import get_supabase
from instruments import INSTRUMENTS
from questions import EXAM_PACKAGES

WIB = ZoneInfo("Asia/Jakarta")
ALL_KEYS = [i["key"] for i in INSTRUMENTS]
INST_MAP = {i["key"]: i for i in INSTRUMENTS}
SERTIFIKASI_LIST = ["CERC", "CMBC", "CPSC", "CPPC", "CRWC", "CCTC"]


class DatabaseError(Exception):
    pass


def sb():
    return get_supabase()


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


def tebak_sertifikasi(nama: str) -> str:
    upper = (nama or "").upper()
    for kode in list(EXAM_PACKAGES.keys()) + SERTIFIKASI_LIST:
        if re.search(rf"\b{re.escape(kode)}\b", upper):
            return kode
    return ""


def get_enabled(training: dict) -> list[str]:
    """Kunci instrumen yang dipilih admin untuk training ini (urutan mengikuti bank item)."""
    raw = training.get("enabled_instruments") if training is not None else None
    if raw is None or (isinstance(raw, float) and raw != raw) or raw == "":
        return list(ALL_KEYS)
    try:
        data = raw if isinstance(raw, list) else json.loads(raw)
        keys = [k for k in ALL_KEYS if k in data]
        return keys or list(ALL_KEYS)
    except Exception:  # noqa: BLE001
        return list(ALL_KEYS)


def _normalize(row: dict) -> dict:
    nama = row.get("name") or ""
    bagian = [b.strip() for b in nama.split(" - ")]
    return {
        **row,
        "nama": nama,
        "kode_akses": row.get("access_code"),
        "perlu_kode": bool(normalize_kode(row.get("access_code"))),
        "sertifikasi": tebak_sertifikasi(nama),
        "perusahaan": bagian[1] if len(bagian) >= 3 else "",
        "batch": bagian[2] if len(bagian) >= 3 else "",
    }


# ----------------------------------------------------------------------------
# Trainings
# ----------------------------------------------------------------------------
def fetch_trainings_raw() -> list[dict]:
    """Baris mentah tabel trainings (dipakai halaman Admin & Trainer)."""
    return sb().table("trainings").select("*").order("name").execute().data or []


@st.cache_data(ttl=60, show_spinner=False)
def get_trainings() -> list[dict]:
    try:
        rows = fetch_trainings_raw()
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    return [_normalize(r) for r in rows]


def training_label(t: dict) -> str:
    return t.get("nama") or t.get("name") or "(tanpa nama)"


def ambil_training(training_id) -> dict | None:
    try:
        res = sb().table("trainings").select("*").eq("id", training_id).limit(1).execute()
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    return _normalize(res.data[0]) if res.data else None


def verifikasi_kode_akses(training_id, kode_input: str) -> dict | None:
    """Dicek langsung ke database supaya perubahan kode dari Admin langsung berlaku.
    Training tanpa kode akses selalu lolos (publik)."""
    t = ambil_training(training_id)
    if not t:
        return None
    if not t["perlu_kode"]:
        return t
    if hmac.compare_digest(normalize_kode(t["kode_akses"]).encode(), normalize_kode(kode_input).encode()):
        return t
    return None


# ----------------------------------------------------------------------------
# Respondents / responses (asesmen)
# ----------------------------------------------------------------------------
def fetch_respondents(training_id) -> list[dict]:
    return sb().table("respondents").select("*").eq("training_id", training_id).execute().data or []


def fetch_responses(ids) -> list[dict]:
    """Ambil SEMUA baris responses (Supabase membatasi ~1000 baris per query, jadi pakai pagination)."""
    if not ids:
        return []
    all_rows, PAGE = [], 1000
    for i in range(0, len(ids), 200):
        part = ids[i:i + 200]
        offset = 0
        while True:
            res = (sb().table("responses").select("*").in_("respondent_id", part)
                   .order("id").range(offset, offset + PAGE - 1).execute())
            rows = res.data or []
            all_rows.extend(rows)
            if len(rows) < PAGE:
                break
            offset += PAGE
    return all_rows


def cari_respondent(training_id, email) -> dict | None:
    res = (sb().table("respondents").select("*").eq("training_id", training_id)
           .eq("email", (email or "").strip().lower()).order("created_at", desc=True).limit(1).execute())
    return res.data[0] if res.data else None


def jawaban_respondent(respondent_id) -> list[dict]:
    return sb().table("responses").select("*").eq("respondent_id", respondent_id).execute().data or []


def simpan_asesmen(training_id, nama, email, dept, job_level, answers: dict) -> str:
    """answers: {(inst_key, item_n): skor_mentah}. Mengembalikan respondent_id."""
    ins = sb().table("respondents").insert(dict(
        training_id=training_id, full_name=nama.strip(), email=email.strip().lower(),
        department=(dept or "").strip() or None, job_level=job_level)).execute()
    rid = ins.data[0]["id"]
    rows = [dict(respondent_id=rid, instrument=k[0], item_n=k[1], score=v) for k, v in answers.items()]
    for i in range(0, len(rows), 500):
        sb().table("responses").insert(rows[i:i + 500]).execute()
    return rid


# ----------------------------------------------------------------------------
# Ujian & sertifikat
# ----------------------------------------------------------------------------
def simpan_ujian(training_id, nama, email, benar, nilai, lulus, paket) -> None:
    sb().table("exam_attempts").insert(dict(
        training_id=training_id, full_name=nama.strip(), email=email.strip().lower(),
        correct=int(benar), score=int(nilai), passed=bool(lulus), package=paket)).execute()


def riwayat_ujian(training_id, email: str) -> list[dict]:
    try:
        res = (sb().table("exam_attempts").select("*").eq("training_id", training_id)
               .ilike("email", (email or "").strip()).order("created_at").execute())
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    return res.data or []


def nomor_sertifikat(attempt: dict, fallback_kode: str = "") -> str:
    """Nomor unik dari id baris exam_attempts, contoh: CERC-2026-000089."""
    kode = attempt.get("package") or fallback_kode or "CJ"
    dt = _parse_waktu(attempt.get("created_at"))
    tahun = dt.year if dt else datetime.now(WIB).year
    return f"{kode}-{tahun}-{int(attempt.get('id') or 0):06d}"


def judul_paket(kode: str) -> str:
    return EXAM_PACKAGES.get(kode, {}).get("title", kode or "")


def cari_sertifikat(sertifikasi: str, kata_kunci: str) -> list[dict]:
    """Cari kelulusan berdasarkan nomor sertifikat (CERC-2026-000089) atau nama lengkap."""
    kata_kunci = (kata_kunci or "").strip()
    try:
        m = re.fullmatch(r"([A-Za-z]+)-(\d{4})-(\d+)", kata_kunci)
        q = sb().table("exam_attempts").select("*").eq("passed", True)
        if m:
            q = q.eq("id", int(m.group(3)))
        else:
            if len(kata_kunci) < 3:
                return []
            q = q.ilike("full_name", f"%{kata_kunci}%")
        attempts = q.order("created_at").limit(100).execute().data or []
        if not attempts:
            return []
        ids = list({a["training_id"] for a in attempts})
        tr = sb().table("trainings").select("id, name").in_("id", ids).execute().data or []
    except Exception as e:  # noqa: BLE001
        raise DatabaseError(str(e)) from e
    nama_tr = {t["id"]: t["name"] for t in tr}
    hasil, sudah = [], set()
    for a in attempts:
        kode = a.get("package") or tebak_sertifikasi(nama_tr.get(a["training_id"], ""))
        if m and kode and kode.upper() != m.group(1).upper():
            continue
        if sertifikasi and kode and kode != sertifikasi:
            continue
        kunci = (a["training_id"], (a.get("email") or a["full_name"] or "").lower(), kode)
        if kunci in sudah:  # satu sertifikat per orang per training per paket (kelulusan pertama)
            continue
        sudah.add(kunci)
        hasil.append({
            "nama": a["full_name"], "training": nama_tr.get(a["training_id"], ""),
            "paket": judul_paket(kode), "nomor": nomor_sertifikat(a), "tanggal": format_tanggal(a["created_at"]),
        })
    return hasil
