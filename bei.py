
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



GROQ_BASE = "https://api.groq.com/openai/v1"
GROQ_FALLBACK_MODELS = ["llama-3.3-70b-versatile", "openai/gpt-oss-120b", "llama-3.1-8b-instant"]

def _groq_models(api_key):
    """Daftar model chat Groq yang tersedia untuk key ini (versi besar dulu)."""
    try:
        import requests as _rq
        r = _rq.get(f"{GROQ_BASE}/models", headers={"Authorization": f"Bearer {api_key}"}, timeout=30)
        if r.status_code != 200:
            return []
        ids = [m.get("id", "") for m in r.json().get("data", [])]
        chat = [i for i in ids if not any(x in i for x in ("whisper", "guard", "tts", "audio"))]
        big = [i for i in chat if any(x in i for x in ("70b", "120b", "405b", "3.3", "gpt-oss"))]
        rest = [i for i in chat if i not in big]
        return big + rest
    except Exception:
        return []

def _structure_with_groq(prompt, api_key):
    """Coba Groq satu per satu; kembalikan (hasil_dict, None) atau (None, status_str)."""
    import requests as _rq
    todo = _groq_models(api_key) or list(GROQ_FALLBACK_MODELS)
    statuses = []
    for model in todo[:6]:
        try:
            r = _rq.post(f"{GROQ_BASE}/chat/completions",
                         headers={"Authorization": f"Bearer {api_key}"},
                         json={"model": model,
                               "messages": [{"role": "user", "content": prompt}],
                               "response_format": {"type": "json_object"},
                               "temperature": 0.3,
                               "max_tokens": 4096},
                         timeout=90)
            if r.status_code in (429, 503):
                statuses.append(f"{model}: sibuk")
                continue
            if r.status_code != 200:
                statuses.append(f"{model}: {r.status_code} {r.text[:120]}")
                continue
            text = r.json()["choices"][0]["message"]["content"].strip()
            if text.startswith("```"):
                text = text.strip("`")
                if text.lower().startswith("json"):
                    text = text[4:]
            parsed = json.loads(text)
            if isinstance(parsed, dict) and parsed:
                return parsed, None
            statuses.append(f"{model}: JSON kosong")
        except Exception as e:
            statuses.append(f"{model}: {e}")
    return None, " | ".join(statuses[:8]) or "tidak ada model Groq yang bisa dicoba"

