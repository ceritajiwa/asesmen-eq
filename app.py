
# -*- coding: utf-8 -*-
import io, json, random
import streamlit as st
import pandas as pd
from supabase import create_client

from instruments import INSTRUMENTS, DIMS, DIM_ORDER, INST_SHORT
from scoring import compute_dim_scores, responses_to_answers, band, group_scores
from insights import individual_insights, gap_analysis, gap_summary_sentences
from charts import radar_chart, bar_chart_targets, dept_chart
from pdf_report import individual_pdf, company_pdf, BAND_LABEL

st.set_page_config(page_title="Asesmen EQ | Cerita Jiwa", page_icon="🧠", layout="wide")

# ===== SEMBUNYIKAN ELEMEN STREAMLIT =====
st.markdown("""
<style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    [data-testid="stStatusWidget"] {display: none;}
</style>
""", unsafe_allow_html=True)

ALL_KEYS = [i["key"] for i in INSTRUMENTS]
INST_MAP = {i["key"]: i for i in INSTRUMENTS}
LABEL2KEY = {v: k for k, v in INST_SHORT.items()}

# ============================== KONEKSI ==============================
@st.cache_resource
def get_sb():
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

try:
    sb = get_sb()
except Exception:
    st.error("Koneksi database gagal. Cek SUPABASE_URL dan SUPABASE_KEY di secrets.")
    st.stop()

def fetch_trainings():
    res = sb.table("trainings").select("*").order("name").execute()
    return res.data or []

def fetch_respondents(training_id):
    res = sb.table("respondents").select("*").eq("training_id", training_id).execute()
    return res.data or []

def fetch_responses(respondent_ids):
    if not respondent_ids:
        return []
    res = sb.table("responses").select("*").in_("respondent_id", respondent_ids).execute()
    return res.data or []

def get_enabled(training):
    """List kunci instrumen yang aktif untuk training ini (default: semua)."""
    raw = training.get("enabled_instruments")
    if not raw:
        return list(ALL_KEYS)
    try:
        keys = [k for k in json.loads(raw) if k in ALL_KEYS]
        return keys or list(ALL_KEYS)
    except Exception:
        return list(ALL_KEYS)

# ============================== SIDEBAR ==============================
st.sidebar.title("🧠 Asesmen EQ")
st.sidebar.caption("Cerita Jiwa Training Center")
page = st.sidebar.radio("Menu", ["📝 Mulai Asesmen", "⬇️ Unduh Hasil Saya", "🔐 Admin"])
st.sidebar.divider()

BANDS_BAD = {"low": "🟢 baik", "mid": "🟡 waspada", "high": "🔴 risiko"}
BANDS_GOOD = {"low": "🔴 kekhawatiran", "mid": "🟡 cukup", "high": "🟢 kekuatan"}

