"""Pembuatan file PDF (laporan asesmen, sertifikat) dan badge PNG yang benar-benar valid."""
import io
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
LOGO_DARK = ROOT / "assets" / "logo_dark.png"
LOGO_WHITE = ROOT / "assets" / "logo_white.png"
FONT_REG = ROOT / "assets" / "fonts" / "DejaVuSans.ttf"
FONT_BOLD = ROOT / "assets" / "fonts" / "DejaVuSans-Bold.ttf"

NAVY = (52, 74, 97)
GRAY = (109, 111, 113)
LIGHT = (217, 219, 220)
TOSCA = (79, 168, 163)
WIB = ZoneInfo("Asia/Jakarta")
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
         "Agustus", "September", "Oktober", "November", "Desember"]


def _hari_ini() -> str:
    d = datetime.now(WIB)
    return f"{d.day} {BULAN[d.month - 1]} {d.year}"


def _pdf(orientation="P") -> FPDF:
    pdf = FPDF(orientation=orientation, unit="mm", format="A4")
    pdf.add_font("DejaVu", "", str(FONT_REG))
    pdf.add_font("DejaVu", "B", str(FONT_BOLD))
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_title("Cerita Jiwa Training Center")
    pdf.set_author("Cerita Jiwa Training Center")
    return pdf


def _to_bytes(pdf: FPDF) -> bytes:
    return bytes(pdf.output())


