"""Tab Admin: kelola NOMOR SERTIFIKAT per peserta (nomor diberikan oleh admin)."""
import re
from datetime import date

import pandas as pd
import streamlit as st

from cjlib.db import (SQL_SERTIFIKAT, DatabaseError, TabelSertifikatBelumAda, cek_nomor_dipakai,
                      fetch_certificates, fetch_passed_attempts, fetch_respondents, fetch_trainings_raw,
                      simpan_sertifikat, tebak_sertifikasi)
from questions import EXAM_PACKAGES

KOLOM = ["Nama", "Email", "Paket", "No. Sertifikat", "Tanggal Terbit", "Catatan", "Sumber", "_cert_id", "_attempt_id"]


def _tanggal(v):
    if v is None or (isinstance(v, float) and v != v) or v == "":
        return None
    if isinstance(v, date):
        return v
    try:
        return pd.to_datetime(str(v)[:10]).date()
    except Exception:  # noqa: BLE001
        return None


def _kosong(v) -> bool:
    return v is None or (isinstance(v, float) and v != v) or str(v).strip() == ""


def _bangun_tabel(training, ikut_asesmen: bool) -> pd.DataFrame:
    certs = fetch_certificates(training["id"])
    lulus = fetch_passed_attempts(training["id"])
    rows = []
    sudah = set()
    for c in certs:
        rows.append({"Nama": c["full_name"], "Email": c.get("email") or "", "Paket": c.get("package") or "",
                     "No. Sertifikat": c.get("cert_no") or "", "Tanggal Terbit": _tanggal(c.get("issued_date")),
                     "Catatan": c.get("notes") or "",
                     "Sumber": "Lulus ujian online" if c.get("exam_attempt_id") else "Input admin",
                     "_cert_id": c["id"], "_attempt_id": c.get("exam_attempt_id")})
        sudah.add(((c.get("email") or "").lower(), c.get("package") or ""))
        if c.get("exam_attempt_id"):
            sudah.add(("#", c["exam_attempt_id"]))
    for a in lulus:
        if ("#", a["id"]) in sudah or ((a.get("email") or "").lower(), a.get("package") or "") in sudah:
            continue
        rows.append({"Nama": a["full_name"], "Email": a.get("email") or "", "Paket": a.get("package") or "",
                     "No. Sertifikat": "", "Tanggal Terbit": _tanggal(a.get("created_at")), "Catatan": "",
                     "Sumber": "Lulus ujian online", "_cert_id": None, "_attempt_id": a["id"]})
        sudah.add(((a.get("email") or "").lower(), a.get("package") or ""))
    if ikut_asesmen:
        paket_default = training.get("_paket") or ""
        emails = {r["Email"].lower() for r in rows if r["Email"]}
        for r in fetch_respondents(training["id"]):
            if (r.get("email") or "").lower() in emails or str(r.get("full_name", "")).startswith("Dummy"):
                continue
            rows.append({"Nama": r["full_name"], "Email": r.get("email") or "", "Paket": paket_default,
                         "No. Sertifikat": "", "Tanggal Terbit": None, "Catatan": "",
                         "Sumber": "Peserta asesmen", "_cert_id": None, "_attempt_id": None})
    df = pd.DataFrame(rows, columns=KOLOM)
    df["_cert_id"] = df["_cert_id"].astype("object")
    df["_attempt_id"] = df["_attempt_id"].astype("object")
    return df


