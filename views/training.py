import streamlit as st

from utils.styles import footer, page_header
from utils.ui import peserta_sidebar, require_peserta_gate

training, peserta = require_peserta_gate("🎓 Training")
peserta_sidebar("training")

page_header(f"🎓 Training {training['sertifikasi']}",
            f"{peserta['nama']} · {training['perusahaan']} · Batch {training['batch']}")

st.info("📚 Materi training akan ditampilkan di sini.")

with st.container(border=True, key="card_training_1"):
    st.markdown("### Jadwal Training Hari Ini")
    st.markdown(
        """
- **08:00 - 09:00** : Asesmen
- **09:00 - 12:00** : Sesi Pagi
- **12:00 - 13:00** : Istirahat
- **13:00 - 16:00** : Sesi Sore
- **16:00 - 17:00** : Ujian
"""
    )

footer()
