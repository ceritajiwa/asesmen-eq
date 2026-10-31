"""Tampilan & PDF hasil asesmen individu (logika asli aplikasi Asesmen EQ)."""
import io
import zipfile

import pandas as pd
import streamlit as st

from charts import radar_chart
from hr_analytics import FLIP, healthify
from insights import grouped_insights
from instruments import DIM_ORDER, DIMS
from pdf_report import individual_pdf
from scoring import band

HTAG = {"low": "🔴 perlu perhatian", "mid": "🟡 cukup", "high": "🟢 baik"}
HLABEL = {"low": "Perlu Perhatian", "mid": "Cukup", "high": "Baik"}


def pdf_individu(name, training_name, dept, job_level, scores) -> bytes:
    groups = grouped_insights(scores)
    png = radar_chart(scores, f"Profil {name}")
    return individual_pdf(name, training_name, dept, job_level, scores, groups, png)


def show_result(name, training_name, dept, job_level, scores, key="hasil"):
    st.success(f"Hasil asesmen untuk **{name}** berhasil dihitung.")
    groups = grouped_insights(scores)
    hsc = healthify(scores)
    c1, c2 = st.columns([1, 1.15])
    with c1:
        fig_bytes = radar_chart(scores, f"Profil {name}")
        st.image(fig_bytes, width=430)
        from insights import CAPTIONS
        st.caption(CAPTIONS["radar"])
    with c2:
        st.subheader("Ringkasan per Tes")
        for _key, title, _plain, rows in groups:
            with st.expander(f"**{title}**"):
                tbl = []
                for label, _b, _text in rows:
                    dim = next(d for d in DIM_ORDER if DIMS[d]["label"] == label)
                    hb = band(hsc[dim])
                    tbl.append(dict(Aspek=label + ("*" if dim in FLIP else ""),
                                    Skor=f"{hsc[dim]:.0f}",
                                    Kategori=HLABEL[hb], Status=HTAG[hb],
                                    Catatan=("* skor dibalik" if dim in FLIP else "-")))
                st.dataframe(pd.DataFrame(tbl), hide_index=True, width="stretch")
        pdf_bytes = individual_pdf(name, training_name, dept, job_level, scores, groups, fig_bytes)
        st.download_button("⬇️ Download Laporan PDF", data=pdf_bytes,
                           file_name=f"Hasil_Asesmen_{name.replace(' ', '_')}.pdf",
                           mime="application/pdf", type="primary", key=f"dl_{key}")
    st.divider()
    st.subheader("💡 Penjelasan Hasil per Tes")
    for _key, title, plain, rows in groups:
        st.markdown(f"#### {title}")
        st.markdown(f"*{plain}*")
        for label, _b, text in rows:
            st.markdown(f"- **{label}**: {text}")
        st.write("")


def build_zip_all(training_name, df_scores, cols, comp_pdf_bytes):
    """ZIP berisi PDF agregat + semua PDF individual. df_scores sudah ter-merge dengan nama/dept."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"Report_Agregat_{training_name.replace(' ', '_')}.pdf", comp_pdf_bytes)
        n = 0
        for _, row in df_scores.iterrows():
            scores = {d: float(row[d]) for d in cols if pd.notna(row[d])}
            if not scores:
                continue
            pdf_b = pdf_individu(row["full_name"], training_name, row.get("department"),
                                 row.get("job_level"), scores)
            z.writestr(f"Individu/{row['full_name'].replace(' ', '_')}.pdf", pdf_b)
            n += 1
    return buf.getvalue(), n
