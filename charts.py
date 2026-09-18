
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from instruments import DIMS, DIM_ORDER
from hr_analytics import CLUSTERS, INDEX_COMPONENTS

COLORS = {"bad": "#D9534F", "good": "#5B4E9E"}

def radar_chart(scores: dict, title: str, dims=None, figsize=(7, 7)):
    dims = dims if dims is not None else [d for d in DIM_ORDER if d in scores]
    labels = [DIMS[d]["radar"] for d in dims]
    vals = [scores[d] for d in dims]
    N = len(labels)
    ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    vals_c = vals + vals[:1]; ang_c = ang + ang[:1]
    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(polar=True))
    ax.plot(ang_c, vals_c, color="#5B4E9E", linewidth=2)
    ax.fill(ang_c, vals_c, color="#5B4E9E", alpha=0.25)
    ax.set_ylim(0, 100)
    ax.set_xticks(ang); ax.set_xticklabels(labels, fontsize=10)
    ax.set_yticks([20, 40, 60, 80, 100]); ax.set_yticklabels(["20","40","60","80","100"], fontsize=8, color="grey")
    for a, v in zip(ang, vals):
        ax.annotate(f"{v:.0f}", (a, v), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=9, fontweight="bold", color="#5B4E9E")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=22)
    fig.tight_layout()
    return _to_png(fig)

def bar_chart_targets(mean_scores: dict, title: str, dims=None, figsize=(9, 6)):
    """Bar horizontal: skor rata-rata vs target per dimensi (warna mengikuti arah tes)."""
    dims = dims if dims is not None else [d for d in DIM_ORDER if d in mean_scores]
    labels = [DIMS[d]["label"] for d in dims]
    vals = [mean_scores[d] for d in dims]
    targets = [DIMS[d]["target"] for d in dims]
    colors = [COLORS[DIMS[d]["dir"]] for d in dims]
    y = np.arange(len(dims))[::-1]
    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(y, vals, color=colors, alpha=0.85, height=0.6)
    for yi, t in zip(y, targets):
        ax.plot([t, t], [yi-0.35, yi+0.35], color="black", linewidth=2, linestyle="--")
    for yi, v in zip(y, vals):
        ax.text(v + 1.5, yi, f"{v:.0f}", va="center", fontsize=9, fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(0, 105); ax.set_xlabel("Skor (0-100)", fontsize=9)
    ax.set_title(title + "\n(garis putus-putus = target; merah = tes yang makin rendah makin baik)",
                 fontsize=11, fontweight="bold")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    return _to_png(fig)

def dept_chart(df_scores, dept_map: dict, title: str, dims=None, figsize=(9, 6)):
    dims = dims if dims is not None else [d for d in DIM_ORDER if d in df_scores.columns]
    df = df_scores.copy()
    df["dept"] = df["respondent_id"].map(dept_map).fillna("(Kosong)")
    top = df["dept"].value_counts()
    top = top[top.index != "(Kosong)"]
    depts = list(top.index[:5])
    if not depts:
        return None
    means = df.groupby("dept")[dims].mean().reindex(depts)
    x = np.arange(len(dims))
    fig, ax = plt.subplots(figsize=figsize)
    width = 0.8 / len(depts)
    palette = plt.cm.tab10.colors
    for i, dept in enumerate(depts):
        ax.bar(x + i*width, means.loc[dept, dims], width=width, label=dept, color=palette[i % 10])
    ax.set_xticks(x + width*(len(depts)-1)/2)
    ax.set_xticklabels([DIMS[d]["radar"] for d in dims], fontsize=8, rotation=30, ha="right")
    ax.set_ylim(0, 100); ax.set_ylabel("Skor rata-rata (0-100)")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.legend(fontsize=8)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    return _to_png(fig)

def cluster_donut(counts: dict, title="Klasterisasi Karyawan", figsize=(6.5, 6.5)):
    """Donut jumlah karyawan per klaster."""
    ids = [i for i in [1, 2, 3, 4] if counts.get(i, 0) > 0]
    if not ids:
        return None
    sizes = [counts[i] for i in ids]
    labels = [f"{CLUSTERS[i]['label']}\n({counts[i]} orang)" for i in ids]
    colors = [CLUSTERS[i]["color"] for i in ids]
    fig, ax = plt.subplots(figsize=figsize)
    wedges, _ = ax.pie(sizes, colors=colors, startangle=90,
                       wedgeprops=dict(width=0.42, edgecolor="white"))
    ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(0.98, 0.5), fontsize=10)
    total = sum(sizes)
    ax.text(0, 0, f"{total}\nkaryawan", ha="center", va="center", fontsize=14, fontweight="bold")
    ax.set_title(title, fontsize=13, fontweight="bold")
    fig.tight_layout()
    return _to_png(fig)

