-- ============================================================
-- ASPENCULTURE: DATA DUMMY REALISTIS 50 ORANG (v2)
-- Tiap orang punya kombinasi dimensi kuat/lemah yang BERBEDA ->
-- ada cluster hijau-kuning-oranye-MERAH, gap merah muncul, kategori
-- konseling+coaching ikut terisi. Hapus dulu SEMUA data AspenCulture.
-- ============================================================

-- 0) Hapus SEMUA responden AspenCulture (isi saat ini memang hanya dummy)
delete from public.respondents
where training_id = (select id from public.trainings where name = 'AspenCulture');

-- 1) 50 responden
insert into public.respondents (training_id, full_name, email, department, job_level)
select t.id,
       fn.first_name || ' ' || fn.last_name,
       lower(fn.first_name || fn.last_name) || lpad(g.n::text, 2, '0') || '@dummy.id',
       (array['Perawat','Dokter','Farmasi','Administrasi','Laboratorium','Radiologi'])[1 + (g.n % 6)],
       (array['Individual Contributor / Staff','Supervisor / Team Lead','Manager ke atas'])[1 + (g.n % 3)]
from public.trainings t
cross join generate_series(1, 50) as g(n)
cross join lateral (
    select (array[
        'Ahmad','Siti','Budi','Dewi','Agus','Rina','Eko','Fitri','Hendra','Wulan',
        'Indra','Maya','Joko','Sari','Rizky','Putri','Andre','Intan','Fajar','Nadia',
        'Bagus','Laras','Dimas','Ratna','Galih','Vina','Yoga','Tania','Arif','Salsa',
        'Bima','Ayu','Farhan','Rani','Ilham','Dini','Reza','Melati','Taufik','Kirana'
    ])[1 + (g.n % 40)] as first_name,
    (array[
        'Saputra','Wulandari','Pratama','Kusuma','Setiawan','Lestari','Nugroho','Anggraini',
        'Hidayat','Sari','Wibowo','Putri','Santoso','Rahayu','Gunawan','Dewanti',
        'Ramadhan','Puspita','Firmansyah','Kartika','Alamsyah','Maharani','Prasetyo','Utami',
        'Hermawan','Wijayanti','Kurniawan','Safitri','Ariyanto','Ningsih','Susanto','Puspitasari'
    ])[1 + ((g.n * 7) % 32)] as last_name
) fn
where t.name = 'AspenCulture';

-- 2) Jawaban 66/orang. Pola: tiap dimensi dinilai kuat atau lemah PER ORANG
--    (lewat hash deterministik). Dimensi lemah -> skor 15-50%; kuat -> 55-95%.
--    Variasi item -> rentang lebar, mirip data manusia asli.
with resp as (
    select r.id
    from public.respondents r
    where r.training_id = (select id from public.trainings where name = 'AspenCulture')
),
items as (
    select 'VALUES' as instrument, gs as item_n,
           case when gs in (1,2) then 'V_RESPECT' when gs in (3,4) then 'V_INTEG'
                when gs in (5,6) then 'V_COMP' when gs in (7,8) then 'V_TEAM'
                else 'V_EXCEL' end as dim, 1 as lo, 5 as hi
    from generate_series(1,10) gs
    union all
    select 'SAFETY', gs,
           case when gs in (1,4,7,10) then 'SAFE_COM'
                when gs in (2,5,8,11) then 'SAFE_JUST'
                else 'SAFE_PRI' end, 1, 5
    from generate_series(1,12) gs
    union all
    select 'CHANGE', gs, 'CHANGE', 1, 5 from generate_series(1,8) gs
    union all
    select 'PSQ', gs, 'PSQ', 1, 7 from generate_series(1,7) gs
    union all
    select 'CULTURE', gs,
           case when gs in (1,5,9) then 'KLAN' when gs in (2,6,10) then 'ADHO'
                when gs in (3,7,11) then 'MARKET' else 'HIER' end, 1, 5
    from generate_series(1,12) gs
    union all
    select 'WHO5', gs, 'WHO5', 0, 4 from generate_series(1,5) gs
    union all
    select 'JUSTICE', gs,
           case when gs in (1,4,7,10) then 'J_DIST' when gs in (2,5,8,11) then 'J_PROC'
                else 'J_INTER' end, 1, 5
    from generate_series(1,12) gs
)
insert into public.responses (respondent_id, instrument, item_n, score)
select resp.id, x.instrument, x.item_n,
       (x.lo + floor(
           case
             -- dimensi LEMAH untuk orang ini (hash < 35): skor rendah-menengah
             when (abs(hashtext(resp.id::text || x.dim)::bigint) % 100) < 35
               then (0.15 + (abs(hashtext(resp.id::text || x.instrument || x.item_n::text || 'w')::bigint) % 100) / 100.0 * 0.35)
             -- dimensi KUAT: skor menengah-tinggi
             else (0.55 + (abs(hashtext(resp.id::text || x.instrument || x.item_n::text || 's')::bigint) % 100) / 100.0 * 0.40)
           end * (x.hi - x.lo)
       ))::int as score
from resp
cross join items x;

-- 3) Verifikasi: tiap instrumen harus 50 orang penuh
select s.instrument, count(distinct s.respondent_id) as orang, count(*) as jawaban
from public.responses s
join public.respondents r on r.id = s.respondent_id
join public.trainings t on t.id = r.training_id
where t.name = 'AspenCulture'
group by s.instrument order by s.instrument;

-- 4) Cek variasi: rata-rata skor per dimensi (harus beragam, tidak seragam)
select x.dim, round(avg(s.score), 1) as rata2
from public.responses s
join public.respondents r on r.id = s.respondent_id
join public.trainings t on t.id = r.training_id
join lateral (
    select case
      when s.instrument='VALUES' and s.item_n in (1,2) then 'V_RESPECT'
      when s.instrument='VALUES' and s.item_n in (3,4) then 'V_INTEG'
      when s.instrument='VALUES' and s.item_n in (5,6) then 'V_COMP'
      when s.instrument='VALUES' and s.item_n in (7,8) then 'V_TEAM'
      when s.instrument='VALUES' then 'V_EXCEL'
      when s.instrument='SAFETY' and s.item_n in (1,4,7,10) then 'SAFE_COM'
      when s.instrument='SAFETY' and s.item_n in (2,5,8,11) then 'SAFE_JUST'
      when s.instrument='SAFETY' then 'SAFE_PRI'
      when s.instrument='CULTURE' and s.item_n in (1,5,9) then 'KLAN'
      when s.instrument='CULTURE' and s.item_n in (2,6,10) then 'ADHO'
      when s.instrument='CULTURE' and s.item_n in (3,7,11) then 'MARKET'
      when s.instrument='CULTURE' then 'HIER'
      when s.instrument='JUSTICE' and s.item_n in (1,4,7,10) then 'J_DIST'
      when s.instrument='JUSTICE' and s.item_n in (2,5,8,11) then 'J_PROC'
      when s.instrument='JUSTICE' then 'J_INTER'
      else s.instrument end as dim
) x on true
where t.name = 'AspenCulture'
group by x.dim order by x.dim;
