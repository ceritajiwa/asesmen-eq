
# -*- coding: utf-8 -*-
from collections import defaultdict
import pandas as pd
from instruments import INSTRUMENTS, DIMS, DIM_ORDER

def apply_reverse(inst, item, raw):
    if item["rev"]:
        return inst["min"] + inst["max"] - raw
    return raw

def compute_dim_scores(answers, instruments=None):
    """answers: dict {(inst_key, item_n): raw} -> {dim: 0-100}
    Hanya menghitung dimensi dari instrumen yang SELURUH itemnya terjawab."""
    instruments = instruments if instruments is not None else INSTRUMENTS
    out = {}
    for inst in instruments:
        vals = []
        for it in inst["items"]:
            k = (inst["key"], it["n"])
            if k in answers:
                vals.append(apply_reverse(inst, it, answers[k]))
        if len(vals) < len(inst["items"]):
            continue
        if inst["key"] == "PSS":  # PSS pakai total 0-40
            out["PSS"] = round(sum(vals) / 40 * 100, 1)
        else:
            # rata-rata per dimensi di dalam instrumen (MBI 3 dim, WLEIS 4, UWES 3)
            by_dim = defaultdict(list)
            for it, v in zip(inst["items"], vals):
                by_dim[it["dim"]].append(v)
            for dim, vs in by_dim.items():
                m = sum(vs) / len(vs)
                out[dim] = round((m - inst["min"]) / (inst["max"] - inst["min"]) * 100, 1)
    return out

def band(score, lo=33.0, hi=66.0):
    return "low" if score < lo else ("mid" if score < hi else "high")

def responses_to_answers(rows):
    return {(r["instrument"], int(r["item_n"])): int(r["score"]) for r in rows}

def group_scores(df_resp):
    """DataFrame responses -> DataFrame skor per responden (hanya dimensi lengkap)."""
    records = []
    for rid, g in df_resp.groupby("respondent_id"):
        ans = {(r.instrument, int(r.item_n)): int(r.score) for r in g.itertuples()}
        rec = {"respondent_id": rid}
        rec.update(compute_dim_scores(ans))
        if len(rec) > 1:
            records.append(rec)
    return pd.DataFrame(records)
