
# -*- coding: utf-8 -*-
# Bank item asesmen (adaptasi Bahasa Indonesia).
# CATATAN LISENSI: MBI-GS adalah properti Mind Garden, Inc.
# Untuk penggunaan komersial (training berbayar) sebaiknya lisensi resmi,
# atau ganti dengan OLBI (Oldenburg Burnout Inventory) yang open access.

SCALE_PSS  = [(0,"Tidak pernah"),(1,"Hampir tidak pernah"),(2,"Kadang-kadang"),(3,"Cukup sering"),(4,"Sangat sering")]
SCALE_MBI  = [(0,"Tidak pernah"),(1,"Beberapa kali setahun atau lebih jarang"),(2,"Satu kali sebulan atau lebih jarang"),(3,"Beberapa kali sebulan"),(4,"Satu kali seminggu"),(5,"Beberapa kali seminggu"),(6,"Setiap hari")]
SCALE_WL   = [(1,"Sangat tidak setuju"),(2,"Tidak setuju"),(3,"Netral"),(4,"Setuju"),(5,"Sangat setuju")]
SCALE_TIS  = [(1,"Sangat tidak setuju"),(2,"Tidak setuju"),(3,"Netral"),(4,"Setuju"),(5,"Sangat setuju")]
SCALE_PSQL = [(1,"Sangat tidak setuju"),(2,"Tidak setuju"),(3,"Agak tidak setuju"),(4,"Netral"),(5,"Agak setuju"),(6,"Setuju"),(7,"Sangat setuju")]

INSTRUMENTS = [
 dict(key="PSS", name="Bagian 1 — Tingkat Stres (PSS-10)",
      intro="Jawab berdasarkan pengalaman Anda dalam SATU BULAN TERAKHIR.",
      scale=SCALE_PSS, min=0, max=4, items=[
   dict(n=1,  dim="PSS", rev=False, text="Dalam sebulan terakhir, seberapa sering Anda merasa kesal karena hal yang terjadi di luar dugaan?"),
   dict(n=2,  dim="PSS", rev=False, text="Seberapa sering Anda merasa tidak mampu mengendalikan hal-hal penting dalam hidup Anda?"),
   dict(n=3,  dim="PSS", rev=False, text="Seberapa sering Anda merasa gelisah dan stres?"),
   dict(n=4,  dim="PSS", rev=True,  text="Seberapa sering Anda merasa yakin dengan kemampuan Anda menangani masalah pribadi?"),
   dict(n=5,  dim="PSS", rev=True,  text="Seberapa sering Anda merasa segala sesuatu berjalan sesuai keinginan Anda?"),
   dict(n=6,  dim="PSS", rev=False, text="Seberapa sering Anda merasa tidak mampu mengatasi semua hal yang harus Anda lakukan?"),
   dict(n=7,  dim="PSS", rev=True,  text="Seberapa sering Anda mampu mengendalikan hal-hal yang mengganggu Anda?"),
   dict(n=8,  dim="PSS", rev=False, text="Seberapa sering Anda merasa mampu mengendalikan cara Anda menggunakan waktu?"),
   dict(n=9,  dim="PSS", rev=False, text="Seberapa sering Anda merasa kesulitan menumpuk begitu banyak hingga Anda yakin tidak bisa mengatasinya?"),
   dict(n=10, dim="PSS", rev=True,  text="Seberapa sering Anda merasa hal-hal terjadi sesuai keinginan Anda?"),
 ]),
 dict(key="MBI", name="Bagian 2 — Tingkat Burnout (MBI-GS)",
      intro="Jawab berdasarkan perasaan Anda terhadap PEKERJAAN saat ini.",
      scale=SCALE_MBI, min=0, max=6, items=[
   dict(n=1,  dim="MBI_EX", rev=False, text="Saya merasa emosi terkuras karena pekerjaan saya."),
   dict(n=2,  dim="MBI_EX", rev=False, text="Di akhir hari kerja, saya merasa kehabisan tenaga."),
   dict(n=3,  dim="MBI_EX", rev=False, text="Saya merasa lelah ketika bangun di pagi hari dan harus menghadapi hari kerja lain."),
   dict(n=4,  dim="MBI_PE",  rev=False, text="Saya mampu menemukan solusi efektif untuk masalah yang muncul dalam pekerjaan."),
   dict(n=5,  dim="MBI_CY", rev=False, text="Saya merasa semakin sinis (tidak peduli) terhadap pekerjaan saya."),
   dict(n=6,  dim="MBI_CY", rev=False, text="Saya merasa ragu akan pentingnya pekerjaan saya."),
   dict(n=7,  dim="MBI_PE",  rev=False, text="Saya merasa mampu menciptakan suasana santai dan menyenangkan bagi rekan kerja."),
   dict(n=8,  dim="MBI_EX", rev=False, text="Saya merasa terkuras secara emosional karena pekerjaan saya."),
   dict(n=9,  dim="MBI_PE",  rev=False, text="Saya merasa energik ketika melakukan pekerjaan saya."),
   dict(n=10, dim="MBI_PE",  rev=False, text="Saya mampu memahami perasaan rekan kerja."),
   dict(n=11, dim="MBI_CY", rev=False, text="Saya merasa kehilangan minat pada pekerjaan saya."),
   dict(n=12, dim="MBI_PE",  rev=False, text="Saya merasa menjadi semakin efektif dalam pekerjaan saya."),
   dict(n=13, dim="MBI_EX", rev=False, text="Saya merasa terbakar habis (burnt out) karena pekerjaan saya."),
   dict(n=14, dim="MBI_PE",  rev=False, text="Saya merasa yakin bahwa saya mampu memberikan kontribusi penting."),
   dict(n=15, dim="MBI_CY", rev=False, text="Saya kehilangan semangat terhadap pekerjaan saya."),
   dict(n=16, dim="MBI_PE",  rev=False, text="Saya merasa mampu membangun suasana positif dengan mudah."),
 ]),
 dict(key="WLEIS", name="Bagian 3 — Kecerdasan Emosional (WLEIS)",
      intro="Jawab sesuai diri Anda sebenarnya.",
      scale=SCALE_WL, min=1, max=5, items=[
   dict(n=1,  dim="SEA", rev=False, text="Saya memahami dengan baik mengapa saya memiliki perasaan tertentu."),
   dict(n=2,  dim="ROE", rev=False, text="Saya mampu mengendalikan emosi saya sendiri."),
   dict(n=3,  dim="OEA", rev=False, text="Saya memiliki pemahaman yang baik tentang emosi orang-orang di sekitar saya."),
   dict(n=4,  dim="UOE", rev=False, text="Saya selalu menetapkan target untuk diri saya lalu berusaha sebaik mungkin untuk mencapainya."),
   dict(n=5,  dim="SEA", rev=True,  text="Saya tidak pernah tahu persis apakah saya sedang bahagia atau tidak."),
   dict(n=6,  dim="ROE", rev=False, text="Saya mampu mengendalikan emosi saya dan menangani kesulitan dengan rasional."),
   dict(n=7,  dim="OEA", rev=False, text="Saya selalu tahu emosi teman-teman saya dari perilaku mereka."),
   dict(n=8,  dim="UOE", rev=True,  text="Saya tidak pernah berusaha memberi semangat pada diri sendiri untuk mencapai target."),
   dict(n=9,  dim="SEA", rev=False, text="Saya benar-benar memahami apa yang saya rasakan."),
   dict(n=10, dim="ROE", rev=False, text="Saya mampu mengendalikan emosi saya sehingga bisa mengekspresikannya secara rasional."),
   dict(n=11, dim="OEA", rev=False, text="Saya peka terhadap perasaan dan emosi orang lain."),
   dict(n=12, dim="ROE", rev=False, text="Saya cukup mampu mengendalikan emosi saya sendiri."),
   dict(n=13, dim="OEA", rev=False, text="Saya selalu bisa mengetahui mengapa orang merasakan sesuatu."),
   dict(n=14, dim="UOE", rev=True,  text="Saya tidak pernah meyakinkan diri sendiri bahwa saya adalah pribadi yang kompeten."),
   dict(n=15, dim="SEA", rev=False, text="Saya cukup sering menyadari perasaan saya sendiri."),
   dict(n=16, dim="ROE", rev=False, text="Saya selalu bisa menenangkan diri dengan cepat ketika sangat marah."),
 ]),
 dict(key="UWES", name="Bagian 4 — Keterlibatan Kerja (UWES-9)",
      intro="Jawab berdasarkan perasaan Anda terhadap pekerjaan saat ini.",
      scale=SCALE_MBI, min=0, max=6, items=[
   dict(n=1, dim="VIG", rev=False, text="Di tempat kerja, saya merasa penuh energi."),
   dict(n=2, dim="DED", rev=False, text="Saya merasa antusias dengan pekerjaan saya."),
   dict(n=3, dim="ABS", rev=False, text="Saya tenggelam dalam pekerjaan saya."),
   dict(n=4, dim="VIG", rev=False, text="Ketika bangun pagi, saya merasa ingin pergi bekerja."),
   dict(n=5, dim="DED", rev=False, text="Pekerjaan saya menginspirasi saya."),
   dict(n=6, dim="ABS", rev=False, text="Ketika bekerja, saya lupa segala sesuatu di sekitar saya."),
   dict(n=7, dim="DED", rev=False, text="Saya bangga dengan pekerjaan yang saya lakukan."),
   dict(n=8, dim="VIG", rev=False, text="Saya mampu bekerja dalam waktu yang lama tanpa lelah."),
   dict(n=9, dim="ABS", rev=False, text="Saya merasa senang ketika bekerja dengan intensitas tinggi."),
 ]),
 dict(key="TIS", name="Bagian 5 — Niat Keluar (TIS-6)",
      intro="Jawab sesuai kondisi Anda saat ini terhadap organisasi/perusahaan Anda.",
      scale=SCALE_TIS, min=1, max=5, items=[
   dict(n=1, dim="TIS", rev=False, text="Saya sering berpikir untuk keluar dari organisasi/perusahaan saya."),
   dict(n=2, dim="TIS", rev=False, text="Sangat mungkin saya akan mencari pekerjaan lain dalam waktu dekat."),
   dict(n=3, dim="TIS", rev=False, text="Saya akan meninggalkan perusahaan jika ada tawaran pekerjaan yang lebih baik."),
   dict(n=4, dim="TIS", rev=False, text="Dalam setahun ke depan, saya akan berusaha mencari pekerjaan di luar perusahaan ini."),
   dict(n=5, dim="TIS", rev=False, text="Saya sering membicarakan keinginan untuk berhenti dengan rekan kerja."),
   dict(n=6, dim="TIS", rev=False, text="Saya berniat meninggalkan perusahaan ini."),
 ]),
 dict(key="PSQ", name="Bagian 6 — Rasa Aman Psikologis (PSQ-ORG)",
      intro="Jawab berdasarkan suasana di TIM / PERUSAHAAN Anda saat ini.",
      scale=SCALE_PSQL, min=1, max=7, items=[
   dict(n=1, dim="PSQ", rev=False, text="Jika saya membuat kesalahan di tempat kerja, hal itu sering dijadikan pembelajaran."),
   dict(n=2, dim="PSQ", rev=False, text="Di tempat kerja saya, anggota tim dapat membahas masalah dan kesulitan secara terbuka."),
   dict(n=3, dim="PSQ", rev=False, text="Orang-orang di tempat kerja saya mampu menerima kekurangan anggota tim lainnya."),
   dict(n=4, dim="PSQ", rev=False, text="Di tempat kerja saya, anggota tim memandang anggota lainnya sebagai pribadi yang kompeten."),
   dict(n=5, dim="PSQ", rev=False, text="Bersama tim saya, saya tidak perlu menyembunyikan siapa diri saya yang sebenarnya."),
   dict(n=6, dim="PSQ", rev=False, text="Orang-orang di tempat kerja saya saling menghormati satu sama lain."),
   dict(n=7, dim="PSQ", rev=False, text="Di tempat kerja saya, orang merasa aman untuk mengambil risiko."),
 ]),
]