def show_result(name, training_name, dept, job_level, scores, insights_list):
    st.success(f"Hasil asesmen untuk **{name}** berhasil dihitung.")
    c1, c2 = st.columns([1, 1.2])
    with c1:
        fig_bytes = radar_chart(scores, f"Profil {name}")
        st.image(fig_bytes, width=430)
    with c2:
        st.subheader("Skor per Dimensi")
        rows = []
        for dim in [d for d in DIM_ORDER if d in scores]:
            d = DIMS[dim]; b = band(scores[dim])
            tag = (BANDS_BAD if d["dir"] == "bad" else BANDS_GOOD)[b]
            rows.append(dict(Dimensi=d["label"], Skor=f"{scores[dim]:.0f}", Kategori=BAND_LABEL[b], Status=tag))
        st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)
        pdf_bytes = individual_pdf(name, training_name, dept, job_level, scores, insights_list, fig_bytes)
        st.download_button("⬇️ Download Laporan PDF Saya", data=pdf_bytes,
                           file_name=f"Hasil_Asesmen_{name.replace(' ','_')}.pdf", mime="application/pdf")
    st.divider()
    st.subheader("💡 Insight")
    for label, b, text in insights_list:
        st.markdown(f"**{label}** — {text}")

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

    # ---- gerbang kode akses dengan tombol Masuk ----
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
    submitted = st.button("✅ Kirim & Lihat Hasil", type="primary", use_container_width=True)

    if submitted:
        if answered < total_q:
            st.error(f"Masih ada {total_q - answered} pernyataan belum dijawab. Lengkapi dulu.")
        else:
            try:
                existing = sb.table("respondents").select("id").eq("training_id", training["id"]).eq("email", email.strip().lower()).execute().data
                if existing:
                    st.error("Email ini sudah pernah mengisi asesmen untuk training ini. Gunakan menu **Unduh Hasil Saya** untuk mengambil laporan.")
                    st.stop()
                ins = sb.table("respondents").insert(dict(
                    training_id=training["id"], full_name=name.strip(),
                    email=email.strip().lower(), department=dept.strip() or None,
                    job_level=job_level)).execute()
                rid = ins.data[0]["id"]
                rows = [dict(respondent_id=rid, instrument=k[0], item_n=k[1], score=v) for k, v in answers.items()]
                sb.table("responses").insert(rows).execute()

                scores = compute_dim_scores(answers, instruments=insts)
                ins_list = individual_insights(scores)
                show_result(name.strip(), training["name"], dept, job_level, scores, ins_list)
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
                ins_list = individual_insights(scores)
                show_result(resp["full_name"], training["name"], resp.get("department"), resp.get("job_level"), scores, ins_list)

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

    # ---- TAB 1: Report per perusahaan ----
    with tab1:
        trainings = fetch_trainings()
        if not trainings:
            st.warning("Belum ada training.")
        else:
            tname = st.selectbox("Pilih Perusahaan / Training", [t["name"] for t in trainings], key="adm_t")
            training = next(t for t in trainings if t["name"] == tname)
            enabled = get_enabled(training)
            st.caption(f"Asesmen aktif: {', '.join(k for k in ALL_KEYS if k in enabled)}")
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

                        c1, c2 = st.columns([1, 1.3])
                        radar_png = radar_chart(mean_scores, f"Profil Rata-rata {tname}", dims=cols)
                        bar_png = bar_chart_targets(mean_scores, f"Skor vs Target - {tname}", dims=cols)
                        with c1: st.image(radar_png, width=420)
                        with c2: st.image(bar_png, use_container_width=True)

                        dept_map = dict(zip(resp_df["id"], resp_df.get("department")))
                        dept_png = dept_chart(df_scores, dept_map, f"Breakdown per Departemen - {tname}", dims=cols)

                        gap_rows, priority = gap_analysis(mean_scores)
                        st.subheader("📋 Gap Analysis")
                        st.dataframe(pd.DataFrame(gap_rows)[["label", "mean", "target", "status", "rekomendasi"]],
                                     hide_index=True, use_container_width=True)
                        st.subheader("🎯 Kesimpulan & Prioritas")
                        for s in gap_summary_sentences(priority):
                            st.markdown(f"• {s.lstrip('- ')}")

                        st.subheader("📦 Download")
                        ec1, ec2, ec3 = st.columns(3)
                        excel_buf = io.BytesIO()
                        with pd.ExcelWriter(excel_buf, engine="openpyxl") as w:
                            df_scores.to_excel(w, sheet_name="Skor_per_Individu", index=False)
                            resp_df.to_excel(w, sheet_name="Data_Responden", index=False)
                            pd.DataFrame(gap_rows).to_excel(w, sheet_name="Gap_Analysis", index=False)
                        ec1.download_button("⬇️ Excel (skor + responden + gap)", excel_buf.getvalue(),
                                            file_name=f"Report_{tname}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                        comp_pdf = company_pdf(tname, len(df_scores), mean_scores, radar_png, bar_png, dept_png,
                                               gap_rows, priority, gap_summary_sentences(priority, 5))
                        ec2.download_button("⬇️ PDF Report Perusahaan", comp_pdf,
                                            file_name=f"Report_Agregat_{tname}.pdf", mime="application/pdf")
                        ec3.download_button("⬇️ CSV Skor Individu", df_scores.to_csv(index=False).encode(),
                                            file_name=f"Skor_{tname}.csv", mime="text/csv")
                else:
                    st.info("Belum ada jawaban yang masuk.")

    # ---- TAB 2: Report per individu ----
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
                rows = sb.table("responses").select("*").eq("respondent_id", resp["id"]).execute().data
                scores = compute_dim_scores(responses_to_answers(rows))
                if scores:
                    ins_list = individual_insights(scores)
                    show_result(resp["full_name"], training["name"], resp.get("department"), resp.get("job_level"), scores, ins_list)
                else:
                    st.warning("Data jawaban belum lengkap.")

    # ---- TAB 3: Kelola training ----
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
                    keys = [LABEL2KEY[l] for l in add_sel]
                    sb.table("trainings").insert(dict(name=new_name.strip(), access_code=new_code.strip() or None,
                                                      enabled_instruments=json.dumps(keys))).execute()
                    st.success(f"Training '{new_name.strip()}' ditambahkan.")
                    st.rerun()
        with c2:
            st.subheader("✏️ Edit Training")
            if trainings:
                edit_name = st.selectbox("Pilih training", [t["name"] for t in trainings], key="edit_t")
                edit_training = next(t for t in trainings if t["name"] == edit_name)
                cur_code = edit_training.get("access_code") or ""
                new_code2 = st.text_input("Kode akses (kosongkan untuk publik)", value=cur_code, key="edit_code")
                cur_keys = get_enabled(edit_training)
                edit_sel = st.multiselect("Asesmen yang ditampilkan", list(INST_SHORT.values()),
                                          default=[INST_SHORT[k] for k in ALL_KEYS if k in cur_keys], key="edit_sel")
                if st.button("Simpan Perubahan", type="primary"):
                    if not edit_sel:
                        st.error("Pilih minimal satu asesmen.")
                    else:
                        keys = [LABEL2KEY[l] for l in edit_sel]
                        sb.table("trainings").update(dict(access_code=new_code2.strip() or None,
                                                          enabled_instruments=json.dumps(keys))).eq("id", edit_training["id"]).execute()
                        st.success(f"Training '{edit_name}' diperbarui.")
                        st.rerun()
            else:
                st.info("Belum ada training untuk diedit.")

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

    # ---- TAB 4: Data dummy ----
    with tab4:
        st.subheader("🧪 Generate Data Dummy (untuk testing report)")
        st.caption("Membuat responden fiktif 'Dummy 01, Dummy 02, ...' dengan jawaban acak "
                   "berdistribusi campuran (ada yang baik, sedang, buruk) agar report terlihat realistis.")
        trainings = fetch_trainings()
        if not trainings:
            st.warning("Buat training dulu di tab Kelola Training.")
        else:
            dname = st.selectbox("Training", [t["name"] for t in trainings], key="dummy_t")
            dtraining = next(t for t in trainings if t["name"] == dname)
            n_dummy = st.slider("Jumlah responden dummy", 5, 100, 20)
            first = ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fitri", "Galih", "Hana", "Indra", "Joko",
                     "Kirana", "Lala", "Maya", "Nadia", "Putri", "Raka", "Sari", "Tono", "Wulan", "Yoga"]
            depts = ["HR", "Finance", "Sales", "Operations", "IT", "Marketing"]
            levels = ["Individual Contributor / Staff", "Supervisor / Team Lead", "Manager ke atas"]
            if st.button("⚡ Generate Dummy", type="primary"):
                insts = [INST_MAP[k] for k in ALL_KEYS if k in get_enabled(dtraining)]
                ids = []
                with st.spinner("Menyimpan data dummy..."):
                    for i in range(n_dummy):
                        nm = f"Dummy {i+1:02d}"
                        dep = random.choice(depts)
                        lvl = random.choices(levels, weights=[0.6, 0.3, 0.1])[0]
                        r = sb.table("respondents").insert(dict(
                            training_id=dtraining["id"], full_name=nm,
                            email=f"dummy{i+1:03d}@test.com", department=dep, job_level=lvl)).execute()
                        ids.append(r.data[0]["id"])
                    for rid in ids:
                        # profil campuran per orang: sebagian sehat, sebagian bermasalah
                        profile = random.choices([(0.25, 0.60), (0.40, 0.75), (0.60, 0.97)], weights=[0.3, 0.45, 0.25])[0]
                        ans_rows = []
                        for inst in insts:
                            for it in inst["items"]:
                                u = random.uniform(*profile)
                                raw = int(round(inst["min"] + u * (inst["max"] - inst["min"])))
                                raw = max(inst["min"], min(inst["max"], raw))
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
