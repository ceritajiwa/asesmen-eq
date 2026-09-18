
# -*- coding: utf-8 -*-
"""Interpretasi hasil + narasi soft-selling untuk kebutuhan pengembangan."""
from instruments import INSTRUMENTS, DIMS, DIM_ORDER, INST_SHORT

INSIGHTS = {
 "PSS": {
  "low":  "Tingkat stres yang dirasakan masih rendah. Secara umum peserta merasa mampu mengelola tuntutan pekerjaan dan hidupnya.",
  "mid":  "Tingkat stres sedang. Beban mulai terasa di beberapa area; ini wajar, tetapi perlu dipantau agar tidak menumpuk terus.",
  "high": "Tingkat stres tinggi. Jika berlanjut, fokus, kualitas keputusan, dan kesehatan bisa ikut menurun."},
 "MBI_EX": {
  "low":  "Energi emosional masih terjaga. Peserta belum menunjukkan tanda kelelahan kronis.",
  "mid":  "Ada tanda awal kelelahan emosional. Waktu pemulihan (istirahat, batasan kerja) perlu dijaga sebelum memburuk.",
  "high": "Kelelahan emosional tinggi. Ini indikator utama burnout - beban kerja dan pola pemulihan perlu segera dievaluasi."},
 "MBI_CY": {
  "low":  "Rasa makna dan keterlibatan terhadap pekerjaan masih terjaga.",
  "mid":  "Mulai muncul jarak emosional dari pekerjaan. Sinisme ringan sering menjadi pintu masuk burnout.",
  "high": "Sikap sinis/dingin terhadap pekerjaan cukup kuat. Tanda bahwa makna kerja perlu diperbaiki sebelum makin parah."},
 "MBI_PE": {
  "low":  "Rasa mampu memberi kontribusi masih rendah. Peserta mungkin butuh dukungan dan 'kemenangan kecil' yang terasa.",
  "mid":  "Rasa mampu cukup, namun masih bisa dikuatkan lewat umpan balik yang jelas dan pengembangan kompetensi.",
  "high": "Rasa mampu tinggi. Peserta merasa kompeten dan mampu memberi kontribusi bermakna."},
 "SEA": {
  "low":  "Kesadaran terhadap emosi diri masih rendah. Emosi sering 'terasa tapi tidak teridentifikasi' - fondasi penting untuk atur reaksi.",
  "mid":  "Pemahaman emosi diri cukup. Kemampuan menamai emosi dengan tepat masih bisa diasah lebih tajam.",
  "high": "Pemahaman emosi diri tinggi. Peserta sadar mengapa dirinya merasakan sesuatu - modal kuat untuk mengatur respons."},
 "OEA": {
  "low":  "Pemahaman emosi orang lain masih rendah. Miskomunikasi dan salah baca situasi tim berisiko terjadi.",
  "mid":  "Pemahaman emosi orang lain cukup. Latihan empati aktif dan membaca situasi akan memperkuatnya.",
  "high": "Pemahaman emosi orang lain tinggi. Peserta peka terhadap dinamika perasaan orang di sekitarnya."},
 "ROE": {
  "low":  "Mengatur emosi masih menjadi tantangan. Reaksi impulsif berpotensi mengganggu relasi kerja dan kualitas keputusan.",
  "mid":  "Kemampuan mengatur emosi cukup, tetapi konsistensinya menurun saat tekanan tinggi.",
  "high": "Kemampuan mengatur emosi baik. Peserta mampu menenangkan diri dan merespons dengan tenang meski dalam situasi sulit."},
 "UOE": {
  "low":  "Emosi belum dimanfaatkan untuk mendorong pencapaian target. Motivasi dari dalam perlu dibangkitkan kembali.",
  "mid":  "Kemampuan memakai emosi sebagai dorongan target cukup, masih bisa diasah lewat goal-setting yang jelas.",
  "high": "Peserta mampu memakai emosi sebagai bahan bakar untuk mencapai target."},
 "VIG": {
  "low":  "Energi kerja rendah. Pekerjaan terasa cepat melelahkan dan semangat memulai hari kerja kurang.",
  "mid":  "Energi kerja cukup namun fluktuatif. Pola istirahat dan pemulihan perlu diperhatikan.",
  "high": "Energi kerja tinggi. Peserta merasa bersemangat dan tahan bekerja dalam waktu lama."},
 "DED": {
  "low":  "Rasa bangga dan makna terhadap pekerjaan rendah. Pekerjaan terasa sekadar rutinitas.",
  "mid":  "Dedikasi cukup, tetapi koneksi dengan makna pekerjaan masih bisa diperkuat.",
  "high": "Dedikasi tinggi. Peserta bangga dan terinspirasi oleh pekerjaannya."},
 "ABS": {
  "low":  "Ketenggelaman (fokus penuh) dalam pekerjaan rendah. Pekerjaan jarang terasa 'mengalir'.",
  "mid":  "Ketenggelaman cukup. Kondisi fokus penuh masih bisa lebih sering dicapai.",
  "high": "Ketenggelaman tinggi. Peserta mudah masuk ke kondisi fokus penuh saat bekerja."},
 "TIS": {
  "low":  "Tidak ada kecenderungan untuk keluar. Peserta merasa ingin bertahan di perusahaan.",
  "mid":  "Ada kecenderungan pasif mencari peluang lain. Ini fase paling tepat untuk upaya retensi.",
  "high": "Kecenderungan keluar cukup kuat. Tanpa tindak lanjut, risiko resign nyata."},
 "PSQ": {
  "low":  "Rasa aman untuk bersuara rendah. Karyawan cenderung diam, takut salah, dan enggan mengambil risiko.",
  "mid":  "Rasa aman psikologis cukup, tetapi belum cukup kuat untuk mendorong kejujuran penuh.",
  "high": "Rasa aman psikologis tinggi. Tim merasa aman berbicara jujur, mengakui kesalahan, dan mencoba hal baru."},
}

