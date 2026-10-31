# Cerita Jiwa Training Center

Platform ujian, asesmen, dan verifikasi sertifikasi untuk Cerita Jiwa.

## Setup 3 Langkah

### STEP 1: GitHub
1. Buka github.com -> New Repository -> Nama: `ceritajiwa-app`
2. Upload semua file ini ke repository
3. Commit & push

### STEP 2: Supabase
1. Buka supabase.com -> New Project -> Nama: `ceritajiwa`
2. Buka SQL Editor -> New query -> paste SQL di bawah -> Run
3. Copy URL & anon key dari Project Settings -> API

```sql
CREATE TABLE profiles (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    nama TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    wa TEXT,
    role TEXT DEFAULT 'peserta',
    password_hash TEXT,
    is_first_login BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE sertifikasi_master (
    id SERIAL PRIMARY KEY,
    kode TEXT UNIQUE NOT NULL,
    nama TEXT NOT NULL,
    harga INTEGER,
    link_mayar TEXT,
    deskripsi TEXT
);

CREATE TABLE peserta_sertifikasi (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES profiles(id),
    sertifikasi_id INTEGER REFERENCES sertifikasi_master(id),
    batch TEXT,
    status TEXT DEFAULT 'pending',
    running_key TEXT UNIQUE,
    tanggal_lulus DATE,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO sertifikasi_master (kode, nama, harga, link_mayar) VALUES
('CERC', 'Certified Emotional Regulation Coach', 5000000, 'https://app.mayar.id/ceritajiwa/cerc'),
('CMBC', 'Certified Money Behavior Coach', 5000000, 'https://app.mayar.id/ceritajiwa/cmbc'),
('CPSC', 'Certified Psychology of Sales Coach', 5000000, 'https://app.mayar.id/ceritajiwa/cpsc'),
('CPPC', 'Certified Positive Parenting Coach', 5000000, 'https://app.mayar.id/ceritajiwa/cppc'),
('CRWC', 'Certified Relationship Wellbeing Coach', 5000000, 'https://app.mayar.id/ceritajiwa/crwc'),
('CCTC', 'Certified Complex Trauma Coach', 5000000, 'https://app.mayar.id/ceritajiwa/cctc');

INSERT INTO profiles (nama, email, role, password_hash, is_first_login) VALUES
('Admin', 'admin@ceritajiwa.id', 'admin', 'admin123', false),
('Trainer', 'trainer@ceritajiwa.id', 'trainer', 'trainer123', false);
```

### STEP 3: Streamlit Cloud
1. Buka share.streamlit.io -> Sign in with GitHub
2. New app -> Pilih repository `ceritajiwa-app`
3. Main file: `app.py`
4. Advanced settings -> Secrets:
```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-key"
```
5. Deploy!

## Login Test
| Role | Email | Password |
|------|-------|----------|
| Admin | admin@ceritajiwa.id | admin123 |
| Trainer | trainer@ceritajiwa.id | trainer123 |
| Peserta | (email apa saja) | 123456 |
