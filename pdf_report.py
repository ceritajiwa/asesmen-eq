
# -*- coding: utf-8 -*-
import io
from datetime import datetime
from fpdf import FPDF
from instruments import DIMS, DIM_ORDER
from insights import band, BAND_LABEL, CAPTIONS, FOLLOWUP, closing_paragraph
from hr_analytics import CLUSTERS, ACTION_META, FLIP

class BasePDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 11)
        self.set_text_color(91, 78, 158)
        self.cell(0, 8, "Cerita Jiwa Training Center", align="L")
        self.set_font("helvetica", "", 9)
        self.set_text_color(120, 120, 120)
        label = getattr(self, "company", None) or "Laporan Asesmen EQ & Emotional Regulation"
        self.cell(0, 8, _safe(label), align="R", ln=1)
        self.set_draw_color(91, 78, 158)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
    def footer(self):
        self.set_y(-14)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, f"Halaman {self.page_no()}  |  Confidential - Cerita Jiwa Training Center", align="C")

def _img(pdf, png_bytes, **kw):
    import tempfile, os as _os
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tf:
        tf.write(png_bytes); path = tf.name
    pdf.image(path, **kw)
    try: _os.unlink(path)
    except OSError: pass

def _safe(s):
    return (str(s).replace("**", "")
            .replace("'", "'").replace("'", "'")
            .replace(""", '"').replace(""", '"')
            .replace("–", "-").replace("—", "-"))

def _mc(pdf, text, h=5.5, size=None, style=""):
    if size: pdf.set_font("helvetica", style, size)
    try:
        pdf.multi_cell(0, h, _safe(text), new_x="LMARGIN", new_y="NEXT")
    except TypeError:
        pdf.multi_cell(0, h, _safe(text))

def _img_fit(pdf, png, x, w):
    """Pasang gambar lalu geser kursor tepat di bawahnya (dihitung dari rasio asli PNG)."""
    from PIL import Image as _Im
    im = _Im.open(io.BytesIO(png))
    h = w * im.height / im.width
    y0 = pdf.get_y()
    _img(pdf, png, x=x, y=y0, w=w)
    pdf.set_y(y0 + h + 2)

def _cap(pdf, text):
    pdf.set_font("helvetica", "I", 8.5)
    pdf.set_text_color(110, 110, 110)
    _mc(pdf, text, h=4.5)
    pdf.set_text_color(30, 30, 30)

def _finish(pdf):
    res = pdf.output()
    return res.encode("latin-1") if isinstance(res, str) else bytes(res)

def _need_space(pdf, threshold=250):
    if pdf.get_y() > threshold:
        pdf.add_page("L")

def _hex(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# ============================== PDF INDIVIDUAL ==============================
def individual_pdf(name, training_name, dept, job_level, scores, grouped, radar_png):
    pdf = BasePDF()
    pdf.company = training_name
    pdf.add_page()
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, "Laporan Hasil Asesmen EQ", ln=1, align="C")
    pdf.ln(2)
    pdf.set_font("helvetica", "", 10)
    for k, v in [("Nama", name), ("Perusahaan / Training", training_name),
                 ("Departemen", dept or "-"), ("Level Jabatan", job_level or "-"),
                 ("Tanggal", datetime.now().strftime("%d %B %Y"))]:
        pdf.set_font("helvetica", "B", 10); pdf.cell(45, 6, _safe(k))
        pdf.set_font("helvetica", "", 10); pdf.cell(0, 6, _safe(str(v)), ln=1)
    pdf.ln(2)
    _img(pdf, radar_png, x=58, w=95)
    pdf.ln(1)
    _cap(pdf, CAPTIONS["radar"])
    pdf.ln(2)
    for key, title, plain, rows in grouped:
        _need_space(pdf, 250)
        pdf.set_font("helvetica", "B", 12)
        pdf.set_text_color(91, 78, 158)
        pdf.cell(0, 8, _safe(title), ln=1)
        pdf.set_text_color(30, 30, 30)
        _mc(pdf, plain, h=5, size=9.5)
        pdf.ln(1)
        pdf.set_fill_color(242, 240, 250)
        pdf.set_font("helvetica", "B", 9)
        pdf.cell(80, 7, "Aspek", border=1, fill=True)
        pdf.cell(22, 7, "Skor", border=1, fill=True, align="C")
        pdf.cell(56, 7, "Catatan", border=1, fill=True, ln=1)
        pdf.set_font("helvetica", "", 9)
        for label, b, text in rows:
            dim = next(d for d in DIM_ORDER if DIMS[d]["label"] == label)
            note = "* skor dibalik" if dim in FLIP else "-"
            pdf.cell(80, 6.5, _safe(label), border=1)
            pdf.cell(22, 6.5, f"{scores[dim]:.0f}", border=1, align="C")
            pdf.cell(56, 6.5, _safe(note), border=1, ln=1)
        pdf.ln(1)
        for label, b, text in rows:
            _mc(pdf, f"- {label}: {text}", h=5, size=9.5)
        pdf.ln(4)
    pdf.set_font("helvetica", "I", 8.5)
    pdf.set_text_color(120, 120, 120)
    _mc(pdf, "Catatan: hasil asesmen bersifat rahasia dan untuk pengembangan. Skor adalah potret satu momen "
             "dan dapat berubah. Tanda * berarti skor tes tersebut dibalik agar searah dengan tes lain "
             "(makin tinggi = makin sehat) - bacanya tetap pada penjelasan tiap aspek.", h=5)
    return _finish(pdf)