# Penjelasan tiap tes dalam bahasa yang mudah dipahami HR & peserta
INSTRUMENT_META = {
 "PSS": dict(title="Tes 1 - Tingkat Stres (PSS-10)",
   plain="Mengukur seberapa besar tekanan yang dirasakan peserta dalam satu bulan terakhir. "
         "Perlu diingat: skor tinggi di sini BUKAN hal yang bagus - artinya beban sedang melebihi "
         "kapasitas mengelola yang tersedia."),
 "MBI": dict(title="Tes 2 - Tingkat Burnout (MBI-GS)",
   plain="Mengukur tiga sisi kelelahan kerja: kelelahan emosi (exhaustion), sikap sinis/dingin "
         "terhadap pekerjaan (cynicism), dan rasa mampu memberi kontribusi (professional efficacy). "
         "Pada dua sisi pertama, skor tinggi berarti risiko; pada efikasi, skor tinggi berarti baik."),
 "WLEIS": dict(title="Tes 3 - Kecerdasan Emosional (WLEIS)",
   plain="Mengukur kemampuan mengenali emosi sendiri, memahami emosi orang lain, mengatur emosi, "
         "dan memakai emosi untuk mencapai tujuan. Skor tinggi di semua aspek = kabar baik."),
 "UWES": dict(title="Tes 4 - Keterlibatan Kerja (UWES-9)",
   plain="Mengukur keterlibatan psikologis terhadap pekerjaan: energi/semangat, rasa bangga dan makna, "
         "serta ketenggelaman (fokus penuh). Skor tinggi = karyawan hidup dalam pekerjaannya."),
 "TIS": dict(title="Tes 5 - Kecenderungan Keluar (TIS-6)",
   plain="Mengukur seberapa kuat keinginan peserta untuk meninggalkan perusahaan dalam waktu dekat. "
         "Skor rendah justru kabar baik - artinya niat bertahan tinggi."),
 "PSQ": dict(title="Tes 6 - Rasa Aman Psikologis (PSQ-ORG)",
   plain="Mengukur rasa aman untuk bersuasa jujur, mengakui kesalahan, dan mengambil risiko di tempat "
         "kerja - fondasi tim yang sehat dan inovatif. Skor tinggi = kabar baik."),
}
INSTRUMENT_META["PSQ"]["plain"] = INSTRUMENT_META["PSQ"]["plain"].replace("bersuasa","bersuara")

