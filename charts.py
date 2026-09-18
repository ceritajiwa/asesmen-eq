
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from instruments import DIMS, DIM_ORDER

COLORS = {"bad": "#D9534F", "good": "#5B4E9E"}

def radar_chart(scores: dict, title: str, dims=None, figsize=(7, 7)):
    """scores: dict dim->0-100. Mengembalikan PNG bytes."""
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
    """Bar horizontal: skor rata-rata vs target per dimensi."""
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
    ax.set_title(title + "\n(garis putus-putus = target)", fontsize=12, fontweight="bold")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    return _to_png(fig)

def dept_chart(df_scores, dept_map: dict, title: str, dims=None, figsize=(9, 6)):
    """Rata-rata skor per dimensi breakdown departemen (top 5 dept terisi)."""
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

def _to_png(fig):
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=140, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return buf.read()
