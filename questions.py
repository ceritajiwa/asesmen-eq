# -*- coding: utf-8 -*-
"""Bank soal ujian sertifikasi - sistem PAKET (bisa ditambah).
Tiap paket: title, passing (nilai kelulusan), sessions {no: nama}, questions [40 soal].
Format soal: n, session, q, opts (4 opsi A-D), key (0=A,1=B,2=C,3=D).
Untuk menambah paket baru: tambahkan entri baru di EXAM_PACKAGES."""

EXAM_PACKAGES = {
 "CERC": {
  "title": "Ujian Sertifikasi CERC (Emotional Regulation)",
  "passing": 70,
  "sessions": {
   "1": "Sesi 1 - Psychological Safety Foundations",
   "2": "Sesi 2 - Regulasi Emosi & Self-Mastery",
   "3": "Sesi 3 - Komunikasi untuk Kepercayaan",
   "4": "Sesi 4 - Kepemimpinan: Empati & Akuntabilitas"
  },
  "questions": [
   {
    "n": 1,
    "session": 1,
    "q": "Sejak atasan tertawa menanggapi ide seorang anggota di rapat (\"Itu ide tahun 90-an, De\"), anggota itu tidak pernah bicara lagi. Analisis paling tepat tentang situasi ini:",
    "opts": [
     "Humor adalah bumbu tim yang sehat; anggota itu perlu melatih mentalnya",
     "Satu insiden penghukuman kejujuran mengajarkan seluruh tim bahwa bersuara berisiko, jadi mereka memilih aman",
     "Atasan hanya perlu meminta maaf pribadi ke anggota itu, lalu semuanya kembali normal",
     "Anggota itu jelas tidak kompeten; tim sebenarnya lebih baik tanpa suaranya"
    ],
    "key": 1
   },
   {
    "n": 2,
    "session": 1,
    "q": "Supervisor baru ingin cepat membangun rasa aman di timnya. Pendekatan paling efektif 30 hari pertama:",
    "opts": [
     "Umumkan bahwa pintu Anda selalu terbuka, lalu kerjakan tugas Anda sebaik mungkin",
     "Menyelidiki dulu siapa yang bermasalah lewat one-on-one dengan anggota lain",
     "Akui kelemahan Anda sendiri di depan tim, minta masukan perubahan, dan buktikan dengan tindakan nyata",
     "Tunjukkan kompetensi Anda lebih dulu agar tim punya alasan percaya"
    ],
    "key": 2
   },
   {
    "n": 3,
    "session": 1,
    "q": "Atasan menulis di grup: \"Lagi-lagi telat. Kamu ini kerja apa nggak sih?\" Karyawan langsung membalas panjang membela diri. Analisis paling akurat:",
    "opts": [
     "Karyawan salah karena membalas di grup; seharusnya privat",
     "Atasan menyerang identitas (\"kamu ini\"), sehingga isu laporan berubah menjadi pertarungan membela diri",
     "Atasan salah karena tidak mengecek dulu sistem; itu satu-satunya akar masalahnya",
     "Keduanya sama-sama salah dan pantas diberi sanksi ringan yang sama"
    ],
    "key": 1
   },
   {
    "n": 4,
    "session": 1,
    "q": "Tim Anda senang, sering bercanda, tidak pernah konflik - tapi tidak ada yang pernah mengusul perbaikan dan hasil kerja stagnan. Penjelasan paling mungkin:",
    "opts": [
     "Tim sudah sehat; tinggal dinaikkan targetnya agar bergerak",
     "Anggota tidak cukup cerdas untuk berinovasi; perlu rekrutmen baru",
     "Pimpinan perlu lebih tegas karena tim sudah terlalu santai",
     "Ini kehangatan palsu: semua saling menjaga perasaan sehingga tidak ada yang jujur soal masalah"
    ],
    "key": 3
   },
   {
    "n": 5,
    "session": 1,
    "q": "Di rapat, anggota berkata: \"Maaf, ini ide saya, tapi nggak yakin sih, mungkin salah...\" - lalu menjelaskan usulan yang sebenarnya bagus. Respons pemimpin rapat terbaik:",
    "opts": [
     "\"Yakin dong, ide bagus kok!\" agar ia percaya diri berikutnya",
     "Minta ia menuliskan dulu usulannya secara rinci sebelum didiskusikan tim",
     "Tanyakan lebih dalam: \"Bagian mana yang menurutmu paling berisiko? Mari kita bedah bareng.\"",
     "Abaikan keraguannya dan langsung minta tim voting untuk ide itu"
    ],
    "key": 2
   },
   {
    "n": 6,
    "session": 1,
    "q": "Karyawan yang melaporkan kesalahan prosedur justru kena teguran tertulis. Enam bulan kemudian kecelakaan terjadi - persis dari kesalahan yang pernah dilaporkan itu. Pelajaran utamanya:",
    "opts": [
     "Prosedur pelaporan memang rumit dan perlu disederhanakan segera",
     "Perusahaan mendapat perilaku yang ia hukum: melapor dihukum = masalah disembunyikan ke depannya",
     "Karyawan sebaiknya memperbaiki kesalahan prosedur diam-diam tanpa melapor",
     "Ini murni kebetulan; tidak ada hubungan antara budaya dan insiden tersebut"
    ],
    "key": 1
   },
   {
    "n": 7,
    "session": 1,
    "q": "Satu anggota selalu menantang ide di rapat; anggota lain mulai resah. Respons paling tepat:",
    "opts": [
     "Hadapi setelah rapat: suruh ia menyimpan kritiknya untuk urusan internal saja",
     "Beri ruang khusus \"penantang ide\" dengan norma jelas: kritik harus disertai usulan perbaikan",
     "Putuskan untuk tidak menggubris komentarnya di rapat agar tidak membesar",
     "Pindahkan ia ke tim lain; tim yang ada butuh suasana kondusif"
    ],
    "key": 1
   },
   {
    "n": 8,
    "session": 1,
    "q": "Tim Anda baru gagal total di depan klien besar; suasana murung dan ada saling sindir di grup chat. Langkah pertama yang menjaga safety SEKALIGUS memastikan evaluasi tetap terjadi:",
    "opts": [
     "Umumkan \"bukan salah siapa-siapa, yang penting move on\" agar tidak makin down",
     "Adakan evaluasi: bedah sistem dan proses lebih dulu, baru peran individu - dan Anda mengakui bagian Anda pertama kali",
     "Minta tiap anggota menulis surat pernyataan kesalahan masing-masing secara tertib",
     "Tunda evaluasi 2 minggu sampai emosi benar-benar reda"
    ],
    "key": 1
   },
   {
    "n": 9,
    "session": 1,
    "q": "Karyawan baru selalu diam; ditanya pendapat selalu \"ikut yang lain saja\".\" Akar masalah dan cara mengatasi yang paling tepat:",
    "opts": [
     "Ia belum merasa aman untuk salah; beri jalur kontribusi rendah risiko dan rayakan saat ia bersuara",
     "Ia memang tipe pendiam; biarkan, lama-lama terbuka dengan sendirinya",
     "Ia belum kompeten; prioritaskan training keterampilan teknis lebih dulu",
     "Ia tidak cocok dengan budaya tim; pindahkan sebelum terlalu lama"
    ],
    "key": 0
   },
   {
    "n": 10,
    "session": 1,
    "q": "Pernyataan paling tepat tentang psychological safety dan standar tinggi:",
    "opts": [
     "Aman psikologis adalah fondasi standar tinggi: orang berani menag standar jika tidak takut dibenci",
     "Keduanya bertolak belakang - tim yang aman cenderung santai dan sulit ditag",
     "Urutannya: standar tinggi dulu terbukti, baru aman psikologis diberikan sebagai hadiah",
     "Safety penting untuk tim kreatif; tim operasional tidak memerlukannya"
    ],
    "key": 0
   },
   {
    "n": 11,
    "session": 2,
    "q": "Jam 4 sore Anda menerima email kritik personal dari klien; tangan gemuruh ingin membalas. Urutan respons paling sehat:",
    "opts": [
     "Balas segera selagi emosinya masih terasa - itulah kejujuran yang sesungguhnya",
     "Tahan sepenuhnya, jawab dingin dan singkat tanpa membaca ulang - begitulah profesionalisme",
     "Beri jeda: napas panjang, namai emosi (\"ini marah + malu\"), tulis draf, tunda kirim minimal 20 menit",
     "Teruskan ke atasan dan minta beliau yang membalas agar situasi tidak memanas"
    ],
    "key": 2
   },
   {
    "n": 12,
    "session": 2,
    "q": "Karyawan berkata: \"Saya memang emosian dari lahir, susah diubah.\" Respons yang paling sesuai materi self-mastery:",
    "opts": [
     "\"Karakter memang sulit diubah; fokus pilih lingkungan yang tidak memancing emosi saja\"",
     "\"Setiap kali emosi datang, segera tinggalkan ruangan - itu satu-satunya cara aman\"",
     "\"Emosi cepat datang memang benar; tetapi respons kita adalah kebiasaan, dan kebiasaan bisa dilatih pelan-pelan\"",
     "\"Kalau sudah sadar diri emosian, setidaknya Anda bisa minta maaf cepat setelah meledak\""
    ],
    "key": 2
   },
   {
    "n": 13,
    "session": 2,
    "q": "Di tengah presentasi Anda diserang pertanyaan tajam yang terasa menjatuhkan; darah naik ke kepala. Teknik paling realistis saat \"di panggung\":",
    "opts": [
     "Hitung mundur dari 100 di dalam kepala sampai tenang",
     "Angkat suara sedikit agar terlihat dominan dan tidak terintimidasi",
     "Minta jeda ke toilet agar bisa tenang sejenak sebelum melanjutkan",
     "Napas 4 detik masuk - 6 detik keluar, tahan kontak mata, katakan \"pertanyaan bagus, izinkan saya tangkap dulu\""
    ],
    "key": 3
   },
   {
    "n": 14,
    "session": 2,
    "q": "Leader sering berkata \"Saya tidak marah, cuma kecewa\" - padahal tim tahu ia marah besar dan mengambil keputusan kasar. Apa masalah utamanya?",
    "opts": [
     "Timnya saja yang terlalu pandai membaca orang; seharusnya fokus kerjaan",
     "Leader sebaiknya belajar mengontrol ekspresi wajah agar tidak terbaca",
     "Menamai emosi dengan jujur justru mempermalukan; lebih baik disimpan",
     "Emosi yang tidak disadari mengendalikan perilaku lewat jalan belakang; menamai emosi adalah bagian dari regulasi"
    ],
    "key": 3
   },
   {
    "n": 15,
    "session": 2,
    "q": "Setiap kali diminta presentasi, karyawan ini gelisah semalaman dan overthinking. Emosinya: cemas. Strategi paling tepat:",
    "opts": [
     "Tantang pikirannya: \"cemas itu tidak logis, tidak ada yang perlu ditakutkan\"",
     "Semangati: \"kamu pasti bisa! jangan cemas!\" - katakan berulang sampai percaya",
     "Hindari presentasi selama memungkinkan; alihkan tugas presentasi ke rekan",
     "Jadwalkan \"waktu cemas\" 15 menit, tulis kekhawatiran + langkah persiapan, plus napas perut rutin"
    ],
    "key": 3
   },
   {
    "n": 16,
    "session": 2,
    "q": "Kesal pada rekan yang telat menyerahkan bagiannya; keluhan ditahan 2 minggu di kepala sampai akhirnya meledak di grup chat. Di titik mana regulasi emosi sebenarnya gagal?",
    "opts": [
     "Saat meledak di grup chat - seharusnya disampaikan lewat email resmi",
     "Sejak awal: emosi yang tak pernah dinamai dan disalurkan menumpuk jadi gunung berapi; seharusnya diolah lebih awal dan lebih kecil",
     "Sejak rekan itu pertama terlambat - seharusnya langsung dilaporkan ke atasan tanpa basa-basi",
     "Tidak ada yang gagal; ledakan seperti itu justru jujur dan sehat untuk tim"
    ],
    "key": 1
   },
   {
    "n": 17,
    "session": 2,
    "q": "Setelah dihardik klien, karyawan menjadi kaku, tidak bisa menjawab pertanyaan sederhana, \"seperti kosong\".\" Berdasarkan konsep window of tolerance, ia berada di...",
    "opts": [
     "Zona hiper-arousal - perlu ditegur pelan agar kembali sadar dan fokus",
     "Zona hipo-arousal (membeku) - sistem overload; butuh tuntutan diturunkan: napas, air, jeda, kalimat pendek menenangkan",
     "Zona fokus optimal - biarkan ia menyelesaikan responsnya dengan tenang",
     "Zona manipulatif - ia pura-pura kosong untuk menghindari tugas berat"
    ],
    "key": 1
   },
   {
    "n": 18,
    "session": 2,
    "q": "Contoh regulasi emosi yang paling tepat:",
    "opts": [
     "Menyimpan amarah di kantor, melampiaskannya habis-habisan di gym setelah pulang",
     "Mengakui \"saya marah\", pahami pemicunya, lalu pilih waktu dan cara menyampaikannya agar pesan sampai tanpa merusak relasi",
     "Segera alihkan pikiran dengan video lucu sampai amarahnya hilang sendiri",
     "Sadar diri marah, lalu putuskan memaafkan demi kedamaian - biarkan berlalu saja"
    ],
    "key": 1
   },
   {
    "n": 19,
    "session": 2,
    "q": "Anggota tim mudah tersinggung; kata \"perlu perbaikan\" saja membuatnya defensif seminggu. Dari sisi self-mastery, apa yang sebaiknya dilakukan pemimpinnya?",
    "opts": [
     "Sesuaikan standar: hindari mengkritiknya sama sekali, beri apresiasi saja",
     "Hadapi langsung: \"kamu terlalu sensitif, dunia kerja tidak selembut itu\"",
     "Utus rekan yang paling dekat dengannya untuk menyampaikan kritik atas nama tim",
     "Feedback spesifik pada perilaku (bukan identitas), tunjukkan niat baik, beri ruang memproses sebelum merespons"
    ],
    "key": 3
   },
   {
    "n": 20,
    "session": 2,
    "q": "Kenapa menamai emosi dengan presisi (\"kecewa karena diabaikan\", bukan \"nggak enak\") bisa menenangkan diri?",
    "opts": [
     "Agar curhat terdengar lebih runtut dan mudah ditanggapi orang lain",
     "Karena emosi yang diberi nama akan lebih kecil intensitasnya secara otomatis",
     "Menamai mengaktifkan bagian otak yang berpikir dan menurunkan alarm emosional; emosi yang jelas bisa diolah, yang kabut hanya bisa ditanggung",
     "Tidak ada dasar ilmiahnya; itu hanya teknik konseling yang kebetulan populer"
    ],
    "key": 2
   },
   {
    "n": 21,
    "session": 3,
    "q": "Atasan berkata: \"Kamu itu orangnya kurang teliti, ya.\" Penerima murung dan tidak berubah. Versi feedback yang lebih efektif:",
    "opts": [
     "\"Kamu kurang teliti\" - itu faktanya; tidak perlu dibungkus-bungkus",
     "\"Laporan berantakan. Kalau perlu kursus Excel, bilang ya - perusahaan yang tanggung\"",
     "\"Tim sudah banyak komentar soal laporan kamu. Ayo kita perbaiki ke depan, ya\"",
     "\"Di halaman 3 dan 5 ada 4 angka tidak konsisten dengan lampiran. Cek ulang ya sebelum jumat - laporan bulan lalu kamu rapi, bisa diulang\""
    ],
    "key": 3
   },
   {
    "n": 22,
    "session": 3,
    "q": "Satu orang terus memotong pembicaraan di rapat. Teguran asertif yang tepat dari pemimpin rapat:",
    "opts": [
     "\"Pak, mohon jangan memotong, tidak sopan\" - tegas di depan umum agar jera",
     "Biarkan saja; orang seperti itu biasanya sadar diri setelah rapat selesai",
     "\"Poin Anda saya simpan. Saya mau dengar Pak B selesai dulu, lalu kembali ke Anda - catatannya bagus.\"",
     "Sapa ia dengan keras di awal rapat berikutnya agar paham situasinya"
    ],
    "key": 2
   },
   {
    "n": 23,
    "session": 3,
    "q": "Jadwal meeting rutin selalu bertabrakan dengan waktu ibadah salah satu anggota. Dari sisi inklusi, apa yang sebaiknya dilakukan tim?",
    "opts": [
     "Biarkan ia sendiri yang mengajukan perubahan jadwal - inisiatif personal",
     "Terapkan norma default: rotasi jam meeting, rekaman, update async - tanpa menunggu individu bersuara",
     "Tanyakan ke semua anggota dulu apa mereka keberatan jadwalnya diubah",
     "Pertahankan jadwal yang sama demi keadilan - semua orang diperlakukan sama rata"
    ],
    "key": 1
   },
   {
    "n": 24,
    "session": 3,
    "q": "Dua anggota konflik; keduanya datang ke Anda menyalahkan satu sama lain. Pendekatan paling efektif membuka dialog:",
    "opts": [
     "Dengar versi keduanya terpisah, lalu putuskan siapa yang salah secara objektif",
     "Jadikan dirimu perantara: sampaikan pesan dari A ke B dan sebaliknya sampai masalah selesai",
     "Adakan percakapan bersama: masing-masing menyampaikan fakta dan perasaannya (bukan dugaan niat), lalu mengulang versi lawan sampai lawan berkata \"iya, itu maksudku\"",
     "Pindahkan salah satu ke divisi lain - konflik lama biasanya tidak punya jalan keluar"
    ],
    "key": 2
   },
   {
    "n": 25,
    "session": 3,
    "q": "Informasi penting tentang perubahan organisasi hanya beredar lewat kabar angin; muncul kecemasan dan spekulasi. Pelajaran utamanya soal kepercayaan:",
    "opts": [
     "Karyawan memang mudah panik; informasi sensitif memang sebaiknya disembunyikan dulu",
     "Perusahaan perlu menyediakan satu jalur resmi dan membatasi komunikasi informal antar karyawan",
     "Kebenaran yang terlambat kalah dari ketakutan yang berkembang tanpa pengawasan; transparansi proaktif - bahkan soal hal yang belum final - bahan bakar kepercayaan",
     "Ini tugas HR untuk memantau grup-grup karyawan agar hoaks tidak menyebar"
    ],
    "key": 2
   },
   {
    "n": 26,
    "session": 3,
    "q": "Karyawan mengeluh soal beban kerja ke rekan, tidak pernah ke atasannya; ia resign dan atasan baru tahu. Penyebab paling mungkin dan pelajarannya:",
    "opts": [
     "Karyawan tidak profesional; keluhan memang wajib disampaikan ke atasan langsung",
     "Resign adalah keputusan pribadi; organisasi tidak bisa berbuat banyak setelahnya",
     "Alur suara ke atas tidak terasa aman atau tidak terasa berguna; kepercayaan dibangun dari bukti bahwa bersuara menghasilkan perubahan",
     "Atasan terlalu sibuk; karyawan seharusnya menunggu momen yang tepat untuk menyampaikan"
    ],
    "key": 2
   },
   {
    "n": 27,
    "session": 3,
    "q": "Seorang anggota baru bicara setelah rapat lewat chat pribadi. Cara paling inklusif melibatkannya:",
    "opts": [
     "Sapa dia di depan tim: \"Aktif dong di rapat, jangan cuma bisa ngetik!\"",
     "Angkat ia sebagai notulen rapat agar terpaksa memperhatikan semua pembicaraan",
     "Kirimkan agenda jauh hari, minta semua menulis pendapat singkat sebelum rapat, buka dengan ronde 1 menit per orang",
     "Gunakan polling anonim untuk semua keputusan tim agar ia ikut terhitung suaranya"
    ],
    "key": 2
   },
   {
    "n": 28,
    "session": 3,
    "q": "Atasan bilang \"pintu saya selalu terbuka\" - tapi setiap pemberi masukan berujung proyek tambahan atau cap \"kurang loyal\".\"\" Apa yang sebenarnya terjadi?",
    "opts": [
     "Tidak ada masalah; masukan memang harus diverifikasi sebelum ditindaklanjuti",
     "Atasan sebaiknya menjelaskan bahwa masukan wajib disertai solusi, agar tidak menumpuk",
     "Karyawan perlu pelatihan komunikasi asertif agar lebih berani menyampaikan",
     "Komunikasi verbal tidak menentukan kepercayaan; perilaku konsisten menentukan - dan pintu itu kini ditutup karyawan dengan cara paling aman: diam"
    ],
    "key": 3
   },
   {
    "n": 29,
    "session": 3,
    "q": "Tim multigenerasi: junior merasa diabaikan usulnya, senior merasa pengalamannya tidak dihargai. Prinsip inklusi paling tepat:",
    "opts": [
     "Beri giliran bicara berdasarkan usia - senior lebih dulu, lebih teratur",
     "Pisahkan meeting senior dan junior agar masing-masing nyaman berbicara",
     "Akui bahwa perbedaan generasi memang sulit diubah; fokus pada target bersama saja",
     "Norma kontribusi setara: giliran bergantian, usul dinilai dari isi bukan siapa bicara, saling mentoring dua arah"
    ],
    "key": 3
   },
   {
    "n": 30,
    "session": 3,
    "q": "Tanda \"mendengarkan aktif\" yang benar-benar terlihat dari luar:",
    "opts": [
     "Mengangguk-angguk sambil menyiapkan jawaban yang akan disampaikan",
     "Bertanya \"jadi maksud kamu...?\", mengulang inti pesannya, dan bertanya lanjutan yang menunjukkan isinya diproses",
     "Langsung memberikan solusi begitu lawan bicara selesai berbicara",
     "Menyela dengan cerita pengalaman pribadi yang serupa agar terasa empati"
    ],
    "key": 1
   },
   {
    "n": 31,
    "session": 4,
    "q": "Anggota yang biasanya rajin tiba-tiba sering absen dan kinerjanya jatuh; ditanya hanya bilang \"baik-baik saja.\"\"\" Langkah paling tepat:",
    "opts": [
     "Tegur kinerjanya: standar harus dijaga, urusan pribadi jangan dibawa ke kantor",
     "Beri cuti paksa seminggu agar ia punya waktu pulih tanpa tekanan",
     "Kepedulian konkret: \"Saya perhatikan ada perubahan 2 minggu ini. Saya tidak mau menebak, tapi saya siap mendengarkan - dan kita bisa cari cara agar pekerjaan tetap berjalan.\"",
     "Minta kawan-kawannya diam-diam mencari tahu apa yang sebenarnya terjadi"
    ],
    "key": 2
   },
   {
    "n": 32,
    "session": 4,
    "q": "Arti \"empati dengan akuntabilitas\" yang paling tepat:",
    "opts": [
     "Empati untuk masa tenang; akuntabilitas ditegakkan saat evaluasi kinerja - waktunya dibedakan",
     "Utamakan akuntabilitas dulu; empati diberikan setelah target tercapai",
     "Pahami perasaannya sepenuhnya, dan tetap tuntut tanggung jawab pada hasilnya - keduanya bersamaan",
     "Beri empati pada yang berusaha; akuntabilitas hanya untuk yang mengulang kesalahan yang sama"
    ],
    "key": 2
   },
   {
    "n": 33,
    "session": 4,
    "q": "Anggota tim berduka kehilangan orangtua; deadline proyek tinggal 5 hari. Pendekatan terbaik:",
    "opts": [
     "\"Kamu istirahat dulu, semua deadline kita mundur - pekerjaan boleh menunggu\"",
     "\"Saya turut berduka. Mari bedah scope 5 hari ini bersama: mana yang tetap kamu pegang, mana yang saya alihkan sementara, mana yang bisa digeser.\"",
     "\"Saya mengerti kondisimu, tapi klien tidak bisa menunggu. Semangat ya - saya tunggu hasilnya.\"",
     "Alihkan seluruh proyek ke anggota lain tanpa memberitahunya agar tidak menambah beban pikirannya"
    ],
    "key": 1
   },
   {
    "n": 34,
    "session": 4,
    "q": "Ciri akuntabilitas yang sehat:",
    "opts": [
     "Konsekuensi diberikan seadanya sesuai penilaian leader agar terasa manusiawi",
     "Hanya untuk kesalahan besar; kesalahan kecil cukup dimaafkan diam-diam agar tidak tegang",
     "Hukuman di depan umum agar jera dan yang lain ikut terpelajari dari kesalahan rekan",
     "Konsekuensi jelas, konsisten, disepakati sebelumnya; dibicarakan privat; fokus pembelajaran; leader ikut bertanggung jawab bila kegagalan sistemik"
    ],
    "key": 3
   },
   {
    "n": 35,
    "session": 4,
    "q": "Anggota berbakat tapi sarkastik; junior jadi tidak berani bertanya. Laporan datang ke Anda. Tindakan tepat:",
    "opts": [
     "Bela ia di depan tim: \"Itu memang gayanya, tapi hatinya baik - dia paling berprestasi\"",
     "Suruh junior melaporkan lagi bila ada kejadian konkret; tanpa bukti, tidak ada tindakan",
     "Percakapan tegas privat: bedah dampak perilakunya (bukan niatnya), tetapkan ekspektasi perilaku, pantau tindak lanjutnya",
     "Panggil semua pihak bersama-sama dan minta maafan di depan tim agar selesai"
    ],
    "key": 2
   },
   {
    "n": 36,
    "session": 4,
    "q": "Tim gagal target kuartal. Leader berkata: \"Ini salah saya, saya salah targetkan\" - padahal sebagian anggota jelas lalai. Penilaian Anda:",
    "opts": [
     "Tepat - leader memang harus selalu melindungi anggotanya dari tekanan",
     "Keliru - akuntabilitas individu gugur dan leader terlihat lemah di mata tim",
     "Jangan dibahas siapa-siapa; fokus ke perbaikan ke depan agar tidak saling tersinggung",
     "Bedah dua-duanya: leader bertanggung jawab pada bagian strategisnya, anggota tetap ditag bagian eksekusinya"
    ],
    "key": 3
   },
   {
    "n": 37,
    "session": 4,
    "q": "Contoh empati kognitif (memahami perspektif orang lain):",
    "opts": [
     "\"Saya juga pernah merasakan hal yang sama\" - berbagi pengalaman serupa",
     "Memberinya waktu cuti tanpa bertanya lebih lanjut agar tidak merasa diintrogasi",
     "\"Kalau saya jadi kamu, bagian mana yang paling berat dari situasi ini?\" - melihat dari kacamata orang itu, bukan dari pengalaman sendiri",
     "Mengiyakan usulannya agar ia merasa pendapatnya didengar dan dihargai"
    ],
    "key": 2
   },
   {
    "n": 38,
    "session": 4,
    "q": "Leader mulai ritual check-in 10 menit tiap Senin: kondisi 1-10 + satu hal yang menyita pikiran. Dampak terbesar yang diharapkan:",
    "opts": [
     "Membuang waktu produktif - 10 menit dikali jumlah anggota adalah jam kerja yang hilang tiap minggu",
     "Leader jadi tahu terlalu banyak urusan pribadi bawahan dan tidak fokus bisnis",
     "Manfaat hanya terasa di tim yang sedang bermasalah; tim normal tidak perlu",
     "Menormalisasi pembicaraan kondisi manusia: masalah terdeteksi lebih awal, penugasan bisa disesuaikan, kepercayaan tumbuh"
    ],
    "key": 3
   },
   {
    "n": 39,
    "session": 4,
    "q": "Prinsip \"psychological safety dimulai dari perilaku terkecil\" - contoh paling kecil yang paling menentukan:",
    "opts": [
     "Program wellbeing besar-besaran yang digulirkan perusahaan setiap tahun",
     "Reaksi leader saat menerima kabar buruk: \"terima kasih sudah jujur\" atau \"kenapa baru bilang sekarang?\" - 3 detik itu yang dipelajari tim",
     "Survey kepuasan karyawan tahunan yang digalakkan dan ditindaklanjuti HR",
     "Jam kerja fleksibel dan fasilitas kantor yang nyaman untuk semua"
    ],
    "key": 1
   },
   {
    "n": 40,
    "session": 4,
    "q": "Leader ingin mulai membangun budaya \"empati + akuntabilitas\" di tim yang selama ini cuek-beban. Langkah AWAL paling realistis:",
    "opts": [
     "Gulirkan program transformasi budaya 6 bulan dengan trainer eksternal",
     "Kirim seluruh tim ke training emotional intelligence agar punya dasar sama",
     "Mulai dari satu perilaku kecil yang dipegang konsisten 90 hari - misal menutup feedback dengan \"ada yang bisa saya bantu agar lebih mudah?\"",
     "Tunggu momentum baik, saat tim sedang stabil dan tidak ada masalah apa pun"
    ],
    "key": 2
   }
  ]
 },
 "CBT": {
  "title": "Ujian Sertifikasi CBT + Counseling",
  "passing": 70,
  "sessions": {
   "1": "Sesi 1 - Foundations of CBT & Counseling",
   "2": "Sesi 2 - The Cognitive Model & Thought Records",
   "3": "Sesi 3 - Emotional Regulation & Window of Tolerance",
   "4": "Sesi 4 - Behavioral Activation & Exposure Therapy",
   "5": "Sesi 5 - Socratic Questioning & Cognitive Restructuring",
   "6": "Sesi 6 - Core Beliefs & Schema Therapy",
   "7": "Sesi 7 - Counseling Microskills in Practice",
   "8": "Sesi 8 - Integration, Case Formulation & Treatment Planning"
  },
  "questions": [
   {
    "n": 1,
    "session": 1,
    "q": "Klien perempuan, 35 tahun, datang dengan keluhan sering menangis setelah keguguran. Dia bilang 'Saya tidak tahu kenapa saya sedih, seharusnya saya sudah move on'. Sebagai konselor, respons awal Anda adalah...",
    "opts": [
     "Langsung memberikan psychoeducation tentang grief dan normalisasi sedih",
     "Menggunakan SOLER, primary empathy, dan validasi: 'Saya dengar, keguguran adalah kehilangan. Sedih itu wajar'",
     "Langsung membuat treatment plan dengan SMART goals untuk mengatasi sedih",
     "Menyarankan klien untuk fokus pada hal positif dan bersyukur"
    ],
    "key": 1
   },
   {
    "n": 2,
    "session": 1,
    "q": "Klien remaja laki-laki, 17 tahun, datang karena dipaksa orang tuanya. Dia duduk dengan tangan bersilang, jawaban singkat, dan sering melihat jam. Microskills apa yang paling penting untuk dilakukan konselor di situasi ini?",
    "opts": [
     "Langsung bertanya 'Apa masalah yang Anda hadapi?' dengan nada tegas",
     "Menggunakan open posture, eye contact, dan minimal encouragers tanpa memaksa klien bicara",
     "Memberikan advice tentang pentingnya komunikasi dengan orang tua",
     "Mengakhiri sesi lebih awal karena klien tidak kooperatif"
    ],
    "key": 1
   },
   {
    "n": 3,
    "session": 1,
    "q": "Klien mengatakan 'Saya merasa hidup saya tidak ada gunanya'. Konselor merespons 'Saya mengerti perasaanmu, dan saya di sini untuk mendengarkan'. Ini adalah contoh dari...",
    "opts": [
     "Reassurance yang efektif",
     "Primary empathy yang akurat",
     "Advanced empathy yang mendalam",
     "Confrontation yang efektif"
    ],
    "key": 1
   },
   {
    "n": 4,
    "session": 1,
    "q": "Klien datang dengan masalah kecemasan berat. Konselor menanyakan riwayat trauma masa kecil dan membuat jadwal exposure. Namun klien belum merasa aman dengan konselor. Apa yang kurang?",
    "opts": [
     "Konselor belum melakukan assessment yang cukup",
     "Therapeutic alliance belum terbentuk dengan baik",
     "Konselor belum melakukan cognitive restructuring",
     "Konselor belum melakukan behavioral activation"
    ],
    "key": 1
   },
   {
    "n": 5,
    "session": 1,
    "q": "Konselor sedang menerapkan SOLER. Bagian mana yang menunjukkan 'Anda punya perhatian penuh saya'?",
    "opts": [
     "Sit squarely",
     "Open posture",
     "Lean slightly forward",
     "Relax"
    ],
    "key": 0
   },
   {
    "n": 6,
    "session": 2,
    "q": "Klien bilang 'Saya gagal total sebagai anak karena tidak bisa kirim uang ke orang tua setiap bulan'. Cognitive distortion apa yang dominan?",
    "opts": [
     "Mind Reading",
     "All-or-Nothing Thinking",
     "Overgeneralization",
     "Personalization"
    ],
    "key": 1
   },
   {
    "n": 7,
    "session": 2,
    "q": "Konselor membantu klien mengisi Thought Record. Di kolom 'Evidence Against', klien tidak bisa menemukan apa pun. Konselor sebaiknya...",
    "opts": [
     "Memberikan contoh evidence dari pengalaman klien lain",
     "Menggunakan Socratic questioning untuk mengeksplorasi evidence perlahan",
     "Mengisi kolom evidence against untuk klien",
     "Mengatakan bahwa evidence against tidak penting jika klien yakin"
    ],
    "key": 1
   },
   {
    "n": 8,
    "session": 2,
    "q": "Klien panic attack setiap kali naik lift. Pikiran otomatisnya 'Saya akan mati di lift'. Distortion apa ini?",
    "opts": [
     "Fortune Telling",
     "Catastrophizing",
     "Mind Reading",
     "Emotional Reasoning"
    ],
    "key": 1
   },
   {
    "n": 9,
    "session": 2,
    "q": "Setelah mengisi Thought Record, emosi klien turun dari 90% ke 40%. Konselor kemudian bilang 'Bagus, sekarang Anda sudah tidak sedih lagi'. Respons konselor ini...",
    "opts": [
     "Memperkuat kemajuan klien dengan positif",
     "Kurang tepat karena invalidasi proses emosi dan memaksa klien 'move on'",
     "Memotivasi klien untuk terus menggunakan Thought Record",
     "Menunjukkan bahwa Thought Record selalu efektif"
    ],
    "key": 1
   },
   {
    "n": 10,
    "session": 2,
    "q": "Klien bilang 'Saya harus sempurna di segala hal, kalau tidak saya tidak berharga'. Distortion dan kemungkinan schema apa?",
    "opts": [
     "Catastrophizing dan Abandonment schema",
     "Should Statements dan Unrelenting Standards schema",
     "Emotional Reasoning dan Defectiveness schema",
     "All-or-Nothing dan Approval-Seeking schema"
    ],
    "key": 1
   },
   {
    "n": 11,
    "session": 3,
    "q": "Klien tiba-tiba sesak napas dan gemetar saat sesi. Konselor melihat klien pucat dan tidak fokus. Langkah pertama konselor adalah...",
    "opts": [
     "Langsung melakukan psychoeducation tentang panic attack",
     "Menggunakan grounding technique (box breathing / 5-4-3-2-1) untuk menurunkan arousal",
     "Menghentikan sesi dan merujuk ke dokter untuk obat penenang",
     "Mengabaikan gejala fisik dan melanjutkan sesi seperti biasa"
    ],
    "key": 1
   },
   {
    "n": 12,
    "session": 3,
    "q": "Klien marah-marah menuduh konselor 'Anda tidak mengerti saya!'. Konselor merasa ingin defend diri. Berdasarkan STOP technique, langkah konselor adalah...",
    "opts": [
     "Stop — jangan bereaksi, Take a breath, lalu respon dengan validasi",
     "Stop — jelaskan ke klien bahwa konselor juga manusia",
     "Stop — langsung problem-solve dengan memberi solusi konkret",
     "Stop — langsung defend diri dengan menjelaskan niat baik konselor"
    ],
    "key": 1
   },
   {
    "n": 13,
    "session": 3,
    "q": "Klien berkata 'Saya tidak apa-apa, saya biasa saja' sambil menangis. Konselor merespons 'Saya lihat Anda menangis. Saya di sini'. Ini menunjukkan...",
    "opts": [
     "Invalidasi emosi klien",
     "Co-regulation dan validasi non-verbal",
     "Confrontation yang efektif",
     "Reassurance yang membuat klien merasa lebih baik"
    ],
    "key": 1
   },
   {
    "n": 14,
    "session": 3,
    "q": "Klien anak 8 tahun trauma kecelakaan, sering mimpi buruk dan tidak mau tidur sendiri. Orang tua bilang 'Dia cuma cari perhatian'. Pendekatan konselor yang tepat adalah...",
    "opts": [
     "Mengabaikan komentar orang tua dan fokus pada anak dengan play therapy",
     "Mengedukasi orang tua tentang trauma dan melibatkan mereka dalam treatment",
     "Menggunakan exposure therapy langsung pada anak",
     "Mengatakan pada orang tua bahwa anak mereka manipulatif"
    ],
    "key": 1
   },
   {
    "n": 15,
    "session": 3,
    "q": "Konselor sedang co-regulate dengan klien yang panik. Konselor menggunakan suara pelan dan napas teratur. Mekanisme apa yang terjadi pada sistem saraf klien?",
    "opts": [
     "Amygdala klien semakin aktif karena merasa diancam",
     "Sistem saraf parasimpatik klien mulai aktif karena merasa aman",
     "Kortisol klien naik karena merasa di-interogasi",
     "Adrenalin klien turun karena konselor menunjukkan otoritas"
    ],
    "key": 1
   },
   {
    "n": 16,
    "session": 4,
    "q": "Klien depresi, 3 bulan tidak keluar kamar kecuali ke kamar mandi. Konselor menyarankan 'Coba keluar rumah setiap hari'. Saran ini...",
    "opts": [
     "Tepat karena klien butuh dorongan untuk keluar dari avoidance",
     "Kurang tepat karena terlalu besar langkahnya untuk klien yang depresi berat",
     "Tepat karena behavioral activation harus dimulai secepatnya",
     "Kurang tepat karena klien butuh medication dulu"
    ],
    "key": 1
   },
   {
    "n": 17,
    "session": 4,
    "q": "Klien takut kucing sejak kecil. Konselor membuat exposure ladder. Rung pertama yang paling tepat adalah...",
    "opts": [
     "Memegang kucing langsung selama 5 menit",
     "Melihat foto kucing di HP selama 1 menit",
     "Melihat kucing dari jendela rumah",
     "Membeli kucing peliharaan untuk dibawa pulang"
    ],
    "key": 1
   },
   {
    "n": 18,
    "session": 4,
    "q": "Klien bilang 'Kalau saya coba ngomong di depan umum, orang pasti ketawa'. Konselor meminta klien untuk benar-benar mencoba sekali dan mencatat apa yang terjadi. Ini adalah...",
    "opts": [
     "Cognitive Restructuring",
     "Behavioral Experiment",
     "Graded Exposure",
     "Behavioral Activation"
    ],
    "key": 1
   },
   {
    "n": 19,
    "session": 4,
    "q": "Klien depresi, tidak punya energi. Konselor membuat jadwal aktivitas harian yang mencakup masak, jalan-jalan, dan main musik. Aktivitas main musik termasuk...",
    "opts": [
     "Mastery activity",
     "Pleasure activity",
     "Values-aligned activity",
     "Mastery dan Pleasure activity"
    ],
    "key": 1
   },
   {
    "n": 20,
    "session": 4,
    "q": "Klien avoidance tinggi. Konselor meminta klien untuk langsung menghadapi ketakutan terbesarnya. Pendekatan ini...",
    "opts": [
     "Tepat karena menghadapi ketakutan langsung adalah exposure yang efektif",
     "Kurang tepat karena bisa traumatis dan memperkuat avoidance",
     "Tepat karena avoidance harus dihancurkan segera",
     "Kurang tepat karena tidak sesuai dengan graduated exposure"
    ],
    "key": 1
   },
   {
    "n": 21,
    "session": 5,
    "q": "Klien bilang 'Saya tidak bisa apa-apa'. Konselor bertanya 'Apa bukti yang mendukung pikiran itu? Apa bukti yang menentang?'. Ini adalah...",
    "opts": [
     "Clarification",
     "Evidence & Reason",
     "Assumption Probing",
     "Alternative Perspective"
    ],
    "key": 1
   },
   {
    "n": 22,
    "session": 5,
    "q": "Klien bilang 'Saya yakin suami saya selingkuh karena dia pulang malam'. Konselor bertanya 'Apa yang sebenarnya Anda lihat dan dengar? Bukan interpretasi Anda'. Ini adalah...",
    "opts": [
     "Assumption Probing",
     "Observation dalam NVC",
     "Clarification",
     "Reframe"
    ],
    "key": 1
   },
   {
    "n": 23,
    "session": 5,
    "q": "Konselor menggunakan Downward Arrow. Klien mulai dari 'Saya gagal ujian' → 'Saya bodoh' → 'Saya tidak akan pernah sukses' → 'Saya tidak berharga hidup'. Level terakhir ini adalah...",
    "opts": [
     "Pikiran otomatis",
     "Core belief",
     "Intermediate belief",
     "Automatic thought"
    ],
    "key": 1
   },
   {
    "n": 24,
    "session": 5,
    "q": "Klien bilang 'Saya benci diri saya'. Konselor merespons 'Saya dengar Anda sangat marah pada diri sendiri. Boleh ceritakan kapan perasaan ini mulai?'. Respons ini...",
    "opts": [
     "Mengabaikan perasaan klien dan mengalihkan topik",
     "Validasi emosi sebelum mengeksplorasi lebih dalam",
     "Reframe yang mengubah pikiran negatif jadi positif",
     "Menggunakan Downward Arrow untuk menembus lebih dalam"
    ],
    "key": 1
   },
   {
    "n": 25,
    "session": 5,
    "q": "Klien bilang 'Saya selalu tidak beruntung dalam cinta'. Konselor bertanya 'Kalau sahabat Anda bilang hal yang sama, apa yang akan Anda katakan?'. Tujuan pertanyaan ini adalah...",
    "opts": [
     "Mengoreksi pikiran irasional klien",
     "Menggunakan Alternative Perspective untuk guided discovery",
     "Menggunakan Implication untuk menakut-nakuti klien",
     "Menggunakan Clarification untuk memperjelas masalah"
    ],
    "key": 1
   },
   {
    "n": 26,
    "session": 6,
    "q": "Klien selalu memilih pasangan yang 'toxic' dan tidak bisa meninggalkan meski disakiti. Schema yang paling mungkin adalah...",
    "opts": [
     "Failure schema",
     "Abandonment schema",
     "Entitlement schema",
     "Social Isolation schema"
    ],
    "key": 1
   },
   {
    "n": 27,
    "session": 6,
    "q": "Klien perfectionist, tidak pernah puas dengan hasil kerjanya, overworking sampai sakit. Konselor bilang 'Perfectionism ini pernah melindungi kamu, tapi sekarang membakar kamu'. Ini adalah...",
    "opts": [
     "Shaming yang memotivasi klien untuk berubah",
     "Compassionate reframe yang memvalidasi masa lalu",
     "Direct advice untuk klien supaya tidak perfectionist",
     "Schema therapy yang menghilangkan perfectionism total"
    ],
    "key": 1
   },
   {
    "n": 28,
    "session": 6,
    "q": "Klien dengan abandonment schema, pasangan tidak balas chat 30 menit, klien panik dan kirim 20 pesan. Coping style ini adalah...",
    "opts": [
     "Surrender",
     "Overcompensation",
     "Avoidance",
     "Surrender"
    ],
    "key": 1
   },
   {
    "n": 29,
    "session": 6,
    "q": "Konselor menggunakan chair work dengan klien. Klien berdialog dengan 'bagian kecilnya yang takut'. Teknik ini bertujuan untuk...",
    "opts": [
     "Mengganti schema lama dengan schema baru",
     "Memperkuat Healthy Adult mode dan memberi voice pada vulnerable child",
     "Menghilangkan vulnerable child mode",
     "Mengganti coping style dengan yang baru"
    ],
    "key": 1
   },
   {
    "n": 30,
    "session": 6,
    "q": "Klien bilang 'Saya tidak peduli' sambil menangis. Konselor mendeteksi detached protector mode. Respons konselor yang tepat adalah...",
    "opts": [
     "Mengabaikan penyangkalan dan fokus pada masalah lain",
     "Menyebutkan mode yang terdeteksi dengan lembut dan mengajak klien eksplorasi",
     "Mendorong klien untuk 'kuat' dan tidak menangis",
     "Mengabaikan detached protector dan fokus pada cognitive restructuring"
    ],
    "key": 1
   },
   {
    "n": 31,
    "session": 7,
    "q": "Klien bercerita tentang masa kecil yang sulit. Konselor duduk dengan tangan bersilang, sering melihat HP, dan bilang 'Saya mengerti'. Klien merasa tidak didengar. Masalahnya adalah...",
    "opts": [
     "Klien terlalu sensitif dan tidak menghargai waktu konselor",
     "Attending behavior konselor tidak konsisten dengan verbal following",
     "Konselor menggunakan microskills dengan baik tapi klien resisten",
     "Klien tidak cocok dengan pendekatan CBT dan perlu rujukan"
    ],
    "key": 1
   },
   {
    "n": 32,
    "session": 7,
    "q": "Klien bilang 'Saya baik-baik saja' dengan suara gemetar dan mata berkaca-kaca. Konselor merespons 'Saya notice suara Anda gemetar. Saya penasaran apa yang sebenarnya Anda rasakan'. Ini adalah...",
    "opts": [
     "Paraphrasing yang efektif",
     "Reflection of feeling yang mendalam",
     "Immediacy yang menantang klien",
     "Advice giving yang membantu klien menyadari perasaannya"
    ],
    "key": 1
   },
   {
    "n": 33,
    "session": 7,
    "q": "Klien sering cerita tentang masalah yang sama tanpa ada perubahan. Konselor bilang 'Saya notice kita sering kembali ke topik ini. Saya penasaran — apa yang membuat perubahan sulit untuk Anda?'. Ini adalah...",
    "opts": [
     "Confrontation yang agresif",
     "Immediacy yang mengajak klien melihat pola di sini dan sekarang",
     "Summarizing yang mengulang masalah klien",
     "Paraphrasing yang mengulang cerita klien"
    ],
    "key": 1
   },
   {
    "n": 34,
    "session": 7,
    "q": "Klien bilang 'Saya tidak butuh bantuan, saya cuma datang karena dipaksa'. Konselor merespons 'Saya dengar Anda tidak merasa butuh bantuan. Boleh saya tanya — apa yang sebenarnya Anda harapkan dari datang ke sini?'. Teknik ini menunjukkan...",
    "opts": [
     "Reassurance yang membangun rapport",
     "Confrontation yang mempertanyakan motivasi klien",
     "Empathy yang membangun rapport awal",
     "Active listening yang membuat klien merasa dipaksa"
    ],
    "key": 1
   },
   {
    "n": 35,
    "session": 7,
    "q": "Klien menuduh konselor 'Anda hanya ingin uang saya!'. Konselor tetap tenang dan berkata 'Saya dengar Anda merasa tidak dihargai. Boleh ceritakan lebih lanjut?'. Ini menunjukkan...",
    "opts": [
     "Konselor defensive dan menyerang balik",
     "Self-regulation dan co-regulation yang efektif",
     "Confrontation yang membuat klien sadar kesalahannya",
     "Avoidance dari konflik dengan klien"
    ],
    "key": 1
   },
   {
    "n": 36,
    "session": 8,
    "q": "Klien datang dengan keluhan anxiety, riwayat bullying di SMP, baru saja pindah kerja. Dalam case formulation 5P, pindah kerja termasuk...",
    "opts": [
     "Predisposing factor",
     "Precipitating factor",
     "Perpetuating factor",
     "Protective factor"
    ],
    "key": 1
   },
   {
    "n": 37,
    "session": 8,
    "q": "Treatment plan untuk klien depresi: 'Klien akan merasa lebih baik dalam 2 minggu'. Goal ini kurang tepat karena...",
    "opts": [
     "Tidak spesifik dan tidak measurable",
     "Tidak realistis karena depresi butuh waktu lebih lama",
     "Tidak achievable karena tidak ada homework",
     "Tidak time-bound karena tidak ada deadline"
    ],
    "key": 0
   },
   {
    "n": 38,
    "session": 8,
    "q": "Klien sudah 10 sesi, anxiety turun drastis, bisa menggunakan coping skills mandiri. Konselor menyarankan 2 sesi lagi lalu stop. Ini menunjukkan...",
    "opts": [
     "Termination yang terlalu cepat",
     "Proses termination yang terencana dengan relapse prevention",
     "Assessment ulang karena kemajuan terlalu cepat",
     "Termination yang terlalu lambat dan membuat klien bergantung"
    ],
    "key": 1
   },
   {
    "n": 39,
    "session": 8,
    "q": "Konselor merasa burnout, sering lupa janji dengan klien, dan mulai menyalahkan klien. Tindakan paling penting yang harus dilakukan konselor adalah...",
    "opts": [
     "Mengambil cuti dari praktik sejenak dan mencari supervision",
     "Meneruskan praktik sambil berusaha lebih keras mengatur jadwal",
     "Mengurangi jumlah klien dan menambah jam kerja",
     "Mencari peer supervision dan menjaga self-care routine"
    ],
    "key": 0
   },
   {
    "n": 40,
    "session": 8,
    "q": "Klien dengan social anxiety sudah bisa ngomong di depan 5 orang tanpa panic. Treatment plan berikutnya yang paling tepat adalah...",
    "opts": [
     "Mengakhiri terapi karena goal sudah tercapai",
     "Graduated exposure: naik ke 10 orang dengan booster session",
     "Mengubah treatment plan ke schema therapy",
     "Mengulang exposure ke 5 orang untuk memperkuat hasil"
    ],
    "key": 1
   }
  ]
 }
}

PASSING_SCORE = 70  # default; tiap paket punya 'passing' sendiri