def structure_bei(narratives: dict, api_key: str | None, groq_key: str | None = None) -> dict:
    """Kirim narasi ke Gemini -> dict terstruktur. Tanpa key: return None."""
    if not api_key:
        return {"_error": "GEMINI_API_KEY tidak ditemukan di Secrets Streamlit."}
    import requests
    joined = "\n\n".join(f"### {k}\n{v}" for k, v in narratives.items() if str(v).strip())
    prompt = (
        "Anda adalah asisten psikolog industri yang membantu konselor merapikan catatan sesi (BEI) menjadi "
        "laporan terstruktur. Berikut catatan narasatifnya.\n\n"
        + joined
        + "\n\nSusun menjadi SATU objek JSON dengan key persis: domain, kekuatan, area_rawan, pemicu, "
        "risiko, prioritas (angka 1-5), rekomendasi_peserta, rekomendasi_perusahaan, ringkasan, skor_visual.\n"
        "Aturan penulisan value:\n"
        "1. Bahasa Indonesia manusiawi dan profesional - seperti psikolog berpengalaman menulis laporan untuk "
        "HR dan manajemen, BUKAN kalimat telegram.\n"
        "2. Setiap value terdiri dari 3-6 kalimat yang utuh: jelaskan apa yang terjadi, mengapa itu penting, "
        "dan implikasinya. Hindari jargon kecuali istilah yang memang standar.\n"
        "3. 'domain': klasifikasi utama kasus (misal: Kinerja & Produktivitas / Kesejahteraan & Retensi / "
        "Relasi & Komunikasi / Karir & Pengembangan / Kesehatan Mental / Lainnya) plus alasan singkat.\n"
        "4. 'kekuatan': kekuatan dan sumber daya peserta yang terlihat, plus bagaimana bisa dimanfaatkan.\n"
        "5. 'area_rawan': pola atau kondisi yang perlu perhatian, dijelaskan dengan konteksnya.\n"
        "6. 'pemicu': faktor pemicu/penguat yang teridentifikasi, bukan sekadar daftar.\n"
        "7. 'risiko': konsekuensi realistis jika tidak ditangani, ditulis untuk audience bisnis.\n"
        "8. 'rekomendasi_peserta': langkah konkret untuk peserta (bukan sekadar 'konseling' - jelaskan "
        "arah dan tujuannya), ditulis dengan bahasa yang membuat peserta merasa didukung, bukan dihakimi.\n"
        "9. 'rekomendasi_perusahaan': langkah konkret untuk perusahaan/HR, fleksibel untuk konteks apapun "
        "(rekrutmen, promosi, retensi, atau pengembangan karyawan).\n"
        "10. 'ringkasan': gambaran utuh kasus dalam 4-6 kalimat, cocok dibaca manajemen yang tidak hadir di sesi.\n"
        "11. 'prioritas': angka 1-5 (1 = bisa menunggu, 5 = sangat mendesak) dengan pertimbangan klinis dan bisnis.\n"
        "12. 'skor_visual': objek JSON berisi 4-6 aspek yang relevan dari narasi (contoh: Kesejahteraan, "
        "Keterlibatan Kerja, Kestabilan Emosi, Relasi & Dukungan, Fungsi Peran) masing-masing dengan "
        "angka estimasi 0-100 berdasarkan bukti di narasi - untuk digambar sebagai radar chart.\n"
        "Jangan tambahkan key lain. Jangan gunakan markdown. Murni JSON.")
    tried = []
    todo = _available_flash_models(api_key)
    if not todo:
        return {"_error": "Gagal mengambil daftar model dari Google (endpoint v1beta/models). "
                          "Key mungkin benar tapi Generative Language API belum diaktifkan di project Google Cloud-nya."}
    statuses = []          # status tiap model yang dicoba
    busy_rounds = 0        # putaran khusus untuk model yang sibuk
    while todo and (len(tried) < 8) and busy_rounds < 4:
        model = todo.pop(0)
        _per_model = []
        for ver in ("v1beta", "v1"):   # model terbaru kadang hanya ada di v1
            try:
                r = requests.post(
                    f"https://generativelanguage.googleapis.com/{ver}/models/{model}:generateContent",
                    params={"key": api_key},
                    json={"contents": [{"parts": [{"text": prompt}]}],
                          "generationConfig": {"responseMimeType": "application/json",
                                               "temperature": 0.3}},
                    timeout=90)
            except Exception as e:
                statuses.append(f"{model}: gagal koneksi ({e})")
                break
            if r.status_code == 404:
                _per_model.append(f"{ver}=404")
                continue                      # coba versi endpoint lain
            if r.status_code in (429, 503):
                _per_model.append(f"{ver}=sibuk")
                todo.append(model)            # dicoba lagi di putaran berikutnya
                busy_rounds += 1
                import time as _t; _t.sleep(5)
                break
            if r.status_code != 200:
                statuses.append(f"{model}: {r.status_code} {r.text[:150]}")
                break
            try:
                text = r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
            except Exception:
                statuses.append(f"{model}: respons tidak dikenali")
                break
            if text.startswith("```"):
                text = text.strip("`")
                if text.lower().startswith("json"):
                    text = text[4:]
            try:
                parsed = json.loads(text)
            except Exception:
                statuses.append(f"{model}: JSON tidak terbaca")
                break
            if not isinstance(parsed, dict) or not parsed:
                statuses.append(f"{model}: JSON kosong")
                break
            return parsed
        else:
            pass
        tried.append(model)
        if _per_model:
            statuses.append(f"{model}: {', '.join(_per_model)}")
    # ---- fallback: Groq ----
    if groq_key:
        import streamlit as _st
        _groq_res, _groq_err = _structure_with_groq(prompt, groq_key)
        if _groq_res:
            return _groq_res
        return {"_error": "Gemini gagal/sibuk. Groq juga gagal. "
                          f"[Gemini: {' | '.join(statuses[:8])}] [Groq: {_groq_err}]"}
    return {"_error": "Semua model Gemini gagal/sibuk (dan GROQ_API_KEY belum diisi). Status: "
                      + " | ".join(statuses[:12])}

