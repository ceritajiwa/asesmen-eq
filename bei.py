
# -*- coding: utf-8 -*-
"""Menu Trainer: sesi konseling BEI (Behavioral Event Interview).
Konselor menulis narasi terpandu -> AI (Gemini) menyusun jadi tabel terstruktur.
Tanpa API key: narita tetap tersimpan, struktur kosong (bisa diisi manual nanti)."""
import json
import pandas as pd
from datetime import datetime
from pdf_report import BasePDF, _safe, _mc, _finish, _img, _cap

BEI_PROMPTS = [
 ("konteks", "1. Konteks & alasan sesi",
  "Siapa peserta, apa posisinya, dan apa yang memicu sesi ini? (contoh: hasil asesmen, permintaan perusahaan, inisiatif sendiri, krisis tertentu)"),
 ("peristiwa", "2. Peristiwa konkret (Behavioral Event)",
  "Ceritakan SATU peristiwa nyata yang paling mewakili keadaan peserta: situasinya apa, apa yang dilakukan peserta, dan apa hasilnya? (STARL: Situation-Task-Action-Result-Learning)"),
 ("pola", "3. Pola berulang",
  "Apakah pola serupa terjadi berulang? Sejak kapan, dan di konteks apa saja (kerja, relasi, keputusan)?"),
 ("pemicu", "4. Pemicu & penguat masalah",
  "Hal-hal apa yang memicu atau memperberat keadaan ini? (orang, situasi, beban, kebiasaan, riwayat)"),
 ("dampak", "5. Dampak nyata",
  "Bagaimana keadaan ini memengaruhi kinerja, relasi kerja, kesejahteraan, dan/atau keluarga peserta?"),
 ("upaya", "6. Upaya yang sudah dicoba",
  "Apa saja yang sudah peserta (atau perusahaan) coba? Apa yang berhasil dan apa yang tidak?"),
 ("kekuatan", "7. Kekuatan & sumber daya peserta",
  "Kekuatan, keterampilan, atau dukungan apa yang terlihat selama sesi? (bisa jadi modal penyelesaian)"),
 ("risiko", "8. Risiko yang terlihat",
  "Apa risiko terburuk jika keadaan ini dibiarkan? (resign, konflik, penurunan performa, kesehatan, dsb)"),
 ("rencana", "9. Rencana tindak lanjut",
  "Apa kesepakatan langkah lanjut dari sesi ini? Apa peran peserta, dan apa yang perlu diperusahaan lakukan?"),
 ("rekomendasi", "10. Rekomendasi Trainer",
  "Apa rekomendasi Anda sebagai trainer? Tulis secara umum - bisa untuk kebutuhan perusahaan "
  "(misal: rekrutmen, promosi, penempatan, retensi) maupun untuk pengembangan peserta "
  "(misal: lanjut konseling, training tambahan, pengembangan diri)."),
]

STRUCT_FIELDS = [
    ("domain", "Domain Utama"),
    ("kekuatan", "Kekuatan Teridentifikasi"),
    ("area_rawan", "Area yang Perlu Perhatian"),
    ("pemicu", "Pemicu / Sumber"),
    ("risiko", "Risiko Jika Dibiarkan"),
    ("prioritas", "Prioritas Tindak Lanjut (1-5)"),
    ("rekomendasi_peserta", "Rekomendasi untuk Peserta"),
    ("rekomendasi_perusahaan", "Rekomendasi untuk Perusahaan"),
    ("ringkasan", "Ringkasan Kasus"),
]

GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/models/"

# urutan kandidat model (paling baru dulu); + auto-parse nama model
# dari pesan error Google ("Please update your code to use models/xxx")
MODEL_CANDIDATES = ["gemini-3.8-flash", "gemini-flash", "gemini-2.5-flash", "gemini-3.8-flash-latest"]