# Metadata dimensi: label panjang, label radar PENDEK & awam, arah favorable, target 0-100
DIMS = {
 "PSS":    dict(label="Stres Persepsian (PSS)",            radar="Stres",        dir="bad",  target=40),
 "MBI_EX": dict(label="Kelelahan Emosional (Exhaustion)",  radar="Lelah Emosi",  dir="bad",  target=33),
 "MBI_CY": dict(label="Sinisme (Cynicism)",                radar="Sinisme",      dir="bad",  target=33),
 "MBI_PE": dict(label="Efikasi Profesional",               radar="Rasa Mampu",   dir="good", target=67),
 "SEA":    dict(label="Pemahaman Emosi Diri (SEA)",        radar="Kenal Diri",   dir="good", target=60),
 "OEA":    dict(label="Pemahaman Emosi Orang Lain (OEA)",  radar="Kenal Orang",  dir="good", target=60),
 "ROE":    dict(label="Regulasi Emosi (ROE)",              radar="Atur Emosi",   dir="good", target=60),
 "UOE":    dict(label="Penggunaan Emosi (UOE)",            radar="Emosi ke Target", dir="good", target=60),
 "VIG":    dict(label="Semangat (Vigour)",                 radar="Energi",       dir="good", target=60),
 "DED":    dict(label="Dedikasi",                          radar="Dedikasi",     dir="good", target=60),
 "ABS":    dict(label="Absorpsi / Fokus Penuh (Flow)",     radar="Fokus",        dir="good", target=60),
 "TIS":    dict(label="Niat Keluar (Turnover Intention)",  radar="Niat Keluar",  dir="bad",  target=33),
 "PSQ":    dict(label="Rasa Aman Psikologis (PSQ-ORG)",    radar="Aman Bersuara",dir="good", target=70),
}
DIM_ORDER = list(DIMS.keys())

MODULE_MAP = {
 "PSS":    "Modul Regulasi Emosi & Manajemen Stres",
 "MBI_EX": "Modul Burnout Recovery & Manajemen Beban Kerja",
 "MBI_CY": "Modul Rekoneksi Makna Kerja (Purpose & Values)",
 "MBI_PE": "Modul Penguatan Kompetensi & Small Wins",
 "SEA":    "Modul 2: Emotional Regulation & Self-Mastery",
 "OEA":    "Modul 3: Communication for Trust & Inclusion",
 "ROE":    "Modul 2: Emotional Regulation & Self-Mastery",
 "UOE":    "Modul 3: Communication for Trust & Inclusion + goal-setting praktis",
 "VIG":    "Modul Engagement & Energy Management",
 "DED":    "Modul Rekoneksi Makna Kerja (Purpose & Values)",
 "ABS":    "Modul Engagement & Deep Work",
 "TIS":    "Modul Retensi & Stay Interview untuk HR/Leader",
 "PSQ":    "Modul 1: Psychological Safety Foundations",
}

# Label pendek untuk tampilan admin (pemilihan asesmen per training)
INST_SHORT = {
 "PSS":   "A. PSS-10 - Stres (10 item)",
 "MBI":   "B. MBI-GS - Burnout (16 item)",
 "WLEIS": "C. WLEIS - Kecerdasan Emosional (16 item)",
 "UWES":  "D. UWES-9 - Work Engagement (9 item)",
 "TIS":   "E. TIS-6 - Niat Keluar (6 item)",
 "PSQ":   "F. PSQ-ORG - Psychological Safety (7 item)",
}


# ============================================================
# INSTRUMEN TAMBAHAN (katalog produk) - sumber: instrumen publik
# BFI-10 (Gosling), Grit-S (Duckworth), BSCS (Tangney), BRS (Smith),
# GPS (Lay), SLQ adaptasi, dimensi budaya (adaptasi OCAI Cameron-Quinn),
# COG = screening kognitif 12 item (buatan, bukan pengganti tes GMA bersistem)
# ============================================================
SCALE_15 = [(1,"Sangat tidak setuju"),(2,"Tidak setuju"),(3,"Netral"),(4,"Setuju"),(5,"Sangat setuju")]

def _mcq(opts, key):
    return dict(opts=opts, key=key)

