
# -*- coding: utf-8 -*-
"""Interpretasi hasil - bahasa manusia, hangat, mudah dipahami awam +
narasi soft-selling untuk kebutuhan pengembangan."""
from instruments import INSTRUMENTS, DIMS, DIM_ORDER

# ---------------------------------------------------------------
# PENJELASAN "APA INI?" TIAP ASPEK (bahasa awam, satu-dua kalimat)
# ---------------------------------------------------------------
DIM_INFO = {
 "PSS": "Stres adalah respons alami tubuh terhadap tuntutan. Sedikit stres justru membuat kita waspada, "
        "tetapi stres yang menumpuk terus-menerus menguras energi, menurunkan kualitas kerja, dan lama-kelamaan "
        "menggerogoti kesehatan dan relasi.",
 "MBI_EX": "Kelelahan emosi adalah kondisi ketika energi mental terasa terkuras habis oleh pekerjaan. "
        "Ini sinyal paling awal — dan paling penting — dari burnout. Seperti HP yang dipakai terus tanpa "
        "di-charge: tetap menyala, tetapi makin lama makin lambat.",
 "MBI_CY": "Sinisme di sini bukan soal bersikap jahat. Ini kondisi ketika pekerjaan yang dulu terasa bermakna "
        "mulai terasa hambar, sehingga tanpa sadar kita menjaga jarak dan merawat diri dengan cara 'tidak "
        "usah terlalu peduli supaya tidak kecewa'.",
 "MBI_PE": "Rasa mampu adalah keyakinan bahwa kita kompeten dan pekerjaan kita berdampak. Inilah bahan bakar "
        "keberanian mengambil tantangan. Orang yang merasa mampu tidak perlu dipaksa untuk tampil; orang yang "
        "ragu pada kemampuannya akan bersembunyi di balik pekerjaan yang aman-aman saja.",
 "SEA": "Mengenal emosi diri berarti mampu menyadari apa yang sedang kita rasakan dan mengapa. Ini seperti "
        "panel instrumen di kokpit pesawat: tanpanya kita tetap bisa terbang, tetapi buta terhadap kondisi "
        "sendiri — dan baru sadar ada masalah setelah semuanya berbunyi.",
 "OEA": "Memahami emosi orang lain adalah kemampuan membaca suasana hati rekan kerja dari kata-kata, nada "
        "suara, dan ekspresi. Inilah kunci komunikasi yang nyambung: kita tidak hanya mendengar apa yang "
        "dikatakan orang, tetapi juga apa yang sebenarnya mereka rasakan.",
 "ROE": "Regulasi emosi bukan berarti menahan atau mematikan perasaan. Ini kemampuan untuk tetap punya "
        "pilihan: merasakan emosi (marah, kecewa, panik), tetapi meresponsnya dengan cara yang kita pilih, "
        "bukan dengan cara yang sedang kita rasakan.",
 "UOE": "Memakai emosi untuk bergerak adalah kemampuan mengubah perasaan — antusiasme, kekecewaan, rasa "
        "ingin membuktikan — menjadi dorongan untuk bertindak dan mencapai target. Emosi yang dialirkan ke "
        "arah yang benar justru menjadi tenaga, bukan beban.",
 "VIG": "Energi kerja adalah semangat fisik dan mental saat bekerja: bangun pagi dengan rasa ingin berangkat, "
        "tetap bertenaga hingga jam pulang, dan merasa badan serta pikiran sanggup menopang hari itu.",
 "DED": "Dedikasi adalah rasa bangga dan makna terhadap pekerjaan. Karyawan yang merasa pekerjaannya berarti "
        "tidak perlu diawasi untuk bekerja sepenuh hati; sedangkan karyawan yang kehilangan makna bisa "
        "terlihat sibuk, tetapi sebenarnya hanya menghabiskan waktu.",
 "ABS": "Fokus (flow) adalah kondisi ketika kita begitu tenggelam dalam pekerjaan hingga lupa waktu. Ini "
        "tanda bahwa tantangan pekerjaan dan kemampuan kita sedang seimbang — tidak membosankan, tetapi juga "
        "tidak membebani.",
 "TIS": "Niat keluar adalah seberapa kuat dorongan untuk mencari pekerjaan lain. Sinyal ini hampir tidak "
        "pernah muncul tiba-tiba; ia bertumbuh pelan-pelan dari ketidakpuasan yang lama diabaikan — sampai "
        "suatu hari terasa lebih mudah untuk pergi daripada bertahan.",
 "PSQ": "Rasa aman psikologis adalah keyakinan bahwa di tim ini kita boleh bicara jujur, mengakui kesalahan, "
        "dan bertanya tanpa takut dipermalukan atau dihukum. Ini fondasi tim yang sehat: tim yang aman "
        "berkembang cepat; tim yang tidak aman diam saat melihat masalah — dan masalah kecil pun tumbuh "
        "besar tanpa ada yang berani bilang.",
}