# ----------------------------------------------------------------------------
# Laporan asesmen
# ----------------------------------------------------------------------------
def laporan_asesmen(training: dict, peserta: dict, hasil: list[dict], detail: list[dict] | None = None) -> bytes:
    """hasil: [{'instrumen','dimensi','skor'}]; detail: [{'teks','jawaban'}] opsional."""
    pdf = _pdf()
    pdf.add_page()

    # Header
    pdf.image(str(LOGO_DARK), x=15, y=12, w=24)
    pdf.set_xy(45, 15)
    pdf.set_font("DejaVu", "B", 16)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 8, "Laporan Hasil Asesmen", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(45)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(*GRAY)
    pdf.cell(0, 6, "Cerita Jiwa Training Center", new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(*TOSCA)
    pdf.set_line_width(0.8)
    pdf.line(15, 40, 195, 40)

    # Identitas
    pdf.set_y(46)
    for label, nilai in [("Nama", peserta.get("nama")), ("Email", peserta.get("email")),
                         ("Training", training.get("nama")), ("Tanggal", _hari_ini())]:
        pdf.set_font("DejaVu", "B", 10)
        pdf.set_text_color(*NAVY)
        pdf.cell(30, 7, label)
        pdf.set_font("DejaVu", "", 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 7, f": {nilai or '-'}", new_x="LMARGIN", new_y="NEXT")

    # Skor per dimensi (grafik batang sederhana)
    pdf.ln(6)
    pdf.set_font("DejaVu", "B", 13)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 8, "Skor per Dimensi", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(*GRAY)
    pdf.multi_cell(0, 5, "Skor ditampilkan dalam skala 0-100. Semakin tinggi, semakin kuat kemampuan pada dimensi tersebut.",
                   new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    bar_x, bar_w = 95, 85
    for h in hasil:
        y = pdf.get_y()
        pdf.set_font("DejaVu", "", 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(78, 6, h["dimensi"], new_x="LMARGIN", new_y="NEXT")
        y_end = max(pdf.get_y(), y + 8)
        pdf.set_fill_color(*LIGHT)
        pdf.rect(bar_x, y + 1, bar_w, 5, style="F")
        pdf.set_fill_color(*NAVY)
        pdf.rect(bar_x, y + 1, bar_w * max(0, min(100, h["skor"])) / 100, 5, style="F")
        pdf.set_xy(bar_x + bar_w + 2, y)
        pdf.set_font("DejaVu", "B", 10)
        pdf.set_text_color(*NAVY)
        pdf.cell(12, 7, str(h["skor"]))
        pdf.set_y(y_end + 2)

    if detail:
        pdf.ln(4)
        pdf.set_font("DejaVu", "B", 13)
        pdf.set_text_color(*NAVY)
        pdf.cell(0, 8, "Jawaban Anda", new_x="LMARGIN", new_y="NEXT")
        for i, d in enumerate(detail, 1):
            pdf.set_font("DejaVu", "", 10)
            pdf.set_text_color(40, 40, 40)
            pdf.multi_cell(0, 6, f"{i}. {d['teks']}", new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("DejaVu", "B", 10)
            pdf.set_text_color(*TOSCA)
            pdf.multi_cell(0, 6, f"    {d['jawaban']}", new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)

    pdf.ln(6)
    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(*GRAY)
    pdf.multi_cell(0, 5, "Laporan ini adalah gambaran awal untuk dibahas bersama trainer saat sesi training, "
                         "bukan diagnosis psikologis.", new_x="LMARGIN", new_y="NEXT")
    return _to_bytes(pdf)


# ----------------------------------------------------------------------------
# Sertifikat
# ----------------------------------------------------------------------------
def sertifikat(nama: str, nama_training: str, nomor: str, tanggal: str, nilai=None) -> bytes:
    pdf = _pdf("L")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    W, H = 297, 210

    # Bingkai
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, W, H, style="F")
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(10, 10, W - 20, H - 20, style="F")
    pdf.set_draw_color(*TOSCA)
    pdf.set_line_width(0.6)
    pdf.rect(15, 15, W - 30, H - 30)

    pdf.image(str(LOGO_DARK), x=W / 2 - 16, y=22, w=32)

    def tengah(y, teks, size, bold=False, color=NAVY):
        pdf.set_xy(20, y)
        pdf.set_font("DejaVu", "B" if bold else "", size)
        pdf.set_text_color(*color)
        pdf.cell(W - 40, size * 0.5, teks, align="C")

    tengah(62, "SERTIFIKAT", 30, bold=True)
    tengah(76, "diberikan kepada", 12, color=GRAY)
    tengah(88, nama, 26, bold=True)
    pdf.set_draw_color(*LIGHT)
    pdf.set_line_width(0.4)
    pdf.line(W / 2 - 70, 101, W / 2 + 70, 101)
    tengah(108, "atas keberhasilannya menyelesaikan dan dinyatakan LULUS pada", 12, color=GRAY)
    tengah(119, nama_training, 15, bold=True)
    if nilai is not None:
        tengah(130, f"dengan nilai ujian {nilai}", 11, color=GRAY)

    # Footer
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(*GRAY)
    pdf.set_xy(30, 160)
    pdf.cell(100, 6, f"Tangerang, {tanggal}")
    pdf.set_xy(30, 166)
    pdf.cell(100, 6, f"No. Sertifikat: {nomor}")
    pdf.set_xy(W - 130, 160)
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*NAVY)
    pdf.cell(100, 6, "Cerita Jiwa Training Center", align="R")
    pdf.set_xy(W - 130, 166)
    pdf.set_font("DejaVu", "", 9)
    pdf.set_text_color(*GRAY)
    pdf.cell(100, 6, "Cek keaslian di menu Cek Sertifikasi", align="R")
    return _to_bytes(pdf)


# ----------------------------------------------------------------------------
# Badge PNG
# ----------------------------------------------------------------------------
def badge_png(kode_sertifikasi: str, nama: str, nomor: str) -> bytes:
    size = 800
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((10, 10, size - 10, size - 10), fill=NAVY + (255,))
    d.ellipse((40, 40, size - 40, size - 40), outline=TOSCA + (255,), width=6)
    logo = Image.open(LOGO_WHITE).convert("RGBA")
    logo.thumbnail((260, 260))
    img.alpha_composite(logo, ((size - logo.width) // 2, 110))

    def font(path, s):
        return ImageFont.truetype(str(path), s)

    def teks_tengah(y, teks, f, fill=(255, 255, 255, 255)):
        w = d.textlength(teks, font=f)
        d.text(((size - w) / 2, y), teks, font=f, fill=fill)

    teks_tengah(400, kode_sertifikasi or "CJ", font(FONT_BOLD, 96))
    teks_tengah(520, "CERTIFIED", font(FONT_BOLD, 40), fill=TOSCA + (255,))
    nama_pendek = nama if len(nama) <= 26 else nama[:25] + "…"
    teks_tengah(585, nama_pendek, font(FONT_REG, 34))
    teks_tengah(640, nomor, font(FONT_REG, 26), fill=(255, 255, 255, 190))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
