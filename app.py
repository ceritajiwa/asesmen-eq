# -*- coding: utf-8 -*-
import io, json, random
import streamlit as st
import pandas as pd
from supabase import create_client

from instruments import INSTRUMENTS, DIMS, DIM_ORDER, INST_SHORT
from scoring import compute_dim_scores, responses_to_answers, band, group_scores
from insights import (individual_insights, grouped_insights, gap_analysis,
                      strengths_and_concerns, soft_recommendations, closing_paragraph,
                      BAND_LABEL, DIRECTION_NOTE, CONSEQUENCE)
from hr_analytics import clusterize, cluster_summary, band_counts, CLUSTERS, compute_indices
from charts import (radar_chart, bar_chart_targets, dept_chart, cluster_donut,
                    index_heatmap, band_distribution_chart)
from pdf_report import individual_pdf, company_pdf

st.set_page_config(page_title="Asesmen EQ | Cerita Jiwa", page_icon="🧠", layout="wide")

ALL_KEYS = [i["key"] for i in INSTRUMENTS]
INST_MAP = {i["key"]: i for i in INSTRUMENTS}
LABEL2KEY = {v: k for k, v in INST_SHORT.items()}

@st.cache_resource
def get_sb():
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

try:
    sb = get_sb()
except Exception:
    st.error("Koneksi database gagal. Cek SUPABASE_URL dan SUPABASE_KEY di secrets.")
    st.stop()

def fetch_trainings():
    return sb.table("trainings").select("*").order("name").execute().data or []

def fetch_respondents(training_id):
    return sb.table("respondents").select("*").eq("training_id", training_id).execute().data or []

def fetch_responses(ids):
    if not ids:
        return []
    return sb.table("responses").select("*").in_("respondent_id", ids).execute().data or []

def get_enabled(training):
    raw = training.get("enabled_instruments")
    if not raw:
        return list(ALL_KEYS)
    try:
        keys = [k for k in json.loads(raw) if k in ALL_KEYS]
        return keys or list(ALL_KEYS)
    except Exception:
        return list(ALL_KEYS)

st.sidebar.title("🧠 Asesmen EQ")
st.sidebar.caption("Cerita Jiwa Training Center")
page = st.sidebar.radio("Menu", ["📝 Mulai Asesmen", "⬇️ Unduh Hasil Saya", "🔐 Admin"])
st.sidebar.divider()

BANDS_BAD = {"low": "🟢 baik", "mid": "🟡 waspada", "high": "🔴 risiko"}
BANDS_GOOD = {"low": "🔴 kekhawatiran", "mid": "🟡 cukup", "high": "🟢 kekuatan"}

def show_result(name, training_name, dept, job_level, scores):
    st.success(f"Hasil asesmen untuk **{name}** berhasil dihitung.")
    groups = grouped_insights(scores)
    c1, c2 = st.columns([1, 1.15])
    with c1:
        fig_bytes = radar_chart(scores, f"Profil {name}")
        st.image(fig_bytes, width=430)
        st.caption("📝 Arah tes: stres, burnout (kelelahan & sinisme), dan niat keluar "
                   "→ **makin rendah makin baik**. Tes lainnya → makin tinggi makin baik.")
    with c2:
        st.subheader("Ringkasan per Tes")
        for key, title, plain, rows in groups:
            with st.expander(f"**{title}**"):
                tbl = []
                for label, b, text in rows:
                    dim = next(d for d in DIM_ORDER if DIMS[d]["label"] == label)
                    tag = (BANDS_BAD if DIMS[dim]["dir"] == "bad" else BANDS_GOOD)[b]
                    tbl.append(dict(Aspek=label, Skor=f"{scores[dim]:.0f}",
                                    Kategori=BAND_LABEL[b], Status=tag))
                st.dataframe(pd.DataFrame(tbl), hide_index=True, use_container_width=True)
        pdf_bytes = individual_pdf(name, training_name, dept, job_level, scores, groups, fig_bytes)
        st.download_button("⬇️ Download Laporan PDF Saya", data=pdf_bytes,
                           file_name=f"Hasil_Asesmen_{name.replace(' ','_')}.pdf", mime="application/pdf")
    st.divider()
    st.subheader("💡 Penjelasan Hasil per Tes")
    for key, title, plain, rows in groups:
        st.markdown(f"#### {title}")
        st.markdown(f"*{plain}*")
        for label, b, text in rows:
            st.markdown(f"- **{label}** — {text}")
        st.write("")