def render():
    st.subheader("🎫 Nomor Sertifikat Peserta")
    if st.session_state.get("cert_msg"):
        st.success(st.session_state.pop("cert_msg"))
    st.caption("Nomor sertifikat diberikan oleh admin. Nomor di sini dipakai untuk sertifikat yang diunduh peserta "
               "dan untuk menu Cek Sertifikasi, jadi samakan dengan nomor yang sudah tercetak.")

    trainings = fetch_trainings_raw()
    if not trainings:
        st.info("Belum ada training.")
        return
    tname = st.selectbox("Perusahaan / Training", [t["name"] for t in trainings], key="cert_t")
    training = dict(next(t for t in trainings if t["name"] == tname))
    training["_paket"] = tebak_sertifikasi(tname)

    ikut_asesmen = st.checkbox("Tampilkan juga peserta asesmen yang belum lulus ujian online", value=False,
                               help="Berguna kalau sertifikat sudah dicetak untuk peserta yang ujiannya tidak lewat aplikasi.")

    try:
        base = _bangun_tabel(training, ikut_asesmen)
    except TabelSertifikatBelumAda:
        st.error("Tabel `certificates` belum ada di Supabase. Jalankan SQL di bawah ini SEKALI di "
                 "Supabase > SQL Editor > New query > Run, lalu muat ulang halaman ini.")
        st.code(open(SQL_SERTIFIKAT, encoding="utf-8").read(), language="sql")
        return
    except DatabaseError as e:
        st.error(f"Gagal membaca data: {e}")
        return

    ada_no = int((base["No. Sertifikat"].astype(str).str.strip() != "").sum())
    c1, c2, c3 = st.columns(3)
    c1.metric("Total peserta di daftar", len(base))
    c2.metric("Sudah bernomor", ada_no)
    c3.metric("Belum bernomor", len(base) - ada_no)

    # ---------------- Isi nomor berurutan (opsional) ----------------
    ver_key = f"cert_ver_{training['id']}"
    st.session_state.setdefault(ver_key, 0)
    prefill_key = f"cert_prefill_{training['id']}"
    with st.expander("⚡ Isi otomatis nomor berurutan untuk baris yang masih kosong"):
        e1, e2, e3 = st.columns([2, 1, 1])
        awalan = e1.text_input("Awalan", value=f"{training['_paket'] or 'CJ'}-{date.today().year}-", key="cert_awalan")
        mulai = e2.number_input("Mulai dari", min_value=1, value=1, step=1, key="cert_mulai")
        digit = e3.number_input("Jumlah digit", min_value=1, max_value=8, value=3, step=1, key="cert_digit")
        st.caption(f"Contoh hasil: {awalan}{int(mulai):0{int(digit)}d}. Nomor yang sudah terisi tidak diubah. "
                   "Hasilnya masih bisa diedit sebelum disimpan.")
        if st.button("Isi nomor kosong", key="cert_isi"):
            df = base.copy()
            n = int(mulai)
            for i in df.index:
                if _kosong(df.at[i, "No. Sertifikat"]):
                    df.at[i, "No. Sertifikat"] = f"{awalan}{n:0{int(digit)}d}"
                    if df.at[i, "Tanggal Terbit"] is None:
                        df.at[i, "Tanggal Terbit"] = date.today()
                    n += 1
            st.session_state[prefill_key] = df
            st.session_state[ver_key] += 1
            st.rerun()

    # ---------------- Import dari CSV / Excel daftar cetak ----------------
    with st.expander("📥 Import nomor dari file (CSV / Excel) daftar sertifikat yang sudah dicetak"):
        st.caption("Kolom yang dibaca: **nama**, **nomor**, dan opsional **email**, **tanggal**. "
                   "Baris dicocokkan lewat email (kalau ada), lalu lewat nama. Yang tidak cocok ditambahkan sebagai baris baru.")
        up = st.file_uploader("Pilih file", type=["csv", "xlsx"], key=f"cert_up_{training['id']}")
        if up is not None and st.button("Gabungkan ke tabel", key="cert_import"):
            try:
                imp = pd.read_csv(up) if up.name.lower().endswith(".csv") else pd.read_excel(up)
            except Exception as ex:  # noqa: BLE001
                st.error(f"File tidak bisa dibaca: {ex}")
                imp = None
            if imp is not None:
                cols = {c.lower().strip(): c for c in imp.columns}
                c_nama = next((cols[k] for k in cols if k in ("nama", "name", "nama lengkap", "full_name")), None)
                c_no = next((cols[k] for k in cols if k in ("nomor", "no", "no. sertifikat", "nomor sertifikat", "cert_no")), None)
                c_mail = next((cols[k] for k in cols if k in ("email", "e-mail")), None)
                c_tgl = next((cols[k] for k in cols if k in ("tanggal", "tanggal terbit", "issued_date")), None)
                if not c_nama or not c_no:
                    st.error("File harus punya kolom 'nama' dan 'nomor'.")
                else:
                    df = st.session_state.get(prefill_key, base).copy()
                    def _norm(x):
                        return re.sub(r"\s+", " ", str(x or "")).strip().lower()
                    cocok, baru = 0, 0
                    for _, r in imp.iterrows():
                        if _kosong(r[c_nama]):
                            continue
                        mail = "" if not c_mail or _kosong(r[c_mail]) else str(r[c_mail]).strip().lower()
                        idx = None
                        if mail:
                            m = df.index[df["Email"].astype(str).str.lower() == mail]
                            idx = m[0] if len(m) else None
                        if idx is None:
                            m = df.index[df["Nama"].map(_norm) == _norm(r[c_nama])]
                            idx = m[0] if len(m) else None
                        tgl = _tanggal(r[c_tgl]) if c_tgl else None
                        if idx is not None:
                            df.at[idx, "No. Sertifikat"] = str(r[c_no]).strip()
                            if tgl:
                                df.at[idx, "Tanggal Terbit"] = tgl
                            if mail and _kosong(df.at[idx, "Email"]):
                                df.at[idx, "Email"] = mail
                            cocok += 1
                        else:
                            df.loc[len(df)] = {"Nama": str(r[c_nama]).strip(), "Email": mail,
                                               "Paket": training["_paket"], "No. Sertifikat": str(r[c_no]).strip(),
                                               "Tanggal Terbit": tgl or date.today(), "Catatan": "",
                                               "Sumber": "Import file", "_cert_id": None, "_attempt_id": None}
                            baru += 1
                    st.session_state[prefill_key] = df.reset_index(drop=True)
                    st.session_state[ver_key] += 1
                    st.success(f"{cocok} baris dicocokkan, {baru} baris baru ditambahkan. Cek tabel, lalu klik Simpan.")
                    st.rerun()

    # ---------------- Tabel yang bisa diedit ----------------
    data = st.session_state.get(prefill_key, base)
    st.markdown("**Edit langsung di tabel.** Klik sel untuk mengubah, tambah baris di bagian bawah untuk peserta "
                "yang belum ada, pilih baris lalu tekan ikon tempat sampah untuk menghapus. "
                "Perubahan baru tersimpan setelah tombol **Simpan** ditekan.")
    edited = st.data_editor(
        data,
        key=f"cert_editor_{training['id']}_{st.session_state[ver_key]}",
        num_rows="dynamic", hide_index=True, width="stretch",
        column_order=["Nama", "Email", "Paket", "No. Sertifikat", "Tanggal Terbit", "Catatan", "Sumber"],
        column_config={
            "Nama": st.column_config.TextColumn(required=True, width="medium"),
            "Email": st.column_config.TextColumn(width="medium"),
            "Paket": st.column_config.SelectboxColumn(options=list(EXAM_PACKAGES.keys()) + ["CMBC", "CPSC", "CPPC", "CRWC", "CCTC", "Lainnya"]),
            "No. Sertifikat": st.column_config.TextColumn(width="medium", help="Samakan dengan nomor yang tercetak"),
            "Tanggal Terbit": st.column_config.DateColumn(format="DD/MM/YYYY"),
            "Catatan": st.column_config.TextColumn(),
            "Sumber": st.column_config.TextColumn(disabled=True, default="Input admin"),
        },
    )

    b1, b2, b3 = st.columns([1, 1, 2])
    simpan = b1.button("💾 Simpan", type="primary", width="stretch", key="cert_simpan")
    if b2.button("↩️ Batalkan perubahan", width="stretch", key="cert_batal"):
        st.session_state.pop(prefill_key, None)
        st.session_state[ver_key] += 1
        st.rerun()
    b3.download_button("⬇️ Download daftar (CSV)",
                       edited[["Nama", "Email", "Paket", "No. Sertifikat", "Tanggal Terbit", "Catatan"]]
                       .to_csv(index=False).encode("utf-8-sig"),
                       file_name=f"Nomor_Sertifikat_{tname.replace(' ', '_')}.csv", mime="text/csv",
                       width="stretch")

    if simpan:
        _simpan(training, base, edited, prefill_key, ver_key)


