import html

import streamlit as st

# Brand Guideline Cerita Jiwa V2.0
NAVY = "#344A61"
NAVY_DARK = "#2A3D52"
GRAY = "#6D6F71"
LIGHT_GRAY = "#D9DBDC"
TOSCA = "#4FA8A3"  # aksen, dipakai seperlunya saja
BG = "#F7F8FA"


def apply_ceritajiwa_styles():
    st.markdown(
        f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700;6..12,800&display=swap');

    html, body, [class*="css"], .stMarkdown, button, input, textarea, select {{
        font-family: 'Avenir Next', 'Nunito Sans', sans-serif;
    }}
    .stApp {{ background: {BG}; }}
    .block-container {{ padding-top: 2.2rem; padding-bottom: 3rem; max-width: 1100px; }}
    h1, h2, h3, h4, h5, h6 {{ color: {NAVY} !important; font-weight: 800 !important; letter-spacing: -0.01em; }}
    p, li, label {{ color: #3B4350; }}

    /* ---------- Tombol ---------- */
    button[data-testid^="stBaseButton-primary"], button[data-testid^="stBaseButton-secondary"] {{
        border-radius: 10px; font-weight: 700; transition: all .15s ease; box-shadow: none;
    }}
    button[data-testid^="stBaseButton-primary"] {{
        background: {NAVY} !important; color: #fff !important; border: 1px solid {NAVY} !important;
    }}
    button[data-testid^="stBaseButton-primary"] * {{ color: #fff !important; }}
    button[data-testid^="stBaseButton-primary"]:hover {{
        background: {NAVY_DARK} !important; border-color: {NAVY_DARK} !important;
    }}
    button[data-testid^="stBaseButton-secondary"] {{
        background: #fff; color: {NAVY}; border: 1.5px solid {NAVY};
    }}
    button[data-testid^="stBaseButton-secondary"]:hover {{
        background: {NAVY}; color: #fff; border-color: {NAVY};
    }}
    button[data-testid^="stBaseButton-secondary"]:hover * {{ color: #fff; }}

    /* ---------- Kartu form & container ---------- */
    [class*="st-key-card_"] {{ background: #fff; border-radius: 16px; border-color: #E6E9EE !important; padding: 22px; }}
    [class*="st-key-card_sertifikat"] [data-testid="stMetricValue"] {{ font-size: 22px; font-weight: 800; color: {NAVY}; }}
    [data-testid="stForm"] {{ background: #fff; border-radius: 16px; border-color: #E6E9EE; padding: 22px; }}

    /* ---------- Input ---------- */
    .stTextInput input, .stDateInput input, .stNumberInput input {{ border-radius: 10px; }}
    div[data-baseweb="select"] > div {{ border-radius: 10px; }}

    /* ---------- Sidebar navy ---------- */
    section[data-testid="stSidebar"] {{ background: {NAVY}; }}
    section[data-testid="stSidebar"] * {{ color: #fff; }}
    section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"]:hover,
    section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"][aria-current="page"] {{
        background: rgba(255,255,255,0.12);
    }}
    section[data-testid="stSidebar"] .stButton > button {{
        background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.35);
    }}
    section[data-testid="stSidebar"] .stButton > button:hover {{
        background: rgba(255,255,255,0.12); border-color: #fff;
    }}
    section[data-testid="stSidebar"] hr {{ border-color: rgba(255,255,255,0.15); }}

    /* ---------- Komponen ---------- */
    .cj-card {{
        background: #fff; border-radius: 16px; padding: 24px 26px;
        border: 1px solid #ECEEF1; box-shadow: 0 2px 14px rgba(52,74,97,0.05);
        margin-bottom: 16px;
    }}
    .cj-cert {{ border-top: 3px solid {TOSCA}; height: 100%; }}
    .cj-cert .kode {{ font-size: 13px; font-weight: 800; letter-spacing: .12em; color: {TOSCA}; margin: 0 0 6px; }}
    .cj-cert .nama {{ font-size: 17px; font-weight: 800; color: {NAVY}; margin: 0 0 6px; }}
    .cj-cert .desk {{ font-size: 14px; color: {GRAY}; margin: 0; }}
    .cj-eyebrow {{ font-size: 12px; font-weight: 800; letter-spacing: .14em; text-transform: uppercase; color: {TOSCA}; margin: 0 0 4px; }}
    .cj-sub {{ color: {GRAY}; font-size: 16px; margin-top: -6px; }}
    .cj-chip {{
        display: inline-block; background: #EEF2F6; color: {NAVY}; border-radius: 999px;
        padding: 4px 12px; font-size: 13px; font-weight: 700; margin: 0 6px 6px 0;
    }}
    .cj-footer {{ text-align: center; color: {GRAY}; font-size: 13px; padding: 24px 0 4px; }}
    .badge-active {{ background: #E6F4F2; color: #2E7D74; padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 800; display: inline-block; }}
    .badge-pending {{ background: #FFF3E0; color: #EF6C00; padding: 4px 14px; border-radius: 20px; font-size: 12px; font-weight: 800; display: inline-block; }}

    /* Menu beranda: tombol lebih tinggi */
    .st-key-menu_beranda .stButton > button {{
        min-height: 64px; font-size: 16px; background: #fff; color: {NAVY};
        border: 1px solid #E3E7EC; box-shadow: 0 2px 10px rgba(52,74,97,0.05);
    }}
    .st-key-menu_beranda .stButton > button:hover {{ border-color: {NAVY}; background: #fff; color: {NAVY}; transform: translateY(-1px); }}

    #MainMenu, footer {{ visibility: hidden; }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def esc(text) -> str:
    return html.escape(str(text if text is not None else ""))


def page_header(title: str, subtitle: str | None = None, eyebrow: str | None = None):
    eb = f"<p class='cj-eyebrow'>{esc(eyebrow)}</p>" if eyebrow else ""
    sub = f"<p class='cj-sub'>{esc(subtitle)}</p>" if subtitle else ""
    st.markdown(f"{eb}<h1 style='margin:0 0 4px;'>{esc(title)}</h1>{sub}", unsafe_allow_html=True)


def footer():
    st.markdown(
        "<div class='cj-footer'>© 2026 Cerita Jiwa Training Center · PT Cerita Jaya Pratama</div>",
        unsafe_allow_html=True,
    )


def card(title, content, status=None):
    badge = ""
    if status == "active":
        badge = '<span class="badge-active">AKTIF</span>'
    elif status == "pending":
        badge = '<span class="badge-pending">MENUNGGU</span>'
    st.markdown(
        f"""<div class="cj-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <h4 style="margin:0;">{esc(title)}</h4> {badge}
        </div>
        <p style="color:{GRAY}; margin:0; line-height:1.6;">{esc(content)}</p>
        </div>""",
        unsafe_allow_html=True,
    )
