
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

# Metadata dimensi: label panjang, label radar pendek, arah favorable, target 0-100
DIMS = {
 "PSS":    dict(label="Stres Persepsian (PSS)",            radar="Stres",     dir="bad",  target=40),
 "MBI_EX": dict(label="Kelelahan Emosional (Exhaustion)",  radar="Exhaust",   dir="bad",  target=33),
 "MBI_CY": dict(label="Sinisme (Cynicism)",                radar="Cynis",     dir="bad",  target=33),
 "MBI_PE": dict(label="Efikasi Profesional",               radar="Efikasi",   dir="good", target=67),
 "SEA":    dict(label="Pemahaman Emosi Diri (SEA)",        radar="SEA",       dir="good", target=60),
 "OEA":    dict(label="Pemahaman Emosi Orang Lain (OEA)",  radar="OEA",       dir="good", target=60),
 "ROE":    dict(label="Regulasi Emosi (ROE)",              radar="ROE",       dir="good", target=60),
 "UOE":    dict(label="Penggunaan Emosi (UOE)",            radar="UOE",       dir="good", target=60),
 "VIG":    dict(label="Semangat (Vigour)",                 radar="Vigour",    dir="good", target=60),
 "DED":    dict(label="Dedikasi",                          radar="Dedikasi",  dir="good", target=60),
 "ABS":    dict(label="Absorpsi (Ketenggelaman)",          radar="Absorpsi",  dir="good", target=60),
 "TIS":    dict(label="Niat Keluar (Turnover Intention)",  radar="Turnover",  dir="bad",  target=33),
 "PSQ":    dict(label="Rasa Aman Psikologis (PSQ-ORG)",    radar="PsySafety", dir="good", target=70),
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