def _simpan(training, base, edited, prefill_key, ver_key):
    errors = []
    inserts, updates = [], []
    nomor_dipakai = {}
    for i, r in edited.iterrows():
        nama = "" if _kosong(r["Nama"]) else str(r["Nama"]).strip()
        nomor = "" if _kosong(r["No. Sertifikat"]) else str(r["No. Sertifikat"]).strip()
        email = "" if _kosong(r["Email"]) else str(r["Email"]).strip().lower()
        if not nama:
            if nomor or email:
                errors.append(f"Baris {i + 1}: nama wajib diisi.")
            continue
        if nomor:
            if nomor.upper() in nomor_dipakai:
                errors.append(f"Nomor **{nomor}** dipakai dua kali ({nomor_dipakai[nomor.upper()]} dan {nama}).")
            nomor_dipakai[nomor.upper()] = nama
        rec = {
            "full_name": nama, "email": email or None,
            "package": None if _kosong(r["Paket"]) else str(r["Paket"]).strip(),
            "cert_no": nomor or None,
            "issued_date": (_tanggal(r["Tanggal Terbit"]) or (date.today() if nomor else None)),
            "notes": None if _kosong(r["Catatan"]) else str(r["Catatan"]).strip(),
        }
        rec["issued_date"] = rec["issued_date"].isoformat() if rec["issued_date"] else None
        cid = r.get("_cert_id")
        att = r.get("_attempt_id")
        if not _kosong(cid):
            updates.append({"id": int(cid), **rec})
        elif nomor or str(r.get("Sumber")) in ("Input admin", "Import file", "None", "nan") or _kosong(r.get("Sumber")):
            # Baris dari ujian/asesmen yang belum diberi nomor tidak perlu disimpan dulu
            inserts.append({**rec, "exam_attempt_id": None if _kosong(att) else int(att)})

    base_ids = {int(x) for x in base["_cert_id"] if not _kosong(x)}
    kept_ids = {u["id"] for u in updates}
    deletes = sorted(base_ids - kept_ids)

    if not errors:
        try:
            bentrok = cek_nomor_dipakai(list(nomor_dipakai.keys()), list(base_ids))
        except DatabaseError as e:
            st.error(f"Gagal mengecek nomor: {e}")
            return
        for b in bentrok:
            errors.append(f"Nomor **{b}** sudah dipakai di training lain.")

    if errors:
        st.error("Belum disimpan. Perbaiki dulu:\n\n" + "\n".join(f"- {e}" for e in errors))
        return
    try:
        simpan_sertifikat(training["id"], inserts, updates, deletes)
    except DatabaseError as e:
        st.error(f"Gagal menyimpan: {e}")
        return
    st.session_state.pop(prefill_key, None)
    st.session_state[ver_key] += 1
    st.session_state["cert_msg"] = (f"Tersimpan: {len(updates)} diperbarui, {len(inserts)} ditambahkan, "
                                    f"{len(deletes)} dihapus.")
    st.rerun()