EXTRA_INSTRUMENTS = [
 dict(key="BFI", name="Bagian 7 - Kepribadian Utuh (Big Five / BFI-10)",
      intro="Jawab sesuai diri Anda sebenarnya. Tidak ada jawaban benar/salah.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="O", rev=False, text="Saya penuh ide baru dan penasaran pada banyak hal."),
   dict(n=2,  dim="O", rev=True,  text="Saya jarang tertarik pada hal baru atau berpikir imajinatif."),
   dict(n=3,  dim="C", rev=False, text="Saya orang yang teratur dan menyiapkan segala sesuatunya."),
   dict(n=4,  dim="C", rev=True,  text="Saya cenderung bersantai dan kurang menepati rencana."),
   dict(n=5,  dim="E", rev=False, text="Saya ekspresif dan mudah bergaul dalam kelompok."),
   dict(n=6,  dim="E", rev=True,  text="Saya cenderung pendiam dan tidak suka menonjol."),
   dict(n=7,  dim="A", rev=False, text="Saya mudah bersimpati dan mempercayai orang lain."),
   dict(n=8,  dim="A", rev=True,  text="Saya cenderung mencari kesalahan orang lain dan curiga."),
   dict(n=9,  dim="N", rev=False, text="Saya mudah cemas dan mudah tersinggung."),
   dict(n=10, dim="N", rev=True,  text="Saya tenang dan stabil menghadapi tekanan."),
 ]),
 dict(key="GRIT", name="Bagian 8 - Grit & Ketekunan (Grit-S)",
      intro="Jawab sesuai diri Anda dalam 1-2 tahun terakhir.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1, dim="GRIT_PE", rev=False, text="Saya pantang menyerah menghadapi kesulitan."),
   dict(n=2, dim="GRIT_CI", rev=True,  text="Saya sering berpindah minat dan sulit fokus pada satu hal."),
   dict(n=3, dim="GRIT_PE", rev=False, text="Kegagalan tidak menghentikan saya, justru membuat saya lebih berusaha."),
   dict(n=4, dim="GRIT_CI", rev=True,  text="Minat saya berubah-ubah dari waktu ke waktu."),
   dict(n=5, dim="GRIT_PE", rev=False, text="Saya adalah pekerja keras."),
   dict(n=6, dim="GRIT_PE", rev=False, text="Saya menyelesaikan apapun yang sudah saya mulai."),
   dict(n=7, dim="GRIT_CI", rev=True,  text="Saya sulit menjaga fokus pada hal yang memakan waktu lama."),
   dict(n=8, dim="GRIT_CI", rev=False, text="Saya bertahan pada tujuan yang sama dalam jangka panjang."),
 ]),
 dict(key="SELFCTRL", name="Bagian 9 - Kontrol Diri (Brief Self-Control Scale)",
      intro="Jawab sesuai kebiasaan Anda sehari-hari.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="SELFCTRL", rev=False, text="Saya pandai menahan godaan."),
   dict(n=2,  dim="SELFCTRL", rev=True,  text="Saya sering melakukan hal yang akhirnya merugikan saya."),
   dict(n=3,  dim="SELFCTRL", rev=True,  text="Saya sering bertindak tanpa berpikir panjang."),
   dict(n=4,  dim="SELFCTRL", rev=True,  text="Saya sering mengucapkan hal yang sebaiknya tidak saya ucapkan."),
   dict(n=5,  dim="SELFCTRL", rev=True,  text="Saya merasa hidup saya kurang teratur dan terkendali."),
   dict(n=6,  dim="SELFCTRL", rev=False, text="Saya mampu bekerja tekun pada tugas jangka panjang."),
   dict(n=7,  dim="SELFCTRL", rev=True,  text="Saya mudah terganggu oleh hal-hal kecil."),
   dict(n=8,  dim="SELFCTRL", rev=False, text="Saya mampu menolak distraksi saat sedang fokus."),
   dict(n=9,  dim="SELFCTRL", rev=True,  text="Saya sering menyesali keputusan yang saya ambil."),
   dict(n=10, dim="SELFCTRL", rev=True,  text="Saya sering tidak memikirkan akibat dari tindakan saya."),
   dict(n=11, dim="SELFCTRL", rev=False, text="Saya mampu bangkit kembali setelah berbuat kesalahan."),
   dict(n=12, dim="SELFCTRL", rev=True,  text="Saya jarang memperhatikan batas yang saya tetapkan untuk diri sendiri."),
   dict(n=13, dim="SELFCTRL", rev=True,  text="Saya mudah kehilangan kendali atas emosi saya."),
 ]),
 dict(key="RESIL", name="Bagian 10 - Resiliensi (Brief Resilience Scale)",
      intro="Jawab sesuai cara Anda menghadapi masa sulit.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1, dim="RESIL", rev=False, text="Saya biasanya pulih dengan cepat setelah kesulitan."),
   dict(n=2, dim="RESIL", rev=True,  text="Saya sulit bangkit kembali setelah pengalaman buruk."),
   dict(n=3, dim="RESIL", rev=False, text="Saya tidak mudah goyah oleh stres."),
   dict(n=4, dim="RESIL", rev=True,  text="Saya kesulitan menyesuaikan diri dengan hal buruk."),
   dict(n=5, dim="RESIL", rev=False, text="Saya mampu melewati masa sulit tanpa terganggu lama."),
   dict(n=6, dim="RESIL", rev=True,  text="Saya cenderung lama terpuruk setelah kegagalan."),
 ]),
 dict(key="PROCR", name="Bagian 11 - Prokrastinasi (General Procrastination Scale)",
      intro="Jawab sesuai kebiasaan kerja Anda.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="PROCR", rev=False, text="Saya menunda tugas yang seharusnya dikerjakan hari ini."),
   dict(n=2,  dim="PROCR", rev=False, text="Saya mengerjakan tugas mendekati tenggat waktu."),
   dict(n=3,  dim="PROCR", rev=True,  text="Saya menyelesaikan tugas jauh sebelum deadline."),
   dict(n=4,  dim="PROCR", rev=True,  text="Saya merencanakan pekerjaan agar selesai tepat waktu."),
   dict(n=5,  dim="PROCR", rev=False, text="Saya menunda memulai tugas yang tidak saya sukai."),
   dict(n=6,  dim="PROCR", rev=True,  text="Saya langsung mengerjakan tugas begitu diberikan."),
   dict(n=7,  dim="PROCR", rev=False, text="Saya mengerjakan hal lain untuk menghindari tugas utama."),
   dict(n=8,  dim="PROCR", rev=True,  text="Saya jarang menunda pekerjaan penting."),
   dict(n=9,  dim="PROCR", rev=False, text="Saya kehabisan waktu karena mengerjakan hal kecil dulu."),
   dict(n=10, dim="PROCR", rev=False, text="Saya kesulitan memulai tugas yang membosankan."),
   dict(n=11, dim="PROCR", rev=True,  text="Saya selalu tepat waktu menyelesaikan kewajiban."),
   dict(n=12, dim="PROCR", rev=False, text="Saya menunda pekerjaan meski tahu konsekuensinya."),
   dict(n=13, dim="PROCR", rev=True,  text="Saya menyelesaikan tugas tepat waktu tanpa perlu didesak."),
   dict(n=14, dim="PROCR", rev=True,  text="Saya jarang terburu-buru di menit-menit terakhir."),
   dict(n=15, dim="PROCR", rev=True,  text="Saya mengerjakan tugas sesuai jadwal yang saya buat."),
   dict(n=16, dim="PROCR", rev=False, text="Saya sering berkata 'nanti saja' pada tugas penting."),
   dict(n=17, dim="PROCR", rev=True,  text="Saya menahan kesenangan sesaat demi tugas penting."),
   dict(n=18, dim="PROCR", rev=True,  text="Saya tidak perlu didesak untuk mulai bekerja."),
   dict(n=19, dim="PROCR", rev=False, text="Saya menunggu 'mood yang tepat' untuk mulai bekerja."),
   dict(n=20, dim="PROCR", rev=True,  text="Saya selalu sempat menyelesaikan yang saya rencanakan."),
 ]),
 dict(key="LEADER", name="Bagian 12 - Kepemimpinan Diri (Self-Leadership)",
      intro="Jawab sesuai cara Anda memimpin diri sendiri dalam bekerja.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1, dim="LEAD_PF", rev=False, text="Saya menetapkan target kerja yang jelas untuk diri sendiri."),
   dict(n=2, dim="LEAD_PF", rev=False, text="Saya memantau kemajuan diri terhadap target."),
   dict(n=3, dim="LEAD_PF", rev=False, text="Saya mengevaluasi diri setelah menyelesaikan tugas."),
   dict(n=4, dim="LEAD_NR", rev=False, text="Saya memilih tugas yang memang saya nikmati."),
   dict(n=5, dim="LEAD_NR", rev=False, text="Saya menemukan kesenangan di balik tugas yang sulit."),
   dict(n=6, dim="LEAD_NR", rev=False, text="Saya menciptakan tantangan bagi diri sendiri."),
   dict(n=7, dim="LEAD_CT", rev=False, text="Saya membayangkan keberhasilan sebelum bertindak."),
   dict(n=8, dim="LEAD_CT", rev=False, text="Saya berbicara positif kepada diri sendiri saat kesulitan."),
   dict(n=9, dim="LEAD_CT", rev=False, text="Saya mencari pelajaran dari setiap kegagalan."),
 ]),
 dict(key="CULTURE", name="Bagian 13 - Budaya Kerja Tim (4 Tipe Budaya)",
      intro="Jawab sesuai suasana tim/perusahaan Anda SAAT INI.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="KLAN",   rev=False, text="Tim kami terasa seperti keluarga - saling peduli satu sama lain."),
   dict(n=2,  dim="ADHO",   rev=False, text="Tim kami suka mengambil risiko dan mencoba hal baru."),
   dict(n=3,  dim="MARKET", rev=False, text="Hasil dan target sangat menentukan penilaian di tim kami."),
   dict(n=4,  dim="HIER",   rev=False, text="Tim kami punya aturan dan prosedur yang jelas."),
   dict(n=5,  dim="KLAN",   rev=False, text="Keputusan penting melibatkan anggota (partisipatif)."),
   dict(n=6,  dim="ADHO",   rev=False, text="Inovasi dan kreativitas sangat dihargai di tim kami."),
   dict(n=7,  dim="MARKET", rev=False, text="Persaingan dan semangat menang terasa di tim kami."),
   dict(n=8,  dim="HIER",   rev=False, text="Jalur karir dan struktur organisasi sudah jelas."),
   dict(n=9,  dim="KLAN",   rev=False, text="Loyalitas dan kepercayaan sangat ditekankan."),
   dict(n=10, dim="ADHO",   rev=False, text="Tim kami dinamis dan selalu mencari peluang baru."),
   dict(n=11, dim="MARKET", rev=False, text="Kami menilai kerja dari output, bukan dari proses."),
   dict(n=12, dim="HIER",   rev=False, text="Stabilitas dan kepastian diutamakan di tim kami."),
 ]),
 dict(key="COG", name="Bagian 14 - Screening Kognitif (Logika & Numerik)",
      intro="Pilih jawaban yang paling tepat. Waktu yang disarankan: 15 menit.",
      scale=None, min=0, max=1, mcq=True, items=[
   dict(n=1,  dim="COG_GMA", **_mcq(["38","40","42","44"], 2), text="Deret angka: 2, 6, 12, 20, 30, ... angka berikutnya?"),
   dict(n=2,  dim="COG_GMA", **_mcq(["1 menit","3 menit","30 menit","100 menit"], 1), text="Jika 3 mesin membuat 3 kue dalam 3 menit, berapa menit yang dibutuhkan 100 mesin untuk 100 kue?"),
   dict(n=3,  dim="COG_GMA", **_mcq(["Semua A adalah C","Sebagian A adalah C","Tidak ada A yang C","B adalah A"], 0), text="Semua A adalah B. Semua B adalah C. Kesimpulan yang pasti benar?"),
   dict(n=4,  dim="COG_GMA", **_mcq(["S","T","U","V"], 2), text="Deret huruf: A, C, F, J, O, ... huruf berikutnya?"),
   dict(n=5,  dim="COG_GMA", **_mcq(["25","30","35","40"], 1), text="15% dari 200 adalah..."),
   dict(n=6,  dim="COG_GMA", **_mcq(["Budi boleh cuti","Budi tidak boleh cuti","Budi bukan karyawan","Cuti hanya untuk Budi"], 0), text="Semua karyawan boleh mengambil cuti. Budi adalah karyawan. Kesimpulan?"),
   dict(n=7,  dim="COG_GMA", **_mcq(["60","70","80","90"], 2), text="Deret: 5, 10, 20, 40, ... angka berikutnya?"),
   dict(n=8,  dim="COG_GMA", **_mcq(["Sedang hujan","Tidak sedang hujan","Jalan akan segera basah","Jalan tidak pernah basah"], 1), text="Jika hujan maka jalan basah. Fakta: jalan tidak basah. Kesimpulan?"),
   dict(n=9,  dim="COG_GMA", **_mcq(["11","12","13","14"], 2), text="Rata-rata dari 4, 8, 15, dan x adalah 10. Nilai x?"),
   dict(n=10, dim="COG_GMA", **_mcq(["A","B","C","Sama tua"], 0), text="A lebih tua dari B. C lebih muda dari B. Siapa yang paling tua?"),
   dict(n=11, dim="COG_GMA", **_mcq(["11","12","13","21"], 2), text="Deret: 1, 1, 2, 3, 5, 8, ... angka berikutnya?"),
   dict(n=12, dim="COG_GMA", **_mcq(["6 hari","10 hari","12 hari","15 hari"], 3), text="Proyek selesai 10 hari oleh 6 orang. Jika dikerjakan 4 orang dengan kecepatan sama, berapa hari?"),
 ]),
]

