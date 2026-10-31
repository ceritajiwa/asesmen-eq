"""
BANK SOAL ASESMEN & UJIAN

Di sinilah soal-soal asli dimasukkan. Selama sebuah instrumen / paket ujian masih
bertanda "demo": True, soalnya tetap tampil tapi HASILNYA TIDAK DISIMPAN ke database,
supaya data contoh tidak tercampur dengan data peserta asli.

------------------------------------------------------------------------------
ASESMEN
------------------------------------------------------------------------------
Kunci INSTRUMEN harus SAMA PERSIS dengan nama yang dipilih admin di kolom
trainings.enabled_instruments (dan yang tersimpan di responses.instrument).

Setiap item:
    "teks"     : pertanyaan
    "dimensi"  : nama dimensi / subskala (untuk grafik & laporan)
    "terbalik" : True kalau item reverse-scored (pilihan pertama = skor tertinggi)
Skala jawaban diatur per instrumen lewat "skala" (urutan dari skor 1 ke skor tertinggi).

------------------------------------------------------------------------------
UJIAN
------------------------------------------------------------------------------
Kunci PAKET_UJIAN = kode sertifikasi (CERC, CMBC, ...). Setiap soal:
    "soal"  : pertanyaan
    "opsi"  : daftar pilihan
    "kunci" : index jawaban benar (0 = pilihan pertama)
"""

SKALA_FREKUENSI = ["Tidak pernah", "Jarang", "Kadang", "Sering", "Selalu"]
SKALA_KUALITAS = ["Sangat buruk", "Buruk", "Cukup", "Baik", "Sangat baik"]
SKALA_KEMUDAHAN = ["Sangat sulit", "Sulit", "Cukup", "Mudah", "Sangat mudah"]

INSTRUMEN = {
    "DEMO": {
        "judul": "Asesmen Regulasi Emosi (contoh)",
        "demo": True,
        "skala": SKALA_FREKUENSI,
        "items": [
            {"teks": "Seberapa sering Anda merasa kewalahan?", "dimensi": "Stress Level & Emotional Awareness", "terbalik": True},
            {"teks": "Seberapa baik Anda mengelola emosi saat marah?", "dimensi": "Stress Level & Emotional Awareness", "skala": SKALA_KUALITAS},
            {"teks": "Seberapa sering Anda menggunakan teknik grounding?", "dimensi": "Stress Level & Emotional Awareness"},
            {"teks": "Seberapa mudah Anda mengenali emosi orang lain?", "dimensi": "Emotional Quotient (EQ)", "skala": SKALA_KEMUDAHAN},
            {"teks": "Seberapa sering Anda bereaksi impulsif?", "dimensi": "Emotional Quotient (EQ)", "terbalik": True},
        ],
    },
    # Contoh format instrumen asli (hapus tanda # lalu isi):
    # "NAMA_INSTRUMEN_DI_SUPABASE": {
    #     "judul": "Judul yang tampil ke peserta",
    #     "demo": False,
    #     "skala": SKALA_FREKUENSI,
    #     "items": [
    #         {"teks": "...", "dimensi": "...", "terbalik": False},
    #     ],
    # },
}

PAKET_UJIAN = {
    "DEMO": {
        "judul": "Ujian (contoh)",
        "demo": True,
        "durasi_menit": 45,
        "nilai_lulus": 80,
        "soal": [
            {"soal": "Dalam teknik active listening, hal yang paling penting adalah...",
             "opsi": ["Memberi saran cepat", "Menunjukkan empati", "Mengalihkan pembicaraan", "Mengkritik perasaan klien"], "kunci": 1},
            {"soal": "Apa tujuan utama dari emotional regulation?",
             "opsi": ["Menekan emosi", "Mengelola emosi secara konstruktif", "Menghindari konflik", "Bersikap netral"], "kunci": 1},
            {"soal": "Teknik grounding paling efektif dilakukan saat...",
             "opsi": ["Santai", "Sedang panik/cemas", "Sedang tidur", "Sedang makan"], "kunci": 1},
        ],
    },
    # "CERC": {"judul": "Ujian CERC", "demo": False, "durasi_menit": 45, "nilai_lulus": 80, "soal": [...]},
}


def instrumen_untuk(training: dict) -> tuple[list[tuple[str, dict]], list[str]]:
    """Kembalikan (instrumen yang siap dipakai, nama instrumen yang dipilih admin tapi soalnya belum ada)."""
    dipilih = training.get("instrumen") or []
    siap = [(n, INSTRUMEN[n]) for n in dipilih if n in INSTRUMEN]
    belum = [n for n in dipilih if n not in INSTRUMEN]
    if not siap:
        siap = [("DEMO", INSTRUMEN["DEMO"])]
    return siap, belum


def paket_ujian_untuk(training: dict) -> tuple[str, dict]:
    kode = training.get("sertifikasi")
    if kode in PAKET_UJIAN:
        return kode, PAKET_UJIAN[kode]
    return "DEMO", PAKET_UJIAN["DEMO"]


def skala_item(instrumen: dict, item: dict) -> list[str]:
    return item.get("skala") or instrumen["skala"]


def skor_item(instrumen: dict, item: dict, index_pilihan: int) -> int:
    n = len(skala_item(instrumen, item))
    return (n - index_pilihan) if item.get("terbalik") else (index_pilihan + 1)


def hitung_hasil_asesmen(instrumen_list: list[tuple[str, dict]], jawaban: list[dict]) -> list[dict]:
    """jawaban: [{'instrument', 'item_n', 'score'}]. Hasil per dimensi dalam persen (0-100)."""
    per_dim: dict[tuple[str, str], list[float]] = {}
    for nama, ins in instrumen_list:
        for j in jawaban:
            if j["instrument"] != nama:
                continue
            idx = j["item_n"] - 1
            if not 0 <= idx < len(ins["items"]):
                continue
            item = ins["items"][idx]
            maks = len(skala_item(ins, item))
            per_dim.setdefault((ins["judul"], item.get("dimensi") or ins["judul"]), []).append(
                (j["score"] - 1) / (maks - 1) * 100 if maks > 1 else 0)
    return [{"instrumen": k[0], "dimensi": k[1], "skor": round(sum(v) / len(v))} for k, v in per_dim.items()]
