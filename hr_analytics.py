
# -*- coding: utf-8 -*-
"""Analitik HR untuk report perusahaan:
- Indeks kesehatan per tes (arah-aware: skor diarahkan semua "tinggi = sehat")
- Klasterisasi profil karyawan (berbasis jumlah area rawan)
- Distribusi kategori per dimensi
"""
import pandas as pd
from instruments import DIMS, DIM_ORDER

# Komponen tiap indeks: (dimensi, arah) — arah -1 = skor tinggi justru tidak sehat
INDEX_COMPONENTS = {
    "Stres":                [("PSS", -1)],
    "Burnout":              [("MBI_EX", -1), ("MBI_CY", -1), ("MBI_PE", 1)],
    "Kecerdasan Emosional": [("SEA", 1), ("OEA", 1), ("ROE", 1), ("UOE", 1)],
    "Keterlibatan Kerja":   [("VIG", 1), ("DED", 1), ("ABS", 1)],
    "Retensi":              [("TIS", -1)],
    "Aman Psikologis":      [("PSQ", 1)],
}

def compute_indices(scores: dict) -> dict:
    """scores: dict dim -> skor 0-100 -> dict indeks (0-100, tinggi = sehat)."""
    idx = {}
    for name, comps in INDEX_COMPONENTS.items():
        vals = []
        for dim, sign in comps:
            if dim in scores:
                vals.append(scores[dim] if sign > 0 else 100 - scores[dim])
        if vals:
            idx[name] = round(sum(vals) / len(vals), 1)
    if idx:
        idx["Indeks Keseluruhan"] = round(sum(idx.values()) / len(idx), 1)
    return idx

# Klaster berbasis jumlah "area rawan" (indeks < 50)
CLUSTERS = {
    1: dict(
        label="Sehat & Terlibat", color="#2E8B57",
        desc="Karyawan dalam kelompok ini menunjukkan kondisi psikologis yang baik di hampir semua aspek: "
             "energi terjaga, emosi teratur, dan terlibat dengan pekerjaan. Mereka adalah pilar stabil tim. "
             "Yang terbaik untuk mereka: tantangan berkembang dan dipertahankan, bukan intervensi intensif."),
    2: dict(
        label="Cukup Baik - 1 Area Rawan", color="#F2C14E",
        desc="Secara umum kondisinya baik, tetapi ada SATU aspek yang mulai menurun — misalnya stres mulai "
             "menumpuk padahal keterlibatan masih tinggi. Ini fase paling efektif untuk intervensi ringan: "
             "sekali area rawannya ditangani, karyawan ini kembali ke jalur sehat sepenuhnya."),
    3: dict(
        label="Perlu Perhatian", color="#E67E22",
        desc="Ada DUA aspek yang menurut bersamaan (misalnya stres tinggi + engagement rendah). Pola seperti "
             "ini cenderung memburuk kalau dibiarkan — bukan karena karyawannya 'lemah', tetapi karena beban "
             "sudah melebihi kapasitas coping yang tersedia. Perhatian tim/HR diperlukan dalam 1-2 bulan ke depan."),
    4: dict(
        label="Prioritas Intervensi", color="#C0392B",
        desc="Tiga aspek atau lebih menunjukkan sinyal serius (kombinasi klasik: stres tinggi + burnout + "
             "niat keluar). Untuk karyawan di kelompok ini, dukungan terstruktur — bukan sekadar motivasi — "
             "sangat dibutuhkan agar tidak berujung resign atau menurunnya performa signifikan."),
}

def assign_cluster(idx: dict):
    flags = [k for k, v in idx.items()
             if k != "Indeks Keseluruhan" and v is not None and v < 50]
    n = len(flags)
    cid = 1 if n == 0 else (2 if n == 1 else (3 if n == 2 else 4))
    return cid, flags

def clusterize(df_scores):
    """df_scores (kolom respondent_id + dimensi) -> df + kolom indeks, cluster, area_rawan."""
    rows = []
    for _, row in df_scores.iterrows():
        scores = {d: float(row[d]) for d in DIM_ORDER
                  if d in df_scores.columns and pd.notna(row[d])}
        idx = compute_indices(scores)
        cid, flags = assign_cluster(idx)
        rec = dict(cluster=cid,
                   cluster_label=CLUSTERS[cid]["label"],
                   area_rawan=", ".join(flags) if flags else "-")
        rec.update(idx)
        rows.append(rec)
    add = pd.DataFrame(rows, index=df_scores.index)
    return pd.concat([df_scores.reset_index(drop=True), add.reset_index(drop=True)], axis=1)

def cluster_summary(idx_df):
    """Ringkasan tiap klaster: jumlah, indeks rata-rata per komponen, daftar area rawan umum."""
    out = []
    for cid in [1, 2, 3, 4]:
        sub = idx_df[idx_df["cluster"] == cid]
        if sub.empty:
            continue
        comp_cols = [c for c in INDEX_COMPONENTS.keys() if c in idx_df.columns]
        means = {c: round(float(sub[c].mean()), 1) for c in comp_cols}
        flags = ", ".join(sorted({f for s in sub["area_rawan"] for f in str(s).split(", ")
                                  if f and f != "-"}))
        out.append(dict(cluster=cid, label=CLUSTERS[cid]["label"], n=len(sub),
                        pct=round(len(sub) / len(idx_df) * 100, 1),
                        means=means, common_flags=flags or "-"))
    return out

def band_counts(df_scores, cols):
    """Distribusi kategori per dimensi, label disesuaikan arah tes."""
    rows = []
    for dim in cols:
        vals = df_scores[dim].dropna()
        if vals.empty:
            continue
        lo = int((vals < 33).sum())
        mid = int(((vals >= 33) & (vals < 66)).sum())
        hi = int((vals >= 66).sum())
        d = DIMS[dim]
        sem = ("Baik", "Waspada", "Risiko") if d["dir"] == "bad" \
              else ("Kekhawatiran", "Cukup", "Kekuatan")
        rows.append(dict(dim=dim, label=d["label"], n=len(vals), dir=d["dir"],
                         low=lo, mid=mid, high=hi,
                         low_label=sem[0], mid_label=sem[1], high_label=sem[2]))
    return rows
