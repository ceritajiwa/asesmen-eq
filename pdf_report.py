
# -*- coding: utf-8 -*-
import io
from datetime import datetime
from fpdf import FPDF
from instruments import DIMS, DIM_ORDER
from insights import band

class BasePDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 11)
        self.set_text_color(91, 78, 158)
        self.cell(0, 8, "Cerita Jiwa Training Center", align="L")
        self.set_font("helvetica", "", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Asesmen EQ & Emotional Regulation", align="R", ln=1)
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

BAND_LABEL = {"low": "Rendah", "mid": "Sedang", "high": "Tinggi"}

def _safe(s):
    return s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')

def individual_pdf(name, training_name, dept, job_level, scores, insights_list, radar_png):
    pdf = BasePDF()
    pdf.add_page()
    pdf.set_text_color(30, 30, 30)

    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, "Laporan Hasil Asesmen EQ", ln=1, align="C")
    pdf.ln(2)

    pdf.set_font("helvetica", "", 10)
    rows = [("Nama", name), ("Perusahaan / Training", training_name),
            ("Departemen", dept or "-"), ("Level Jabatan", job_level or "-"),
            ("Tanggal Asesmen", datetime.now().strftime("%d %B %Y"))]
    for k, v in rows:
        pdf.set_font("helvetica", "B", 10); pdf.cell(45, 6, _safe(k))
        pdf.set_font("helvetica", "", 10); pdf.cell(0, 6, _safe(str(v)), ln=1)
    pdf.ln(3)

    _img(pdf, radar_png, x=55, w=100)
    pdf.ln(2)

    # Ringkasan skor per dimensi
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 8, "Ringkasan Skor per Dimensi (0-100)", ln=1)
    pdf.ln(1)
    pdf.set_text_color(30, 30, 30)
    pdf.set_fill_color(242, 240, 250)
    pdf.set_font("helvetica", "B", 9)
    pdf.cell(95, 7, "Dimensi", border=1, fill=True)
    pdf.cell(25, 7, "Skor", border=1, fill=True, align="C")
    pdf.cell(35, 7, "Kategori", border=1, fill=True, align="C")
    pdf.cell(35, 7, "Target", border=1, fill=True, align="C", ln=1)
    pdf.set_font("helvetica", "", 9)
    for dim in [x for x in DIM_ORDER if x in scores]:
        d = DIMS[dim]
        pdf.cell(95, 6.5, _safe(d["label"]), border=1)
        pdf.cell(25, 6.5, f"{scores[dim]:.0f}", border=1, align="C")
        pdf.cell(35, 6.5, BAND_LABEL[band(scores[dim])], border=1, align="C")
        pdf.cell(35, 6.5, f"{'max ' if d['dir']=='bad' else 'min '}{d['target']}", border=1, align="C", ln=1)
    pdf.ln(4)

    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 8, "Insight & Interpretasi", ln=1)
    pdf.ln(1)
    pdf.set_text_color(30, 30, 30)
    for label, b, text in insights_list:
        pdf.set_font("helvetica", "B", 9.5)
        pdf.multi_cell(0, 5.5, _safe(f"{label} ({BAND_LABEL[b]})"))
        pdf.set_font("helvetica", "", 9.5)
        pdf.multi_cell(0, 5.5, _safe(text))
        pdf.ln(1.5)

    pdf.set_font("helvetica", "I", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.multi_cell(0, 5, _safe("Catatan: Hasil asesmen bersifat rahasia dan digunakan untuk pengembangan "
        "kapasitas emosional. Skor 0-100 dinormalisasi antar instrumen agar dapat dibandingkan. "
        "Instrumen: PSS-10, MBI-GS, WLEIS, UWES-9, TIS-6, PSQ-ORG."))
    res = pdf.output()
    return res.encode("latin-1") if isinstance(res, str) else bytes(res)

def company_pdf(training_name, n_respondents, mean_scores, radar_png, bar_png, dept_png,
                gap_rows, priority, summary_sentences):
    pdf = BasePDF("L")  # landscape untuk tabel gap
    pdf.add_page()
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, f"Laporan Agregat Asesmen EQ - {training_name}", align="C", ln=1)
    pdf.set_font("helvetica", "", 10)
    pdf.cell(0, 7, f"Jumlah responden: {n_respondents}  |  Dicetak: {datetime.now().strftime('%d %B %Y')}",
             align="C", ln=1)
    pdf.ln(3)
    _img(pdf, radar_png, x=15, y=pdf.get_y(), w=110)
    _img(pdf, bar_png, x=140, y=pdf.get_y(), w=145)
    pdf.ln(95)

    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 8, "Gap Analysis: Skor Rata-rata vs Target", ln=1)
    pdf.ln(1)
    pdf.set_text_color(30, 30, 30)
    pdf.set_fill_color(242, 240, 250)
    pdf.set_font("helvetica", "B", 8.5)
    pdf.cell(70, 7, "Dimensi", border=1, fill=True)
    pdf.cell(20, 7, "Rata2", border=1, fill=True, align="C")
    pdf.cell(20, 7, "Target", border=1, fill=True, align="C")
    pdf.cell(28, 7, "Status", border=1, fill=True, align="C")
    pdf.cell(120, 7, "Rekomendasi Intervensi", border=1, fill=True, ln=1)
    pdf.set_font("helvetica", "", 8.5)
    for r in gap_rows:
        pdf.cell(70, 6.5, _safe(r["label"]), border=1)
        pdf.cell(20, 6.5, f"{r['mean']:.0f}", border=1, align="C")
        pdf.cell(20, 6.5, f"{r['target']}", border=1, align="C")
        pdf.cell(28, 6.5, _safe(r["status"]), border=1, align="C")
        pdf.cell(120, 6.5, _safe(r["rekomendasi"]), border=1, ln=1)
    pdf.ln(4)

    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(91, 78, 158)
    pdf.cell(0, 8, "Kesimpulan & Prioritas Intervensi", ln=1)
    pdf.ln(1)
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("helvetica", "", 9.5)
    for s in summary_sentences:
        pdf.multi_cell(0, 5.5, _safe(s))
    pdf.ln(2)
    if dept_png:
        if pdf.get_y() > 150:
            pdf.add_page("L")
        _img(pdf, dept_png, x=45, w=180)
    res = pdf.output()
    return res.encode("latin-1") if isinstance(res, str) else bytes(res)