INSTRUMENTS += EXTRA_INSTRUMENTS

DIMS.update({
 "O":        dict(label="Keterbukaan & Keingintahuan (Openness)",      radar="Keterbukaan",  dir="good", target=60),
 "C":        dict(label="Ketertiban & Disiplin (Conscientiousness)",   radar="Ketertiban",   dir="good", target=65),
 "E":        dict(label="Extraversi & Keaktifan Sosial",               radar="Sosial",       dir="good", target=55),
 "A":        dict(label="Keramahan & Kerja Sama",                      radar="Keramahan",    dir="good", target=60),
 "N":        dict(label="Neurotisisme (Emosional Tak Stabil)",         radar="Neurotis",     dir="bad",  target=33),
 "GRIT_PE":  dict(label="Ketekunan (Perseverance)",                    radar="Tekun",        dir="good", target=60),
 "GRIT_CI":  dict(label="Konsistensi Minat",                           radar="Konsisten",    dir="good", target=55),
 "SELFCTRL": dict(label="Kontrol Diri",                                radar="Kontrol Diri", dir="good", target=60),
 "RESIL":    dict(label="Resiliensi (Kemampuan Pulih)",                radar="Resiliensi",   dir="good", target=60),
 "PROCR":    dict(label="Prokrastinasi (Menunda-nunda)",               radar="Prokrastinasi",dir="bad",  target=33),
 "LEAD_PF":  dict(label="Kepemimpinan Diri: Fokus Perilaku",           radar="Fokus Aksi",   dir="good", target=60),
 "LEAD_NR":  dict(label="Kepemimpinan Diri: Motivasi Alami",           radar="Motivasi Alami",dir="good",target=60),
 "LEAD_CT":  dict(label="Kepemimpinan Diri: Pikiran Konstruktif",      radar="Pikiran Positif",dir="good",target=60),
 "KLAN":     dict(label="Budaya Klan (Rasa Keluarga)",                 radar="Budaya Klan",  dir="good", target=50),
 "ADHO":     dict(label="Budaya Adhocracy (Inovasi)",                  radar="Budaya Inovasi",dir="good",target=50),
 "MARKET":   dict(label="Budaya Pasar (Orientasi Hasil)",              radar="Budaya Pasar", dir="good", target=50),
 "HIER":     dict(label="Budaya Hierarki (Struktur & Kepastian)",      radar="Budaya Struktur",dir="good",target=50),
 "COG_GMA":  dict(label="Kemampuan Kognitif (Screening)",              radar="Kognitif",     dir="good", target=60),
})
DIM_ORDER = list(DIMS.keys())

INST_SHORT.update({
 "BFI":      "G. Big Five - Kepribadian (10 item)",
 "GRIT":     "H. Grit - Ketekunan (8 item)",
 "SELFCTRL": "I. Kontrol Diri (13 item)",
 "RESIL":    "J. Resiliensi (6 item)",
 "PROCR":    "K. Prokrastinasi (20 item)",
 "LEADER":   "L. Self-Leadership (9 item)",
 "CULTURE":  "M. Budaya Kerja Tim (12 item)",
 "COG":      "N. Screening Kognitif (12 soal)",
})