def _available_flash_models(api_key):
    """Tanya Google daftar model yang tersedia untuk key ini, kembalikan
    id model gemini-flash yang mendukung generateContent (urut pilihan utama dulu)."""
    try:
        import requests as _rq
        r = _rq.get("https://generativelanguage.googleapis.com/v1beta/models",
                    params={"key": api_key, "pageSize": 250}, timeout=30)
        if r.status_code != 200:
            return []
        ids = [m.get("name", "").replace("models/", "") for m in r.json().get("models", [])]
        flash = [i for i in ids if "gemini" in i and "flash" in i
                 and all(x not in i for x in ("image", "aqa", "tts", "live", "thinking", "lite"))]
        # prioritas: yang ada di MODEL_CANDIDATES duluan, lalu sisanya (versi terbaru di atas)
        pri = [m for m in MODEL_CANDIDATES if m in flash]
        rest = [m for m in flash if m not in pri]
        rest.sort(reverse=True)
        return pri + rest
    except Exception:
        return []

def structure_bei(narratives: dict, api_key: str | None) -> dict:
    """Kirim narasi ke Gemini -> dict terstruktur. Tanpa key: return None."""
    if not api_key:
        return {"_error": "GEMINI_API_KEY tidak ditemukan di Secrets Streamlit."}
    import requests
    joined = "\n\n".join(f"### {k}\n{v}" for k, v in narratives.items() if str(v).strip())
    prompt = (
        "Anda adalah asisten psikolog industri. Berikut catatan narasatif sesi konseling BEI dari konselor. "
        "Susun menjadi SATU objek JSON dengan key persis: domain, kekuatan, area_rawan, pemicu, risiko, "
        "prioritas (angka 1-5), rekomendasi_peserta, rekomendasi_perusahaan, ringkasan. "
        "Setiap value berupa string Bahasa Indonesia yang ringkas dan profesional (maks 3 kalimat). "
        "Jangan tambahkan key lain, jangan markdown.\n\n" + joined)
    tried = []
    todo = _available_flash_models(api_key)
    if not todo:
        return {"_error": "Gagal mengambil daftar model dari Google (endpoint v1beta/models). "
                          "Key mungkin benar tapi Generative Language API belum diaktifkan di project Google Cloud-nya."}
    last_err = ""
    for _attempt in range(5):
        if not todo:
            break
        model = todo.pop(0)
        if model in tried:
            continue
        tried.append(model)
        try:
            r = requests.post(f"{GEMINI_BASE}{model}:generateContent", params={"key": api_key},
                              json={"contents": [{"parts": [{"text": prompt}]}],
                                    "generationConfig": {"responseMimeType": "application/json",
                                                         "temperature": 0.3}},
                              timeout=90)
            if r.status_code == 404:
                last_err = f"[{model} 404] {r.text[:180]}"
                continue
            if r.status_code in (429, 503):
                last_err = f"[{model} {r.status_code}] sibuk sementara"
                todo.append(model)
                import time as _t
                _t.sleep(2)
                continue
            if r.status_code != 200:
                return {"_error": f"Gemini menolak (status {r.status_code}, model {model}): {r.text[:250]}"}
            text = r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
            if text.startswith("```"):
                text = text.strip("`")
                if text.lower().startswith("json"):
                    text = text[4:]
            parsed = json.loads(text)
            if not isinstance(parsed, dict) or not parsed:
                return {"_error": "Respons AI kosong/bukan objek JSON."}
            return parsed
        except Exception as e:
            return {"_error": f"Gagal memproses respons AI (model {model}): {e}"}
    return {"_error": "Semua model gagal. Model tersedia dari Google: "
                      + ", ".join(tried[:10])
                      + (" | Terakhir: " + last_err if last_err else "")}

def fetch_bei(sb, training_id):
    try:
        return sb.table("bei_sessions").select("*").eq("training_id", training_id).order("created_at", desc=True).execute().data or []
    except Exception:
        return []

def _struct_table(structured):
    rows = [{"Aspek": label, "Hasil": structured.get(k, "-") or "-"} for k, label in STRUCT_FIELDS]
    return pd.DataFrame(rows)

