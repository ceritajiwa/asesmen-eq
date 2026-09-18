
# -*- coding: utf-8 -*-
from collections import defaultdict
import pandas as pd
from instruments import INSTRUMENTS, DIMS, DIM_ORDER

def apply_reverse(inst, item, raw):
    if item["rev"]:
        return inst["min"] + inst["max"] - raw
    return raw

def compute_dim_scores(answers):
    """answers: dict {(inst_key, item_n): raw_score} -> dict {dim: skor 0-100}"""
    sums = defaultdict(float); counts = defaultdict(int)
    for inst in INSTRUMENTS:
        for it in inst["items"]:
            v = apply_reverse(inst, it, answers[(inst["key"], it["n"])])
            sums[it["dim"]] += v; counts[it["dim"]] += 1
    out = {}
    for dim in DIM_ORDER:
        if dim == "PSS":  # PSS pakai total 0-40
            out[dim] = round(sums[dim] / 40 * 100, 1)
        else:
            inst = next(i for i in INSTRUMENTS if any(x["dim"]==dim for x in i["items"]))
            out[dim] = round((sums[dim]/counts[dim] - inst["min"]) / (inst["max"]-inst["min"]) * 100, 1)
    return out

def band(score, lo=33.0, hi=66.0):
    return "low" if score < lo else ("mid" if score < hi else "high")

def responses_to_answers(rows):
    """rows dari tabel responses -> dict answers"""
    amap = {i["key"]: i for i in INSTRUMENTS}
    ans = {}
    for r in rows:
        ans[(r["instrument"], int(r["item_n"]))] = int(r["score"])
    return ans

def group_scores(df_resp):
    """DataFrame responses per perusahaan -> DataFrame skor per responden x dimensi"""
    amap = {i["key"]: i for i in INSTRUMENTS}
    records = []
    for rid, g in df_resp.groupby("respondent_id"):
        ans = {(r.instrument, int(r.item_n)): int(r.score) for r in g.itertuples()}
        if len(ans) < 64:
            continue
        rec = {"respondent_id": rid}
        rec.update(compute_dim_scores(ans))
        records.append(rec)
    df = pd.DataFrame(records)
    return df
