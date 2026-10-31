# Cerita Jiwa Training Center

Aplikasi Streamlit untuk asesmen, training, ujian, dan sertifikat Cerita Jiwa.

## Struktur

```
app.py                  # entrypoint + daftar menu (st.navigation)
views/                  # isi tiap halaman
cjlib/db.py             # semua akses ke Supabase
cjlib/konten.py         # BANK SOAL asesmen & ujian (isi soal asli di sini)
cjlib/pdf.py            # pembuat PDF laporan, sertifikat, dan badge
cjlib/ui.py                # form kode akses + data peserta (dipakai 4 halaman peserta)
cjlib/auth.py           # session & cek password
cjlib/styles.py         # tampilan (warna brand, font, komponen)
supabase/               # query bantu untuk cek struktur database
```

> Folder `pages/` versi lama **dihapus**. Kalau masih ada di GitHub, hapus saja; aplikasi sudah tidak memakainya.

## Menu & Akses

| Menu | Cara Akses |
|------|-----------|
| 🏠 Beranda | Bebas |
| 📝 Asesmen | Pilih Training → Kode Akses Training → Nama & Email |
| 🎓 Training | Pilih Training → Kode Akses Training → Nama & Email |
| 📋 Ujian | Pilih Training → Kode Akses Training → Nama & Email |
| 📜 Sertifikat | Pilih Training → Kode Akses Training → Nama & Email |
| 🔍 Cek Sertifikasi | Publik |
| ⚙️ Admin | Password Admin |
| 👨‍🏫 Trainer / BEI | Password Trainer |

## Database (Supabase, schema `public`)

| Tabel | Dipakai untuk |
|---|---|
| `trainings` | Daftar training & kode akses (`name`, `access_code`) |
| `respondents` | Data peserta yang mengisi asesmen |
| `exam_attempts` | Hasil ujian, status lulus, nomor sertifikat (CERC-2026-<id>) |
| `responses` | Jawaban asesmen (per item) |
| `bei_sessions` | Belum dipakai di versi ini |

Aturan kode akses:
- Training **dibuka** kalau `access_code` terisi, **ditutup** kalau kosong.
- Huruf besar/kecil dan spasi di awal/akhir kode diabaikan saat peserta mengetik.
- Admin bisa membuat training baru, membuat ulang kode, atau menutup akses dari menu Admin.

## Secrets (Streamlit Cloud > Manage app > Settings > Secrets)

Isi di Streamlit Cloud, **jangan** ditulis di repo:

```toml
SUPABASE_URL = "https://xxxx.supabase.co"
SUPABASE_KEY = "..."
ADMIN_PASSWORD = "..."
TRAINER_PASSWORD = "..."   # kalau kosong, pakai ADMIN_PASSWORD
GEMINI_API_KEY = "..."
GROQ_API_KEY = "..."
```
