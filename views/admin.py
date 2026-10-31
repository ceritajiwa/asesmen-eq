import io
import json
import random

import pandas as pd
import streamlit as st

from bei import bei_company_pdf, bei_participant_pdf, fetch_bei
from charts import (action_map_chart, band_distribution_chart, cluster_donut, dims_heatmap, index_heatmap,
                    radar_chart)
from cjlib.auth import check_password, is_admin_logged_in
from cjlib.db import (ALL_KEYS, INST_MAP, fetch_respondents, fetch_responses, fetch_trainings_raw, get_enabled,
                      get_trainings, sb as _sb)
from cjlib.hasil import build_zip_all, show_result
from cjlib.styles import footer, page_header
from hr_analytics import (CLUSTERS, FLIP, band_counts_health, build_action_plan, cluster_summary, clusterize,
                          healthify)
from insights import (CAPTIONS, CONSEQUENCE, FOLLOWUP, closing_paragraph, gap_analysis, grouped_insights,
                      hr_opening, hr_risks, soft_recommendations, strengths_and_concerns)
from instruments import DIM_ORDER, DIMS, INST_SHORT
from pdf_report import company_pdf
from scoring import compute_dim_scores, group_scores, responses_to_answers

LABEL2KEY = {v: k for k, v in INST_SHORT.items()}


def _jloads(v):
    if not v:
        return None
    if isinstance(v, (dict, list)):
        return v
    return json.loads(v)

# ---------------- Login ----------------
if not is_admin_logged_in():
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.image("assets/logo_dark.png", width=96)
        page_header("⚙️ Admin Panel", "Masukkan password admin.")
        with st.form("form_admin_login", border=True):
            password = st.text_input("Password Admin", type="password")
            submit = st.form_submit_button("Masuk", type="primary", width="stretch")
        if submit:
            ok = check_password(password, "ADMIN_PASSWORD")
            if ok is None:
                st.error("ADMIN_PASSWORD belum diatur di Secrets Streamlit.")
            elif ok:
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("Password salah.")
    footer()
    st.stop()

with st.sidebar:
    st.markdown("<p style='font-weight:800; margin:6px 0 0;'>Admin Panel</p><hr>", unsafe_allow_html=True)
    if st.button("🚪 Logout", width="stretch", key="logout_admin"):
        st.session_state.admin_logged_in = False
        st.switch_page("views/beranda.py")

sb = _sb()

page_header("⚙️ Dashboard Admin")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Report per Perusahaan", "👤 Report per Individu", "🏢 Kelola Training", "🧪 Data Dummy", "🎓 Riwayat Ujian"])