# ---------------------------------------------------------------
# INTERPRETASI PER ASPEK PER KATEGORI (panjang, hangat, manusiawi)
# ---------------------------------------------------------------
INSIGHTS = {
 "PSS": {
  "low":  "Kabar baik: tingkat stres yang dirasakan masih rendah. Secara umum Anda merasa mampu mengelola "
          "tuntutan pekerjaan maupun kehidupan. Jaga ritme ini — istirahat cukup, jangan menunggu lelah "
          "baru berhenti, karena pencegahan selalu lebih murah daripada pemulihan.",
  "mid":  "Tingkat stres Anda sedang — masih wajar dan masih bisa dikelola, tetapi beban mulai terasa di "
          "beberapa area. Ini fase 'lampu kuning': belum darurat, namun ini saat yang tepat untuk memetakan "
          "sumber tekanan (bukan hanya gejalanya) dan mulai membangun kebiasaan melepas penat secara rutin.",
  "high": "Tingkat stres Anda tergolong tinggi. Ini bukan tanda kelemahan — ini tanda bahwa beban yang "
          "Anda pikul sudah melebihi kapasitas pemulihan yang tersedia. Jika dibiarkan, fokus, kualitas "
          "keputusan, tidur, dan bahkan relasi dengan orang terdekat ikut terkorek. Prioritaskan diri Anda "
          "seperti Anda memprioritaskan deadline: bukan nanti, tetapi mulai minggu ini."},
 "MBI_EX": {
  "low":  "Energi emosional Anda masih terjaga. Anda belum menunjukkan tanda kelelahan kronis — masih ada "
          "ruang di 'tangki' untuk menerima tugas, mendengar keluhan, dan menemani hari yang berat tanpa "
          "terasa terkuras.",
  "mid":  "Ada tanda awal kelelahan emosional: mungkin pulang kerja terasa lebih capek dari biasanya, atau "
          "akhir pekan tidak lagi cukup untuk 'mengisi ulang'. Ini titik paling murah untuk diperbaiki — "
          "perbanyak waktu pemulihan yang benar-benar memulihkan, dan evaluasi beban yang bisa ditolak "
          "atau dibagi.",
  "high": "Kelelahan emosional Anda tergolong tinggi — ini indikator utama burnout, dan biasanya sudah "
          "terasa dalam tubuh: mudah tersulut, sulit tidur, badan pegal tanpa sebab jelas. Yang Anda "
          "butuhkan bukan semangat, melainkan pemulihan yang terstruktur: batasi beban, bicarakan "
          "distribusi tugas dengan atasan, dan jangan menunggu 'habis benar-benar' baru bertindak."},
 "MBI_CY": {
  "low":  "Rasa makna dan keterlibatan Anda terhadap pekerjaan masih terjaga. Anda masih merasa pekerjaan "
          "ini 'milik Anda', bukan sekadar tempat menunggu gajian. Pertahankan dengan terus menemukan "
          "alasan kecil setiap hari mengapa pekerjaan ini penting bagi Anda.",
  "mid":  "Mulai terlihat jarak emosional dengan pekerjaan: dulu semangat, sekadar selesai; dulu peduli, "
          "kini 'urusan siapa'. Sinisme ringan seperti ini hampir tidak pernah disadari, dan justru menjadi "
          "pintu masuk burnout. Cobalah bereksperimen kecil — projek baru, cara kerja baru, atau sekadar "
          "bertanya pada diri sendiri: bagian mana dari pekerjaan ini yang dulu saya sukai?",
  "high": "Sikap sinis/dingin terhadap pekerjaan sudah cukup kuat. Biasanya di titik ini perasaan sudah "
          "berbunyi: 'buat apa berusaha, toh tidak berubah'. Perasaan itu valid — dan justru karena valid, "
          "ia perlu ditanggapi dengan serius: makna kerja yang hilang tidak kembali dengan motivasi semata, "
          "melainkan dengan perubahan nyata pada cara kerja, peran, atau lingkungan."},
 "MBI_PE": {
  "low":  "Rasa mampu Anda sedang rendah: mungkin Anda merasa kontribusi Anda tidak terlihat, atau "
          "tantangan terasa di luar jangkauan. Ini bukan soal kompetensi — sering kali ini soal tidak "
          "adanya umpan balik yang jelas dan kemenangan kecil yang dirayakan. Mulailah dari skala kecil: "
          "selesaikan satu hal dengan baik, minta masukan spesifik, dan biarkan bukti itu menumpuk.",
  "mid":  "Rasa mampu Anda cukup — Anda pada umumnya yakin bisa menangani pekerjaan, meski kadang masih "
          "ragu pada tantangan baru. Yang paling menguatkan orang di level ini bukan pelatihan besar, "
          "melainkan umpan balik yang konkret dan kesempatan menggunakan keahlian pada hal yang terasa bermakna.",
  "high": "Rasa mampu Anda tinggi. Anda merasa kompeten, dan Anda yakin pekerjaan Anda berdampak. Orang "
          "dengan rasa mampu tinggi adalah penggerak tim — pertahankan dengan terus menantang diri pada "
          "peran yang sedikit di atas zona nyaman, dan bagikan rasa mampu itu dengan membimbing rekan yang lain."},
 "SEA": {
  "low":  "Kesadaran terhadap emosi diri masih rendah. Mungkin Anda sering merasakan sesuatu (geram, "
          "cemas, hampa) tanpa bisa menyebutkan persis apa dan kenapa. Ini seperti mengemudi tanpa spidometer "
          "— kita baru menyadari kecepatan setelah ada tilang. Kabar baiknya: kemampuan ini bisa dilatih, "
          "mulai dari kebiasaan kecil menamai perasaan sebelum bereaksi.",
  "mid":  "Anda cukup peka terhadap emosi sendiri — biasanya tahu apa yang sedang dirasakan, meski kadang "
          "baru sadar setelah sempat bereaksi. Latihan yang paling menajamkan kemampuan ini adalah menulis "
          "satu-dua kalimat refleksi di akhir hari: hari ini saya merasa apa, dan pemicunya kemungkinan apa.",
  "high": "Pemahaman emosi diri Anda tinggi. Anda sadar mengapa Anda merasakan sesuatu — dan kesadaran ini "
          "adalah modal utama pengaturan diri. Orang yang mengenal emosinya tidak kebal terhadap badai "
          "perasaan, tetapi ia selalu tahu sedang badai apa dan dari arah mana."},
 "OEA": {
  "low":  "Pemahaman terhadap emosi orang lain masih rendah. Bukan karena tidak peduli — lebih sering karena "
          "kita fokus pada isi pembicaraan dan melewatkan sinyal di baliknya: nada suara yang berubah, "
          "bahasa tubuh yang menarik diri. Akibatnya, miskomunikasi dan salah baca situasi sering terjadi "
          "tanpa disadari. Latihan paling sederhananya: dengarkan untuk memahami, bukan untuk menjawab.",
  "mid":  "Anda cukup mampu membaca emosi orang lain — biasanya bisa merasakan kalau rekan kerja sedang "
          "tidak bersemangat atau ada yang mengganjal, meski kadang meleset. Kemampuan ini tumbuh paling "
          "cepat lewat empati aktif: bertanya lebih dalam, memeriksa asumsi, dan tidak buru-buru menyimpulkan.",
  "high": "Pemahaman emosi orang lain Anda tinggi. Anda peka terhadap dinamika perasaan di sekitar — bisa "
          "merasakan perubahan suasana ruangan sebelum orang bicara. Kemampuan ini membuat Anda menjadi "
          "orang yang 'nyaman diajak bicara', dan di level tim, orang seperti inilah yang paling cepat "
          "mendeteksi konflik sebelum membesar."},
 "ROE": {
  "low":  "Pengaturan emosi masih menjadi tantangan. Reaksi Anda cenderung langsung — marah langsung "
          "terucap, cemas langsung menguasai pikiran. Ini bukan karakter buruk; hampir selalu ini kebiasaan "
          "yang terbentuk karena dulu merasa tidak punya pilihan lain. Kabar baiknya: jeda antara rasa dan "
          "reaksi itu bisa dilatih, dan setiap milidetik jeda itu adalah kebebasan.",
  "mid":  "Anda cukup mampu mengatur emosi — tenang dalam keadaan normal, tetapi konsistensinya menurun "
          "ketika tekanan tinggi atau bad mood. Itu wajar: kemampuan regulasi seperti otot, ia melemah "
          "saat lelah. Kuncinya bukan menghindari pemicu, melainkan punya 'rencana darurat' pribadi: "
          "napas panjang, jeda sebelum membalas pesan, atau mundur sebentar dari ruangan.",
  "high": "Kemampuan mengatur emosi Anda baik. Anda mampu menenangkan diri dan merespons secara rasional "
          "bahkan dalam situasi sulit — kemampuan yang jarang dan berharga. Di mata orang lain Anda "
          "menjadi 'anchor' tim: saat semua panik, Anda tetap bisa berpikir. Jaga kemampuan ini dengan "
          "tidak mengabaikan emosi sendiri — orang yang menahan segalanya juga bisa kelelahan."},
 "UOE": {
  "low":  "Anda belum banyak memakai emosi sebagai dorongan untuk bergerak. Target terasa seperti beban, "
          "bukan undangan. Biasanya ini bukan soal malas, melainkan energi yang terkuras duluan oleh hal "
          "lain — stres, ketidakjelasan arah, atau rasa percuma. Mulailah dari target kecil yang benar-benar "
          "Anda pilih sendiri, bukan yang diberikan; dorongan dari dalam selalu menyala dari hal yang terasa milik.",
  "mid":  "Anda cukup mampu memakai emosi sebagai bahan bakar target — kadang tersulut, kadang juga perlu "
          "didorong dari luar. Yang paling membantu di level ini adalah kejelasan: target yang terukur, "
          "alasan yang masuk akal, dan penanda kemajuan yang terlihat. Motivasi tumbuh bukan dari semangat, "
          "melainkan dari bukti bahwa usaha bergerak.",
  "high": "Anda mampu mengubah perasaan menjadi tenaga kerja — kekecewaan menjadi pembuktian, antusiasme "
          "menjadi aksi. Orang dengan kemampuan ini jarang menunggu 'mood yang tepat' karena ia tahu mood "
          "bisa dibuat, bukan hanya ditunggu. Pertahankan, dan hati-hati pada satu hal: jangan sampai "
          "semua emosi dikonversi jadi produktivitas sampai lupa istirahat."},
 "VIG": {
  "low":  "Energi kerja Anda sedang rendah. Bukan sekadar malas pagi hari — lebih sering ini akumulasi: "
          "tidur yang tidak pulih, beban yang menumpuk, atau pekerjaan yang terasa tiada habisnya. "
          "Energi bukan soal kemauan; ia soal persediaan. Cek dulu tiga hal mendasar: tidur, beban, dan "
          "makna. Biasanya salah satunya sedang defisit.",
  "mid":  "Energi kerja Anda cukup, tetapi fluktuatif — ada hari bertenaga penuh, ada hari yang terasa "
          "seperti jalan menanjak sepanjang hari. Itu normal. Yang bisa dilakukan: kenali pola defisitnya "
          "(tidur? makan? meeting beruntun?), lalu susun ritme kerja mengikuti energi, bukan melawannya.",
  "high": "Energi kerja Anda tinggi — Anda bangun dengan rasa ingin berangkat dan tetap bertenaga hingga "
          "hari selesai. Ini aset besar, baik untuk Anda maupun tim Anda. Satu pengingat: energi tinggi "
          "bikin kita merasa bisa segalanya, dan itulah pintu masuk burnout. Alih-alih menambal beban, "
          "gunakan energi ini untuk membangun sistem yang berjalan bahkan saat Anda sedang tidak bertenaga."},
 "DED": {
  "low":  "Rasa bangga dan makna terhadap pekerjaan sedang rendah — pekerjaan terasa sekadar rutinitas, "
          "selesai satu tugas, datang tugas berikutnya, tanpa benar-benar tahu untuk apa semua itu. Perasaan "
          "ini sangat manusiawi dan hampir tidak pernah berarti Anda tidak becus. Lebih sering artinya: "
          "jarak antara apa yang Anda lakukan dan mengapa Anda memilih pekerjaan ini sudah terlalu jauh. "
          "Pertanyaan penyembuhnya bukan 'bagaimana caranya semangat lagi', melainkan 'bagian mana yang "
          "dulu terasa bermakna, dan kenapa sekarang tidak'.",
  "mid":  "Dedikasi Anda cukup — Anda masih merasa pekerjaan ini layak diperjuangkan, meski apinya tidak "
          "selalu besar. Ini kondisi mayoritas orang dewasa yang bekerja, dan itu tidak apa-apa. Makna "
          "tidak harus heroik; sering kali ia bertahan lewat hal-hal kecil: satu pelanggan yang terbantu, "
          "satu rekan yang berkembang karena bimbingan Anda, satu masalah yang beres karena ketelitian Anda.",
  "high": "Dedikasi Anda tinggi — Anda bangga dengan pekerjaan Anda dan merasa ia menginspirasi Anda. "
          "Karyawan dengan dedikasi tinggi adalah magnet tim: standar mereka menular. Dua hal yang perlu "
          "diperhatikan: dedikasi tinggi membuat Anda jadi sasaran empuk bagi beban berlebih, dan pastikan "
          "kebanggaan ini terus dibuktikan dengan kondisi kerja yang layak — dedikasi yang tidak dihargai "
          "lama-kelamaan berubah menjadi kekecewaan."},
 "ABS": {
  "low":  "Ketenggelaman (flow) dalam pekerjaan masih jarang terjadi. Anda bekerja, tetapi jarang sampai "
          "merasa 'masuk' ke dalamnya — lebih sering terasa seperti mengecek daftar tugas satu per satu. "
          "Flow muncul saat tantangan dan kemampuan bertemu: terlalu mudah membuat bosan, terlalu berat "
          "membuat cemas. Cek pekerjaan Anda: mungkin terlalu banyak yang 'gampang-gampang' atau terlalu "
          "sering diinterupsi untuk flow bisa muncul.",
  "mid":  "Anda kadang mengalami flow — ada momen kerja yang terasa mengalir, tetapi belum menjadi rutinitas. "
          "Untuk memperbanyaknya: kurangi perpindahan konteks (notifikasi, meeting dadakan), dan sediakan "
          "blok waktu tanpa gangguan untuk pekerjaan yang paling menantang. Flow menyukai keheningan "
          "dan benci multitasking.",
  "high": "Kemampuan fokus penuh Anda tinggi — Anda mudah tenggelam dalam pekerjaan sampai lupa waktu. "
          "Ini tanda pekerjaan Anda sedang berada di zona optimal: cukup menantang untuk menarik, cukup "
          "menguasai untuk menyenangkan. Hanya satu hal: orang yang mudah flow juga sering lupa makan, "
          "lupa istirahat, dan lupa bahwa tubuh punya batas. Timer bukan musuh flow."},
 "TIS": {
  "low":  "Tidak ada kecenderungan untuk keluar — Anda merasa ingin bertahan dan membangun di perusahaan ini. "
          "Ini bukan sesuatu yang bisa dianggap remeh: niat bertahan adalah hasil dari rasa nyaman, "
          "keadilan, dan harapan yang terpenuhi. Pertahankan dengan terus tumbuh — orang bertahan bukan "
          "karena tidak punya pilihan lain, tetapi karena di sinilah ia merasa paling berkembang.",
  "mid":  "Ada kecenderungan pasif untuk melihat peluang lain: Anda belum aktif mencari, tetapi telinga "
          "mulai terbuka ketika ada tawaran, dan LinkedIn mulai sering dibuka. Ini alarm paling awal dan "
          "paling bernilai bagi perusahaan — dan kabar baiknya, di fase inilah retensi paling mudah dan "
          "paling murah: cukup satu percakapan jujur dengan atasan tentang apa yang mulai tidak beres.",
  "high": "Kecenderungan untuk keluar tergolong kuat. Bagi individu: perasaan ini layak didengar, bukan "
          "dibungkam — tuliskan dengan jujur apa yang tidak beres, diskusikan bila masih bisa diperbaiki, "
          "dan putuskan dengan sadar, bukan dengan kelelahan. Bagi perusahaan/HR: orang di level ini "
          "biasanya sudah lama memberi sinyal. Jika ingin mempertahankannya, obrolan stay interview perlu "
          "terjadi dalam minggu ini, bukan bulan depan."},
 "PSQ": {
  "low":  "Rasa aman untuk bersuara tergolong rendah. Lingkungan kerja terasa menghukum ketidaklancaran: "
          "salah sedikit dipermalukan, bertanya dianggap bodoh, menyampaikan masalah dianggap mengeluh. "
          "Akibatnya orang-orang terbaik justru paling diam — mereka memilih aman daripada jujur. Ini "
          "bukan masalah orang-orangnya; ini karakteristik lingkungan. Dan lingkungan selalu bisa diubah, "
          "dimulai dari satu hal: apa yang terjadi pada orang yang berani bicara jujur di sini?",
  "mid":  "Rasa aman psikologis cukup — kebanyakan orang merasa nyaman bekerja, tetapi belum sepenuhnya "
          "aman untuk bersuara tanpa saringan. Biasanya ada topik-topik yang 'tidak enak dibahas': "
          "keputusan atasan, masalah antar-departemen, atau kegagalan proyek. Untuk naik ke level aman "
          "penuh, yang paling menentukan adalah perilaku para pemimpin saat menerima kabar buruk — "
          "apakah berterima kasih, atau justru menghukum pembawanya.",
  "high": "Rasa aman psikologis tinggi — tim ini terasa seperti tempat di mana orang boleh jujur, boleh "
          "salah, boleh bertanya, dan boleh mencoba hal baru tanpa takut dipermalukan. Ini aset paling "
          "langka di dunia kerja: tim yang aman belajar paling cepat, karena masalah disampaikan sebelum "
          "membesar dan ide-ide terbaik tidak mati di tenggorokan. Jaga budaya ini — aman psikologis "
          "mudah hilang oleh satu insiden pemimpin yang marah di depan umum."},
}

