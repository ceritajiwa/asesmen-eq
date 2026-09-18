
# -*- coding: utf-8 -*-
import io
import streamlit as st
import pandas as pd
from supabase import create_client

from instruments import INSTRUMENTS, DIMS, DIM_ORDER
from scoring import compute_dim_scores, responses_to_answers, band, group_scores
from insights import individual_insights, gap_analysis, gap_summary_sentences
from pdf_report import BAND_LABEL
from charts import radar_chart, bar_chart_targets, dept_chart
from pdf_report import individual_pdf, company_pdf

st.set_page_config(page_title="Asesmen EQ | Cerita Jiwa", page_icon="🧠", layout="wide")

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

# ============================== SIDEBAR ==============================
st.sidebar.image("https://img.icons8.com/color/96/brain--v1.png", width=48)
st.sidebar.title("Asesmen EQ")
st.sidebar.caption("Cerita Jiwa Training Center")
page = st.sidebar.radio("Menu", ["📝 Mulai Asesmen", "⬇️ Unduh Hasil Saya", "🔐 Admin"])
st.sidebar.divider()
total_items = sum(len(i["items"]) for i in INSTRUMENTS)
st.sidebar.caption(f"{total_items} pertanyaan | {len(DIM_ORDER)} dimensi | ±15 menit")

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
        for dim in DIM_ORDER:
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
        st.warning("Belum ada training terdaftar. Silakan tambahkan dulu di menu Admin / database.")
        st.stop()

    tname = st.selectbox("1. Pilih Perusahaan / Training", [t["name"] for t in trainings])
    training = next(t for t in trainings if t["name"] == tname)
    if training.get("access_code"):
        code = st.text_input("Kode akses", type="password")
        if code != training["access_code"]:
            st.info("Masukkan kode akses yang benar untuk melanjutkan.")
            st.stop()

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
    answers = {}
    for inst in INSTRUMENTS:
        with st.expander(f"**{inst['name']}** ({len(inst['items'])} pernyataan)", expanded=(inst["key"] == "PSS")):
            st.caption(inst["intro"])
            for it in inst["items"]:
                opts = [s[1] for s in inst["scale"]]
                val = st.radio(f"**{it['n']}.** {it['text']}", opts, key=f"{inst['key']}_{it['n']}", index=None)
                if val is not None:
                    val_map = {lbl: num for num, lbl in inst["scale"]}
                    answers[(inst["key"], it["n"])] = val_map[val]
                st.write("")

    st.divider()
    answered = len(answers)
    st.progress(answered / total_items, text=f"Terjawab: {answered}/{total_items}")
    submitted = st.button("✅ Kirim & Lihat Hasil", type="primary", use_container_width=True)

    if submitted:
        if answered < total_items:
            st.error(f"Masih ada {total_items - answered} pernyataan belum dijawab. Lengkapi dulu.")
        else:
            try:
                # cek duplikat email di training yg sama
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

                scores = compute_dim_scores(answers)
                ins_list = individual_insights(scores)
                show_result(name.strip(), training["name"], dept, job_level, scores, ins_list)
            except Exception as e:
                st.error(f"Gagal menyimpan: {e}")