# ---------- TAB 1 ----------
with tab1:
    trainings = fetch_trainings_raw()
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
                    mean_scores = {k: v for k, v in mean_scores.items()
                                   if k in DIMS and not (isinstance(v, float) and v != v)}  # buang NaN & asing
                    gap_rows, priority = gap_analysis(mean_scores)
                    strengths, concerns = strengths_and_concerns(gap_rows)
                    recs = soft_recommendations(priority)

                    st.markdown(hr_opening(tname, len(df_scores), *strengths_and_concerns(gap_analysis(mean_scores)[0]),
                                           cluster_summary(clusterize(df_scores))))
                    c1, c2 = st.columns(2)
                    radar_png = radar_chart(mean_scores, f"Profil Rata-rata {tname}", dims=cols)
                    with c1:
                        st.image(radar_png, width=400)
                        st.caption("Gambar 1. " + CAPTIONS["radar"])
                    idx_df = clusterize(df_scores)
                    counts = idx_df["cluster"].value_counts().to_dict()
                    donut_png = cluster_donut(counts)
                    with c2:
                        if donut_png:
                            st.image(donut_png, width=400)
                            st.caption("Gambar 2. " + CAPTIONS["donut"])

                    # ---- klasterisasi ----
                    st.subheader("👥 Klasterisasi Profil Karyawan")
                    st.caption("Karyawan dikelompokkan berdasarkan jumlah aspek yang menunjukkan sinyal rawan "
                               "(indeks di bawah 50). Indeks diarahkan seragam: makin tinggi makin sehat.")
                    csum = cluster_summary(idx_df)
                    cc = st.columns(len(csum))
                    for col, c in zip(cc, csum):
                        col.metric(f"{c['label']}", f"{c['n']} orang", f"{c['pct']}%")
                    heat_png = index_heatmap(idx_df)
                    if heat_png:
                        st.image(heat_png, width="stretch")
                        st.caption("Gambar 4. " + CAPTIONS["heat"])
                    dims_heat_png = dims_heatmap(df_scores, cols)
                    if dims_heat_png:
                        st.subheader("🗺️ Peta Skor per Dimensi")
                        st.image(dims_heat_png, width="stretch")
                        st.caption("Gambar 4b. Setiap kolom adalah satu dimensi yang diukur; "
                                   "merah = area yang perlu intervensi, hijau = kekuatan tim.")
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
                                hide_index=True, width="stretch")

                    # ---- distribusi kategori ----
                    st.subheader("📶 Distribusi Kategori per Dimensi")
                    df_h = df_scores.copy()
                    for d in cols:
                        if d in FLIP:
                            df_h[d] = 100 - df_h[d]
                    band_rows = band_counts_health(df_h, cols)
                    band_png = band_distribution_chart(band_rows)
                    if band_png:
                        st.image(band_png, width="stretch")
                        st.caption("Gambar 3. " + CAPTIONS["band"])

                    # ---- analisis kebutuhan (soft selling) ----
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
                                        f"{CONSEQUENCE.get(r['dim'], 'Kondisi ini perlu perhatian berkelanjutan.')}")
                    st.markdown("**🌱 Kebutuhan pengembangan yang disarankan**")
                    for s in recs:
                        st.markdown(s if s.startswith("- ") else f"- {s}")
                    st.info(closing_paragraph(len(concerns)))

                    # ---- download ----
                    st.subheader("⚠️ Risiko yang Perlu Diwaspadai")
                    st.caption("Angka diterjemahkan menjadi konsekuensi bisnis - bersifat preventif, masih ada waktu bertindak.")
                    for s in hr_risks(concerns):
                        st.markdown(f"- {s}")

                    st.subheader("🗺️ Peta Tindak Lanjut & Rekomendasi Pengembangan")
                    action_cats = build_action_plan(gap_rows)
                    action_png = action_map_chart(action_cats)
                    if action_png:
                        st.image(action_png, width="stretch")
                        st.caption("Gambar 5. " + CAPTIONS["action"])
                    from hr_analytics import ACTION_META
                    for cat in ["konseling", "training", "pantau", "pertahankan"]:
                        rows_cat = action_cats.get(cat) or []
                        if not rows_cat:
                            continue
                        with st.expander(f"**{ACTION_META[cat]['label']}** ({len(rows_cat)} aspek)"):
                            st.markdown(f"*{ACTION_META[cat]['desc']}*")
                            for r in rows_cat:
                                fu = FOLLOWUP.get(r["dim"], "")
                                line = (f"- **{r['label']}** (selisih {abs(r['gap']):.0f} poin) → {r['rekomendasi']}.")
                                if cat in ("konseling", "training") and fu:
                                    line += f" *Asesmen lanjutan: {fu}*"
                                st.markdown(line)

                    st.subheader("📦 Download")
                    ec1, ec2, ec3 = st.columns(3)
                    idx_out = idx_df.copy()
                    for c in ["cluster_label"]:
                        pass
                    excel_buf = io.BytesIO()
                    with pd.ExcelWriter(excel_buf, engine="openpyxl") as w:
                        df_scores.to_excel(w, sheet_name="Skor_per_Individu", index=False)
                        idx_out.to_excel(w, sheet_name="Klasterisasi", index=False)
                        resp_df.to_excel(w, sheet_name="Data_Responden", index=False)
                        pd.DataFrame(gap_rows).to_excel(w, sheet_name="Gap_Analysis", index=False)
                    ec1.download_button("⬇️ Excel (skor + klaster + responden + gap)", excel_buf.getvalue(),
                                        file_name=f"Report_{tname}.xlsx",
                                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                    h_mean = healthify(mean_scores)
                    grouped = []
                    for key, title, plain, grows in grouped_insights(mean_scores):
                        trows = []
                        for label, b, text in grows:
                            dim = next(d for d in DIM_ORDER if DIMS[d]["label"] == label)
                            note = ("* skor asli dibalik agar searah: makin tinggi = makin sehat"
                                    if dim in FLIP else "makin tinggi = makin baik")
                            trows.append((label, h_mean[dim], mean_scores[dim], DIMS[dim]["dir"], note))
                        grouped.append((key, title, plain, trows))
                    cluster_members = {}
                    for cid in [1, 2, 3, 4]:
                        sub = idx_df[idx_df["cluster"] == cid]
                        cluster_members[cid] = [
                            (r["full_name"], r.get("department"),
                             r.get("Indeks Keseluruhan"), r.get("area_rawan"))
                            for _, r in sub.iterrows()]
                    bundle = dict(
                        training_name=tname, n_respondents=len(df_scores),
                        radar_png=radar_png, donut_png=donut_png, heat_png=heat_png, band_png=band_png,
                        grouped=grouped, gap_rows=gap_rows,
                        strengths=strengths, concerns=concerns, recommendations=recs,
                        cluster_summary=csum, cluster_members=cluster_members,
                        opening=hr_opening(tname, len(df_scores), strengths, concerns, csum),
                        risks=hr_risks(concerns),
                        action_cats=action_cats, action_png=action_png,
                        closing=closing_paragraph(len(concerns)))
                    comp_pdf = company_pdf(bundle)
                    ec2.download_button("⬇️ PDF Report Perusahaan", comp_pdf,
                                        file_name=f"Report_Agregat_{tname}.pdf", mime="application/pdf")
                    ec3.download_button("⬇️ CSV Skor Individu", df_scores.to_csv(index=False).encode(),
                                        file_name=f"Skor_{tname}.csv", mime="text/csv")
                    st.write("")
                    if st.button(f"📦 Buat ZIP Lengkap (agregat + {len(df_scores)} PDF individu)", type="primary"):
                        with st.spinner("Membuat PDF untuk setiap peserta... (1-2 menit untuk banyak peserta)"):
                            try:
                                zip_bytes, n_pdf = build_zip_all(tname, df_scores, cols, comp_pdf)
                                st.session_state["zip_ready"] = (zip_bytes, n_pdf)
                            except Exception as ex:
                                st.error(f"Gagal membuat ZIP: {ex}")
                    st.write("")
                    bei_sessions = fetch_bei(sb, training["id"])
                    if bei_sessions:
                        bei_pdf = bei_company_pdf(tname, bei_sessions)
                        st.download_button(f"⬇️ PDF Report BEI ({len(bei_sessions)} sesi konseling)",
                                           data=bei_pdf, file_name=f"Report_BEI_{tname.replace(' ','_')}.pdf",
                                           mime="application/pdf")
                        with st.expander("Lihat & download PDF per peserta (BEI)"):
                            for s in bei_sessions:
                                nar = _jloads(s.get("narratives")) or {}
                                stc = _jloads(s.get("structured"))
                                pdf_p = bei_participant_pdf(tname, s["participant_name"],
                                                            s.get("counselor_name", "-"), nar, stc)
                                st.download_button(f"⬇️ {s['participant_name']} ({str(s.get('created_at',''))[:10]})",
                                                   data=pdf_p,
                                                   file_name=f"BEI_{s['participant_name'].replace(' ','_')}.pdf",
                                                   mime="application/pdf", key=f"beipdf_{s['id']}")
                    else:
                        st.caption("Belum ada data sesi konseling (BEI) untuk perusahaan ini. "
                                   "Report BEI akan tersedia setelah trainer mencatat sesi di Menu Trainer.")
                    if "zip_ready" in st.session_state:
                        zip_bytes, n_pdf = st.session_state.pop("zip_ready")
                        st.download_button(f"⬇️ Download ZIP ({n_pdf + 1} file PDF)", data=zip_bytes,
                                           file_name=f"Report_Lengkap_{tname.replace(' ','_')}.zip",
                                           mime="application/zip")
            else:
                st.info("Belum ada jawaban yang masuk.")

# ---------- TAB 2 ----------
with tab2:
    trainings = fetch_trainings_raw()
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
                show_result(resp["full_name"], training["name"], resp.get("department"), resp.get("job_level"), scores, key="admin")
            else:
                st.warning("Data jawaban belum lengkap.")

# ---------- TAB 3 ----------
with tab3:
    trainings = fetch_trainings_raw()
    if trainings:
        disp = pd.DataFrame(trainings)
        disp["asesmen_aktif"] = disp.apply(lambda r: ", ".join(INST_SHORT[k] for k in ALL_KEYS if k in get_enabled(r)), axis=1)
        st.dataframe(disp[["name", "access_code", "asesmen_aktif"]], hide_index=True, width="stretch")
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
                get_trainings.clear()
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
                    get_trainings.clear()
                    st.success(f"Training '{edit_name}' diperbarui.")
                    st.rerun()
    st.divider()
    if trainings:
        st.subheader("🗑️ Hapus Training")
        del_name = st.selectbox("Pilih yang dihapus", [t["name"] for t in trainings], key="del_t")
        if st.button("Hapus (beserta semua datanya)"):
            tid = next(t["id"] for t in trainings if t["name"] == del_name)
            sb.table("trainings").delete().eq("id", tid).execute()
            get_trainings.clear()
            st.success("Training dihapus.")
            st.rerun()

# ---------- TAB 5 ----------
with tab5:
    st.subheader("🎓 Riwayat Ujian Sertifikasi")
    trainings = fetch_trainings_raw()
    if not trainings:
        st.info("Belum ada training.")
    else:
        tname = st.selectbox("Perusahaan / Training", [t["name"] for t in trainings], key="exam_hist_t")
        training = next(t for t in trainings if t["name"] == tname)
        try:
            att = sb.table("exam_attempts").select("*").eq("training_id", training["id"]).order("created_at", desc=True).execute().data or []
        except Exception:
            att = []
        if not att:
            st.info("Belum ada percobaan ujian untuk training ini. "
                    "(Kalau baru deploy, jalankan migrasi SQL untuk tabel exam_attempts dulu.)")
        else:
            lulus = sum(1 for a in att if a["passed"])
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Percobaan", len(att))
            c2.metric("Lulus", lulus)
            c3.metric("Belum Lulus", len(att) - lulus)
            cols_t5 = ["full_name", "email", "package", "correct", "score", "passed", "created_at"]
            df_att = pd.DataFrame(att)[[c for c in cols_t5 if c in pd.DataFrame(att).columns]]
            df_att.columns = [c for c in ["Nama", "Email", "Paket", "Benar", "Nilai", "Lulus", "Waktu"][:len(df_att.columns)]]
            df_att["Lulus"] = df_att["Lulus"].map({True: "✅ Lulus", False: "❌ Belum"})
            st.dataframe(df_att, hide_index=True, width="stretch")
            st.download_button("⬇️ CSV Riwayat Ujian", df_att.to_csv(index=False).encode(),
                               file_name=f"Riwayat_Ujian_{tname}.csv", mime="text/csv")

    st.divider()
    if st.button("🚪 Keluar dari mode admin"):
        del st.session_state["admin_ok"]
        st.rerun()

# ---------- TAB 4 ----------
with tab4:
    st.subheader("🧪 Generate Data Dummy (untuk testing report)")
    st.caption("Membuat responden fiktif 'Dummy ...' dengan jawaban acak berdistribusi campuran "
               "agar report terlihat realistis.")
    trainings = fetch_trainings_raw()
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

footer()