# ---------------------------------------------------------------
# PENJELASAN TIAP TES (bagi pembaca awam: HR & peserta)
# ---------------------------------------------------------------
INSTRUMENT_META = {
 "PSS": dict(title="Tes 1 - Tingkat Stres (PSS-10)",
   plain="Tes ini mengukur seberapa besar tekanan yang Anda rasakan dalam satu bulan terakhir — bukan "
         "kemampuan Anda, bukan karakter Anda, melainkan beban yang sedang Anda pikul. Perlu diingat: "
         "skor tinggi di sini BUKAN prestasi. Artinya beban sudah melebihi kapasitas mengelola yang "
         "tersedia, dan itu adalah kondisi yang bisa diperbaiki — oleh individu maupun oleh sistem kerjanya."),
 "MBI": dict(title="Tes 2 - Tingkat Burnout (MBI-GS)",
   plain="Burnout bukan sekadar capek. Tes ini membedakan tiga sisinya: kelelahan emosi (energi terasa "
         "terkuras), sinisme (pekerjaan terasa hambar sehingga kita menjaga jarak), dan rasa mampu "
         "(keyakinan bahwa kita kompeten dan berdampak). Pada dua sisi pertama, skor tinggi berarti "
         "risiko; pada rasa mampu, skor tinggi justru kabar baik. Orang bisa tampak produktif sambil "
         "terbakar perlahan — burnout sering tidak terlihat sampai orangnya pergi."),
 "WLEIS": dict(title="Tes 3 - Kecerdasan Emosional (WLEIS)",
   plain="Kecerdasan emosional di sini bukan 'pintar merayu' atau selalu tersenyum. Ia adalah empat "
         "keterampilan nyata yang bisa dilatih: mengenali emosi sendiri, membaca emosi orang lain, "
         "mengatur respons terhadap emosi, dan memakai emosi sebagai bahan bakar untuk mencapai target. "
         "Skor di keempat aspek ini menunjukkan seberapa jauh Anda bisa memimpin diri sendiri sebelum "
         "memimpin orang lain — dan kabar baiknya, tidak ada satu pun yang lahir bakat; semuanya latihan."),
 "UWES": dict(title="Tes 4 - Keterlibatan Kerja (UWES-9)",
   plain="Tes ini mengukur seberapa 'hidup' Anda dalam pekerjaan — bukan seberapa sibuk. Ada tiga "
         "tandanya: energi (badan dan pikiran sanggup menopang hari kerja), dedikasi (rasa bangga dan "
         "makna terhadap apa yang dikerjakan), dan fokus (kemampuan tenggelam dalam pekerjaan sampai "
         "lupa waktu). Karyawan yang terlibat tidak perlu diawasi; karyawan yang tidak terlibat bisa "
         "terlihat sangat sibuk sambil perlahan pergi."),
 "TIS": dict(title="Tes 5 - Kecenderungan Keluar (TIS-6)",
   plain="Tes ini membaca seberapa kuat dorongan untuk mencari pekerjaan lain dalam waktu dekat. Perlu "
         "dipahami dengan tenang: niat keluar hampir tidak pernah muncul tiba-tiba — ia tumbuh dari "
         "kebutuhan yang lama tidak terpenuhi, entah itu keadilan, pertumbuhan, penghargaan, atau rasa "
         "aman. Skor rendah artinya orang ini ingin bertahan; skor tinggi bukan berarti pengkhianat, "
         "melainkan sinyal bahwa ada sesuatu yang perlu didengar — selagi masih ada waktu."),
 "PSQ": dict(title="Tes 6 - Rasa Aman Psikologis (PSQ-ORG)",
   plain="Rasa aman psikologis adalah keyakinan bahwa di tim ini kita boleh bicara jujur, mengakui "
         "kesalahan, bertanya tanpa takut dianggap bodoh, dan mencoba hal baru tanpa takut dipermalukan. "
         "Ini bukan soal suasana yang santai atau permisif — tim paling aman justru tim yang paling "
         "berani menag standar tinggi, karena masalah disampaikan sebelum membesar. Tim yang tidak aman "
         "terlihat tenang dari luar, tetapi diamnya orang-orangnya adalah biaya yang paling mahal."),
}

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

def _read(scores, dim):
    """Satu kalimat 'apa ini' + interpretasi kondisi saat ini."""
    info = DIM_INFO.get(dim, f"{DIMS[dim]['label']} adalah salah satu aspek yang diukur dalam asesmen ini.")
    ins = INSIGHTS.get(dim, {}).get(band(scores[dim]), f"Skor berada pada kategori {BAND_LABEL[band(scores[dim])]} (0-100).")
    return f"{info} Kondisi saat ini: {ins}"

def individual_insights(scores):
    out = []
    for dim in DIM_ORDER:
        if dim not in scores:
            continue
        out.append((DIMS[dim]["label"], band(scores[dim]), _read(scores, dim)))
    return out

def grouped_insights(scores):
    """Kelompokkan per tes: [(key, title, plain, [(label, band, teks_panjang), ...])]."""
    groups = []
    for inst in INSTRUMENTS:
        dims_present = [d for d in DIM_ORDER if d in scores
                        and d in {x["dim"] for x in inst["items"]}]
        if not dims_present:
            continue
        meta = INSTRUMENT_META.get(inst["key"]) or {"title": inst["name"], "plain": inst.get("intro", "")}
        rows = [(DIMS[d]["label"], band(scores[d]), _read(scores, d)) for d in dims_present]
        groups.append((inst["key"], meta["title"], meta["plain"], rows))
    return groups

def gap_analysis(mean_scores):
    """Arah-aware: gap positif = sudah baik/melebihi target; negatif = perlu perhatian."""
    rows = []
    for dim in DIM_ORDER:
        if dim not in mean_scores or dim not in DIMS:
            continue
        d = DIMS[dim]; val = mean_scores[dim]
        gap = (val - d["target"]) if d["dir"] == "good" else (d["target"] - val)
        status = "Melebihi target" if gap >= 0 else "Perlu perhatian"
        rows.append(dict(dim=dim, label=d["label"], mean=round(val, 1),
                         target=d["target"], gap=round(gap, 1), status=status,
                         dir=d["dir"], rekomendasi=MODULE_MAP.get(dim, f"Program pengembangan: {d['label']}")))
    priority = sorted([r for r in rows if r["gap"] < 0], key=lambda r: r["gap"])
    return rows, priority

def _valid_row(r):
    return isinstance(r, dict) and "dim" in r and "gap" in r

def strengths_and_concerns(gap_rows):
    rows = [r for r in gap_rows if _valid_row(r)]
    strengths = [r for r in rows if r["gap"] >= 0]
    concerns = sorted([r for r in rows if r["gap"] < 0], key=lambda r: r["gap"])
    return strengths, concerns

def soft_recommendations(priority):
    if not priority:
        return ["Secara keseluruhan kondisi tim sudah berada pada jalur yang sehat. Fokus terbaik "
                "saat ini adalah mempertahankan: apresiasi rutin, ruang tumbuh, dan menjaga pola "
                "pemulihan kerja. Tidak ada intervensi mendesak yang diperlukan."]
    sents = []
    for r in priority[:4]:
        sents.append(f"- **{r['label']}** (rata-rata {r['mean']:.0f}/100, target "
                     f"{'maksimal' if r['dir']=='bad' else 'minimal'} {r['target']}). "
                     f"{CONSEQUENCE.get(r['dim'], 'Kondisi ini perlu perhatian berkelanjutan.')} Program yang relevan: {r['rekomendasi']}.")
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


# ============ KONTEN KHUSUS REPORT HR (insight dalam + risiko + caption) ============

# Risiko bisnis per dimensi (untuk bagian "Risiko yang Perlu Diwaspadai")
RISK = {
 "PSS": "Secara bisnis, stres kronis adalah biaya tersembunyi yang paling jarang dihitung: kualitas keputusan "
        "menurun, kesalahan kerja naik, dan absensi mulai meningkat pelan-pelan. Yang paling berbahaya: "
        "karyawan yang stres biasanya tetap masuk kerja (presenteeism) - badannya di kantor, pikirannya tidak.",
 "MBI_EX": "Karyawan yang kelelahan emosinya tinggi adalah kandidat resign paling 'senyap'. Mereka jarang "
        "mengeluh - mereka hanya makin dingin, makin pelan, lalu suatu hari menyerahkan surat. Biaya pergantian "
        "satu karyawan bisa mencapai 6-9 bulan gajinya, belum termasuk beban kerja yang berpindah ke rekan lain.",
 "MBI_CY": "Sinisme menular dalam tim lebih cepat dari semangat. Satu orang yang merasa 'buat apa berusaha' "
        "bisa menurunkan energi seluruh mejanya dalam hitungan minggu - terutama jika orang itu adalah "
        "panutan atau anggota paling senior.",
 "MBI_PE": "Ketika rasa mampu menurun, perusahaan kehilangan inisiatif tanpa kehilangan orangnya. Karyawan "
        "yang ragu pada kemampuannya tidak akan mengusulkan ide, tidak akan mengambil proyek menantang, dan "
        "akan memilih 'aman' di setiap kesempatan - padahal pertumbuhan perusahaan lahir dari orang yang berani.",
 "SEA": "Karyawan yang tidak mengenali emosinya sendiri adalah 'mesin tanpa indikator': mereka bisa "
        "meledak di meeting penting, membuat keputusan di bawah amarah, atau membawa masalah pribadi ke "
        "ruang kerja - semuanya tanpa peringatan. Konflik yang seharusnya kecil jadi besar karena tidak ada "
        "jeda antara rasa dan reaksi.",
 "OEA": "Ketidakpekaan terhadap emosi orang lain adalah pemicu miskomunikasi terbesar: instruksi yang "
        "diberikan tanpa membaca kondisi penerima, feedback yang terasa seperti serangan, dan konflik yang "
        "sebenarnya cuma kebutuhan untuk didengar. Di level tim, ini berarti banyak masalah kecil yang "
        "dibiarkan membesar karena tidak ada yang peka mendeteksinya.",
 "ROE": "Tim dengan regulasi emosi yang lemah hidup dalam mode 'api-unggun': konflik kecil menyala terus di "
        "bawah permukaan, meeting terasa tegang, dan energi kreatif habis untuk menjaga amarah, bukan untuk "
        "bekerja. Turnover di tim seperti ini hampir selalu lebih tinggi dari rata-rata perusahaan.",
 "UOE": "Tanpa kemampuan mengubah emosi jadi dorongan, target perusahaan hidup sebagai angka di slide - "
        "diketahui semua orang, dirasakan tidak ada. Karyawan yang kehilangan bahan bakar dari dalam hanya "
        "bergerak saat diawasi, dan berhenti tepat saat pengawasan berhenti.",
 "VIG": "Energi rendah adalah produktivitas yang hilang tanpa jejak: pekerjaan yang biasanya selesai 2 jam "
        "jadi 4 jam, meeting jadi tidak menghasilkan, dan 'capek' menjadi alasan yang makin sering terdengar. "
        "Jika ini dibiarkan di banyak orang sekaligus, biasanya ada akar sistemik: beban, jadwal, atau budaya "
        "yang perlu diperbaiki - bukan sekadar masalah individu.",
 "DED": "Kehilangan makna adalah awal dari 'karyawan hantu': hadir di semua meeting, menyelesaikan semua "
        "tugas, tetapi tanpa kepemilikan. Karyawan seperti ini tidak akan pernah mengeluh - mereka hanya "
        "tidak akan pernah memberi lebih. Dan perusahaan yang tidak pernah mendapatkan 'lebih' dari "
        "karyawannya akan selalu kalah dari pesaing yang bisa.",
 "ABS": "Tanpa kemampuan fokus, perusahaan membayar 8 jam kerja tetapi hanya menerima 4-5 jam hasil. "
        "Pekerjaan berkualitas butuh blok waktu tanpa gangguan - jika karyawan tidak pernah mencapai fokus "
        "penuh, output mereka akan selalu berada di bawah kemampuan sebenarnya.",
 "TIS": "Niat keluar adalah aset yang sedang mengalir keluar lewat keran yang tidak terlihat. Setiap "
        "karyawan berniat kuat untuk pergi yang tidak tertahan akan membawa: pengetahuan proses, relasi "
        "dengan klien, dan - yang paling mahal - keyakinan rekan-rekannya bahwa 'di sini tidak layak bertahan'.",
 "PSQ": "Tim tanpa rasa aman psikologis adalah tim yang buta terhadap masalahnya sendiri. Karyawan diam bukan "
        "karena tidak ada masalah, tetapi karena berbicara terasa berisiko. Akibatnya: kesalahan ditemukan "
        "klien sebelum ditemukan internal, ide perbaikan mati di tenggorokan, dan keputusan penting diambil "
        "berdasarkan apa yang 'aman dibbilang', bukan apa yang benar.",
}

