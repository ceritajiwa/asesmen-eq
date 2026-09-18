-- ===== Skema Database Asesmen EQ (jalankan di SQL Editor Supabase) =====

create table if not exists public.trainings (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  access_code text,
  enabled_instruments text default '["PSS","MBI","WLEIS","UWES","TIS","PSQ"]',
  created_at timestamptz not null default now()
);

-- >>> JIKA DATABASE LAMA (sudah punya tabel trainings), jalankan 2 baris ini saja: <<<
alter table public.trainings add column if not exists enabled_instruments text;
update public.trainings set enabled_instruments = '["PSS","MBI","WLEIS","UWES","TIS","PSQ"]' where enabled_instruments is null;

create table if not exists public.respondents (
  id uuid primary key default gen_random_uuid(),
  training_id uuid not null references public.trainings(id) on delete cascade,
  full_name text not null,
  email text not null,
  department text,
  job_level text,
  created_at timestamptz not null default now()
);

create table if not exists public.responses (
  id bigint generated always as identity primary key,
  respondent_id uuid not null references public.respondents(id) on delete cascade,
  instrument text not null,
  item_n int not null,
  score int not null
);

create index if not exists idx_responses_resp on public.responses(respondent_id);
create index if not exists idx_resp_training on public.respondents(training_id);
create index if not exists idx_resp_email on public.respondents(email);

-- ===== Contoh data (opsional) =====
-- insert into public.trainings (name, access_code) values ('Zurich', 'ZURICH2026'), ('CERC', 'CERC2026');

-- ===== Tabel riwayat ujian sertifikasi (jalankan SEKALI di SQL Editor) =====
create table if not exists public.exam_attempts (
  id bigint generated always as identity primary key,
  training_id uuid not null references public.trainings(id) on delete cascade,
  full_name text not null,
  email text not null,
  correct int not null,
  score int not null,
  passed boolean not null,
  created_at timestamptz not null default now()
);
create index if not exists idx_exam_training on public.exam_attempts(training_id);