# ============================== PDF PERUSAHAAN ==============================
def company_pdf(bundle):
    b = bundle
    pdf = BasePDF("L")
    pdf.company = b["training_name"]
    pdf.add_page("L")
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 6, "Laporan Agregat Kondisi Psikologis Karyawan", align="C", ln=1)
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 12, _safe(b["training_name"]), align="C", ln=1)
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 7, f"Jumlah responden: {b['n_respondents']}  |  Dicetak: {datetime.now().strftime('%d %B %Y')}",
             align="C", ln=1)
    pdf.ln(2)
    if b.get("opening"):
        _mc(pdf, b["opening"], h=5.5, size=10)
        pdf.ln(2)
    from PIL import Image as _Im
    hs = []
    for png, w in ([(b["radar_png"], 105)] + ([(b["donut_png"], 122)] if b.get("donut_png") else [])):
        im = _Im.open(io.BytesIO(png))
        hs.append(w * im.height / im.width)
    if pdf.get_y() + max(hs) + 28 > 200:
        pdf.add_page("L")
    y0 = pdf.get_y()
    _img(pdf, b["radar_png"], x=15, y=y0, w=105)
    if b.get("donut_png"):
        _img(pdf, b["donut_png"], x=148, y=y0, w=122)
    pdf.set_y(y0 + max(hs) + 3)
    _cap(pdf, "Gambar 1 (kiri): " + CAPTIONS["radar"])
    if b.get("donut_png"):
        _cap(pdf, "Gambar 2 (kanan): " + CAPTIONS["donut"])
    pdf.ln(3)

    # ---- Bagian 1: hasil per tes ----
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 9, "1. Hasil per Tes", ln=1)
    pdf.set_text_color(30, 30, 30)
    for key, title, plain, rows in b["grouped"]:
        _need_space(pdf, 190)
        pdf.set_font("helvetica", "B", 11)
        pdf.set_text_color(91, 78, 158)
        pdf.cell(0, 7, _safe(title), ln=1)
        pdf.set_text_color(30, 30, 30)
        _mc(pdf, plain, h=5, size=9.5)
        pdf.ln(1)
        pdf.set_fill_color(242, 240, 250)
        pdf.set_font("helvetica", "B", 9)
        pdf.cell(95, 7, "Aspek", border=1, fill=True)
        pdf.cell(28, 7, "Rata-rata", border=1, fill=True, align="C")
        pdf.cell(38, 7, "Kategori", border=1, fill=True, align="C")
        pdf.cell(110, 7, "Keterangan", border=1, fill=True, ln=1)
        pdf.set_font("helvetica", "", 9)
        for label, mean, raw_mean, dir_, note in rows:
            pdf.cell(95, 6.5, _safe(label), border=1)
            pdf.cell(28, 6.5, f"{mean:.0f}", border=1, align="C")
            pdf.cell(38, 6.5, BAND_LABEL[band(mean)], border=1, align="C")
            pdf.cell(110, 6.5, _safe(note), border=1, ln=1)
        pdf.ln(4)

    # ---- Bagian 2: distribusi kategori ----
    _need_space(pdf, 150)
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 9, "2. Distribusi Kategori Karyawan per Dimensi", ln=1)
    pdf.set_text_color(30, 30, 30)
    if b.get("band_png"):
        if pdf.get_y() > 55:
            pdf.add_page("L")
            pdf.set_font("helvetica", "B", 14); pdf.set_text_color(91, 78, 158)
            pdf.cell(0, 9, "2. Distribusi Kategori Karyawan per Dimensi (lanjutan)", ln=1)
            pdf.set_text_color(30, 30, 30)
        _img_fit(pdf, b["band_png"], x=52, w=182)
    _cap(pdf, "Gambar 3: " + CAPTIONS["band"])
    pdf.ln(3)

    # ---- Bagian 3: klasterisasi (selalu halaman baru) ----
    pdf.add_page("L")
    pdf.set_font("helvetica", "B", 14); pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 9, "3. Klasterisasi Profil Karyawan", ln=1)
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 9, "3. Klasterisasi Profil Karyawan", ln=1)
    pdf.set_text_color(30, 30, 30)
    if b.get("heat_png"):
        _img_fit(pdf, b["heat_png"], x=60, w=170)
    _cap(pdf, "Gambar 4: " + CAPTIONS["heat"])
    pdf.ln(2)
    for c in b["cluster_summary"]:
        _need_space(pdf, 200)
        pdf.set_font("helvetica", "B", 10.5)
        pdf.set_text_color(*_hex(CLUSTERS[c["cluster"]]["color"]))
        pdf.cell(0, 6.5, _safe(f"{c['label']} - {c['n']} orang ({c['pct']}%)"), ln=1)
        pdf.set_text_color(30, 30, 30)
        _mc(pdf, CLUSTERS[c["cluster"]]["desc"], h=5, size=9.5)
        if c.get("common_flags") and c["common_flags"] != "-":
            pdf.set_font("helvetica", "I", 9)
            _mc(pdf, f"Area yang paling sering muncul pada kelompok ini: {c['common_flags']}.", h=5)
        members = (b.get("cluster_members") or {}).get(c["cluster"], [])
        if members:
            _need_space(pdf, 210)
            pdf.set_font("helvetica", "B", 8.5)
            pdf.set_fill_color(242, 240, 250)
            pdf.cell(70, 6, "Nama", border=1, fill=True)
            pdf.cell(50, 6, "Departemen", border=1, fill=True)
            pdf.cell(30, 6, "Indeks", border=1, fill=True, align="C")
            pdf.cell(110, 6, "Area Rawan", border=1, fill=True, ln=1)
            pdf.set_font("helvetica", "", 8.5)
            for nm, dp, ix, ar in members[:15]:
                pdf.cell(70, 5.5, _safe(nm), border=1)
                pdf.cell(50, 5.5, _safe(dp or "-"), border=1)
                pdf.cell(30, 5.5, _safe(str(ix)), border=1, align="C")
                pdf.cell(110, 5.5, _safe(ar), border=1, ln=1)
            if len(members) > 15:
                pdf.set_font("helvetica", "I", 8)
                _mc(pdf, f"... dan {len(members)-15} karyawan lainnya (lihat sheet Klasterisasi di file Excel).", h=5)
        pdf.ln(2)

    # ---- Bagian 4: risiko ----
    pdf.add_page("L")
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 9, "4. Risiko yang Perlu Diwaspadai", ln=1)
    pdf.set_text_color(30, 30, 30)
    _mc(pdf, "Bagian ini menerjemahkan angka menjadi konsekuensi bisnis. Setiap risiko di bawah bersifat "
             "preventif - artinya masih ada waktu untuk bertindah sebelum berubah menjadi biaya nyata.",
        h=5.5, size=9.5)
    pdf.ln(1)
    for i, s in enumerate(b.get("risks", []), 1):
        _mc(pdf, f"{i}. {s}", h=5.5, size=9.5)
        pdf.ln(1.5)

    # ---- Bagian 5: peta tindak lanjut ----
    pdf.add_page("L")
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 9, "5. Peta Tindak Lanjut & Rekomendasi Pengembangan", ln=1)
    pdf.set_text_color(30, 30, 30)
    if b.get("action_png"):
        _img_fit(pdf, b["action_png"], x=28, w=228)
    _cap(pdf, "Gambar 5: " + CAPTIONS["action"])
    pdf.ln(2)
    cats = b.get("action_cats") or {}
    for cat in ["konseling", "training", "pantau", "pertahankan"]:
        rows = cats.get(cat) or []
        if not rows:
            continue
        _need_space(pdf, 200)
        pdf.set_font("helvetica", "B", 10.5)
        pdf.set_text_color(*_hex(ACTION_META[cat]["color"]))
        pdf.cell(0, 6.5, _safe(f"{ACTION_META[cat]['label']} ({len(rows)} aspek)"), ln=1)
        pdf.set_text_color(30, 30, 30)
        _mc(pdf, ACTION_META[cat]["desc"], h=5, size=9)
        pdf.ln(1)
        for r in rows:
            fu = FOLLOWUP.get(r["dim"], "")
            line = f"- {r['label']} (selisih {abs(r['gap']):.0f} poin dari target). Program yang relevan: {r['rekomendasi']}."
            if cat in ("konseling", "training") and fu:
                line += f" Asesmen lanjutan yang disarankan: {fu}"
            _mc(pdf, line, h=5, size=9)
        pdf.ln(2)

    pdf.set_font("helvetica", "B", 11)
    _mc(pdf, "Penutup", h=6)
    pdf.set_font("helvetica", "", 9.5)
    for i, s in enumerate(b["recommendations"], 1):
        _mc(pdf, f"{i}. {s.lstrip('- ')}", h=5.5)
    pdf.ln(2)
    pdf.set_font("helvetica", "I", 9)
    _mc(pdf, b["closing"], h=5)
    return _finish(pdf)