# Panduan membaca setiap grafik (tampil di bawah gambar)
CAPTIONS = {
 "radar": "Cara membaca: semakin jauh titik dari pusat, semakin sehat kondisi karyawan pada aspek itu. "
          "Bentuk yang melebar ke kanan-atas menandakan kondisi baik; 'cekung' di satu sisi menunjukkan "
          "area yang perlu perhatian. Skala sudah diseragamkan: makin tinggi = makin baik.",
 "donut": "Cara membaca: seluruh karyawan dikelompokkan ke 4 profil berdasarkan jumlah aspek yang menunjukkan "
          "sinyal rawan. Donat yang didominasi hijau/kuning berarti mayoritas karyawan dalam kondisi baik; "
          "irisan oranye/merah menunjukkan siapa yang perlu ditindaklanjuti lebih dulu.",
 "heat":  "Cara membaca: setiap baris adalah satu karyawan, setiap kolom satu aspek. Hijau = sehat, kuning = "
          "cukup, merah = rawan. Lihat pola: baris yang penuh merah butuh perhatian segera; kolom yang "
          "banyak merahnya menandakan masalah sistemik di level tim, bukan individu.",
 "band":  "Cara membaca: untuk setiap aspek, batang menunjukkan persentase karyawan di tiap kategori. "
          "Hijau selalu berarti baik, merah selalu berarti perlu perhatian (skor tes yang arahnya terbalik "
          "sudah dibalik otomatis). Aspek dengan porsi merah/kuning besar adalah kandidat intervensi.",
 "action":"Cara membaca: batang adalah skor kesehatan rata-rata, garis putus-putus adalah target sehat. "
          "Warna menentukan tindak lanjut: hijau = pertahankan, kuning = pantau, oranye = prioritas training, "
          "merah = prioritas konseling + training. Semakin jauh batang di kiri garis, semakin mendesak.",
 "dept":  "Cara membaca: membandingkan rata-rata antar departemen. Jika satu departemen konsisten lebih "
          "merah di banyak aspek, masalahnya kemungkinan pada kepemimpinan atau beban departemen itu - "
          "bukan pada individu-individunya.",
}

# Saran asesmen lanjutan (sederhana, berguna, tidak complicated)
FOLLOWUP = {
 "PSS":    "Survei Sumber Stres (stressor mapping) 10 menit - untuk memastikan stresnya datang dari beban kerja, relasi atasan, atau sistem.",
 "MBI_EX": "Audit beban kerja + cek keadilan distribusi tugas per orang.",
 "MBI_CY": "Survei makna kerja singkat + sesi fokus grup dengan anggota tim.",
 "MBI_PE": "Cek kejelasan peran (role clarity) dan frekuensi umpan balik dari atasan langsung.",
 "SEA":    "DERS-16 (Difficulties in Emotion Regulation) - memetakan secara spesifik titik lemah dalam mengenali & mengatur emosi.",
 "OEA":    "Survei iklim komunikasi tim (bagaimana feedback biasanya diberikan dan diterima).",
 "ROE":    "DERS-16 + observasi pola konflik dalam meeting untuk melihat pemicu regulasi emosi.",
 "UOE":    "Wellness pulse check bulanan (5 menit) untuk memantau energi dan motivasi.",
 "VIG":    "Cek pola istirahat, beban meeting, dan jam kerja aktual vs kontrak.",
 "DED":    "Survei makna & kebanggaan kerja + stay conversation dengan karyawan bernilai kritis.",
 "ABS":    "Observasi pola gangguan kerja (notifikasi, meeting dadakan) + percobaan blok fokus 2 minggu.",
 "TIS":    "Stay interview terstruktur untuk karyawan berisiko keluar (15-20 menit per orang).",
 "PSQ":    "Survei psychological safety mendalam per tim + observasi cara leader menanggapi kabar buruk.",
}

def hr_opening(training_name, n, strengths, concerns, csum):
    """Paragraf pembuka panjang, bahasa manusia, untuk HR awam."""
    cl_text = ", ".join(f"{c['n']} orang {c['label']}" for c in csum) if csum else ""
    if concerns:
        top = concerns[0]
        fokus = (f"Hal yang paling menonjol dan layak didengar adalah **{top['label'].lower()}** "
                 f"- bukan untuk dipermasalahkan, tetapi karena inilah area yang paling berdampak "
                 f"jika ditangani, dan paling berisiko jika dibiarkan.")
    else:
        fokus = ("Secara keseluruhan kondisi tim berada di jalur yang sehat - dan ini patut diapresiasi, "
                 "karena tidak banyak perusahaan yang berani mengukur dan menemukan kabar baik.")
    return (f"Report ini adalah potret kondisi psikologis **{n} karyawan {training_name}** pada satu titik waktu - "
            f"bukan rapor, bukan vonis, dan bukan alat menilai siapa salah. Angka-angka di halaman-halaman "
            f"berikutnya adalah cara paling jujur untuk mendengar apa yang biasanya tidak diucapkan karyawan "
            f"di ruang meeting: seberapa berat beban yang mereka pikul, seberapa besar energi yang masih mereka "
            f"miliki, dan seberapa kuat keinginan mereka untuk bertahan. Dari komposisi kelompoknya, "
            f"saat ini tim tersusun atas: {cl_text}. {fokus} Semua penjelasan disusun dengan bahasa yang "
            f"bisa langsung dipakai untuk percakapan dengan manajemen - tanpa istilah teknis yang berbelit.")

def hr_risks(concerns):
    """Daftar kalimat risiko untuk dimensi yang di bawah target (maks 5). Tahan-banting."""
    out = []
    for r in concerns[:5]:
        if not isinstance(r, dict):
            continue
        dim = r.get("dim")
        label = r.get("label") or dim or "Aspek"
        out.append(f"**{label}** - {RISK.get(dim, 'Kondisi ini berisiko membesar jika dibiarkan tanpa tindak lanjut.')}")
    return out or ["Tidak ada risiko signifikan yang teridentifikasi pada data saat ini."]

# --- Dimensi instrumen tambahan (katalog produk) ---
DIM_INFO.update({'O': 'Keterbukaan mengukur seberapa jauh seseorang menyukai ide baru dan cara berpikir imajinatif.', 'C': 'Ketertiban mengukur seberapa jauh seseorang terorganisir, dapat diandalkan, dan menepati rencana.', 'E': 'Extraversi mengukur energi sosial: kenyamanan berinteraksi dan terlihat dalam kelompok.', 'A': 'Keramahan mengukur kecenderungan percaya, bekerja sama, dan berempati pada orang lain.', 'N': 'Neurotisisme mengukur kecenderungan cemas, mudah tersinggung, dan tidak stabil secara emosional. Skor tinggi = perlu perhatian.', 'GRIT_PE': 'Ketekunan mengukur kemampuan mempertahankan usaha meski bosan, gagal, atau butuh waktu lama.', 'GRIT_CI': 'Konsistensi minat mengukur kemampuan bertahan pada minat dan tujuan jangka panjang.', 'SELFCTRL': 'Kontrol diri mengukur kemampuan menahan godaan, menjaga fokus, dan bertindak sesuai rencana.', 'RESIL': 'Resiliensi mengukur kecepatan dan kemampuan diri pulih setelah tekanan atau kegagalan.', 'PROCR': 'Prokrastinasi mengukur kecenderungan menunda-nunda tugas penting. Skor tinggi = produktivitas terancam.', 'LEAD_PF': 'Fokus perilaku mengukur kemampuan menetapkan target diri, memantau kemajuan, dan mengevaluasi hasil kerja sendiri.', 'LEAD_NR': 'Motivasi alami mengukur kemampuan menemukan kesenangan dan makna dari tugas itu sendiri.', 'LEAD_CT': 'Pikiran konstruktif mengukur kebiasaan berpikir positif dan mengambil pelajaran dari kegagalan.', 'KLAN': 'Budaya klan menilai sejauh mana tim terasa seperti keluarga: saling peduli, partisipatif, dan loyal.', 'ADHO': 'Budaya adhocracy menilai sejauh mana tim mendukung inovasi, risiko, dan hal baru.', 'MARKET': 'Budaya pasar menilai sejauh mana tim digerakkan target, kompetisi, dan hasil.', 'HIER': 'Budaya hierarki menilai sejauh mana tim dijalankan aturan, prosedur, struktur, dan kepastian.', 'COG_GMA': 'Screening kognitif mengukur kemampuan logika dan numerik dasar; ini penapisan awal, bukan pengganti tes inteligensi bersistem penuh.'})

INSIGHTS.update({'O': {'low': 'Cenderung nyaman dengan rutinitas; hal baru terasa sebagai gangguan daripada peluang.', 'mid': 'Cukup terbuka pada hal baru, meski butuh waktu beradaptasi.', 'high': 'Sangat terbuka pada ide baru; kuat untuk peran yang menuntut kreativitas dan pembelajaran.'}, 'C': {'low': 'Cenderung spontan dan kurang terencana; tugas berjadwal panjang berisiko terbengkalai.', 'mid': 'Cukup teratur dalam bekerja; konsistensinya naik-turun tergantung beban.', 'high': 'Sangat teratur dan dapat diandalkan; kuat untuk peran dengan tenggat ketat.'}, 'E': {'low': 'Lebih nyaman bekerja mandiri; peran ber-eksposur sosial tinggi bisa menguras energi.', 'mid': 'Fleksibel; nyaman bekerja sama maupun mandiri.', 'high': 'Energik secara sosial; kuat untuk peran networking, presentasi, dan membangun relasi.'}, 'A': {'low': 'Cenderung skeptis dalam relasi; kolaborasi bisa terasa sulit.', 'mid': 'Cukup kooperatif; kerja sama berjalan baik dengan orang yang dikenal.', 'high': 'Sangat kooperatif dan mudah percaya; kuat untuk peran kolaborasi dan layanan.'}, 'N': {'low': 'Emosi stabil; tekanan kerja jarang mengganggu performa maupun relasi.', 'mid': 'Kadang cemas atau tersinggung, namun umumnya masih terkendali.', 'high': 'Cenderung cemas dan labil; berisiko pada stres, konflik, dan burnout tanpa dukungan.'}, 'GRIT_PE': {'low': 'Cenderung berhenti saat tugas menjadi sulit atau membosankan.', 'mid': 'Cukup bertahan dalam kesulitan; tergantung minat pada tugas.', 'high': 'Sangat tekun; kegagalan justru memicu usaha lebih besar.'}, 'GRIT_CI': {'low': 'Minat berpindah-pindah; fokus jangka panjang sulit dipertahankan.', 'mid': 'Cukup mampu mempertahankan fokus pada minat utama.', 'high': 'Sangat konsisten pada minat dan tujuan jangka panjang.'}, 'SELFCTRL': {'low': 'Sulit menahan godaan dan distraksi; sering bertindak tanpa rencana.', 'mid': 'Kontrol diri cukup; melemah saat lelah atau tertekan.', 'high': 'Sangat mampu menjaga fokus dan bertindak sesuai rencana.'}, 'RESIL': {'low': 'Butuh waktu lama untuk pulih dari kegagalan atau tekanan.', 'mid': 'Umumnya mampu pulih, meski butuh waktu dan dukungan.', 'high': 'Pulih cepat dari tekanan; bahkan tumbuh dari kesulitan.'}, 'PROCR': {'low': 'Jarang menunda; tugas dikerjakan sesuai jadwal.', 'mid': 'Kadang menunda tugas yang tidak disukai, namun masih terkendali.', 'high': 'Sering menunda-nunda hingga berisiko pada tenggat dan kualitas kerja.'}, 'LEAD_PF': {'low': 'Target pribadi kabur; kerja berjalan tanpa arah yang jelas.', 'mid': 'Ada target dan evaluasi diri, meski belum konsisten.', 'high': 'Sangat disiplin dalam menetapkan target, memantau, dan mengevaluasi diri.'}, 'LEAD_NR': {'low': 'Tugas terasa sekadar kewajiban; motivasi bergantung pada imbalan luar.', 'mid': 'Mulai menemukan kesenangan dalam sebagian tugas.', 'high': 'Mampu menciptakan makna dari tugas itu sendiri - motivasi tahan lama.'}, 'LEAD_CT': {'low': 'Cenderung berpikir pesimis dan sulit bangkit dari kegagalan.', 'mid': 'Secara umum berpikir positif, meski terpengaruh kegagalan.', 'high': 'Sangat konstruktif; mengubah kegagalan menjadi bahan belajar.'}, 'KLAN': {'low': 'Ikatan tim lemah; anggota bekerja sekadar tugas.', 'mid': 'Ada rasa kekeluargaan, meski belum kuat.', 'high': 'Tim sangat solid dan saling mendukung - aset retensi.'}, 'ADHO': {'low': 'Tim jarang mencoba hal baru; inovasi terhambat.', 'mid': 'Ada ruang untuk inovasi, meski terbatas.', 'high': 'Tim sangat inovatif dan berani mengambil risiko.'}, 'MARKET': {'low': 'Orientasi hasil lemah; target tidak terasa hidup.', 'mid': 'Cukup berorientasi hasil.', 'high': 'Sangat berorientasi target dan kompetisi - kuat untuk bisnis agresif.'}, 'HIER': {'low': 'Struktur dan aturan kabur; kekacauan prosedural.', 'mid': 'Struktur cukup jelas.', 'high': 'Sangat terstruktur - cocok untuk operasional sensitif risiko.'}, 'COG_GMA': {'low': 'Kemampuan logika-numerik dasar di bawah rata-rata untuk pekerjaan analitis.', 'mid': 'Kemampuan logika-numerik cukup untuk sebagian besar pekerjaan umum.', 'high': 'Kemampuan logika-numerik kuat; cocok untuk peran analitis dan kompleks (tetap perlu tes GMA bersistem untuk keputusan besar).'}})