# ============================================================
# INSTRUMEN BATCH 3
# CATATAN KEJUJURAN:
# - DASS-21, PHQ-9, GAD-7, WHO-5 = instrumen teruji, bebas utk penggunaan riset/praktik
# - CFIT-style matriks = pendekatan fluid reasoning bersistem (gambar generate programatik),
#   layak utk screening GMA; keputusan besar tetap disarankan tes GMA penuh oleh psikolog berlisensi
# - DISC & MBTI-style = INDIKATOR GAYA untuk self-awareness, BUKAN alat seleksi (validitas prediktif rendah)
# - Profil Sales, Gaya Kepemimpinan Situasional, Servant, Keadilan = adaptasi berbasis literatur
# ============================================================
SCALE_03 = [(0,"Tidak berlaku sama sekali"),(1,"Berlaku sebagian"),(2,"Berlaku cukup banyak"),(3,"Berlaku sangat banyak / hampir selalu")]
SCALE_04 = [(0,"Tidak pernah"),(1,"Kadang-kadang"),(2,"Cukup sering"),(3,"Sering"),(4,"Selalu")]

def _img_item(n, key):
    return dict(n=n, dim="COG_IMG", rev=False,
                img=f"assets/mx/q{n}.png",
                opts=["A","B","C","D","E","F","G","H"], key=key)

EXTRA2 = [
 dict(key="CFIT", name="Bagian 15 - Penalaran Matriks Bergambar (GMA Fluid)",
      intro="Lihat pola pada matriks 3x3, lalu pilih gambar (A-H) yang tepat mengisi kotak bertanda '?'. "
            "Kerjakan searah, 1 soal = 1 pola. Ini penalaran fluid - kemampuan memecahkan masalah baru.",
      scale=None, min=0, max=1, mcq=True, items=[
   _img_item(1, 1), _img_item(2, 4),
   _img_item(3, 2), _img_item(4, 4),
   _img_item(5, 4), _img_item(6, 0),
   _img_item(7, 2), _img_item(8, 1),
 ]),
 dict(key="DASS", name="Bagian 16 - Kesehatan Mental: DASS-21 (Depresi, Anxiety, Stress)",
      intro="Jawab berdasarkan kondisi Anda dalam SATU MINGGU TERAKHIR. Hasil bersifat screening, "
            "bukan diagnosis - hasil 'perlu perhatian' sebaiknya ditindaklanjuti konseling profesional.",
      scale=SCALE_03, min=0, max=3, items=[
   dict(n=1,  dim="DASS_S", rev=False, text="Saya merasa sulit untuk tenang."),
   dict(n=2,  dim="DASS_A", rev=False, text="Saya merasa mulut kering."),
   dict(n=3,  dim="DASS_D", rev=False, text="Saya tampak tidak dapat merasakan hal positif sama sekali."),
   dict(n=4,  dim="DASS_S", rev=False, text="Saya mengalami kesulitan bernapas (napas pendek, tersedak)."),
   dict(n=5,  dim="DASS_D", rev=False, text="Saya sulit mengambil inisiatif untuk melakukan sesuatu."),
   dict(n=6,  dim="DASS_S", rev=False, text="Saya cenderung bereaksi berlebihan terhadap situasi."),
   dict(n=7,  dim="DASS_A", rev=False, text="Saya merasa gemetar (pada tangan atau kaki)."),
   dict(n=8,  dim="DASS_S", rev=False, text="Saya merasa banyak energi terkuras oleh kecemasan."),
   dict(n=9,  dim="DASS_A", rev=False, text="Saya cemas pada situasi yang bisa membuat saya panik dan malu."),
   dict(n=10, dim="DASS_D", rev=False, text="Saya merasa tidak ada hal yang bisa saya nantikan."),
   dict(n=11, dim="DASS_S", rev=False, text="Saya merasa gelisah."),
   dict(n=12, dim="DASS_S", rev=False, text="Saya sulit untuk bersantai."),
   dict(n=13, dim="DASS_D", rev=False, text="Saya merasa murung dan sedih."),
   dict(n=14, dim="DASS_S", rev=False, text="Saya tidak toleran terhadap gangguan yang menghalangi pekerjaan saya."),
   dict(n=15, dim="DASS_A", rev=False, text="Saya merasa panik."),
   dict(n=16, dim="DASS_D", rev=False, text="Saya tidak antusias terhadap apapun."),
   dict(n=17, dim="DASS_D", rev=False, text="Saya merasa tidak berharga sebagai pribadi."),
   dict(n=18, dim="DASS_S", rev=False, text="Saya merasa mudah tersinggung."),
   dict(n=19, dim="DASS_A", rev=False, text="Saya menyadari detak jantung berdebar tanpa alasan fisik."),
   dict(n=20, dim="DASS_A", rev=False, text="Saya merasa takut tanpa alasan yang jelas."),
   dict(n=21, dim="DASS_D", rev=False, text="Saya merasa hidup tidak berarti."),
 ]),
 dict(key="PHQ", name="Bagian 17 - Screening Depresi (PHQ-9)",
      intro="Dalam 2 MINGGU terakhir, seberapa sering Anda terganggu oleh hal berikut? Screening, bukan diagnosis.",
      scale=SCALE_03, min=0, max=3, items=[
   dict(n=1, dim="PHQ", rev=False, text="Kurang berminat atau bergairah melakukan sesuatu."),
   dict(n=2, dim="PHQ", rev=False, text="Merasa murung, sedih, atau putus asa."),
   dict(n=3, dim="PHQ", rev=False, text="Sulit tidur/sulit tetap tidur, atau terlalu banyak tidur."),
   dict(n=4, dim="PHQ", rev=False, text="Merasa lelah atau kurang bertenaga."),
   dict(n=5, dim="PHQ", rev=False, text="Kurang nafsu makan atau terlalu banyak makan."),
   dict(n=6, dim="PHQ", rev=False, text="Merasa diri gagal, atau mengecewakan diri/keluarga."),
   dict(n=7, dim="PHQ", rev=False, text="Sulit berkonsentrasi pada pekerjaan atau kegiatan lain."),
   dict(n=8, dim="PHQ", rev=False, text="Gerak/berbicara sangat lambat, atau sebaliknya gelisah (orang lain menyadarinya)."),
   dict(n=9, dim="PHQ", rev=False, text="Merasa lebih baik mati, atau ingin melukai diri sendiri."),
 ]),
 dict(key="GAD", name="Bagian 18 - Screening Kecemasan (GAD-7)",
      intro="Dalam 2 MINGGU terakhir, seberapa sering Anda terganggu oleh hal berikut? Screening, bukan diagnosis.",
      scale=SCALE_03, min=0, max=3, items=[
   dict(n=1, dim="GAD", rev=False, text="Merasa cemas, gelisah, atau tegang."),
   dict(n=2, dim="GAD", rev=False, text="Tidak mampu menghentikan kekhawatiran."),
   dict(n=3, dim="GAD", rev=False, text="Terlalu banyak mengkhawatirkan berbagai hal."),
   dict(n=4, dim="GAD", rev=False, text="Sulit bersantai."),
   dict(n=5, dim="GAD", rev=False, text="Sangat gelisah sehingga sulit diam."),
   dict(n=6, dim="GAD", rev=False, text="Mudah tersinggung atau marah."),
   dict(n=7, dim="GAD", rev=False, text="Merasa takut seolah sesuatu yang buruk akan terjadi."),
 ]),
 dict(key="WHO5", name="Bagian 19 - Kesejahteraan Psikologis (WHO-5)",
      intro="Seberapa sering hal berikut terjadi pada Anda dalam 2 MINGGU terakhir?",
      scale=SCALE_04, min=0, max=4, items=[
   dict(n=1, dim="WHO5", rev=False, text="Saya merasa bersemangat dan penuh energi."),
   dict(n=2, dim="WHO5", rev=False, text="Saya merasa tenang dan santai."),
   dict(n=3, dim="WHO5", rev=False, text="Saya merasa aktif dan bersemangat."),
   dict(n=4, dim="WHO5", rev=False, text="Saya bangun dengan rasa segar dan beristirahat cukup."),
   dict(n=5, dim="WHO5", rev=False, text="Keseharian saya penuh dengan hal yang menarik."),
 ]),
]

