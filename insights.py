
# -*- coding: utf-8 -*-
from instruments import DIMS, DIM_ORDER, MODULE_MAP
from scoring import band

# Interpretasi per dimensi per band.
# Untuk dim 'bad': low = baik, high = risiko. Untuk 'good': low = kekhawatiran, high = kekuatan.
INSIGHTS = {
 "PSS": {
  "low":  "Tingkat stres persepsian rendah. Responden umumnya merasa mampu mengelola tuntutan hidup dan pekerjaan.",
  "mid":  "Tingkat stres sedang. Beban mulai terasa di beberapa area dan perlu pemantauan agar tidak menumpuk.",
  "high": "Tingkat stres tinggi. Risiko penurunan fokus, kesehatan, dan performa. Prioritas untuk intervensi manajemen stres."},
 "MBI_EX": {
  "low":  "Energi emosional masih terjaga. Responden belum menunjukkan gejala kelelahan kronis.",
  "mid":  "Tanda awal kelelahan emosional mulai muncul. Pemulihan (recovery) perlu diperhatikan sebelum memburuk.",
  "high": "Kelelahan emosional tinggi - indikator utama burnout. Segera evaluasi beban kerja dan pola pemulihan."},
 "MBI_CY": {
  "low":  "Makna dan keterlibatan terhadap pekerjaan masih terjaga.",
  "mid":  "Mulai ada jarak emosional dari pekerjaan. Sinisme ringan bisa menjadi pintu masuk burnout.",
  "high": "Sinisme tinggi terhadap pekerjaan. Tanda burnout berkembang - perlu intervensi makna & re-engagement."},
 "MBI_PE": {
  "low":  "Efikasi profesional rendah. Responden merasa kurang mampu memberikan kontribusi. Perlu dukungan dan kemenangan kecil yang terasa.",
  "mid":  "Efikasi cukup, namun masih bisa dikuatkan lewat umpan balik dan pengembangan kompetensi.",
  "high": "Efikasi profesional tinggi. Responden merasa kompeten dan mampu memberi kontribusi bermakna."},
 "SEA": {
  "low":  "Kesadaran akan emosi diri rendah. Emosi sering 'terasa tapi tidak teridentifikasi' - fondasi regulasi emosi yang perlu dibangun.",
  "mid":  "Pemahaman emosi diri cukup, namun penamaan emosi (emotional granularity) masih bisa diasah.",
  "high": "Pemahaman emosi diri tinggi. Responden sadar mengapa ia merasakan sesuatu - modal kuat untuk regulasi."},
 "OEA": {
  "low":  "Pemahaman emosi orang lain rendah. Risiko miskomunikasi dan salah baca situasi tim.",
  "mid":  "Pemahaman emosi orang lain cukup. Latihan empati aktif dan membaca non-verbal akan memperkuatnya.",
  "high": "Pemahaman emosi orang lain tinggi. Responden peka terhadap dinamika perasaan di sekitarnya."},
 "ROE": {
  "low":  "Regulasi emosi masih menjadi tantangan. Reaksi impulsif berpotensi mengganggu relasi dan pengambilan keputusan. (inti dari training ini)",
  "mid":  "Regulasi emosi cukup, namun konsistensinya menurun saat tekanan tinggi.",
  "high": "Regulasi emosi baik. Responden mampu menenangkan diri dan bereaksi rasional bahkan dalam situasi sulit."},
 "UOE": {
  "low":  "Emosi belum dimanfaatkan untuk mendorong pencapaian target. Motivasi intrinsik perlu dibangkitkan.",
  "mid":  "Penggunaan emosi untuk mencapai target cukup, masih bisa diasah lewat goal-setting emosional.",
  "high": "Responden mampu memakai emosi sebagai bahan bakar pencapaian target."},
 "VIG": {
  "low":  "Energi kerja rendah. Responden merasa cepat lelah dan kurang bersemangat memulai hari kerja.",
  "mid":  "Energi kerja cukup namun fluktuatif. Pola tidur, istirahat, dan pemulihan perlu diperhatikan.",
  "high": "Energi kerja tinggi. Responden merasa penuh energi dan tahan bekerja lama."},
 "DED": {
  "low":  "Dedikasi rendah. Pekerjaan terasa kurang bermakna dan menginspirasi.",
  "mid":  "Dedikasi cukup, namun koneksi dengan makna pekerjaan bisa diperkuat.",
  "high": "Dedikasi tinggi. Responden bangga dan terinspirasi oleh pekerjaannya."},
 "ABS": {
  "low":  "Ketenggelaman (flow) dalam pekerjaan rendah. Responden jarang 'larut' dalam pekerjaan.",
  "mid":  "Ketenggelaman cukup. Kondisi fokus penuh masih bisa lebih sering dicapai.",
  "high": "Ketenggelaman tinggi. Responden mudah masuk ke kondisi fokus penuh saat bekerja."},
 "TIS": {
  "low":  "Niat keluar rendah. Responden tidak mempertimbangkan untuk meninggalkan perusahaan.",
  "mid":  "Ada kecenderungan pasif untuk mencari peluang lain. Waktu tepat untuk intervensi retensi.",
  "high": "Niat keluar tinggi - risiko turnover nyata. Perlu tindak lanjut stay interview dan perbaikan pengalaman kerja."},
 "PSQ": {
  "low":  "Rasa aman psikologis rendah. Karyawan cenderung diam, takut salah, dan tidak berani bersuara. Fondasi utama yang harus diperbaiki.",
  "mid":  "Rasa aman psikologis cukup, namun belum kuat untuk mendorong keberanian bersuara penuh.",
  "high": "Rasa aman psikologis tinggi. Tim merasa aman berbicara jujur, mengakui kesalahan, dan mengambil risiko."},
}

def individual_insights(scores):
    """-> list of (dim_label, band, teks_insight), hanya dimensi yang tersedia"""
    out = []
    for dim in DIM_ORDER:
        if dim not in scores:
            continue
        b = band(scores[dim])
        out.append((DIMS[dim]["label"], b, INSIGHTS[dim][b]))
    return out

def gap_analysis(mean_scores):
    """mean_scores: dict dim -> rata-rata 0-100 -> DataFrame-like list of rows + prioritas"""
    rows = []
    for dim in DIM_ORDER:
        if dim not in mean_scores:
            continue
        d = DIMS[dim]; val = mean_scores[dim]
        gap = (d["target"] - val) if d["dir"] == "bad" else (val - d["target"])
        status = "Melebihi target" if gap >= 0 else "Di bawah target"
        rows.append(dict(dim=dim, label=d["label"], mean=round(val,1),
                         target=d["target"], gap=round(gap,1), status=status,
                         rekomendasi=MODULE_MAP[dim]))
    priority = sorted([r for r in rows if r["gap"] < 0], key=lambda r: r["gap"])
    return rows, priority

def gap_summary_sentences(priority, n=3):
    """Kalimat ringkas hasil gap analysis untuk report keseluruhan."""
    if not priority:
        return ["Seluruh domain berada pada atau di atas target. Pertahankan dan perdalam program yang sudah berjalan."]
    sents = []
    for r in priority[:n]:
        sents.append(f"- {r['label']}: rata-rata {r['mean']}/100 "
                     f"(target {'maksimal' if DIMS[r['dim']]['dir']=='bad' else 'minimal'} {r['target']}). "
                     f"Rekomendasi: {r['rekomendasi']}.")
    return sents