# Konsekuensi bisnis per dimensi (untuk bagian 'yang perlu diperhatikan')
CONSEQUENCE = {
 "PSS":    "Stres yang menumpuk tanpa saluran berisiko menurunkan fokus, kualitas keputusan, dan bisa memicu absensi.",
 "MBI_EX": "Kelelahan emosi berkepanjangan adalah pintu masuk burnout - produktivitas menurun pelan-pelan dan sering tidak disadari.",
 "MBI_CY": "Karyawan yang mulai sinis cenderung menarik diri dari tim dan kehilangan inisiatif.",
 "MBI_PE": "Rendahnya rasa mampu membuat karyawan menghindari tantangan dan cenderung bertahan pada pekerjaan minimum.",
 "SEA":    "Sulitnya mengenali emosi diri membuat reaksi defensif atau meledak-ledak sulit dicegah sebelum terjadi.",
 "OEA":    "Kurang peka terhadap emosi rekan kerja menimbulkan miskomunikasi dan konflik yang sebenarnya bisa dihindari.",
 "ROE":    "Regulasi emosi yang lemah membuat konflik kecil cepat membesar dan mencemari suasana tim.",
 "UOE":    "Tanpa dorongan dari dalam, target kerja terasa seperti beban dan pencapaian stagnan.",
 "VIG":    "Energi rendah membuat pekerjaan terasa lebih berat dari sebenarnya dan berjalan lebih lambat.",
 "DED":    "Tanpa rasa bangga dan makna, karyawan cenderung sekadar 'menghabiskan waktu kerja'.",
 "ABS":    "Sulitnya fokus penuh membuat pekerjaan penting sering tertunda dan kualitas goyah.",
 "TIS":    "Kecenderungan keluar yang tinggi berisiko menjadi resign sesungguhnya - biaya rekrutmen dan training ulang tidak kecil.",
 "PSQ":    "Tim yang tidak aman secara psikologis cenderung diam saat melihat masalah - masalah kecil jadi besar tanpa terdeteksi.",
}

MODULE_MAP = {
 "PSS":    "Modul Regulasi Emosi & Manajemen Stres",
 "MBI_EX": "Modul Burnout Recovery & Manajemen Beban Kerja",
 "MBI_CY": "Modul Rekoneksi Makna Kerja (Purpose & Values)",
 "MBI_PE": "Modul Penguatan Kompetensi & Pemberian Umpan Balik",
 "SEA":    "Modul 2: Emotional Regulation & Self-Mastery",
 "OEA":    "Modul 3: Communication for Trust & Inclusion",
 "ROE":    "Modul 2: Emotional Regulation & Self-Mastery",
 "UOE":    "Modul 3: Communication + Goal-Setting Praktis",
 "VIG":    "Modul Energy Management & Pola Pemulihan Kerja",
 "DED":    "Modul Rekoneksi Makna Kerja (Purpose & Values)",
 "ABS":    "Modul Fokus & Deep Work",
 "TIS":    "Program Retensi & Stay Interview untuk HR/Leader",
 "PSQ":    "Modul 1: Psychological Safety Foundations",
}

DIRECTION_NOTE = {
 "bad":  "Arah tes: skor RENDAH = kondisi baik, skor TINGGI = perlu perhatian.",
 "good": "Arah tes: skor TINGGI = kondisi baik, skor RENDAH = perlu perhatian.",
}

def band(score, lo=33.0, hi=66.0):
    return "low" if score < lo else ("mid" if score < hi else "high")