MODULE_MAP.update({
    "O": "Modul Pengembangan: Keterbukaan & kreativitas",
    "C": "Modul Pengembangan: Kedisiplinan & manajemen tugas",
    "E": "Modul Pengembangan: Komunikasi & energi sosial",
    "A": "Modul Pengembangan: Kerja sama & empati",
    "N": "Modul Pengembangan: Stabilitas emosi & manajemen stres",
    "GRIT_PE": "Modul Pengembangan: Mental growth & ketekunan",
    "GRIT_CI": "Modul Pengembangan: Fokus jangka panjang & goal alignment",
    "SELFCTRL": "Modul Pengembangan: Manajemen diri & fokus",
    "RESIL": "Modul Pengembangan: Pembangunan resiliensi",
    "PROCR": "Modul Pengembangan: Manajemen waktu & anti-prokrastinasi",
    "LEAD_PF": "Modul Pengembangan: Self-leadership & goal setting",
    "LEAD_NR": "Modul Pengembangan: Motivasi intrinsik",
    "LEAD_CT": "Modul Pengembangan: Growth mindset & positive reframing",
    "KLAN": "Modul Pengembangan: Penguatan kebersamaan tim",
    "ADHO": "Modul Pengembangan: Inovasi & kreativitas",
    "MARKET": "Modul Pengembangan: Orientasi hasil & kompetisi sehat",
    "HIER": "Modul Pengembangan: Kejelasan struktur & proses",
    "COG_GMA": "Modul Pengembangan: Pelatihan analitis & pemecahan masalah",
})

# --- Dimensi batch 3 ---
DIM_INFO.update({'COG_IMG': 'Penalaran matriks mengukur penalaran fluid: kemampuan memecahkan masalah baru tanpa mengandalkan hafalan. Ini komponen inti dari kecerdasan umum (GMA).', 'DASS_D': 'Skala depresi menilai gejala seperti kehilangan minat, murung, dan perasaan tidak berharga. Ini instrumen SCREENING - bukan diagnosis.', 'DASS_A': 'Skala anxiety menilai gejala cemas fisik dan psikologis. Ini instrumen SCREENING - bukan diagnosis.', 'DASS_S': 'Skala stress menilai ketegangan, gelisah, dan kesulitan santai. Ini instrumen SCREENING - bukan diagnosis.', 'PHQ': "PHQ-9 adalah screening depresi yang paling banyak dipakai di dunia. Hasil 'perlu perhatian' menandakan perlunya tindak lanjut profesional - bukan diagnosis.", 'GAD': "GAD-7 adalah screening kecemasan standar. Hasil 'perlu perhatian' menandakan perlunya tindak lanjut profesional - bukan diagnosis.", 'WHO5': 'WHO-5 mengukur kesejahteraan psikologis umum; skor di bawah 50 umumnya menandakan perlu perhatian.', 'DISC_D': 'Gaya D (Dominance): fokus pada hasil, kecepatan, dan mengendalikan situasi.', 'DISC_I': 'Gaya I (Influence): fokus pada orang, antusiasme, dan memengaruhi.', 'DISC_S': 'Gaya S (Steadiness): fokus pada kestabilan, kesabaran, dan kerja sama.', 'DISC_C': 'Gaya C (Compliance): fokus pada akurasi, aturan, dan analisis.', 'SALES_DRIVE': 'Drive berjualan adalah dorongan internal untuk meyakinkan, membujuk, dan closing.', 'SALES_RES': 'Ketahanan penolakan adalah kemampuan tetap bersemangat setiap ditolak klien.', 'SALES_REL': 'Orientasi relasi adalah kecenderungan membangun kepercayaan jangka panjang dengan klien.', 'SALES_TGT': 'Orientasi target adalah kebiasaan mengejar angka dan memantau hasil penjualan.', 'SERV': 'Servant leadership adalah kepemimpinan yang mengutamakan pengembangan orang lain di atas hasil pribadi.', 'J_DIST': 'Keadilan imbalan menilai apakah hasil yang diterima (gaji, bonus, penghargaan) sesuai kontribusi.', 'J_PROC': 'Keadilan prosedural menilai apakah proses keputusan konsisten, tidak bias, dan memberi ruang suara.', 'J_INTER': 'Keadilan interpersonal menilai apakah atasan memperlakukan karyawan dengan hormat dan jujur.'})

INSIGHTS.update({'DASS_D': {'low': 'Tidak ada gejala depresi yang signifikan. Kondisi psikologis dasar tampak baik.', 'mid': 'Ada gejala depresi ringan-sedang. Perlu dipantau; pertimbangkan dukungan konseling.', 'high': 'Gejala depresi signifikan. WAJIB ditindaklanjuti dengan konseling/psikolog profesional - screening ini bukan diagnosis, tapi sinyalnya serius.'}, 'DASS_A': {'low': 'Tidak ada gejala kecemasan yang signifikan.', 'mid': 'Ada gejala cemas ringan-sedang. Identifikasi sumbernya dan pantau perkembangannya.', 'high': 'Gejala cemas signifikan. WAJIB ditindaklanjuti profesional - kecemasan tinggi berdampak langsung pada performa dan kualitas hidup.'}, 'DASS_S': {'low': 'Tingkat stress masih terkendali.', 'mid': 'Stress sedang. Perhatikan pola pemulihan (tidur, istirahat, batas kerja).', 'high': 'Stress tinggi. Ini kondisi kesehatan, bukan kelemahan - segera lakukan intervensi stres dan pertimbangkan konseling.'}, 'PHQ': {'low': 'Screening depresi negatif / minimal.', 'mid': 'Ada gejala depresi ringan-sedang. Pertimbangkan konseling sebagai langkah pencegahan.', 'high': 'Screening depresi positif signifikan. WAJIB dirujuk ke psikolog/psikiater profesional.'}, 'GAD': {'low': 'Screening kecemasan negatif / minimal.', 'mid': 'Ada kecemasan ringan-sedang. Pantau sumbernya.', 'high': 'Screening kecemasan positif signifikan. WAJIB ditindaklanjuti profesional.'}, 'WHO5': {'low': 'Kesejahteraan psikologis rendah - sinyal penting yang perlu diperhatikan.', 'mid': 'Kesejahteraan cukup, masih ada ruang untuk ditingkatkan.', 'high': 'Kesejahteraan psikologis baik - modal utama produktivitas jangka panjang.'}, 'COG_IMG': {'low': 'Penalaran fluid di bawah rata-rata. Untuk peran analitis kompleks, pertimbangkan tes GMA bersistem penuh.', 'mid': 'Penalaran fluid cukup untuk sebagian besar pekerjaan umum.', 'high': 'Penalaran fluid kuat - kemampuan memecahkan masalah baru dengan cepat. Tetap konfirmasi dengan tes GMA penuh untuk keputusan besar.'}, 'SALES_DRIVE': {'low': 'Drive berjualan rendah; peran sales intensif akan terasa membebani.', 'mid': 'Ada dorongan berjualan, meski masih bisa dikembangkan.', 'high': 'Drive berjualan tinggi - dorongan alami untuk meyakinkan dan closing.'}, 'SALES_RES': {'low': 'Penolakan mudah mempengaruhi semangat; perlu penguatan mental selling.', 'mid': 'Cukup tahan terhadap penolakan.', 'high': 'Sangat tahan penolakan - aset utama untuk peran sales.'}, 'SALES_REL': {'low': 'Cenderung fokus pada transaksi, belum pada relasi jangka panjang.', 'mid': 'Mulai membangun relasi klien.', 'high': 'Orientasi relasi kuat - klien cenderung loyal.'}, 'SALES_TGT': {'low': 'Target tidak terasa menjadi dorongan.', 'mid': 'Cukup berorientasi target.', 'high': 'Sangat berorientasi target - termotivasi angka dan kompetisi.'}, 'SERV': {'low': 'Kecenderungan memimpin dengan melayani masih rendah.', 'mid': 'Ada kecenderungan servant leadership.', 'high': 'Kuat dalam memimpin dengan melayani - tim cenderung loyal dan bertumbuh.'}, 'J_DIST': {'low': 'Imbalan dirasa tidak sesuai kontribusi - risiko ketidakpuasan.', 'mid': 'Keadilan imbalan cukup.', 'high': 'Imbalan dirasa adil - fondasi retensi.'}, 'J_PROC': {'low': 'Prosedur dirasa tidak adil/tidak konsisten - sumber konflik potensial.', 'mid': 'Prosedural cukup adil.', 'high': 'Prosedur dirasa adil dan konsisten.'}, 'J_INTER': {'low': 'Perlakuan interpersonal dirasa kurang hormat - perlu perhatian serius.', 'mid': 'Cukup diperlakukan dengan hormat.', 'high': 'Perlakuan atasan dirasa jujur dan bermartabat.'}})

