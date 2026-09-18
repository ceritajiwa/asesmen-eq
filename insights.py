
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
    return f"{DIM_INFO[dim]} Kondisi Anda saat ini: {INSIGHTS[dim][band(scores[dim])]}"

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
        meta = INSTRUMENT_META[inst["key"]]
        rows = [(DIMS[d]["label"], band(scores[d]), _read(scores, d)) for d in dims_present]
        groups.append((inst["key"], meta["title"], meta["plain"], rows))
    return groups

def gap_analysis(mean_scores):
    """Arah-aware: gap positif = sudah baik/melebihi target; negatif = perlu perhatian."""
    rows = []
    for dim in DIM_ORDER:
        if dim not in mean_scores:
            continue
        d = DIMS[dim]; val = mean_scores[dim]
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
    """Daftar kalimat risiko untuk dimensi yang di bawah target (maks 5)."""
    out = []
    for r in concerns[:5]:
        out.append(f"**{r['label']}** - {RISK[r['dim']]}")
    return out