# ============================== PAGE: ASESmen ==============================
if page == "📝 Mulai Asesmen":
    st.title("Asesmen EQ & Emotional Regulation")
    st.caption("Isi seluruh pernyataan dengan jujur sesuai kondisi Anda saat ini. Tidak ada jawaban benar/salah.")

    trainings = fetch_trainings()
    if not trainings:
        st.warning("Belum ada training terdaftar. Silakan tambahkan dulu di menu Admin.")
        st.stop()

    tname = st.selectbox("1. Pilih Perusahaan / Training", [t["name"] for t in trainings])
    training = next(t for t in trainings if t["name"] == tname)

    if training.get("access_code") and st.session_state.get("access_ok") != training["id"]:
        code = st.text_input("Kode akses", type="password")
        cbtn, _ = st.columns([1, 3])
        if cbtn.button("🔓 Masuk ke Asesmen", type="primary", use_container_width=True):
            if code == training["access_code"]:
                st.session_state["access_ok"] = training["id"]
                st.rerun()
            else:
                st.error("Kode akses salah. Coba lagi atau hubungi trainer Anda.")
        st.stop()
    elif st.session_state.get("access_ok") == training["id"]:
        st.info(f"✅ Kode akses **{training['name']}** terverifikasi. Silakan isi data diri di bawah.")

    enabled = get_enabled(training)
    insts = [INST_MAP[k] for k in ALL_KEYS if k in enabled]
    total_q = sum(len(i["items"]) for i in insts)

    st.divider()
    st.subheader("2. Data Diri")
    c1, c2, c3 = st.columns(3)
    name = c1.text_input("Nama lengkap")
    email = c2.text_input("Email")
    dept = c3.text_input("Departemen")
    job_level = st.selectbox("Level jabatan", ["Individual Contributor / Staff", "Supervisor / Team Lead", "Manager ke atas", "Lainnya"])
    if not name.strip() or not email.strip():
        st.warning("Lengkapi nama dan email untuk mulai.")
        st.stop()

    st.divider()
    st.subheader("3. Pernyataan Asesmen")
    st.caption(f"Training ini menggunakan **{len(insts)} asesmen** ({total_q} pernyataan).")
    answers = {}
    for idx, inst in enumerate(insts):
        with st.expander(f"**{inst['name']}** ({len(inst['items'])} pernyataan)", expanded=(idx == 0)):
            st.caption(inst["intro"])
            for it in inst["items"]:
                opts = [s[1] for s in inst["scale"]]
                val = st.radio(f"**{it['n']}.** {it['text']}", opts, key=f"{inst['key']}_{it['n']}", index=None)
                if val is not None:
                    val_map = {lbl: num for num, lbl in inst["scale"]}
                    answers[(inst["key"], it["n"])] = val_map[val]

    st.divider()
    answered = len(answers)
    st.progress(answered / total_q, text=f"Terjawab: {answered}/{total_q}")
    if st.button("✅ Kirim & Lihat Hasil", type="primary", use_container_width=True):
        if answered < total_q:
            st.error(f"Masih ada {total_q - answered} pernyataan belum dijawab. Lengkapi dulu.")
        else:
            try:
                existing = sb.table("respondents").select("id").eq("training_id", training["id"]).eq("email", email.strip().lower()).execute().data
                if existing:
                    st.error("Email ini sudah pernah mengisi asesmen untuk training ini. Gunakan menu **Unduh Hasil Saya**.")
                    st.stop()
                ins = sb.table("respondents").insert(dict(
                    training_id=training["id"], full_name=name.strip(),
                    email=email.strip().lower(), department=dept.strip() or None,
                    job_level=job_level)).execute()
                rid = ins.data[0]["id"]
                rows = [dict(respondent_id=rid, instrument=k[0], item_n=k[1], score=v) for k, v in answers.items()]
                sb.table("responses").insert(rows).execute()
                scores = compute_dim_scores(answers, instruments=insts)
                show_result(name.strip(), training["name"], dept, job_level, scores)
            except Exception as e:
                st.error(f"Gagal menyimpan: {e}")