MODULE_MAP.update({'COG_IMG': 'Program pengembangan: pelatihan analitis & pemecahan masalah', 'DASS_D': 'Rujukan konseling profesional + program kesejahteraan', 'DASS_A': 'Rujukan konseling profesional + program manajemen kecemasan', 'DASS_S': 'Rujukan konseling profesional + program manajemen stres', 'PHQ': 'Rujukan konseling profesional (screening depresi positif)', 'GAD': 'Rujukan konseling profesional (screening kecemasan positif)', 'WHO5': 'Program peningkatan kesejahteraan kerja', 'DISC_D': 'Modul pengembangan: gaya komunikasi & delegasi', 'DISC_I': 'Modul pengembangan: komunikasi & memengaruhi', 'DISC_S': 'Modul pengembangan: stabilitas & layanan', 'DISC_C': 'Modul pengembangan: akurasi & kualitas kerja', 'EI': 'Modul pengembangan: gaya energi & komunikasi tim', 'SN': 'Modul pengembangan: gaya informasi & perencanaan', 'TF': 'Modul pengembangan: gaya pengambilan keputusan', 'JP': 'Modul pengembangan: gaya kerja & manajemen tugas', 'SALES_DRIVE': 'Modul pengembangan: teknik selling & closing', 'SALES_RES': 'Modul pengembangan: mental resilience untuk sales', 'SALES_REL': 'Modul pengembangan: relationship selling', 'SALES_TGT': 'Modul pengembangan: target management & sales pipeline', 'LS_DIR': 'Modul pengembangan: kepemimpinan situasional (directing)', 'LS_COACH': 'Modul pengembangan: kepemimpinan situasional (coaching)', 'LS_SUP': 'Modul pengembangan: kepemimpinan situasional (supporting)', 'LS_DEL': 'Modul pengembangan: kepemimpinan situasional (delegating)', 'SERV': 'Modul pengembangan: servant leadership', 'J_DIST': 'Modul pengembangan: keadilan imbalan & reward system', 'J_PROC': 'Modul pengembangan: keadilan prosedural & proses keputusan', 'J_INTER': 'Modul pengembangan: kepemimpinan interpersonal'})

CONSEQUENCE.update({'O': 'Keterbukaan rendah membatasi adaptasi terhadap perubahan dan masukan baru.', 'C': 'Ketertiban rendah berisiko pada tenggat terlewat dan kualitas kerja yang tidak konsisten.', 'E': 'Extraversi rendah bukan masalah, tetapi untuk peran ber-hubungan-intensif perlu jalur kerja yang sesuai.', 'A': 'Keramahan rendah meningkatkan risiko konflik interpersonal dan kesulitan kolaborasi.', 'N': 'Neurotisisme tinggi adalah risiko utama burnout, konflik, dan absensi jika tanpa dukungan.', 'GRIT_PE': 'Ketekunan rendah membuat proyek panjang mudak berhenti di tengah jalan.', 'GRIT_CI': 'Minat yang berpindah-pindah menyulitkan pembangunan keahlian mendalam.', 'SELFCTRL': 'Kontrol diri rendah berdampak langsung pada fokus, kualitas, dan konsistensi kerja.', 'RESIL': 'Resiliensi rendah membuat tekanan kecil berubah menjadi absensi atau penurunan performa.', 'PROCR': 'Prokrastinasi tinggi diam-diam memakan tenggat, kualitas, dan kepercayaan atasan.', 'LEAD_PF': 'Tanpa fokus perilaku, pekerjaan berjalan tanpa target dan evaluasi yang jelas.', 'LEAD_NR': 'Motivasi alami rendah membuat performa bergantung penuh pada imbalan luar.', 'LEAD_CT': 'Pola pikir tidak konstruktif memperpanjang dampak kegagalan dan memperlambat pemulihan.', 'KLAN': 'Ikatan tim lemah meningkatkan risiko retensi dan memperlambat kolaborasi.', 'ADHO': 'Inovasi terhambat membuat organisasi rentan tertinggal dari pesaing.', 'MARKET': 'Orientasi hasil lemah membuat target tidak terasa hidup di tim.', 'HIER': 'Struktur kabur menciptakan ketidakpastian peran dan konflik prosedural.', 'COG_IMG': 'Penalaran fluid rendah membatasi kemampuan memecahkan masalah baru di peran kompleks.', 'DASS_D': 'Gejala depresi yang tidak ditangani berisiko pada performa, absensi, dan retensi.', 'DASS_A': 'Kecemasan tinggi menguras fokus dan kualitas keputusan setiap hari.', 'DASS_S': 'Stress tinggi menumpuk menjadi burnout jika tidak ada intervensi.', 'PHQ': 'Screening depresi positif memerlukan tindak lanjut profesional - bukan sekadar isu HR.', 'GAD': 'Kecemasan tidak tertangani berdampak pada kualitas kerja dan kesehatan jangka panjang.', 'WHO5': 'Kesejahteraan rendah adalah prediktor awal penurunan performa dan niat keluar.', 'DISC_D': 'Gaya dominan yang tidak terkalibrasi bisa terbaca sebagai arogan dan merusak tim.', 'DISC_I': 'Gaya influencer tanpa struktur bisa menghasilkan banyak bicara, sedikit eksekusi.', 'DISC_S': 'Gaya stabil yang berlebihan bisa membuat konflik tersembunyi dan perubahan lambat.', 'DISC_C': 'Gaya cermat berlebihan bisa memperlambat keputusan dan inovasi.', 'EI': 'Ketidakcocokan gaya energi dengan peran bisa menguras produktivitas - pertimbangkan penempatan.', 'SN': 'Gaya informasi yang berbeda di dalam tim bisa memicu miskomunikasi bila tidak disadari.', 'TF': "Perbedaan gaya keputusan tanpa kesadaran tim memicu konflik 'dingin-panas'.", 'JP': 'Perbedaan gaya kerja menimbulkan friksi antara yang butuh kepastian dan yang butuh fleksibilitas.', 'SALES_DRIVE': 'Drive berjualan rendah membuat peran sales terasa memaksa dan hasilnya stagnan.', 'SALES_RES': 'Tidak tahan penolakan membuat siklus sales berhenti di penolakan pertama.', 'SALES_REL': 'Orientasi transaksi tanpa relasi membuat klien tidak loyal.', 'SALES_TGT': 'Tanpa orientasi target, performa sales tidak terukur dan tidak terarah.', 'LS_DIR': 'Ketergantungan pada satu gaya memimpin membuat leader tidak efektif di situasi berbeda.', 'LS_COACH': 'Gaya melatih yang minim membuat anggota tidak berkembang.', 'LS_SUP': 'Dukungan minim membuat anggota merasa tidak dilihat dan tidak dihargai.', 'LS_DEL': 'Delegasi minim membuat leader kewalahan dan anggota tidak tumbuh.', 'SERV': 'Servant leadership rendah membuat kepercayaan tim sulit dibangun.', 'J_DIST': 'Ketidakadilan imbalan adalah salah satu pemicu resign paling kuat yang ada.', 'J_PROC': 'Prosedur yang dirasa tidak adil memicu keluhan, konflik, dan sikap acuh.', 'J_INTER': 'Perlakuan interpersonal tidak adil merusak kepercayaan langsung pada atasan dan organisasi.'})

CONSEQUENCE.update({"COG_GMA": "Kemampuan logika-numerik dasar di bawah rata-rata membatasi efektivitas di peran yang menuntut analisis cepat."})

RISK.update({'O': 'Keterbukaan rendah di banyak orang membuat organisasi lambat beradaptasi terhadap perubahan pasar dan teknologi.', 'C': 'Ketertiban rendah di populasi membuat tenggat dan kualitas menjadi taruhan; biaya perbaikan kesalahan akan tumbuh diam-diam.', 'E': 'Profil energi sosial yang tidak sesuai dengan tuntutan peran membuat banyak karyawan bekerja di bawah kapasitasnya yang sesungguhnya.', 'A': 'Keramahan rendah membuat kolaborasi antar-divisi mahal: meeting panjang, kesepakatan lambat, konflik kecil yang berulang.', 'N': 'Populasi dengan neurotisisme tinggi adalah lahan subur burnout - dan burnout adalah biaya turnover yang paling sering tidak dihitung.', 'GRIT_PE': 'Tanpa ketekunan, program jangka panjang (transformasi digital, kultur baru) akan berhenti di tengah jalan.', 'GRIT_CI': 'Minat yang berpindah-pindah membuat investasi pelatihan tidak bertahan; keterampilan dangkal sulit bersaing.', 'SELFCTRL': 'Kontrol diri rendah berdampak langsung pada output harian - jam kerja sama, hasilnya tidak.', 'RESIL': 'Resiliensi rendah membuat satu krisis kecil berubah menjadi gelombang absensi dan permintaan pindah divisi.', 'PROCR': "Prokrastinasi adalah pencuri tenggat yang paling sulit dilihat: pekerjaan 'selesai', tetapi kualitas dan biaya lemburnya tidak pernah dihitung.", 'LEAD_PF': 'Tanpa self-leadership, karyawan senior pun membutuhkan pengawasan seperti staf baru - biaya manajemen membengkak.', 'LEAD_NR': 'Motivasi alami rendah berarti seluruh dorongan kerja harus dibeli ulang setiap bulan lewat insentif.', 'LEAD_CT': 'Pola pikir yang tidak konstruktif membuat satu kegagalan proyek berdampak berlipat pada moral tim.', 'KLAN': 'Ikatan tim lemah membuat rekrutmen baru sulit bertahan: orang masuk, tidak merasa punya tempat, lalu pergi.', 'ADHO': 'Inovasi yang terhambat membuat perusahaan bereaksi, bukan memimpin pasar.', 'MARKET': 'Tanpa orientasi hasil, target menjadi angka dekoratif - diketahui semua, dikejar tidak ada.', 'HIER': 'Struktur kabur membuat keputusan terjebak di mana-mana dan pertanggungjawaban tidak jelas.', 'COG_GMA': 'Tanpa kemampuan analitis yang memadai, kesalahan logis dalam keputusan bisnis akan sering lolos tanpa terdeteksi.', 'COG_IMG': 'Penalaran fluid rendah membatasi kemampuan tim memecahkan masalah yang belum pernah dihadapi - persis jenis masalah yang paling sering menentukan masa depan perusahaan.', 'DASS_D': 'Depresi yang tidak tertangani adalah biaya terbesar yang tidak terlihat di laporan keuangan: presenteeism, absensi, dan resign tanpa peringatan.', 'DASS_A': 'Kecemasan populasi tinggi menurunkan kualitas seluruh keputusan organisasi, satu orang satu keputusan setiap hari.', 'DASS_S': 'Stress kronis adalah pintu masuk segala masalah lainnya: burnout, konflik, dan penurunan kualitas yang merata.', 'PHQ': 'Screening depresi positif pada populasi bukan alarm palsu - ini peta lokasi masalah yang perlu tanggapan sistematis, bukan kasus per kasus.', 'GAD': 'Kecemasan yang tidak tertangani membuat organisasi berjalan dalam mode bertahan hidup, bukan bertumbuh.', 'WHO5': 'Kesejahteraan rendah di populasi adalah prediktor paling awal dari gelombang resign - selalu mendahului turnover 3-6 bulan.', 'DISC_D': 'Dominan tanpa kesadaran diri merusak psychological safety - dan safety yang rusak mematikan suara terbaik tim.', 'DISC_I': 'Influencer tanpa eksekusi menciptakan tim yang ramai di meeting, kosong di hasil.', 'DISC_S': 'Stabilitas tanpa keberanian berubah membuat organisasi terlambat merespons krisis.', 'DISC_C': 'Kecermatan berlebih tanpa fleksibilitas membuat keputusan penting tertahan di analisis tanpa akhir.', 'EI': 'Perbedaan gaya energi yang tidak dikelola membuat setiap meeting berisi dua percakapan yang tidak pernah bertemu.', 'SN': 'Perbedaan gaya informasi membuat instruksi dari atas sering tiba di bawah dalam bentuk yang berbeda sepenuhnya.', 'TF': 'Konflik gaya keputusan membuat keputusan bisnis bergantung pada siapa yang paling keras, bukan yang paling benar.', 'JP': 'Friksi gaya kerja membuat deadline menjadi sumber konflik rutin, bukan alat koordinasi.', 'SALES_DRIVE': 'Tim sales tanpa drive akan menunggu order, bukan menciptakannya - dan pasar tidak menunggu siapapun.', 'SALES_RES': 'Satu penolakan yang tidak tertangani dengan baik bisa mematikan seminggu aktivitas sales.', 'SALES_REL': 'Relasi yang dibangun transaksional akan hilang begitu kompetitor menawarkan harga lebih baik.', 'SALES_TGT': 'Tanpa orientasi target, performa sales tidak bisa dikelola - yang tidak terukur tidak bisa diperbaiki.', 'LS_DIR': 'Satu gaya memimpin untuk semua situasi berarti memimpin sebagian tim dengan cara yang salah setiap saat.', 'LS_COACH': 'Leader yang tidak melatih membuat timnya bergantung selamanya - pertumbuhan berhenti pada level leader-nya.', 'LS_SUP': 'Dukungan yang minim membuat anggota menilai dirinya tidak dilihat, dan orang yang tidak dilihat tidak bertahan lama.', 'LS_DEL': 'Tanpa delegasi, leader menjadi bottleneck dan anggota tidak pernah siap menggantikannya.', 'SERV': 'Kepemimpinan tanpa pelayanan membuat tim yang patuh, bukan tim yang percaya.', 'J_DIST': 'Ketidakadilan imbalan adalah pemicu resign yang paling sering disebutkan langsung di exit interview.', 'J_PROC': 'Prosedur yang tidak adil mengajarkan karyawan bahwa usaha tidak menentukan hasil - dan itu pelajaran yang tidak pernah bisa dibatalkan.', 'J_INTER': 'Perlakuan tidak hormat dari atasan adalah alasan resign yang paling jarang dilaporkan, dan paling sering menjadi penyebabnya.'})

