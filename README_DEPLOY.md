
# Asesmen EQ & Emotional Regulation — Cerita Jiwa Training Center

Aplikasi asesmen berbasis **Streamlit + Supabase** untuk training B2B.
Peserta mengisi 64 pertanyaan (6 instrumen, 13 dimensi), lalu bisa mengunduh
laporan PDF individual. Admin bisa mengunduh report agregat per perusahaan
(radar chart, gap analysis, rekomendasi modul) dalam PDF dan Excel.

## Struktur Asesmen (64 item / 13 dimensi)

| Bagian | Instrumen | Item | Dimensi |
|---|---|---|---|
| 1 | PSS-10 (Perceived Stress Scale) | 10 | Stres Persepsian |
| 2 | MBI-GS (Maslach Burnout Inventory - General Survey) | 16 | Exhaustion, Cynicism, Professional Efficacy |
| 3 | WLEIS (Wong & Law Emotional Intelligence Scale) | 16 | SEA, OEA, ROE, UOE |
| 4 | UWES-9 (Utrecht Work Engagement Scale) | 9 | Vigour, Dedication, Absorption |
| 5 | TIS-6 (Turnover Intention Scale) | 6 | Niat Keluar |
| 6 | PSQ-ORG (Psychological Safety - 7 item Edmondson) | 7 | Rasa Aman Psikologis |

Semua skor dinormalisasi 0-100 agar comparable antar instrumen.

## Isi File

- `app.py` — aplikasi utama (3 halaman: Asesmen, Unduh Hasil Saya, Admin)
- `instruments.py` — bank item, skala, metadata dimensi & target
- `scoring.py` — logika skoring & normalisasi
- `insights.py` — kalimat interpretasi + gap analysis + pemetaan modul
- `charts.py` — radar chart, bar chart vs target, breakdown departemen
- `pdf_report.py` — generator PDF individual & report perusahaan
- `supabase_schema.sql` — skema database
- `.streamlit/secrets.toml.example` — template konfigurasi rahasia

## Deploy Langkah demi Langkah

### LANGKAH 1 — Buat project Supabase (gratis)

1. Buka https://supabase.com → **New Project** → isi nama & password database → Create.
2. Tunggu project selesai dibuat (±2 menit).
3. Buka menu **SQL Editor** (kiri) → klik **+ New query**.
4. Buka file `supabase_schema.sql` dari zip ini, salin seluruh isinya, paste ke
   query editor → klik **Run**.
   (Opsional: uncomment baris `insert into public.trainings ...` di bagian bawah
   untuk langsung membuat contoh training Zurich & CERC.)
5. Ambil kredensial: buka **Project Settings → API**:
   - `URL` → ini `SUPABASE_URL`
   - `service_role` key (jangan share ke publik) → ini `SUPABASE_KEY`

### LANGKAH 2 — Isi secrets

1. Rename file `.streamlit/secrets.toml.example` menjadi `.streamlit/secrets.toml`
2. Isi 3 baris:
   - `SUPABASE_URL` = URL dari Langkah 1
   - `SUPABASE_KEY` = service_role key dari Langkah 1
   - `ADMIN_PASSWORD` = password bebas untuk halaman admin (buat yang susah ditebak)

### LANGKAH 3 — Deploy ke Streamlit Community Cloud (gratis)

1. Buat akun di https://share.streamlit.io (bisa login GitHub/Google).
2. Upload folder ini sebagai **repository GitHub pribadi**. JANGAN commit
   `secrets.toml` ke GitHub — secrets diisi lewat dashboard Streamlit (Langkah 4).
3. Di Streamlit Cloud: **Create app** → pilih repo → main file: `app.py` → Deploy.
4. Buka **App settings (⋮) → Secrets** → paste isi `secrets.toml` → Save.
   App akan restart otomatis dan terhubung ke database.
5. Sebarkan link app ke peserta training.

### Deploy lokal (alternatif / untuk tes cepat)

    pip install -r requirements.txt
    streamlit run app.py

## Cara Pakai

**Admin (kamu):**
1. Buka app → menu **🔐 Admin** → masukkan `ADMIN_PASSWORD`.
2. Tab **🏢 Kelola Training** → tambahkan perusahaan/training (mis. "Zurich")
   beserta **kode akses** agar hanya peserta Zurich yang bisa masuk.
3. Tab **📊 Report per Perusahaan** → pilih training → lihat radar rata-rata,
   bar chart vs target, gap analysis, dan prioritas intervensi → download
   **PDF report perusahaan** atau **Excel** (3 sheet: skor individu, data
   responden, gap analysis).
4. Tab **👤 Report per Individu** → pilih responden → lihat/download PDF
   individual (berguna jika peserta kehilangan link).

**Peserta:**
1. Buka link app → **📝 Mulai Asesmen** → pilih perusahaan/training →
   masukkan kode akses (jika ada) → isi data diri → jawab 64 pernyataan → Kirim.
2. Di layar hasil, klik **⬇️ Download Laporan PDF Saya**.
3. Kapan saja bisa kembali lewat **⬇️ Unduh Hasil Saya** (pilih training + email).

## Catatan Penting

1. **MBI-GS & lisensi.** MBI-GS adalah properti Mind Garden, Inc. Gratis untuk
   riset, tetapi penggunaan komersial (training berbayar) secara resmi memerlukan
   lisensi. Alternatif open access dengan validitas sebanding: **OLBI (Oldenburg
   Burnout Inventory, 16 item)**. Untuk menukar: edit `instruments.py`, ganti blok
   instrumen `MBI` dengan item OLBI (Exhaustion 8 item + Disengagement 8 item,
   skala 1-4), sesuaikan `DIMS` dan `insights.py`. Kalau mau, saya buatkan versi
   OLBI-nya — tinggal bilang.
2. **Keamanan.** `SUPABASE_KEY` yang dipakai adalah service_role key. Aplikasi ini
   mengandalkan password admin + kode akses training — cukup untuk skala internal
   training. Jangan pernah commit `secrets.toml` ke GitHub.
3. **Anti duplikat.** Satu email hanya bisa mengisi satu kali per training
   (peserta yang sudah isi diarahkan ke menu "Unduh Hasil Saya").
4. **Reverse scoring** sudah otomatis: PSS item 4,5,6,7,9,10 dan WLEIS item 5,8,14.
5. **Kustomisasi target & pemetaan modul** ada di `instruments.py` (dict `DIMS`
   field `target`) dan `insights.py` (`MODULE_MAP`).

— Dibuat untuk Cerita Jiwa Training Center