EXTRA3 = [
 dict(key="DISC", name="Bagian 20 - Gaya Perilaku DISC (Indikator Gaya Kerja)",
      intro="Jawab sesuai diri Anda di TEMPAT KERJA. CATATAN: DISC adalah indikator gaya komunikasi "
            "untuk pengembangan diri dan kerja sama tim - bukan alat seleksi rekrutmen.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="DISC_D", rev=False, text="Saya mengambil keputusan cepat dan tegas."),
   dict(n=2,  dim="DISC_D", rev=False, text="Saya menantang orang lain untuk perform lebih baik."),
   dict(n=3,  dim="DISC_D", rev=False, text="Saya langsung ke intinya saat berbicara."),
   dict(n=4,  dim="DISC_D", rev=False, text="Saya frustrasi kalau orang terlalu lambat."),
   dict(n=5,  dim="DISC_D", rev=False, text="Saya suka mengambil kendali dalam situasi sulit."),
   dict(n=6,  dim="DISC_D", rev=False, text="Saya berani mengambil risiko."),
   dict(n=7,  dim="DISC_I", rev=False, text="Saya mudah akrab dengan orang baru."),
   dict(n=8,  dim="DISC_I", rev=False, text="Saya suka meyakinkan dan memotivasi orang lain."),
   dict(n=9,  dim="DISC_I", rev=False, text="Saya ceria dan bisa mencairkan suasana."),
   dict(n=10, dim="DISC_I", rev=False, text="Saya nyaman menjadi pusat perhatian."),
   dict(n=11, dim="DISC_I", rev=False, text="Saya optimis dan penuh antusiasme."),
   dict(n=12, dim="DISC_I", rev=False, text="Saya pandai membujuk orang lain."),
   dict(n=13, dim="DISC_S", rev=False, text="Saya pendengar yang sabar."),
   dict(n=14, dim="DISC_S", rev=False, text="Saya menghindari konflik sebisa mungkin."),
   dict(n=15, dim="DISC_S", rev=False, text="Saya setia pada orang dan rutinitas."),
   dict(n=16, dim="DISC_S", rev=False, text="Saya tenang dan stabil dalam situasi tegang."),
   dict(n=17, dim="DISC_S", rev=False, text="Saya senang membantu orang lain."),
   dict(n=18, dim="DISC_S", rev=False, text="Saya tidak suka perubahan mendadak."),
   dict(n=19, dim="DISC_C", rev=False, text="Saya memperhatikan detail dan akurasi."),
   dict(n=20, dim="DISC_C", rev=False, text="Saya mengikuti aturan dan prosedur."),
   dict(n=21, dim="DISC_C", rev=False, text="Saya menganalisis dulu sebelum bertindak."),
   dict(n=22, dim="DISC_C", rev=False, text="Saya menyukai kualitas dan ketepatan."),
   dict(n=23, dim="DISC_C", rev=False, text="Saya hati-hati dalam mengambil keputusan."),
   dict(n=24, dim="DISC_C", rev=False, text="S menyukai pekerjaan yang terstruktur.".replace("S menyukai","Saya menyukai")),
 ]),
 dict(key="MBTIX", name="Bagian 21 - Indikator Tipe Kepribadian (4 Dimensi)",
      intro="Jawab sesuai diri Anda yang paling sering terjadi, bukan yang diinginkan. CATATAN: "
            "indikator tipe seperti ini berguna untuk self-awareness dan komunikasi tim - "
            "tidak direkomendasikan untuk seleksi atau penilaian kinerja.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="EI", rev=False, text="Saya bersemangat saat berada di tengah banyak orang."),
   dict(n=2,  dim="EI", rev=True,  text="Saya butuh waktu sendiri untuk mengisi ulang energi."),
   dict(n=3,  dim="EI", rev=False, text="Saya berpikir sambil berbicara."),
   dict(n=4,  dim="EI", rev=True,  text="Saya memproses pikiran lebih dulu sebelum berbicara."),
   dict(n=5,  dim="SN", rev=False, text="Saya fokus pada fakta dan detail yang konkret."),
   dict(n=6,  dim="SN", rev=True,  text="Saya suka memikirkan kemungkinan dan gambaran besar."),
   dict(n=7,  dim="SN", rev=False, text="Saya percaya pada pengalaman yang sudah terbukti."),
   dict(n=8,  dim="SN", rev=True,  text="Saya tertarik pada ide-ide baru dan pola masa depan."),
   dict(n=9,  dim="TF", rev=False, text="Saya mengambil keputusan berdasarkan logika dan analisis."),
   dict(n=10, dim="TF", rev=True,  text="Saya mengambil keputusan berdasarkan nilai dan dampaknya pada orang."),
   dict(n=11, dim="TF", rev=False, text="Saya menilai argumen dari kebenarannya."),
   dict(n=12, dim="TF", rev=True,  text="Saya menilai argumen dari bagaimana perasaan orangnya."),
   dict(n=13, dim="JP", rev=False, text="Saya suka rencana yang jelas dan jadwal yang pasti."),
   dict(n=14, dim="JP", rev=True,  text="Saya suka fleksibel dan terbuka pada perubahan."),
   dict(n=15, dim="JP", rev=False, text="Saya merasa lega saat tugas selesai tepat waktu."),
   dict(n=16, dim="JP", rev=True,  text="Saya nyaman mengerjakan tugas mendekati tenggat."),
 ]),
 dict(key="SALES", name="Bagian 22 - Profil Sales & Drive Berjualan",
      intro="Jawab sesuai diri Anda dalam konteks berjualan / menghadapi klien.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="SALES_DRIVE", rev=False, text="Saya merasa bersemangat saat harus meyakinkan orang."),
   dict(n=2,  dim="SALES_RES",   rev=False, text="Penolakan tidak membuat saya patah semangat lama."),
   dict(n=3,  dim="SALES_REL",   rev=False, text="Saya menikmati membangun relasi jangka panjang dengan klien."),
   dict(n=4,  dim="SALES_TGT",   rev=False, text="Target angka membuat saya justru termotivasi."),
   dict(n=5,  dim="SALES_DRIVE", rev=False, text="Saya aktif mencari peluang berjualan tanpa disuruh."),
   dict(n=6,  dim="SALES_RES",   rev=False, text="Saya bisa kembali bersemangat dalam waktu singkat setelah ditolak."),
   dict(n=7,  dim="SALES_REL",   rev=False, text="Klien cenderung percaya dan terbuka pada saya."),
   dict(n=8,  dim="SALES_TGT",   rev=False, text="Saya memantau angka penjualan saya secara berkala."),
   dict(n=9,  dim="SALES_DRIVE", rev=False, text="Saya senang berada di situasi 'harus closing'."),
   dict(n=10, dim="SALES_RES",   rev=False, text="Kritik klien saya jadikan bahan perbaikan, bukan beban."),
   dict(n=11, dim="SALES_REL",   rev=False, text="Saya mengingat hal-hal pribadi tentang klien saya."),
   dict(n=12, dim="SALES_TGT",   rev=False, text="Saya punya target pribadi yang lebih tinggi dari target kantor."),
   dict(n=13, dim="SALES_DRIVE", rev=False, text="Membujuk orang adalah hal yang saya nikmati."),
   dict(n=14, dim="SALES_RES",   rev=False, text="Saya tetap tenang saat klien marah atau komplain."),
   dict(n=15, dim="SALES_REL",   rev=False, text="Saya rela mengorbankan waktu untuk menjaga kepercayaan klien."),
   dict(n=16, dim="SALES_TGT",   rev=False, text="Saya tidak nyaman kalau hasil penjualan saya di bawah rekan lain."),
 ]),
 dict(key="LEADSIT", name="Bagian 23 - Gaya Kepemimpinan Situasional",
      intro="Bayangkan Anda memimpin tim. Jawab sesuai yang paling sering Anda lakukan.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="LS_DIR",   rev=False, text="Saya memberi instruksi rinci dan memantau pelaksanaannya ketat."),
   dict(n=2,  dim="LS_DIR",   rev=False, text="Saya memutuskan sendiri lalu menyampaikannya ke tim."),
   dict(n=3,  dim="LS_DIR",   rev=False, text="Saya menetapkan aturan kerja yang jelas dan menag kepatuhan."),
   dict(n=4,  dim="LS_COACH", rev=False, text="Saya menjelaskan 'mengapa' di balik instruksi yang saya berikan."),
   dict(n=5,  dim="LS_COACH", rev=False, text="Saya memberi masukan sambil tetap memantau hasil kerja anggota."),
   dict(n=6,  dim="LS_COACH", rev=False, text="Saya mengoreksi kesalahan sambil tetap memberi arah yang jelas."),
   dict(n=7,  dim="LS_SUP",   rev=False, text="Saya bertanya dan mendengarkan lebih banyak daripada memerintah."),
   dict(n=8,  dim="LS_SUP",   rev=False, text="Saya melibatkan anggota dalam pengambilan keputusan."),
   dict(n=9,  dim="LS_SUP",   rev=False, text="Saya fokus membangun kepercayaan dan motivasi tim."),
   dict(n=10, dim="LS_DEL",   rev=False, text="Saya menyerahkan tanggung jawab penuh pada anggota yang sudah mampu."),
   dict(n=11, dim="LS_DEL",   rev=False, text="Saya membiarkan anggota menentukan caranya sendiri selama hasil tercapai."),
   dict(n=12, dim="LS_DEL",   rev=False, text="Saya hanya camp tangan jika diminta atau jika ada masalah besar."),
 ]),
 dict(key="SERVANT", name="Bagian 24 - Kecenderungan Servant Leadership",
      intro="Jawab sesuai cara Anda memimpin atau bekerja dengan orang lain.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1, dim="SERV", rev=False, text="Keberhasilan orang lain terasa seperti keberhasilan saya sendiri."),
   dict(n=2, dim="SERV", rev=False, text="Saya mengutamakan kebutuhan tim di atas kepentingan pribadi."),
   dict(n=3, dim="SERV", rev=False, text="Saya berusaha mengembangkan orang lain, bukan hanya mengejar hasil."),
   dict(n=4, dim="SERV", rev=False, text="Saya mendengarkan orang lain dengan sungguh-sungguh sebelum bertindak."),
   dict(n=5, dim="SERV", rev=False, text="Saya mementingkan keadilan bagi semua anggota tim."),
   dict(n=6, dim="SERV", rev=False, text="Saya bersedia melakukan pekerjaan yang tidak glamor demi tim."),
   dict(n=7, dim="SERV", rev=False, text="Saya membantu orang lain menemukan kekuatan terbaiknya."),
   dict(n=8, dim="SERV", rev=False, text="Orang merasa dibantu, bukan diperalat, saat bekerja dengan saya."),
 ]),
 dict(key="JUSTICE", name="Bagian 25 - Keadilan Organisasi yang Dirasakan",
      intro="Jawab berdasarkan pengalaman Anda di perusahaan saat ini.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="J_DIST",  rev=False, text="Hasil kerja saya (gaji, bonus, penghargaan) sesuai dengan kontribusi saya."),
   dict(n=2,  dim="J_PROC",  rev=False, text="Prosedur keputusan di perusahaan diterapkan konsisten untuk semua orang."),
   dict(n=3,  dim="J_INTER", rev=False, text="Atasan memperlakukan saya dengan hormat dan bermartabat."),
   dict(n=4,  dim="J_DIST",  ref=False if False else False, rev=False, text="Keputusan tentang imbalan di sini dibuat dengan cara yang adil."),
   dict(n=5,  dim="J_PROC",  rev=False, text="Prosedur di sini dibuat dengan cara yang tidak bias."),
   dict(n=6,  dim="J_INTER", rev=False, text="Atasan memperlakukan saya dengan sopan."),
   dict(n=7,  dim="J_DIST",  rev=False, text="Imbalan yang saya terima mencerminkan usaha yang saya keluarkan."),
   dict(n=8,  dim="J_PROC",  rev=False, text="Saya bisa menyampaikan pendapat atau keluhan tentang prosedur."),
   dict(n=9,  dim="J_INTER", rev=False, text="Atasan peduli pada hak-hak saya sebagai karyawan."),
   dict(n=10, dim="J_DIST",  rev=False, text="Saya merasa imbalan di sini adil dibanding rekan-rekan setara."),
   dict(n=11, dim="J_PROC",  rev=False, text="Prosedur memberi kesempatan untuk menyampaikan keberatan."),
   dict(n=12, dim="J_INTER", rev=False, text="Atasan memperlakukan saya dengan jujur."),
 ]),
]

