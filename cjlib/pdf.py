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
# Sertifikat (memakai desain resmi assets/sertifikat_template.png, 4000 x 2828 px)
# Bagian tetap (bingkai, logo, QR izin, tanda tangan) diambil dari template.
# Nama, judul program, nomor sertifikat, dan tanggal ditulis di atasnya.
# ----------------------------------------------------------------------------
TEMPLATE = ROOT / "assets" / "sertifikat_template.png"
NUNITO = {w: ROOT / "assets" / "fonts" / f"NunitoSans-{w}.ttf" for w in ("Light", "Regular", "Bold", "ExtraBold")}
TEXT_GRAY = (109, 111, 113)
LINE_GRAY = (217, 219, 220)

JUDUL_PROGRAM = {
    "CERC": "Ujian Sertifikasi CERC (Certified Emotional Regulation Coach)",
    "CMBC": "Ujian Sertifikasi CMBC (Certified Money Behavior Coach)",
    "CPSC": "Ujian Sertifikasi CPSC (Certified Psychology of Sales Coach)",
    "CPPC": "Ujian Sertifikasi CPPC (Certified Positive Parenting Coach)",
    "CRWC": "Ujian Sertifikasi CRWC (Certified Relationship Wellbeing Coach)",
    "CCTC": "Ujian Sertifikasi CCTC (Certified Complex Trauma Coach)",
    "CBT": "Ujian Sertifikasi CBT + Counseling",
}


def judul_program(kode: str, fallback: str = "") -> str:
    return JUDUL_PROGRAM.get((kode or "").upper(), fallback or f"Ujian Sertifikasi {kode}".strip())


def _font(weight, size):
    return ImageFont.truetype(str(NUNITO[weight]), int(size))


def _pas(draw, teks, weight, size, max_w):
    """Perkecil ukuran font kalau teks terlalu panjang."""
    f = _font(weight, size)
    while draw.textlength(teks, font=f) > max_w and size > 20:
        size -= 2
        f = _font(weight, size)
    return f


def _tulis_tengah(draw, teks, f, top, fill, cx=2000):
    b = f.getbbox(teks)
    w = b[2] - b[0]
    draw.text((cx - w / 2 - b[0], top - b[1]), teks, font=f, fill=fill)
    return w


def sertifikat_png(nama: str, program: str, nomor: str, tanggal: str) -> Image.Image:
    img = Image.open(TEMPLATE).convert("RGB")
    d = ImageDraw.Draw(img)
    putih = (255, 255, 255)
    # Hapus teks contoh di template
    d.rectangle((300, 1225, 3700, 1395), fill=putih)   # nama + garis
    d.rectangle((300, 1645, 3700, 1770), fill=putih)   # judul program
    d.rectangle((2770, 2100, 3560, 2168), fill=putih)  # tanggal

    # Nama + garis bawah
    f_nama = _pas(d, nama, "ExtraBold", 124, 2900)
    lebar = d.textlength(nama, font=f_nama)
    garis = max(1890, lebar + 240)
    d.rectangle((2000 - garis / 2, 1357, 2000 + garis / 2, 1362), fill=LINE_GRAY)
    b = f_nama.getbbox(nama)
    # baseline nama di y~1345 (sama dengan desain)
    asc = f_nama.getbbox("H")
    d.text((2000 - (b[2] - b[0]) / 2 - b[0], 1345 - asc[3]), nama, font=f_nama, fill=NAVY)

    # Judul program
    f_prog = _pas(d, program, "ExtraBold", 73, 3100)
    asc = f_prog.getbbox("H")
    bp = f_prog.getbbox(program)
    d.text((2000 - (bp[2] - bp[0]) / 2 - bp[0], 1727 - asc[3]), program, font=f_prog, fill=NAVY)

    # Nomor sertifikat (di tengah, di bawah judul program)
    if nomor:
        f_lbl = _font("Regular", 54)
        f_no = _font("ExtraBold", 56)
        lbl = "No. Sertifikat: "
        w_lbl = d.textlength(lbl, font=f_lbl)
        w_no = d.textlength(nomor, font=f_no)
        x0 = 2000 - (w_lbl + w_no) / 2
        base = 1880
        d.text((x0, base - f_lbl.getbbox("H")[3]), lbl, font=f_lbl, fill=TEXT_GRAY)
        d.text((x0 + w_lbl, base - f_no.getbbox("H")[3]), nomor, font=f_no, fill=NAVY)

    # Tanggal (rata kiri, sejajar "Cerita Jiwa Training Center")
    f_tgl = _font("ExtraBold", 50)
    teks_tgl = f"Tangerang, {tanggal}"
    bt = f_tgl.getbbox(teks_tgl)
    d.text((2788 - bt[0], 2148 - f_tgl.getbbox("H")[3]), teks_tgl, font=f_tgl, fill=TEXT_GRAY)
    return img


def sertifikat(nama: str, program: str, nomor: str, tanggal: str) -> bytes:
    """PDF A4 landscape siap cetak (gambar 4000 px, sekitar 340 dpi)."""
    img = sertifikat_png(nama, program, nomor, tanggal)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=95)
    buf.seek(0)
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.set_margin(0)
    pdf.set_title(f"Sertifikat {nama}")
    pdf.set_author("Cerita Jiwa Training Center")
    pdf.add_page()
    pdf.image(buf, x=0, y=0, w=297, h=210)
    return _to_bytes(pdf)


# ----------------------------------------------------------------------------
# Badge PNG
# ----------------------------------------------------------------------------
def badge_png(kode_sertifikasi: str, nama: str, nomor: str) -> bytes:
    """Badge 1000x1000 untuk LinkedIn: kode sertifikasi dibuat dominan, logo kecil."""
    size = 1000
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((8, 8, size - 8, size - 8), fill=NAVY + (255,))
    d.ellipse((40, 40, size - 40, size - 40), outline=TOSCA + (255,), width=10)

    # Logo kecil di atas
    logo = Image.open(LOGO_WHITE).convert("RGBA")
    logo.thumbnail((150, 150))
    img.alpha_composite(logo, ((size - logo.width) // 2, 95))

    def tengah(teks, f, top, fill):
        b = f.getbbox(teks)
        d.text(((size - (b[2] - b[0])) / 2 - b[0], top - b[1]), teks, font=f, fill=fill)
        return b[3] - b[1]

    # Kode sertifikasi sebesar mungkin (maks. lebar 760 px)
    kode = (kode_sertifikasi or "CJ").upper()
    s = 270  # tinggi maksimum, supaya CBT/CERC/CMBC tampil seragam
    f_kode = _font("ExtraBold", s)
    while d.textlength(kode, font=f_kode) > 760 and s > 80:
        s -= 6
        f_kode = _font("ExtraBold", s)
    h = tengah(kode, f_kode, 330, (255, 255, 255, 255))

    y = 330 + h + 45
    tengah("CERTIFIED", _font("ExtraBold", 64), y, TOSCA + (255,))
    y += 110
    f_nama = _font("Bold", 40)
    nama_pendek = nama if d.textlength(nama, font=f_nama) <= 600 else nama[:28].rstrip() + "…"
    tengah(nama_pendek, f_nama, y, (255, 255, 255, 235))
    tengah(nomor, _font("Regular", 32), y + 62, (255, 255, 255, 170))

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