# ============================== PAGE: UNDUH HASIL ==============================
elif page == "⬇️ Unduh Hasil Saya":
    st.title("Unduh Hasil Asesmen")
    trainings = fetch_trainings()
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
            if len(rows) < 64:
                st.error("Data jawaban belum lengkap. Hubungi admin.")
            else:
                scores = compute_dim_scores(responses_to_answers(rows))
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

    tab1, tab2, tab3 = st.tabs(["📊 Report per Perusahaan", "👤 Report per Individu", "🏢 Kelola Training"])

    # ---- TAB 1: Report per perusahaan ----
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
                    df_resp = pd.DataFrame(rows)
                    df_scores = group_scores(df_resp)
                    df_scores = df_scores.merge(resp_df[["id", "full_name", "department", "job_level"]],
                                                left_on="respondent_id", right_on="id", how="left")
                    mean_scores = {d: float(df_scores[d].mean()) for d in DIM_ORDER}

                    c1, c2 = st.columns([1, 1.3])
                    radar_png = radar_chart(mean_scores, f"Profil Rata-rata {tname}")
                    bar_png = bar_chart_targets(mean_scores, f"Skor vs Target - {tname}")
                    with c1: st.image(radar_png, width=420)
                    with c2: st.image(bar_png, use_container_width=True)

                    dept_map = dict(zip(resp_df["id"], resp_df.get("department")))
                    dept_png = dept_chart(df_scores, dept_map, f"Breakdown per Departemen - {tname}")

                    gap_rows, priority = gap_analysis(mean_scores)
                    st.subheader("📋 Gap Analysis")
                    st.dataframe(pd.DataFrame(gap_rows)[["label", "mean", "target", "status", "rekomendasi"]],
                                 hide_index=True, use_container_width=True)
                    st.subheader("🎯 Kesimpulan & Prioritas")
                    for s in gap_summary_sentences(priority):
                        st.markdown(s.replace("- ", "• ", 1) if s.startswith("- ") else f"• {s}")

                    st.subheader("📦 Download")
                    ec1, ec2, ec3 = st.columns(3)
                    # Excel lengkap
                    excel_buf = io.BytesIO()
                    with pd.ExcelWriter(excel_buf, engine="openpyxl") as w:
                        df_scores.to_excel(w, sheet_name="Skor_per_Individu", index=False)
                        df_resp.to_excel(w, sheet_name="Data_Responden", index=False)
                        pd.DataFrame(gap_rows).to_excel(w, sheet_name="Gap_Analysis", index=False)
                    ec1.download_button("⬇️ Excel (skor + responden + gap)", excel_buf.getvalue(),
                                        file_name=f"Report_{tname}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                    comp_pdf = company_pdf(tname, len(df_scores), mean_scores, radar_png, bar_png, dept_png, gap_rows, priority, gap_summary_sentences(priority, 5))
                    ec2.download_button("⬇️ PDF Report Perusahaan", comp_pdf,
                                        file_name=f"Report_Agregat_{tname}.pdf", mime="application/pdf")
                    csv_buf = df_scores.to_csv(index=False).encode()
                    ec3.download_button("⬇️ CSV Skor Individu", csv_buf, file_name=f"Skor_{tname}.csv", mime="text/csv")

    # ---- TAB 2: Report per individu ----
    with tab2:
        trainings = fetch_trainings()
        tname = st.selectbox("Perusahaan / Training", [t["name"] for t in trainings], key="adm_i")
        training = next(t for t in trainings if t["name"] == tname)
        resps = fetch_respondents(training["id"])
        if not resps:
            st.info("Belum ada responden.")
        else:
            pick = st.selectbox("Pilih responden", [f"{r['full_name']} ({r.get('email','')})" for r in resps])
            resp = next(r for r in resps if f"{r['full_name']} ({r.get('email','')})" == pick)
            rows = sb.table("responses").select("*").eq("respondent_id", resp["id"]).execute().data
            if len(rows) >= 64:
                scores = compute_dim_scores(responses_to_answers(rows))
                ins_list = individual_insights(scores)
                show_result(resp["full_name"], training["name"], resp.get("department"), resp.get("job_level"), scores, ins_list)
            else:
                st.warning("Data jawaban belum lengkap.")

    # ---- TAB 3: Kelola training ----
    with tab3:
        trainings = fetch_trainings()
        st.dataframe(pd.DataFrame(trainings)[["name", "access_code", "created_at"]], hide_index=True)
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Tambah Training")
            new_name = st.text_input("Nama perusahaan / training")
            new_code = st.text_input("Kode akses (opsional, kosongkan jika publik)")
            if st.button("➕ Tambah", type="primary"):
                if new_name.strip():
                    sb.table("trainings").insert(dict(name=new_name.strip(), access_code=new_code.strip() or None)).execute()
                    st.success("Training ditambahkan.")
                    st.rerun()
        with c2:
            st.subheader("Hapus Training")
            del_name = st.selectbox("Pilih yang dihapus", [t["name"] for t in trainings], key="del_t") if trainings else None
            if st.button("🗑️ Hapus (beserta semua datanya)"):
                tid = next(t["id"] for t in trainings if t["name"] == del_name)
                sb.table("trainings").delete().eq("id", tid).execute()
                st.success("Training dihapus.")
                st.rerun()
        st.divider()
        if st.button("🚪 Keluar dari mode admin"):
            del st.session_state["admin_ok"]
            st.rerun()