BAND_LABEL = {"low": "Rendah", "mid": "Sedang", "high": "Tinggi"}

def individual_insights(scores):
    """list (dim_label, band, teks) - hanya dimensi yang tersedia."""
    out = []
    for dim in DIM_ORDER:
        if dim not in scores:
            continue
        out.append((DIMS[dim]["label"], band(scores[dim]), INSIGHTS[dim][band(scores[dim])]))
    return out

def grouped_insights(scores):
    """Kelompokkan insight per tes: [(key, title, plain, [(label, band, teks), ...])]."""
    groups = []
    for inst in INSTRUMENTS:
        dims_present = [d for d in DIM_ORDER if d in scores
                        and d in {x["dim"] for x in inst["items"]}]
        if not dims_present:
            continue
        meta = INSTRUMENT_META[inst["key"]]
        rows = [(DIMS[d]["label"], band(scores[d]), INSIGHTS[d][band(scores[d])]) for d in dims_present]
        groups.append((inst["key"], meta["title"], meta["plain"], rows))
    return groups

def gap_analysis(mean_scores):
    """gap arah-aware: dir='bad' -> gap = target - mean (positif = melebihi batas, bermasalah jika negatif? ...)
    gap positif = di atas target (baik untuk 'good', bermasalah untuk 'bad'?)."""
    rows = []
    for dim in DIM_ORDER:
        if dim not in mean_scores:
            continue
        d = DIMS[dim]; val = mean_scores[dim]
        # selisih "kebaikan": positif = sudah baik/melebihi target, negatif = perlu perhatian
        gap = (val - d["target"]) if d["dir"] == "good" else (d["target"] - val)
        status = "Melebihi target" if gap >= 0 else "Perlu perhatian"
        rows.append(dict(dim=dim, label=d["label"], mean=round(val, 1),
                         target=d["target"], gap=round(gap, 1), status=status,
                         dir=d["dir"], rekomendasi=MODULE_MAP[dim]))
    priority = sorted([r for r in rows if r["gap"] < 0], key=lambda r: r["gap"])
    return rows, priority

def strengths_and_concerns(gap_rows):
    strengths = [r for r in gap_rows if r["gap"] >= 0]
    concerns = sorted([r for r in gap_rows if r["gap"] < 0], key=lambda r: r["gap"])
    return strengths, concerns

def soft_recommendations(priority):
    """Narasi kebutuhan pengembangan - soft selling: saran, bukan vonis."""
    if not priority:
        return ["Secara keseluruhan kondisi tim sudah berada pada jalur yang sehat. Fokus terbaik "
                "saat ini adalah mempertahankan: apresiasi rutin, ruang tumbuh, dan menjaga pola "
                "pemulihan kerja. Tidak ada intervensi mendesak yang diperlukan."]
    sents = []
    for r in priority[:4]:
        sents.append(f"- **{r['label']}** (rata-rata {r['mean']:.0f}/100, target "
                     f"{'maksimal' if r['dir']=='bad' else 'minimal'} {r['target']}). "
                     f"{CONSEQUENCE[r['dim']]} Program yang relevan: {r['rekomendasi']}.")
    return sents

def closing_paragraph(n_prioritas):
    if n_prioritas == 0:
        return ("Catatan: angka di atas adalah potret satu momen, bukan vonis. Kondisi karyawan "
                "bergerak - pengukuran berkala (misal sebelum-sesudah program) akan memberi gambaran "
                "perkembangan yang lebih akurat.")
    return ("Catatan penutup: angka di atas adalah potret kondisi saat ini, bukan penilaian terhadap "
            "individu maupun perusahaan. Pola yang terlihat menunjukkan AREA BERKEMBANG - bukan kegagalan. "
            "Dengan dukungan yang tepat, aspek-aspek ini justru menjadi peluang terbesar untuk naik kelas. "
            "Kami sarankan pengukuran berulang (misalnya sebelum dan sesudah program) agar perkembangan "
            "terlihat nyata dan terukur.")
