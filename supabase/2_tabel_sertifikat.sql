-- ============================================================
-- Tabel NOMOR SERTIFIKAT (diisi oleh admin)
-- Jalankan SEKALI di Supabase > SQL Editor > New query > Run.
-- Aman dijalankan ulang (tidak menghapus data yang sudah ada).
-- ============================================================
create table if not exists public.certificates (
  id              bigint generated always as identity primary key,
  training_id     uuid not null references public.trainings(id) on delete cascade,
  full_name       text not null,
  email           text,
  package         text,
  cert_no         text,
  issued_date     date,
  notes           text,
  exam_attempt_id bigint,
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now()
);

-- Nomor sertifikat tidak boleh dobel (huruf besar/kecil dianggap sama)
create unique index if not exists uq_certificates_cert_no
  on public.certificates (upper(cert_no)) where cert_no is not null;

create index if not exists idx_certificates_training on public.certificates(training_id);
create index if not exists idx_certificates_email on public.certificates(lower(email));