def fetch_bei(sb, training_id):
    try:
        return sb.table("bei_sessions").select("*").eq("training_id", training_id).order("created_at", desc=True).execute().data or []
    except Exception:
        return []

def _struct_table(structured):
    rows = [{"Aspek": label, "Hasil": structured.get(k, "-") or "-"} for k, label in STRUCT_FIELDS]
    return pd.DataFrame(rows)



def bei_radar_png(skor: dict, title="Peta Aspek Sesi (estimasi AI dari narasi)", figsize=(6, 6)):
    """Radar chart dari dict {aspek: 0-100} hasil analisis AI."""
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    if not skor:
        return None
    labels = list(skor.keys())[:8]
    vals = [min(100, max(0, float(skor[k]))) for k in labels]
    N = len(labels)
    ang = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    vals_c = vals + vals[:1]; ang_c = ang + ang[:1]
    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(polar=True))
    ax.plot(ang_c, vals_c, color="#5B4E9E", linewidth=2)
    ax.fill(ang_c, vals_c, color="#5B4E9E", alpha=0.25)
    ax.set_ylim(0, 100)
    ax.set_xticks(ang); ax.set_xticklabels([l[:18] for l in labels], fontsize=9)
    ax.set_yticks([20, 40, 60, 80, 100]); ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=7, color="grey")
    for a, v in zip(ang, vals):
        ax.annotate(f"{v:.0f}", (a, v), textcoords="offset points", xytext=(0, 6),
                    ha="center", fontsize=9, fontweight="bold", color="#5B4E9E")
    ax.set_title(title, fontsize=11, fontweight="bold", pad=20)
    fig.tight_layout()
    import io as _io
    buf = _io.BytesIO(); fig.savefig(buf, format="png", dpi=140, bbox_inches="tight")
    plt.close(fig); buf.seek(0)
    return buf.read()

def bei_participant_pdf(training_name, p_name, counselor, narratives, structured, tanggal=None):
    pdf = BasePDF()
    pdf.company = training_name
    pdf.add_page()
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "B", 15)
    pdf.cell(0, 10, "Laporan Sesi Konseling (BEI)", ln=1, align="C")
    pdf.ln(2)
    pdf.set_font("helvetica", "", 10)
    for k, v in [("Peserta", p_name), ("Perusahaan / Training", training_name),
                 ("Konselor / Trainer", counselor),
                 ("Tanggal Sesi", (tanggal or "")[:10] or datetime.now().strftime("%d %B %Y"))]:
        pdf.set_font("helvetica", "B", 10); pdf.cell(45, 6, _safe(k))
        pdf.set_font("helvetica", "", 10); pdf.cell(0, 6, _safe(str(v)), ln=1)
    pdf.ln(2)
    pdf.set_font("helvetica", "B", 12); pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 8, "Hasil Terstruktur", ln=1)
    pdf.set_text_color(30, 30, 30)
    _sv = (structured or {}).get("skor_visual") if isinstance(structured, dict) else None
    if isinstance(_sv, dict) and _sv:
        _png = bei_radar_png(_sv)
        if _png:
            _img(pdf, _png, x=62, w=88)
            pdf.ln(2)
            _cap(pdf, "Gambar: estimasi aspek hasil analisis AI atas narasi sesi (0-100).")
            pdf.ln(2)
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