INSIGHTS.update({'DISC_D': ('Gaya D rendah: cenderung menghindari konfrontasi dan mengambil kendali. Ini bukan kelemahan - sesuaikan perannya.', 'Gaya D cukup terlihat: mampu mengambil keputusan saat dibutuhkan tanpa mendominasi.', 'Gaya D dominan: berorientasi hasil dan kecepatan. Pasangkan dengan kesadaran untuk tidak menggilas suara orang lain.'), 'DISC_I': ('Gaya I rendah: cenderung bekerja di belakang layar. Untuk peran hubungan, beri latihan bertahap.', 'Gaya I cukup: nyaman berinteraksi tanpa perlu menjadi pusat perhatian.', 'Gaya I dominan: energi sosial tinggi, pandai memengaruhi. Arahkan agar antusiasme selalu berujung eksekusi.'), 'DISC_S': ('Gaya S rendah: cenderung cepat dan dinamis; perhatikan kebutuhan tim akan stabilitas.', 'Gaya S cukup: mampu stabil namun tetap bergerak.', 'Gaya S dominan: pilar kestabilan tim. Jaga agar kestabilan tidak berubah jadi penolakan perubahan.'), 'DISC_C': ('Gaya C rendah: cenderung cepat bertindak dan fleksibel; untuk pekerjaan detail, sediakan sistem pendukung.', 'Gaya C cukup: memperhatikan kualitas tanpa terjebak perfeksionisme.', 'Gaya C dominan: sangat teliti dan terstruktur. Jaga agar analisis tidak menggantikan aksi.'), 'EI': ('Skor condong ke arah Introversi (I): energi didapat dari waktu sendiri; peran interaksi intensif perlu diimbangi jeda pemulihan.', 'Seimbang antara ekstroversi dan introversi; fleksibel di berbagai situasi sosial.', 'Condong ke Ekstroversi (E): energi didapat dari interaksi; cocok untuk peran hubungan dan representasi.'), 'SN': ('Condong ke Sensing (S): praktis, berpijak pada fakta dan pengalaman terbukti.', 'Seimbang antara Sensing dan Intuition; mampu detail sekaligus melihat gambar besar.', 'Condong ke Intuition (N): visioner, suka pola dan kemungkinan; cocok untuk peran strategis dan inovasi.'), 'TF': ('Condong ke Thinking (T): keputusan berbasis logika dan analisis.', 'Seimbang antara Thinking dan Feeling; mampu objektif sekaligus mempertimbangkan dampak pada orang.', 'Condong ke Feeling (F): keputusan mempertimbangkan nilai dan dampak manusia; kuat untuk peran people-oriented.'), 'JP': ('Condong ke Judging (J): terencana, suka kepastian dan penyelesaian.', 'Seimbang antara Judging dan Perceiving; fleksibel namun tetap terarah.', 'Condong ke Perceiving (P): spontan, terbuka pada opsi baru; cocok untuk lingkungan dinamis.'), 'LS_DIR': ('Jarang memakai gaya mengarahkan; untuk anggota baru atau krisis, tim bisa kehilangan arah.', 'Menggunakan gaya mengarahkan secukupnya.', 'Sering memakai gaya mengarahkan; efektif untuk anggota baru, pastikan tidak berlebihan pada anggota senior.'), 'LS_COACH': ('Gaya melatih minim; anggota tidak mendapat umpan balik berkembang.', 'Gaya melatih cukup; ada arahan dan masukan.', 'Gaya melatih dominan; kuat mengembangkan orang, pastikan tetap memberi ruang mandiri.'), 'LS_SUP': ('Gaya mendukung minim; anggota bisa merasa tidak dilihat.', 'Gaya mendukung cukup; suasana tim terjaga.', 'Gaya mendukung dominan; tim merasa didengar, jaga agar standar tetap terjaga.'), 'LS_DEL': ('Delegasi minim; Anda berisiko jadi bottleneck dan anggota tidak bertumbuh.', 'Delegasi cukup; tanggung jawab mulai dibagi.', 'Delegasi kuat; anggota diberi ruang penuh, pastikan dukungan tetap tersedia saat diminta.')})

DIM_INFO.update({'EI': 'Dimensi energi: seberapa besar interaksi sosial mengisi (Ekstroversi) atau menguras (Introversi) energi.', 'SN': 'Dimensi informasi: fokus pada fakta konkret (Sensing) atau pada pola dan kemungkinan (Intuition).', 'TF': 'Dimensi keputusan: berbasis logika dan analisis (Thinking) atau nilai dan dampak manusia (Feeling).', 'JP': 'Dimensi gaya hidup: terencana dan pasti (Judging) atau fleksibel dan terbuka (Perceiving).', 'LS_DIR': 'Gaya mengarahkan: memberi instruksi rinci dan pengawasan ketat; efektif untuk anggota baru atau krisis.', 'LS_COACH': 'Gaya melatih: memberi arah sambil menjelaskan alasan dan membangun keterampilan.', 'LS_SUP': 'Gaya mendukung: fokus pada relasi, partisipasi, dan motivasi anggota.', 'LS_DEL': 'Gaya mendelegasikan: menyerahkan tanggung jawab penuh pada anggota yang sudah mampu.'})

INSTRUMENT_META.update({'BFI': ('Tes 7 - Kepribadian Utuh (Big Five)', "Big Five adalah peta kepribadian yang paling banyak dipakai dalam psikologi modern: terbuka pada hal baru, disiplin, keaktifan sosial, keramahan, dan stabilitas emosi. Cocok untuk memahami gaya kerja dasar seseorang, bukan untuk menghakimi - tidak ada kepribadian yang 'salah', hanya yang lebih atau kurang cocok dengan konteks."), 'GRIT': ('Tes 8 - Grit & Ketekunan', 'Grit membedakan orang yang bertahan dari yang berbakat tapi mudah berhenti. Dua sayapnya: ketekunan (terus berusaha saat sulit) dan konsistensi minat (tetap pada tujuan jangka panjang). Prediktor kuat untuk keberhasilan di peran yang panjang dan menantang.'), 'SELFCTRL': ('Tes 9 - Kontrol Diri', 'Kontrol diri adalah kemampuan menjaga fokus, menahan godaan, dan bertindak sesuai rencana - kemampuan dasar yang mendasari hampir semua aspek produktivitas. Skor rendah bukan vonis; ia menunjukkan tempat intervensi yang paling berdampak.'), 'RESIL': ('Tes 10 - Resiliensi', 'Resiliensi adalah kecepatan pulih setelah tekanan atau kegagalan. Di dunia kerja yang penuh perubahan, ini bukan kemewahan melainkan perlindungan: orang yang pulih cepat tidak membawa kemarin ke hari ini.'), 'PROCR': ('Tes 11 - Prokrastinasi', 'Prokrastinasi bukan soal malas - ia soal pengaturan emosi terhadap tugas yang tidak nyaman. Skor tinggi berarti banyak energi terkuras oleh penundaan; kabar baiknya, ini salah satu kebiasaan yang paling bisa diubah lewat pelatihan dan desain kerja.'), 'LEADER': ('Tes 12 - Self-Leadership', 'Sebelum memimpin orang lain, seseorang perlu bisa memimpin dirinya: menetapkan target, memantau diri, menciptakan motivasi alami, dan berpikir konstruktif. Fondasi kepemimpinan yang sering dilupakan.'), 'CULTURE': ('Tes 13 - Budaya Kerja Tim', 'Budaya tim dapat dibaca lewat 4 kecenderungan: klan (kekeluargaan), adhocracy (inovasi), pasar (orientasi hasil), dan hierarki (struktur). Tidak ada budaya yang paling benar - yang penting adalah kesadaran tim akan budayanya sendiri dan kesesuaiannya dengan strategi perusahaan.'), 'COG': ('Tes 14 - Screening Kognitif (Logika & Numerik)', 'Screening ini menilai kemampuan logika dan numerik dasar lewat soal cerita dan pola. Berguna sebagai penapisan awal untuk peran yang menuntut pemikiran analitis; untuk keputusan besar tetap disarankan tes GMA bersistem penuh.'), 'CFIT': ('Tes 15 - Penalaran Matriks (GMA Fluid)', "Soal matriks bergambar mengukur penalaran fluid: kemampuan memecahkan masalah BARU tanpa hafalan - inti dari kecerdasan umum. Karena jawaban bergambar, sulit 'ditebak' dan lebih adil bagi peserta dari berbagai latar belakang pendidikan."), 'DASS': ('Tes 16 - Kesehatan Mental (DASS-21)', "DASS-21 membedakan tiga hal yang sering tertukar: depresi (kehilangan minat dan harapan), anxiety (cemas dan waspada berlebih), dan stress (ketegangan yang menumpuk). Hasil adalah SCREENING - bukan diagnosis; skor 'perlu perhatian' artinya saatnya dukungan profesional, bukan penilaian."), 'PHQ': ('Tes 17 - Screening Depresi (PHQ-9)', 'PHQ-9 adalah instrumen screening depresi yang paling banyak dipakai di dunia. Sembilan pertanyaannya memetakan gejala dua minggu terakhir. Ini alat deteksi dini - bukan vonis, bukan label.'), 'GAD': ('Tes 18 - Screening Kecemasan (GAD-7)', 'GAD-7 menilai kecemasan yang berlebih dalam dua minggu terakhir: sulit berhenti cemas, gelisah, mudah tersinggung. Sama seperti PHQ-9, ini screening yang mengarahkan pada tindak lanjut, bukan diagnosis.'), 'WHO5': ('Tes 19 - Kesejahteraan Psikologis (WHO-5)', 'WHO-5 adalah termometer kesejahteraan: lima pertanyaan singkat tentang energi, ketenangan, dan kebermaknaan. Skor di bawah 50 adalah sinyal dini yang layak ditanggapi sebelum menjadi masalah besar.'), 'DISC': ('Tes 20 - Gaya Perilaku DISC', 'DISC membaca empat gaya perilaku dominan: Dominance (mengendalikan), Influence (memengaruhi), Steadiness (menstabilkan), Compliance (mengerjakan dengan teliti). CATATAN: ini indikator gaya untuk self-awareness dan kerja sama tim - bukan alat seleksi atau penilaian kinerja.'), 'MBTIX': ('Tes 21 - Indikator Tipe Kepribadian', 'Empat dimensi ini membaca preferensi alami: arah energi (E/I), cara menyerap informasi (S/N), dasar mengambil keputusan (T/F), dan gaya menjalani hidup (J/P). CATATAN: seperti DISC, ini alat memahami diri dan komunikasi tim - bukan alat seleksi; tipe tidak menentukan kemampuan.'), 'SALES': ('Tes 22 - Profil Sales & Drive Berjualan', 'Profil sales menilai empat bahan bakar penjualan: dorongan untuk meyakinkan, ketahanan terhadap penolakan, kemampuan membangun relasi, dan orientasi pada target. Berguna untuk menyusun tim sales, mendiagnosis penyebab stagnasi, atau memilih jalur karir.'), 'LEADSIT': ('Tes 23 - Gaya Kepemimpinan Situasional', 'Tidak ada satu gaya memimpin yang selalu benar. Instrumen ini membaca kecenderungan Anda pada empat gaya: mengarahkan (anggota baru), melatih (anggota bersemangat tapi belirum mampu), mendukung (mampu tapi ragu), dan mendelegasikan (mampu dan percaya diri). Pemimpin efektif bergaya sesuai kebutuhan.'), 'SERVANT': ('Tes 24 - Servant Leadership', "Servant leadership membalik arah kepemimpinan: bukan 'orang bekerja untuk leader', melainkan 'leader bekerja untuk orangnya'. Skor tinggi menandakan kecenderungan memimpin lewat pelayanan, pengembangan orang, dan kepedulian pada keadilan."), 'JUSTICE': ('Tes 25 - Keadilan Organisasi', 'Karyawan menilai keadilan lewat tiga lensa: keadilan imbalan (apakah hasil sesuai kontribusi), keadilan prosedural (apakah proses konsisten dan tidak bias), dan keadilan interpersonal (apakah perlakuannya hormat). Ketiganya adalah fondasi kepercayaan dan retensi.')})

