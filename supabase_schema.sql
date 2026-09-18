-- ===== Skema Database Asesmen EQ (jalankan di SQL Editor Supabase) =====

create table if not exists public.trainings (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  access_code text,
  created_at timestamptz not null default now()
);

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
