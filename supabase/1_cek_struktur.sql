-- Jalankan di Supabase > SQL Editor, lalu Export hasilnya ke CSV.
-- Tidak mengubah data apa pun (hanya membaca struktur).

-- A. Semua tabel & kolom
select table_name, column_name, data_type, is_nullable, column_default
from information_schema.columns
where table_schema = 'public'
order by table_name, ordinal_position;

-- B. Status RLS tiap tabel
-- select tablename, rowsecurity from pg_tables where schemaname = 'public';

-- C. Policy RLS
-- select tablename, policyname, cmd, roles, qual, with_check from pg_policies where schemaname = 'public';
