import streamlit as st

NAVY = "#344A61"

def apply_ceritajiwa_styles():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
    .main {{ background-color: #FAFBFC; }}
    h1, h2, h3, h4, h5, h6 {{ color: {NAVY} !important; font-weight: 700 !important; }}
    .stButton>button {{ background-color: {NAVY}; color: white; border-radius: 8px; border: none; padding: 10px 24px; font-weight: 600; }}
    .stButton>button:hover {{ background-color: #2A3D52; color: white; }}
    .stButton>button[kind="secondary"] {{ background-color: transparent; color: {NAVY}; border: 2px solid {NAVY}; }}
    .stTabs [data-baseweb="tab"] {{ background-color: #F5F7FA; border-radius: 8px 8px 0 0; padding: 12px 24px; font-weight: 600; }}
    .stTabs [aria-selected="true"] {{ background-color: {NAVY} !important; color: white !important; }}
    .card {{ background-color: white; border-radius: 16px; padding: 28px; box-shadow: 0 2px 12px rgba(52,74,97,0.06); border: 1px solid #EEF0F4; margin-bottom: 16px; }}
    .badge-active {{ background-color: #E8F5E9; color: #2E7D32; padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; display: inline-block; }}
    .badge-pending {{ background-color: #FFF3E0; color: #EF6C00; padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; display: inline-block; }}
    </style>
    """, unsafe_allow_html=True)

def card(title, content, status=None):
    badge = ""
    if status == "active": badge = '<span class="badge-active">AKTIF</span>'
    elif status == "pending": badge = '<span class="badge-pending">MENUNGGU</span>'
    st.markdown(f"""
    <div class="card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <h4 style="margin:0; color:#344A61;">{title}</h4> {badge}
        </div>
        <p style="color:#6D6F71; margin:0; line-height:1.6;">{content}</p>
    </div>
    """, unsafe_allow_html=True)
