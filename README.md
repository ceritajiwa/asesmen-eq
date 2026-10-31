# Cerita Jiwa Training Center (Asesmen EQ)

Aplikasi Streamlit + Supabase untuk asesmen, ujian sertifikasi, sertifikat, dan catatan sesi BEI.

## Struktur

```
app.py              # entrypoint + daftar menu (st.navigation)
views/              # halaman: beranda, asesmen, training, ujian, sertifikat, verifikasi, admin, trainer
cjlib/              # kode bersama: db (Supabase), ui (form kode akses), hasil (tampilan hasil asesmen),
                    #   pdf (sertifikat & badge), auth, styles
instruments.py      # BANK ITEM ASESMEN (PSS, MBI, WLEIS, UWES, TIS, PSQ, BFI, dst.)
questions.py        # BANK SOAL UJIAN per paket (CERC, CBT, ...)
scoring.py          # skoring 0-100 per dimensi
insights.py, hr_analytics.py, charts.py, pdf_report.py   # interpretasi, analitik HR, grafik, PDF laporan
bei.py              # sesi konseling BEI + strukturisasi AI (Gemini / Groq)
```

Folder `pages/` dan `utils/` versi lama sudah tidak dipakai. **Hapus dari GitHub** kalau masih ada.

## Menu

| Menu | Akses | Isi |
|---|---|---|
| 🏠 Beranda | Publik | Menu utama |
| 📝 Asesmen | Pilih training (+ kode akses bila ada) → nama & email | Semua instrumen yang dipilih admin, satu halaman |
| 🎓 Training | sama | Info training |
| 📋 Ujian | sama | Paket ujian 40 soal, satu halaman, review jawaban, ulangi soal salah |
| 📜 Sertifikat | sama | Sertifikat PDF, badge, riwayat ujian, report asesmen |
| 🔍 Cek Sertifikasi | Publik | Cari nama / nomor sertifikat |
| ⚙️ Admin | Password admin | Report perusahaan & individu, kelola training, nomor sertifikat, data dummy, riwayat ujian |
| 👨‍🏫 Trainer / BEI | Password trainer | Catatan sesi konseling + AI |

Kode akses: kalau `access_code` sebuah training dikosongkan, training itu publik (tanpa kode).

## Secrets (Streamlit Cloud > Manage app > Settings > Secrets)

```toml
SUPABASE_URL = "https://xxxx.supabase.co"
SUPABASE_KEY = "..."
ADMIN_PASSWORD = "..."
TRAINER_PASSWORD = "..."   # kalau kosong, pakai ADMIN_PASSWORD
GEMINI_API_KEY = "..."
GROQ_API_KEY = "..."
```

Jangan tulis password atau key di file mana pun di repo, karena repo ini publik.

## Nomor sertifikat

Nomor sertifikat diberikan admin di Admin > Nomor Sertifikat (edit langsung di tabel, isi otomatis berurutan,
atau import dari CSV/Excel daftar cetak). Butuh tabel `certificates`: jalankan `supabase/2_tabel_sertifikat.sql`
sekali di Supabase SQL Editor. Peserta baru bisa mengunduh sertifikat dan badge setelah nomornya diisi admin.
Desain sertifikat ada di `assets/sertifikat_template.png` (ganti file ini kalau desain berubah).