# normalisasi bentuk INSTRUMENT_META (tuple -> dict)
for _k, _v in list(INSTRUMENT_META.items()):
    if isinstance(_v, tuple):
        INSTRUMENT_META[_k] = {'title': _v[0], 'plain': _v[1]}

# normalisasi INSIGHTS tuple -> dict (low/mid/high)
for _k in ['DISC_D','DISC_I','DISC_S','DISC_C','EI','SN','TF','JP','LS_DIR','LS_COACH','LS_SUP','LS_DEL']:
    _v = INSIGHTS.get(_k)
    if isinstance(_v, tuple):
        INSIGHTS[_k] = {'low': _v[0], 'mid': _v[1], 'high': _v[2]}

# --- batch 4: Aspen Medical ---
DIM_INFO.update({'V_RESPECT': 'Nilai Respect: sejauh mana setiap orang - pasien, keluarga, staf - diperlakukan dengan hormat dalam praktik sehari-hari.', 'V_INTEG': 'Nilai Integrity: kejujuran dan konsistensi kata-tindakan, termasuk dari pemimpin, dalam praktik nyata.', 'V_COMP': 'Nilai Compassion: kepedulian nyata pada pasien, di luar sekadar prosedur dan target.', 'V_TEAM': 'Nilai Teamwork: kerja sama lintas profesi (dokter-perawat-admin) sebagai satu tim.', 'V_EXCEL': 'Nilai Pursuit of Excellence: standar mutu yang terus dinaikkan dan pembelajaran dari kesalahan.', 'SAFE_COM': 'Komunikasi keselamatan: keterbukan melaporkan masalah dan komunikasi antar-shift/antar-profesi yang aman.', 'SAFE_JUST': 'Just culture: insiden dipakai untuk memperbaiki sistem, bukan menghukum orang; melapor diapresiasi.', 'SAFE_PRI': 'Prioritas keselamatan: keselamatan pasien didahulukan bahkan saat sibuk, dengan dukungan nyata manajemen.', 'CHANGE': 'Kesiapan perubahan: pemahaman, kepercayaan, dan kapasitas individu menghadapi masa transisi.'})
INSIGHTS.update({'V_RESPECT': {'low': 'Respect belum hidup dalam praktik; ini fondasi semua nilai lain - perhatian paling mendesak.', 'mid': 'Respect cukup terasa, namun belum konsisten di semua unit.', 'high': 'Respect telah menjadi praktik nyata - fondasi budaya yang kuat.'}, 'V_INTEG': {'low': 'Integritas rapuh: jarak antara kata dan tindakan merusak kepercayaan.', 'mid': 'Integritas cukup, meski konsistensi pemimpin masih bisa ditingkatkan.', 'high': 'Integritas kuat: jujur dan konsisten menjadi norma yang terlihat.'}, 'V_COMP': {'low': 'Kompasi belum menjadi identitas layanan; pasien terasa sebagai proses, bukan manusia.', 'mid': 'Kepedulian pada pasien cukup, namun sering kalah oleh prosedur.', 'high': 'Kompasi hidup dalam layanan - identitas yang membedakan RS ini.'}, 'V_TEAM': {'low': 'Profesi bekerja dalam silo; pasien merasakan kepotongan layanan.', 'mid': 'Kerja sama cukup dalam unit, namun rapat antar-unit.', 'high': 'Tim lintas profesi berjalan solid - layanan terasa menyatu bagi pasien.'}, 'V_EXCEL': {'low': 'Standar mutu stagnan; kesalahan diulang karena tidak ada pembelajaran.', 'mid': 'Ada dorongan mutu, meski belum menjadi budaya belajar yang sistematis.', 'high': 'Keunggulan dikejar lewat pembelajaran berkelanjutan - budaya improvement hidup.'}, 'SAFE_COM': {'low': 'Masalah keselamatan disembunyikan karena takut - risiko pasien tertinggi di sini.', 'mid': 'Komunikasi keselamatan cukup, namun masih ada yang takut bersuara.', 'high': 'Laporan keselamatan mengalir bebas - sistem pendeteksi dini berfungsi.'}, 'SAFE_JUST': {'low': 'Budaya menyalahkan masih hidup; insiden dipendam, kesalahan berulang.', 'mid': 'Ada niat belajar dari insiden, namun masih bercampur dengan menghakimi.', 'high': 'Just culture berjalan: insiden menjadi bahan perbaikan sistem, bukan vonis.'}, 'SAFE_PRI': {'low': 'Keselamatan masih kalah oleh kesibukan - sinyal berbahaya untuk RS yang akan dibuka kembali.', 'mid': 'Prioritas keselamatan cukup, meski konsistensinya goyah saat puncak.', 'high': 'Keselamatan adalah kompas utama - kesiapan klinis yang sesungguhnya.'}, 'CHANGE': {'low': 'Kesiapan perubahan rendah - komunikasi transisi dan kepercayaan perlu dibangun SEBELUM training dimulai.', 'mid': 'Cukup siap, namun butuh penguatan pemahaman arah dan dukungan.', 'high': 'Tim siap bergerak - masa transisi bisa dimanfaatkan untuk membangun budaya baru.'}})
CONSEQUENCE.update({'V_RESPECT': 'Skor Nilai Respect rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.', 'V_INTEG': 'Skor Nilai Integrity rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.', 'V_COMP': 'Skor Nilai Compassion rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.', 'V_TEAM': 'Skor Nilai Teamwork rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.', 'V_EXCEL': 'Skor Nilai Pursuit of Excellence rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.', 'SAFE_COM': 'Skor Komunikasi keselamatan rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.', 'SAFE_JUST': 'Skor Just culture rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.', 'SAFE_PRI': 'Skor Prioritas keselamatan rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.', 'CHANGE': 'Skor Kesiapan perubahan rendah berarti nilai ini belum menjadi praktik nyata - gap budaya yang harus ditutup sebelum reopening.'})
RISK.update({'V_RESPECT': 'Tanpa respect, semua program budaya lain akan ditolak diam-diam oleh staf. Ini fondasi yang harus dibangun paling pertama.', 'V_INTEG': 'Ketika pemimpin tidak konsisten kata-tindakan, kepercayaan ke pemilik baru hilang dalam hitungan minggu - dan sulit dibangun ulang.', 'V_COMP': 'Rumah sakit tanpa kompasi kehilangan reputasinya lebih cepat daripada membangunnya, terutama di komunitas lokal yang saling berbicara.', 'V_TEAM': 'Silo antar-profesi di rumah sakit bukan hanya masalah efisiensi - ia bisa berakibat fatal pada keselamatan pasien.', 'V_EXCEL': 'Tanpa budaya keunggulan, standar klinis Aspen tidak akan tertanam; RS akan kembali ke kebiasaan lama begitu tekanan awal berlalu.', 'SAFE_COM': 'Staf yang takut melaporkan = masalah keselamatan yang tidak terlihat sampai menjadi insiden besar. Ini risiko operasional langsung.', 'SAFE_JUST': 'Budaya menyalahkan membuat insiden berulang; setiap insiden yang dipendam adalah insiden berikutnya yang sedang menunggu.', 'SAFE_PRI': 'Reopening dengan budaya keselamatan lemah adalah risiko reputasi dan regulasi yang tidak perlu diambil.', 'CHANGE': 'Staf yang tidak siap perubahan akan sabotas budaya baru dengan cara paling aman: kembali ke kebiasaan lama begitu pintu RS dibuka.'})
MODULE_MAP.update({'V_RESPECT': 'Modul 1: Psychological Safety Foundations (fondasi respect)', 'V_INTEG': 'Modul kepemimpinan: integritas & role modelling pemimpin', 'V_COMP': 'Modul layanan: patient-centred care & empathy', 'V_TEAM': 'Modul 3: Communication for Trust & Inclusion (kolaborasi lintas profesi)', 'V_EXCEL': 'Modul continuous improvement & just culture (Aspen Excellence)', 'SAFE_COM': 'Modul budaya keselamatan: komunikasi terbuka & speaking up', 'SAFE_JUST': 'Modul just culture & pembelajaran dari insiden', 'SAFE_PRI': 'Modul patient safety essentials (pre-reopening wajib)', 'CHANGE': 'Modul manajemen transisi & change communication'})
INSTRUMENT_META.update({'VALUES': {'title': 'Tes 26 - Kesesuaian Nilai Aspen Medical', 'plain': 'Lima nilai inti Aspen - Respect, Integrity, Compassion, Teamwork, Pursuit of Excellence - diukur bukan dari poster di dinding, melainkan dari praktik yang benar-benar dirasakan staf hari ini. Selisih skor terhadap target 80 adalah peta gap budaya: nilai mana yang sudah hidup, mana yang baru di atas kertas. Inilah kristalisasi budaya yang menjadi titik tolak program training.'}, 'SAFETY': {'title': 'Tes 27 - Budaya Keselamatan Pasien', 'plain': 'Keselamatan pasien adalah fondasi klinis Aspen Medical dan syarat mutlak reopening. Instrumen ini (adaptasi dari survei budaya keselamatan pasien AHRQ/HSOPSC yang berdomain publik) membaca tiga hal: apakah staf berani bersuara soal masalah, apakah insiden dipakai untuk belajar dan bukan menghukum, dan apakah keselamatan benar-benar didahulukan saat RS sibuk.'}, 'CHANGE': {'title': 'Tes 28 - Kesiapan Perubahan', 'plain': 'RS ini baru saja berpindah tangan. Program budaya hanya akan tertanam jika staf siap secara mental dan emosional menghadapi perubahan. Tes ini membaca pemahaman arah, kepercayaan pada kepemimpinan, dan kapasitas adaptasi - sehingga program training bisa disusun pada kesiapan yang sesungguhnya, bukan pada asumsi.'}})
