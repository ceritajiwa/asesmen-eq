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


def judul_paket(kode: str) -> str:
    return EXAM_PACKAGES.get(kode, {}).get("title", kode or "")


# ----------------------------------------------------------------------------
# Nomor sertifikat (tabel certificates, diisi admin)
# ----------------------------------------------------------------------------
SQL_SERTIFIKAT = "supabase/2_tabel_sertifikat.sql"


class TabelSertifikatBelumAda(DatabaseError):
    pass


def _cek_tabel(e: Exception):
    teks = str(e)
    if "certificates" in teks and ("does not exist" in teks or "PGRST205" in teks or "schema cache" in teks):
        raise TabelSertifikatBelumAda(teks) from e
    raise DatabaseError(teks) from e


def fetch_certificates(training_id) -> list[dict]:
    try:
        return (sb().table("certificates").select("*").eq("training_id", training_id)
                .order("full_name").execute().data or [])
    except Exception as e:  # noqa: BLE001
        _cek_tabel(e)


def fetch_passed_attempts(training_id) -> list[dict]:
    """Kelulusan pertama per (email, paket) di training ini."""
    rows = (sb().table("exam_attempts").select("*").eq("training_id", training_id).eq("passed", True)
            .order("created_at").execute().data or [])
    out, seen = [], set()
    for r in rows:
        k = ((r.get("email") or "").lower(), r.get("package"))
        if k not in seen:
            seen.add(k)
            out.append(r)
    return out


def cek_nomor_dipakai(nomor_list: list[str], kecuali_ids: list) -> list[str]:
    """Nomor sertifikat yang sudah dipakai baris lain di database (semua training)."""
    if not nomor_list:
        return []
    try:
        rows = sb().table("certificates").select("id, cert_no, full_name").not_.is_("cert_no", "null").execute().data or []
    except Exception as e:  # noqa: BLE001
        _cek_tabel(e)
    kecuali = set(kecuali_ids)
    target = {n.upper() for n in nomor_list}
    return sorted({f"{r['cert_no']} (dipakai {r['full_name']})" for r in rows
                   if r["id"] not in kecuali and (r.get("cert_no") or "").upper() in target})


def simpan_sertifikat(training_id, insert_rows: list[dict], update_rows: list[dict], delete_ids: list) -> None:
    now = datetime.now(WIB).isoformat()
    try:
        for cid in delete_ids:
            sb().table("certificates").delete().eq("id", cid).execute()
        # Tahap 1: kosongkan dulu nomor baris yang diubah, supaya tukar-menukar nomor
        # antar peserta tidak bentrok dengan aturan "nomor tidak boleh dobel".
        for r in update_rows:
            sb().table("certificates").update({"cert_no": None}).eq("id", r["id"]).execute()
        for r in update_rows:
            r = dict(r)
            cid = r.pop("id")
            sb().table("certificates").update({**r, "updated_at": now}).eq("id", cid).execute()
        if insert_rows:
            sb().table("certificates").insert([{**r, "training_id": training_id} for r in insert_rows]).execute()
    except Exception as e:  # noqa: BLE001
        _cek_tabel(e)


def sertifikat_peserta(training_id, email: str) -> list[dict]:
    """Sertifikat (yang sudah diberi nomor oleh admin) milik peserta di training ini."""
    try:
        rows = (sb().table("certificates").select("*").eq("training_id", training_id)
                .ilike("email", (email or "").strip()).execute().data or [])
    except Exception as e:  # noqa: BLE001
        try:
            _cek_tabel(e)
        except TabelSertifikatBelumAda:
            return []
    return rows


def cari_sertifikat(sertifikasi: str, kata_kunci: str) -> list[dict]:
    """Cari sertifikat yang SUDAH diberi nomor oleh admin, berdasarkan nomor atau nama lengkap."""
    kata_kunci = (kata_kunci or "").strip()
    if len(kata_kunci) < 3:
        return []
    try:
        q = sb().table("certificates").select("*").not_.is_("cert_no", "null")
        by_no = q.ilike("cert_no", kata_kunci).execute().data or []
        rows = by_no or (sb().table("certificates").select("*").not_.is_("cert_no", "null")
                         .ilike("full_name", f"%{kata_kunci}%").limit(50).execute().data or [])
        if not rows:
            return []
        ids = list({r["training_id"] for r in rows})
        tr = sb().table("trainings").select("id, name").in_("id", ids).execute().data or []
    except Exception as e:  # noqa: BLE001
        _cek_tabel(e)
    nama_tr = {t["id"]: t["name"] for t in tr}
    hasil = []
    for r in rows:
        if sertifikasi and r.get("package") and r["package"] != sertifikasi:
            continue
        hasil.append({
            "nama": r["full_name"], "training": nama_tr.get(r["training_id"], ""),
            "paket": judul_paket(r.get("package")) or "-", "nomor": r["cert_no"],
            "tanggal": format_tanggal(r.get("issued_date")),
        })
    return hasil