# ============================== PAGE: UNDUH HASIL ==============================
elif page == "⬇️ Unduh Hasil Saya":
    st.title("Unduh Hasil Asesmen")
    trainings = fetch_trainings()
    if not trainings:
        st.warning("Belum ada training terdaftar.")
        st.stop()
    tname = st.selectbox("Perusahaan / Training", [t["name"] for t in trainings])
    training = next(t for t in trainings if t["name"] == tname)
    email = st.text_input("Email yang digunakan saat mengisi")
    if st.button("🔍 Cari Hasil", type="primary"):
        res = sb.table("respondents").select("*").eq("training_id", training["id"]).eq("email", email.strip().lower()).execute().data
        if not res:
            st.error("Data tidak ditemukan. Pastikan email dan training sudah benar.")
        else:
            resp = res[0]
            rows = sb.table("responses").select("*").eq("respondent_id", resp["id"]).execute().data
            scores = compute_dim_scores(responses_to_answers(rows))
            if not scores:
                st.error("Data jawaban belum lengkap. Hubungi admin.")
            else:
                show_result(resp["full_name"], training["name"], resp.get("department"), resp.get("job_level"), scores)

# ============================== PAGE: ADMIN ==============================
else:
    st.title("🔐 Area Admin")
    if "admin_ok" not in st.session_state:
        pwd = st.text_input("Password admin", type="password")
        if st.button("Masuk"):
            if pwd == st.secrets["ADMIN_PASSWORD"]:
                st.session_state["admin_ok"] = True
                st.rerun()
            else:
                st.error("Password salah.")
        st.stop()

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Report per Perusahaan", "👤 Report per Individu", "🏢 Kelola Training", "🧪 Data Dummy"])

    # ---------- TAB 1 ----------
    with tab1:
        trainings = fetch_trainings()
        if not trainings:
            st.warning("Belum ada training.")
        else:
            tname = st.selectbox("Pilih Perusahaan / Training", [t["name"] for t in trainings], key="adm_t")
            training = next(t for t in trainings if t["name"] == tname)
            resps = fetch_respondents(training["id"])
            st.caption(f"Responden terdaftar: {len(resps)}")
            if resps:
                resp_df = pd.DataFrame(resps)
                rows = fetch_responses(list(resp_df["id"]))
                if rows:
                    df_scores = group_scores(pd.DataFrame(rows))
                    if df_scores.empty:
                        st.info("Belum ada jawaban lengkap untuk dihitung.")
                    else:
                        df_scores = df_scores.merge(resp_df[["id", "full_name", "department", "job_level"]],
                                                    left_on="respondent_id", right_on="id", how="left")
                        cols = [d for d in DIM_ORDER if d in df_scores.columns]
                        mean_scores = {d: float(df_scores[d].mean()) for d in cols}
                        gap_rows, priority = gap_analysis(mean_scores)
                        strengths, concerns = strengths_and_concerns(gap_rows)
                        recs = soft_recommendations(priority)

                        c1, c2 = st.columns(2)
                        radar_png = radar_chart(mean_scores, f"Profil Rata-rata {tname}", dims=cols)
                        with c1:
                            st.image(radar_png, width=400)
                            st.caption("Merah = tes yang makin rendah makin baik (stres, burnout, niat keluar). Ungu = makin tinggi makin baik.")
                        idx_df = clusterize(df_scores)
                        counts = idx_df["cluster"].value_counts().to_dict()
                        donut_png = cluster_donut(counts)
                        with c2:
                            if donut_png:
                                st.image(donut_png, width=400)

                        st.subheader("👥 Klasterisasi Profil Karyawan")
                        st.caption("Karyawan dikelompokkan berdasarkan jumlah aspek yang menunjukkan sinyal rawan "
                                   "(indeks di bawah 50). Indeks diarahkan seragam: makin tinggi makin sehat.")
                        csum = cluster_summary(idx_df)
                        cc = st.columns(len(csum))
                        for col, c in zip(cc, csum):
                            col.metric(f"{c['label']}", f"{c['n']} orang", f"{c['pct']}%")
                        heat_png = index_heatmap(idx_df)
                        if heat_png:
                            st.image(heat_png, use_container_width=True)
                        for cid in [1, 2, 3, 4]:
                            sub = idx_df[idx_df["cluster"] == cid]
                            if sub.empty:
                                continue
                            with st.expander(f"{'🟢' if cid==1 else '🟡' if cid==2 else '🟠' if cid==3 else '🔴'} "
                                             f"{CLUSTERS[cid]['label']} — {len(sub)} orang"):
                                st.markdown(CLUSTERS[cid]["desc"])
                                show_cols = ["full_name", "department", "Indeks Keseluruhan", "area_rawan"]
                                show_cols = [c for c in show_cols if c in sub.columns]
                                st.dataframe(sub[show_cols].rename(columns={
                                    "full_name": "Nama", "department": "Departemen",
                                    "Indeks Keseluruhan": "Indeks", "area_rawan": "Area Rawan"}),
                                    hide_index=True, use_container_width=True)

                        st.subheader("📶 Distribusi Kategori per Dimensi")
                        st.caption("Hijau selalu = kondisi baik, merah = perlu perhatian (sudah dikoreksi arah tiap tes).")
                        band_rows = band_counts(df_scores, cols)
                        band_png = band_distribution_chart(band_rows)
                        if band_png:
                            st.image(band_png, use_container_width=True)

                        st.subheader("🎯 Analisis Kebutuhan & Rekomendasi Pengembangan")
                        st.markdown("**✅ Yang sudah baik**")
                        if strengths:
                            for r in strengths:
                                st.markdown(f"- {r['label']} (rata-rata {r['mean']:.0f}/100): berada pada atau di atas level sehat.")
                        else:
                            st.markdown("- Belum ada aspek yang mencapai level sehat — ini titik awal yang jelas untuk memulai, bukan vonis.")
                        if concerns:
                            st.markdown("**⚠️ Yang perlu diperhatikan**")
                            for r in concerns:
                                st.markdown(f"- **{r['label']}** (rata-rata {r['mean']:.0f}/100; target "
                                            f"{'maksimal' if r['dir']=='bad' else 'minimal'} {r['target']}): "
                                            f"{CONSEQUENCE[r['dim']]}")
                        st.markdown("**🌱 Kebutuhan pengembangan yang disarankan**")
                        for s in recs:
                            st.markdown(s if s.startswith("- ") else f"- {s}")
                        st.info(closing_paragraph(len(concerns)))

                        st.subheader("📦 Download")
                        ec1, ec2, ec3 = st.columns(3)
                        excel_buf = io.BytesIO()
                        with pd.ExcelWriter(excel_buf, engine="openpyxl") as w:
                            df_scores.to_excel(w, sheet_name="Skor_per_Individu", index=False)
                            idx_df.to_excel(w, sheet_name="Klasterisasi", index=False)
                            resp_df.to_excel(w, sheet_name="Data_Responden", index=False)
                            pd.DataFrame(gap_rows).to_excel(w, sheet_name="Gap_Analysis", index=False)
                        ec1.download_button("⬇️ Excel (skor + klaster + responden + gap)", excel_buf.getvalue(),
                                            file_name=f"Report_{tname}.xlsx",
                                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                        grouped = []
                        for key, title, plain, grows in grouped_insights(mean_scores):
                            trows = []
                            for label, b, text in grows:
                                dim = next(d for d in DIM_ORDER if DIMS[d]["label"] == label)
                                trows.append((label, mean_scores[dim], DIMS[dim]["dir"], DIRECTION_NOTE[DIMS[dim]["dir"]]))
                            grouped.append((key, title, plain, trows))
                        bundle = dict(
                            training_name=tname, n_respondents=len(df_scores),
                            radar_png=radar_png, donut_png=donut_png, heat_png=heat_png, band_png=band_png,
                            grouped=grouped, gap_rows=gap_rows,
                            strengths=strengths, concerns=concerns, recommendations=recs,
                            cluster_summary=csum, closing=closing_paragraph(len(concerns)))
                        comp_pdf = company_pdf(bundle)
                        ec2.download_button("⬇️ PDF Report Perusahaan", comp_pdf,
                                            file_name=f"Report_Agregat_{tname}.pdf", mime="application/pdf")
                        ec3.download_button("⬇️ CSV Skor Individu", df_scores.to_csv(index=False).encode(),
                                            file_name=f"Skor_{tname}.csv", mime="text/csv")
                else:
                    st.info("Belum ada jawaban yang masuk.")

    # ---------- TAB 2 ----------
    with tab2:
        trainings = fetch_trainings()
        if not trainings:
            st.warning("Belum ada training.")
        else:
            tname = st.selectbox("Perusahaan / Training", [t["name"] for t in trainings], key="adm_i")
            training = next(t for t in trainings if t["name"] == tname)
            resps = fetch_respondents(training["id"])
            if not resps:
                st.info("Belum ada responden.")
            else:
                pick = st.selectbox("Pilih responden", [f"{r['full_name']} ({r.get('email','')})" for r in resps])
                resp = next(r for r in resps if f"{r['full_name']} ({r.get('email','')})" == pick)
                rows_q = sb.table("responses").select("*").eq("respondent_id", resp["id"]).execute().data
                scores = compute_dim_scores(responses_to_answers(rows_q))
                if scores:
                    show_result(resp["full_name"], training["name"], resp.get("department"), resp.get("job_level"), scores)
                else:
                    st.warning("Data jawaban belum lengkap.")

    # ---------- TAB 3 ----------
    with tab3:
        trainings = fetch_trainings()
        if trainings:
            disp = pd.DataFrame(trainings)
            disp["asesmen_aktif"] = disp.apply(lambda r: ", ".join(k for k in ALL_KEYS if k in get_enabled(r)), axis=1)
            st.dataframe(disp[["name", "access_code", "asesmen_aktif"]], hide_index=True, use_container_width=True)
        else:
            st.info("Belum ada training.")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("➕ Tambah Training")
            new_name = st.text_input("Nama perusahaan / training", key="add_name")
            new_code = st.text_input("Kode akses (opsional)", key="add_code")
            add_sel = st.multiselect("Asesmen yang ditampilkan", list(INST_SHORT.values()),
                                     default=list(INST_SHORT.values()), key="add_sel")
            if st.button("Tambah", type="primary"):
                if not new_name.strip():
                    st.error("Nama training wajib diisi.")
                elif not add_sel:
                    st.error("Pilih minimal satu asesmen.")
                else:
                    sb.table("trainings").insert(dict(name=new_name.strip(), access_code=new_code.strip() or None,
                                                      enabled_instruments=json.dumps([LABEL2KEY[l] for l in add_sel]))).execute()
                    st.success(f"Training '{new_name.strip()}' ditambahkan.")
                    st.rerun()
        with c2:
            st.subheader("✏️ Edit Training")
            if trainings:
                edit_name = st.selectbox("Pilih training", [t["name"] for t in trainings], key="edit_t")
                et = next(t for t in trainings if t["name"] == edit_name)
                new_code2 = st.text_input("Kode akses (kosongkan untuk publik)", value=et.get("access_code") or "", key="edit_code")
                cur_keys = get_enabled(et)
                edit_sel = st.multiselect("Asesmen yang ditampilkan", list(INST_SHORT.values()),
                                          default=[INST_SHORT[k] for k in ALL_KEYS if k in cur_keys], key="edit_sel")
                if st.button("Simpan Perubahan", type="primary"):
                    if not edit_sel:
                        st.error("Pilih minimal satu asesmen.")
                    else:
                        sb.table("trainings").update(dict(access_code=new_code2.strip() or None,
                              enabled_instruments=json.dumps([LABEL2KEY[l] for l in edit_sel]))).eq("id", et["id"]).execute()
                        st.success(f"Training '{edit_name}' diperbarui.")
                        st.rerun()
        st.divider()
        if trainings:
            st.subheader("🗑️ Hapus Training")
            del_name = st.selectbox("Pilih yang dihapus", [t["name"] for t in trainings], key="del_t")
            if st.button("Hapus (beserta semua datanya)"):
                tid = next(t["id"] for t in trainings if t["name"] == del_name)
                sb.table("trainings").delete().eq("id", tid).execute()
                st.success("Training dihapus.")
                st.rerun()
        st.divider()
        if st.button("🚪 Keluar dari mode admin"):
            del st.session_state["admin_ok"]
            st.rerun()

    # ---------- TAB 4 ----------
    with tab4:
        st.subheader("🧪 Generate Data Dummy (untuk testing report)")
        st.caption("Membuat responden fiktif 'Dummy ...' dengan jawaban acak berdistribusi campuran "
                   "agar report terlihat realistis.")
        trainings = fetch_trainings()
        if not trainings:
            st.warning("Buat training dulu di tab Kelola Training.")
        else:
            dname = st.selectbox("Training", [t["name"] for t in trainings], key="dummy_t")
            dtraining = next(t for t in trainings if t["name"] == dname)
            n_dummy = st.slider("Jumlah responden dummy", 5, 100, 20)
            depts = ["HR", "Finance", "Sales", "Operations", "IT", "Marketing"]
            levels = ["Individual Contributor / Staff", "Supervisor / Team Lead", "Manager ke atas"]
            if st.button("⚡ Generate Dummy", type="primary"):
                insts = [INST_MAP[k] for k in ALL_KEYS if k in get_enabled(dtraining)]
                ids = []
                with st.spinner("Menyimpan data dummy..."):
                    for i in range(n_dummy):
                        r = sb.table("respondents").insert(dict(
                            training_id=dtraining["id"], full_name=f"Dummy {i+1:02d}",
                            email=f"dummy{i+1:03d}@test.com", department=random.choice(depts),
                            job_level=random.choices(levels, weights=[0.6, 0.3, 0.1])[0])).execute()
                        ids.append(r.data[0]["id"])
                    for rid in ids:
                        profile = random.choices([(0.25, 0.60), (0.40, 0.75), (0.60, 0.97)], weights=[0.3, 0.45, 0.25])[0]
                        ans_rows = []
                        for inst in insts:
                            for it in inst["items"]:
                                u = random.uniform(*profile)
                                raw = max(inst["min"], min(inst["max"], int(round(inst["min"] + u * (inst["max"] - inst["min"])))))
                                ans_rows.append(dict(respondent_id=rid, instrument=inst["key"], item_n=it["n"], score=raw))
                        for chunk in [ans_rows[j:j+500] for j in range(0, len(ans_rows), 500)]:
                            sb.table("responses").insert(chunk).execute()
                st.success(f"{n_dummy} responden dummy dibuat untuk '{dname}'. Cek tab Report per Perusahaan.")
            if st.button("🧹 Hapus Semua Data Dummy di Training Ini"):
                dummies = sb.table("respondents").select("id").eq("training_id", dtraining["id"]).like("full_name", "Dummy%").execute().data
                for d in dummies:
                    sb.table("respondents").delete().eq("id", d["id"]).execute()
                st.success(f"{len(dummies)} data dummy dihapus.")
                st.rerun()