INSTRUMENTS += EXTRA2 + EXTRA3


DIMS.update({
 "COG_IMG":   dict(label="Penalaran Matriks / GMA Fluid (gambar)",   radar="Matriks",      dir="good", target=60),
 "DASS_D":    dict(label="Depresi (DASS-21)",                        radar="Depresi",      dir="bad",  target=19),
 "DASS_A":    dict(label="Anxiety / Cemas (DASS-21)",                radar="Cemas",        dir="bad",  target=19),
 "DASS_S":    dict(label="Stress (DASS-21)",                         radar="Stress",       dir="bad",  target=19),
 "PHQ":       dict(label="Screening Depresi (PHQ-9)",                radar="PHQ-9",        dir="bad",  target=19),
 "GAD":       dict(label="Screening Kecemasan (GAD-7)",              radar="GAD-7",        dir="bad",  target=19),
 "WHO5":      dict(label="Kesejahteraan Psikologis (WHO-5)",         radar="Well-being",   dir="good", target=50),
 "DISC_D":    dict(label="DISC - Dominance (Mengendalikan)",         radar="D - Dominan",  dir="good", target=50),
 "DISC_I":    dict(label="DISC - Influence (Memengaruhi)",           radar="I - Influencer",dir="good",target=50),
 "DISC_S":    dict(label="DISC - Steadiness (Kestabilan)",           radar="S - Stabil",   dir="good", target=50),
 "DISC_C":    dict(label="DISC - Compliance (Ketelitian)",           radar="C - Cermat",   dir="good", target=50),
 "EI":        dict(label="Tipe Energi: Ekstroversi-Introversi",      radar="Energi E/I",   dir="good", target=50),
 "SN":        dict(label="Tipe Informasi: Sensing-Intuition",        radar="Info S/N",     dir="good", target=50),
 "TF":        dict(label="Tipe Keputusan: Thinking-Feeling",         radar="Putusan T/F",  dir="good", target=50),
 "JP":        dict(label="Tipe Gaya Hidup: Judging-Perceiving",      radar="Gaya J/P",     dir="good", target=50),
 "SALES_DRIVE":dict(label="Drive Berjualan",                         radar="Drive Jualan", dir="good", target=55),
 "SALES_RES":  dict(label="Ketahanan terhadap Penolakan",            radar="Tahan Tolak",  dir="good", target=55),
 "SALES_REL":  dict(label="Orientasi Relasi Klien",                  radar="Relasi Klien", dir="good", target=55),
 "SALES_TGT":  dict(label="Orientasi Target Jualan",                 radar="Target Jualan",dir="good", target=55),
 "LS_DIR":    dict(label="Kepemimpinan: Mengarahkan (Directing)",    radar="Mengarahkan",  dir="good", target=50),
 "LS_COACH":  dict(label="Kepemimpinan: Melatih (Coaching)",         radar="Melatih",      dir="good", target=50),
 "LS_SUP":    dict(label="Kepemimpinan: Mendukung (Supporting)",     radar="Mendukung",    dir="good", target=50),
 "LS_DEL":    dict(label="Kepemimpinan: Mendelegasikan (Delegating)",radar="Delegasi",     dir="good", target=50),
 "SERV":      dict(label="Servant Leadership",                       radar="Servant",      dir="good", target=60),
 "J_DIST":    dict(label="Keadilan Imbalan (Distributive)",          radar="Adil Imbalan", dir="good", target=60),
 "J_PROC":    dict(label="Keadilan Prosedural",                      radar="Adil Prosedur",dir="good", target=60),
 "J_INTER":   dict(label="Keadilan Interpersonal",                   radar="Adil Personal",dir="good", target=60),
})
DIM_ORDER = list(DIMS.keys())