def bei_participant_pdf(training_name, p_name, counselor, narratives, structured):
    pdf = BasePDF()
    pdf.company = training_name
    pdf.add_page()
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "B", 15)
    pdf.cell(0, 10, "Laporan Sesi Konseling (BEI)", ln=1, align="C")
    pdf.ln(2)
    pdf.set_font("helvetica", "", 10)
    for k, v in [("Peserta", p_name), ("Perusahaan / Training", training_name),
                 ("Konselor / Trainer", counselor), ("Tanggal", datetime.now().strftime("%d %B %Y"))]:
        pdf.set_font("helvetica", "B", 10); pdf.cell(45, 6, _safe(k))
        pdf.set_font("helvetica", "", 10); pdf.cell(0, 6, _safe(str(v)), ln=1)
    pdf.ln(2)
    pdf.set_font("helvetica", "B", 12); pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 8, "Hasil Terstruktur", ln=1)
    pdf.set_text_color(30, 30, 30)
    if structured:
        pdf.set_font("helvetica", "", 9.5)
        for k, label in STRUCT_FIELDS:
            pdf.set_font("helvetica", "B", 9.5)
            _mc(pdf, f"{label}:", h=5)
            pdf.set_font("helvetica", "", 9.5)
            _mc(pdf, str(structured.get(k, "-") or "-"), h=5)
            pdf.ln(1)
        pdf.ln(2)
    else:
        _mc(pdf, "Belum ada struktur AI untuk sesi ini (API key Gemini belum dikonfigurasi atau proses gagal).", size=9.5)
        pdf.ln(2)
    pdf.set_font("helvetica", "B", 12); pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 8, "Catatan Narasi Konselor", ln=1)
    pdf.set_text_color(30, 30, 30)
    for key, title, _ in BEI_PROMPTS:
        val = narratives.get(key, "").strip()
        if val:
            pdf.set_font("helvetica", "B", 9.5)
            _mc(pdf, title, h=5.5)
            pdf.set_font("helvetica", "", 9.5)
            _mc(pdf, val, h=5.5)
            pdf.ln(1.5)
    return _finish(pdf)

def bei_company_pdf(training_name, sessions):
    pdf = BasePDF("L")
    pdf.company = training_name
    pdf.add_page("L")
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, _safe(f"Laporan Agregat Sesi Konseling (BEI) - {training_name}"), align="C", ln=1)
    pdf.set_font("helvetica", "", 10)
    pdf.cell(0, 7, f"Jumlah sesi: {len(sessions)}  |  Dicetak: {datetime.now().strftime('%d %B %Y')}", align="C", ln=1)
    pdf.ln(3)
    if not sessions:
        _mc(pdf, "Belum ada data sesi konseling (BEI) untuk perusahaan ini. "
                 "Report ini akan terisi otomatis setelah trainer mencatat sesi di Menu Trainer.", size=10)
        return _finish(pdf)
    pdf.set_fill_color(242, 240, 250)
    pdf.set_font("helvetica", "B", 9)
    pdf.cell(50, 7, "Peserta", border=1, fill=True)
    pdf.cell(35, 7, "Konselor", border=1, fill=True)
    pdf.cell(28, 7, "Prioritas", border=1, fill=True, align="C")
    pdf.cell(65, 7, "Domain", border=1, fill=True)
    pdf.cell(75, 7, "Area Perhatian Utama", border=1, fill=True, ln=1)
    pdf.set_font("helvetica", "", 9)
    for s in sessions:
        stc = s.get("structured") or {}
        pdf.cell(50, 6.5, _safe(s.get("participant_name", "-")), border=1)
        pdf.cell(35, 6.5, _safe(s.get("counselor_name", "-")), border=1)
        pdf.cell(28, 6.5, _safe(str(stc.get("prioritas", "-"))), border=1, align="C")
        pdf.cell(65, 6.5, _safe(str(stc.get("domain", "-"))[:60]), border=1)
        pdf.cell(75, 6.5, _safe(str(stc.get("area_rawan", "-"))[:80]), border=1, ln=1)
    pdf.ln(4)
    pdf.set_font("helvetica", "B", 12); pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 8, "Ringkasan per Peserta", ln=1)
    pdf.set_text_color(30, 30, 30)
    for s in sessions:
        stc = s.get("structured") or {}
        pdf.set_font("helvetica", "B", 10)
        _mc(pdf, f"{s.get('participant_name','-')}  ({s.get('created_at','')[:10]})", h=6)
        pdf.set_font("helvetica", "", 9.5)
        _mc(pdf, f"Ringkasan: {stc.get('ringkasan','-')}", h=5)
        _mc(pdf, f"Rekomendasi peserta: {stc.get('rekomendasi_peserta','-')}", h=5)
        _mc(pdf, f"Rekomendasi perusahaan: {stc.get('rekomendasi_perusahaan','-')}", h=5)
        pdf.ln(2)
    return _finish(pdf)