def index_heatmap(idx_df, title="Peta Indeks Karyawan (merah = rawan, hijau = sehat)",
                  max_rows=30, figsize=(10, 8)):
    """Heatmap responden (baris) x indeks (kolom), 0-100, tinggi = sehat."""
    comp = [c for c in INDEX_COMPONENTS.keys() if c in idx_df.columns]
    if not comp or idx_df.empty:
        return None
    cols = comp + (["Indeks Keseluruhan"] if "Indeks Keseluruhan" in idx_df.columns else [])
    df = idx_df.sort_values("Indeks Keseluruhan" if "Indeks Keseluruhan" in idx_df.columns else cols[0])
    df = df.head(max_rows)
    name_col = "full_name" if "full_name" in df.columns else None
    labels = [str(n)[:18] for n in df[name_col]] if name_col else [f"Resp {i+1}" for i in range(len(df))]
    data = df[cols].values.astype(float)
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(data, cmap="RdYlGn", vmin=0, vmax=100, aspect="auto")
    ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols, fontsize=9, rotation=25, ha="right")
    ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels, fontsize=8)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, f"{data[i,j]:.0f}", ha="center", va="center", fontsize=7.5)
    ax.set_title(title + (f" (tampil {len(df)} dari {len(idx_df)})" if len(idx_df) > max_rows else ""),
                 fontsize=11, fontweight="bold")
    fig.colorbar(im, ax=ax, shrink=0.8, label="Indeks (0-100, tinggi = sehat)")
    fig.tight_layout()
    return _to_png(fig)

def band_distribution_chart(rows: list, title="Distribusi Kategori per Dimensi", figsize=(10, 7)):
    """Stacked horizontal bar persentase kategori per dimensi.
    Warna mengikuti makna: hijau = kondisi baik, kuning = waspada, merah = risiko."""
    if not rows:
        return None
    labels = [r["label"] for r in rows][::-1]
    lo_p = [r["low"] / r["n"] * 100 for r in rows][::-1]
    mid_p = [r["mid"] / r["n"] * 100 for r in rows][::-1]
    hi_p = [r["high"] / r["n"] * 100 for r in rows][::-1]
    colors_lo = [("#2E8B57" if r["dir"] == "bad" else "#C0392B") for r in rows][::-1]
    colors_hi = [("#C0392B" if r["dir"] == "bad" else "#2E8B57") for r in rows][::-1]
    y = np.arange(len(rows))
    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(y, lo_p, color=colors_lo, label="Kategori bawah", height=0.62)
    ax.barh(y, mid_p, left=lo_p, color="#F2C14E", label="Kategori tengah", height=0.62)
    left2 = [a + b for a, b in zip(lo_p, mid_p)]
    ax.barh(y, hi_p, left=left2, color=colors_hi, label="Kategori atas", height=0.62)
    for i, r in enumerate(rows[::-1]):
        ax.text(lo_p[i]/2, y[i], f"{lo_p[i]:.0f}%", ha="center", va="center", fontsize=8,
                color="white", fontweight="bold")
        ax.text(lo_p[i]+mid_p[i]/2, y[i], f"{mid_p[i]:.0f}%", ha="center", va="center", fontsize=8, color="#333")
        if hi_p[i] > 8:
            ax.text(left2[i]+hi_p[i]/2, y[i], f"{hi_p[i]:.0f}%", ha="center", va="center",
                    fontsize=8, color="white", fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(0, 100); ax.set_xlabel("Persentase karyawan (%)")
    ax.set_title(title + "\n(hijau selalu = kondisi baik, merah = perlu perhatian, mengikuti arah tiap tes)",
                 fontsize=11, fontweight="bold")
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    return _to_png(fig)

def _to_png(fig):
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=140, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return buf.read()