INST_SHORT.update({
 "CFIT":    "O. Penalaran Matriks GMA - GAMBAR (8 soal)",
 "DASS":    "P. DASS-21 - Depresi/Anxiety/Stress (21 item)",
 "PHQ":     "Q. PHQ-9 - Screening Depresi (9 item)",
 "GAD":     "R. GAD-7 - Screening Kecemasan (7 item)",
 "WHO5":    "S. WHO-5 - Kesejahteraan Psikologis (5 item)",
 "DISC":    "T. DISC - Gaya Perilaku (24 item)",
 "MBTIX":   "U. Indikator Tipe Kepribadian (16 item)",
 "SALES":   "V. Profil Sales & Drive Berjualan (16 item)",
 "LEADSIT": "W. Gaya Kepemimpinan Situasional (12 item)",
 "SERVANT": "X. Servant Leadership (8 item)",
 "JUSTICE": "Y. Keadilan Organisasi (12 item)",
})


# ============================================================
# INSTRUMEN BATCH 4 - KONTEKS ASPEN MEDICAL (RS hasil akuisisi)
# VALUES  = Kesesuaian 5 nilai inti Aspen (Respect/Integrity/Compassion/Teamwork/Excellence)
#           yang dirasakan di RS saat ini -> kristalisasi budaya & gap vs aspirasi (target 80)
# SAFETY  = Budaya Keselamatan Pasien (adaptasi HSOPSC/AHRQ, domain publik)
# CHANGE  = Kesiapan Perubahan (konteks masa transisi pasca-akuisisi)
# ============================================================
EXTRA4 = [
 dict(key="VALUES", name="Bagian 26 - Kesesuaian Nilai Aspen Medical",
      intro="Nilai apa yang TERLIHAT dalam praktik sehari-hari di rumah sakit ini SAAT INI? "
            "Bukan nilai yang diharapkan, melainkan yang benar-benar terjadi. Target aspirasi = 80.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="V_RESPECT", rev=False, text="Di sini, setiap orang diperlakukan dengan hormat, apa pun jabatannya."),
   dict(n=2,  dim="V_RESPECT", rev=False, text="Pendapat pasien dan keluarganya didengarkan dengan sungguh-sungguh."),
   dict(n=3,  dim="V_INTEG",   rev=False, text="Orang-orang di sini berkata jujur bahkan ketika jujur itu tidak menguntungkan."),
   dict(n=4,  dim="V_INTEG",   rev=False, text="Kata dan tindakan para pemimpin di sini konsisten."),
   dict(n=5,  dim="V_COMP",    rev=False, text="Kebutuhan pasien diutamakan di atas prosedur yang kaku."),
   dict(n=6,  dim="V_COMP",    rev=False, text="Karyawan peduli pada kesejahteraan pasien bahkan di luar tugasnya."),
   dict(n=7,  dim="V_TEAM",    rev=False, text="Berbagai profesi (dokter, perawat, admin) bekerja sebagai satu tim."),
   dict(n=8,  dim="V_TEAM",    rev=False, text="Bantuan antar-unit datang dengan cepat saat dibutuhkan."),
   dict(n=9,  dim="V_EXCEL",   rev=False, text="Standar mutu pelayanan terus ditingkatkan, bukan sekadar dipertahankan."),
   dict(n=10, dim="V_EXCEL",   rev=False, text="Kesalahan dipelajari untuk memperbaiki sistem, bukan untuk menyalahkan orang."),
 ]),
 dict(key="SAFETY", name="Bagian 27 - Budaya Keselamatan Pasien (adaptasi HSOPSC)",
      intro="Jawab berdasarkan kondisi rumah sakit SAAT INI. Keselamatan pasien adalah fondasi klinis Aspen.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1,  dim="SAFE_COM",  rev=False, text="Staf merasa aman melaporkan kesalahan atau hampir-salah tanpa takut dihukum."),
   dict(n=2,  dim="SAFE_JUST", rev=False, text="Ketika insiden terjadi, fokusnya memperbaiki proses, bukan mencari kambing hitam."),
   dict(n=3,  dim="SAFE_PRI",  rev=False, text="Keselamatan pasien diutamakan bahkan saat rumah sakit sangat sibuk."),
   dict(n=4,  dim="SAFE_COM",  rev=False, text="Informasi penting tentang kondisi pasien disampaikan jelas antar-shift."),
   dict(n=5,  dim="SAFE_JUST", rev=False, text="Staf berani mengakui kesalahan mereka sendiri."),
   dict(n=6,  dim="SAFE_PRI",  rev=False, text="Peralatan dan prosedur keselamatan selalu dicek sebelum digunakan."),
   dict(n=7,  dim="SAFE_COM",  rev=False, text="Atasan menyambut laporan masalah keselamatan sebagai masukan, bukan gangguan."),
   dict(n=8,  dim="SAFE_JUST", rev=False, text="Kesalahan tidak disembunyikan, melainkan dibahas untuk dicari solusinya."),
   dict(n=9,  dim="SAFE_PRI",  rev=False, text="Jika ada risiko terhadap pasien, tugas lain boleh tertunda."),
   dict(n=10, dim="SAFE_COM",  rev=False, text="Komunikasi antar-profesi (dokter-perawat-farmasi) berjalan terbuka."),
   dict(n=11, dim="SAFE_JUST", rev=False, text="Staf yang melaporkan masalah mendapat apresiasi, bukan masalah tambahan."),
   dict(n=12, dim="SAFE_PRI",  rev=False, text="Manajemen menunjukkan komitmen nyata pada keselamatan pasien, bukan hanya slogan."),
 ]),
 dict(key="CHANGE", name="Bagian 28 - Kesiapan Perubahan (Masa Transisi)",
      intro="Jawab berdasarkan perasaan Anda menghadapi masa perubahan yang sedang berlangsung.",
      scale=SCALE_15, min=1, max=5, items=[
   dict(n=1, dim="CHANGE", rev=False, text="Saya paham mengapa rumah sakit ini perlu berubah."),
   dict(n=2, dim="CHANGE", rev=False, text="Perubahan yang sedang berlangsung memiliki arah yang jelas."),
   dict(n=3, dim="CHANGE", rev=False, text="Saya percaya kepemimpinan mampu membawa perubahan ini."),
   dict(n=4, dim="CHANGE", rev=False, text="Saya merasa mampu beradaptasi dengan cara kerja yang baru."),
   dict(n=5, dim="CHANGE", rev=False, text="Perubahan ini membawa harapan yang lebih baik bagi rumah sakit."),
   dict(n=6, dim="CHANGE", rev=False, text="Saya mendapat informasi yang cukup tentang perubahan yang terjadi."),
   dict(n=7, dim="CHANGE", rev=False, text="Saya punya dukungan yang cukup untuk melewati masa perubahan ini."),
   dict(n=8, dim="CHANGE", rev=False, text="Secara umum, saya siap dengan masa transisi ini."),
 ]),
]
INSTRUMENTS += EXTRA4

DIMS.update({
 "V_RESPECT": dict(label="Nilai: Respect (Dihormati)",              radar="Respect",    dir="good", target=80),
 "V_INTEG":   dict(label="Nilai: Integrity (Integritas)",            radar="Integrity",  dir="good", target=80),
 "V_COMP":    dict(label="Nilai: Compassion (Kompasi)",              radar="Compassion", dir="good", target=80),
 "V_TEAM":    dict(label="Nilai: Teamwork (Kerja Sama)",             radar="Teamwork",   dir="good", target=80),
 "V_EXCEL":   dict(label="Nilai: Pursuit of Excellence (Keunggulan)",radar="Excellence", dir="good", target=80),
 "SAFE_COM":  dict(label="Keselamatan: Komunikasi Terbuka",          radar="Komunikasi Aman", dir="good", target=65),
 "SAFE_JUST": dict(label="Keselamatan: Belajar dari Insiden",        radar="Just Culture",    dir="good", target=65),
 "SAFE_PRI":  dict(label="Keselamatan: Prioritas Keselamatan",       radar="Safety First",    dir="good", target=65),
 "CHANGE":    dict(label="Kesiapan Perubahan (Masa Transisi)",       radar="Siap Berubah",    dir="good", target=60),
})
DIM_ORDER = list(DIMS.keys())

INST_SHORT.update({
 "VALUES": "Z. Kesesuaian Nilai Aspen (10 item)",
 "SAFETY": "AA. Budaya Keselamatan Pasien (12 item)",
 "CHANGE": "AB. Kesiapan Perubahan (8 item)",
})

# tampilkan nama asesmen tanpa prefix huruf (A., B., ..., AA.)
import re as _re
INST_SHORT = {k: _re.sub(r"^[A-Z]{1,2}\.\s*", "", v) for k, v in INST_SHORT.items()}
