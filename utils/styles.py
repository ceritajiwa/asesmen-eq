import streamlit as st

NAVY = "#344A61"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#D9DBDC"
MED_GRAY = "#6D6F71"
DARK_BG = "#2A3D52"
GREEN = "#22C55E"
ORANGE = "#EF6C00"

def apply_ceritajiwa_styles():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}
    
    .main {{
        background-color: #FAFBFC;
    }}
    
    h1, h2, h3, h4, h5, h6 {{
        color: {NAVY} !important;
        font-weight: 700 !important;
    }}
    
    .stButton>button {{
        background-color: {NAVY};
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.2s;
    }}
    
    .stButton>button:hover {{
        background-color: {DARK_BG};
        color: white;
        transform: translateY(-1px);
    }}
    
    .stButton>button[kind="secondary"] {{
        background-color: transparent;
        color: {NAVY};
        border: 2px solid {NAVY};
    }}
    
    .stButton>button[kind="secondary"]:hover {{
        background-color: {NAVY};
        color: white;
    }}
    
    div[data-testid="stSidebarNav"] {{
        background-color: {NAVY};
    }}
    
    .st-emotion-cache-1cypcdb {{
        background-color: {NAVY};
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background-color: #F5F7FA;
        border-radius: 8px 8px 0 0;
        padding: 12px 24px;
        font-weight: 600;
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: {NAVY} !important;
        color: white !important;
    }}
    
    .stProgress > div > div > div > div {{
        background-color: {NAVY};
    }}
    
    .stRadio > div {{
        gap: 12px;
    }}
    
    .stRadio [role="radiogroup"] label {{
        padding: 8px 16px;
        border-radius: 8px;
        border: 1px solid {LIGHT_GRAY};
        background-color: white;
    }}
    
    .stRadio [role="radiogroup"] label:hover {{
        border-color: {NAVY};
    }}
    
    div[data-testid="stMetricValue"] {{
        color: {NAVY};
        font-weight: 700;
    }}
    
    .stDataFrame {{
        border-radius: 12px;
        overflow: hidden;
    }}
    
    .stAlert {{
        border-radius: 12px;
    }}
    
    .card {{
        background-color: white;
        border-radius: 16px;
        padding: 28px;
        box-shadow: 0 2px 12px rgba(52,74,97,0.06);
        border: 1px solid #EEF0F4;
        margin-bottom: 16px;
    }}
    
    .badge-active {{
        background-color: #E8F5E9;
        color: #2E7D32;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
    }}
    
    .badge-pending {{
        background-color: #FFF3E0;
        color: {ORANGE};
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
    }}
    
    .badge-locked {{
        background-color: #ECEFF1;
        color: {MED_GRAY};
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
    }}
    
    .badge-lulus {{
        background-color: #E8F5E9;
        color: #2E7D32;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
    }}
    
    .badge-gagal {{
        background-color: #FFEBEE;
        color: #C62828;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
    }}
    </style>
    """, unsafe_allow_html=True)

def card(title, content, status=None):
    badge = ""
    if status == "active":
        badge = '<span class="badge-active">AKTIF</span>'
    elif status == "pending":
        badge = '<span class="badge-pending">MENUNGGU</span>'
    elif status == "locked":
        badge = '<span class="badge-locked">BELUM DIBELI</span>'
    elif status == "lulus":
        badge = '<span class="badge-lulus">LULUS</span>'
    elif status == "gagal":
        badge = '<span class="badge-gagal">BELUM LULUS</span>'
    
    st.markdown(f"""
    <div class="card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <h4 style="margin:0; color:#344A61;">{title}</h4>
            {badge}
        </div>
        <p style="color:#6D6F71; margin:0; line-height:1.6;">{content}</p>
    </div>
    """, unsafe_allow_html=True)

def sidebar_branding():
    st.sidebar.markdown(f"""
    <div style="text-align:center; padding: 20px 0;">
        <img src="app/static/logo_white.png" width="140" style="margin-bottom:12px;">
        <p style="color:white; font-size:14px; font-weight:600; margin:0;">Cerita Jiwa</p>
        <p style="color:rgba(255,255,255,0.6); font-size:12px; margin:4px 0 0 0;">Training Center</p>
    </div>
    <hr style="border-color:rgba(255,255,255,0.15); margin:16px 0;">
    """, unsafe_allow_html=True)
