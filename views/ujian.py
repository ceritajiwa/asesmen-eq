import json

import streamlit as st
import streamlit.components.v1 as components

from cjlib.db import DatabaseError, simpan_ujian
from cjlib.konten import paket_ujian_untuk
from cjlib.styles import footer, page_header
from cjlib.ui import peserta_sidebar, require_peserta_gate, show_db_error, subjudul

training, peserta = require_peserta_gate("📋 Ujian")
peserta_sidebar("ujian")

kode_paket, paket = paket_ujian_untuk(training)
soal_list = paket["soal"]
durasi = int(paket.get("durasi_menit", 45))
nilai_lulus = int(paket.get("nilai_lulus", 80))

col1, col2 = st.columns([3, 1])
with col1:
    page_header(f"📋 Ujian {training['sertifikasi'] or ''}", subjudul(training, peserta))
with col2:
    # Hitung mundur berjalan di browser saja, jadi halaman tidak reload
    timer_key = json.dumps(f"cj_ujian_{training['id']}_{peserta['email']}")
    components.html(
        f"""
        <div style="font-family:sans-serif; text-align:right; color:#344A61;">
          <div style="font-size:13px; color:#6D6F71;">⏱️ Sisa Waktu</div>
          <div id="t" style="font-size:30px; font-weight:800;">{durasi:02d}:00</div>
        </div>
        <script>
          const key = {timer_key};
          let end = 0;
          try {{ end = Number(sessionStorage.getItem(key)) || 0; }} catch (e) {{}}
          if (!end) {{ end = Date.now() + {durasi} * 60000; try {{ sessionStorage.setItem(key, end); }} catch (e) {{}} }}
          const el = document.getElementById("t");
          const tick = () => {{
            const s = Math.max(0, Math.round((end - Date.now()) / 1000));
            el.textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
            if (s === 0) {{ el.style.color = "#C0392B"; el.textContent = "Waktu habis"; }}
          }};
          tick(); setInterval(tick, 1000);
        </script>
        """,
        height=80,
    )

if paket.get("demo"):
    st.info("Ini **soal contoh**. Nilai bisa dilihat, tapi tidak disimpan ke database.")

st.caption(f"Ada {len(soal_list)} soal. Semua ada di halaman ini, cukup scroll ke bawah. "
           f"Nilai minimum lulus {nilai_lulus}. Jawaban baru dikirim setelah tombol **Submit Ujian** ditekan.")

# ---------------- Semua soal dalam satu form (tidak reload sampai submit) ----------------
with st.form("form_ujian", border=False):
    for i, s in enumerate(soal_list):
        with st.container(border=True, key=f"card_soal_{i}"):
            st.markdown(f"**Soal {i + 1}**")
            st.radio(s["soal"], s["opsi"], index=None, key=f"uj_{kode_paket}_{i}")
    kirim = st.form_submit_button("✅ Submit Ujian", type="primary", width="stretch")

if kirim:
    kosong = [i + 1 for i in range(len(soal_list)) if st.session_state.get(f"uj_{kode_paket}_{i}") is None]
    if kosong:
        st.error(f"Masih ada {len(kosong)} soal yang belum dijawab: nomor " + ", ".join(map(str, kosong)) + ".")
    else:
        benar = sum(
            1 for i, s in enumerate(soal_list)
            if s["opsi"].index(st.session_state[f"uj_{kode_paket}_{i}"]) == s["kunci"]
        )
        nilai = round(benar / len(soal_list) * 100)
        lulus = nilai >= nilai_lulus
        st.session_state.ujian_attempts += 1
        st.session_state.current_nilai = nilai

        if not paket.get("demo"):
            try:
                simpan_ujian(training["id"], peserta["nama"], peserta["email"], benar, nilai, lulus, kode_paket)
            except DatabaseError as e:
                show_db_error(e)
                st.stop()

        if lulus:
            st.success(f"🎉 Selamat! Anda lulus dengan nilai {nilai} ({benar} dari {len(soal_list)} benar).")
            st.balloons()
            st.markdown("Sertifikat bisa diunduh di menu **📜 Sertifikat**.")
        else:
            st.warning(f"Nilai Anda: {nilai} ({benar} dari {len(soal_list)} benar). Belum memenuhi minimum {nilai_lulus}.")
            st.info(f"Percobaan ke-{st.session_state.ujian_attempts}. Silakan perbaiki jawaban di atas lalu submit lagi.")

footer()
