import streamlit as st
from supabase import create_client, Client

def get_supabase() -> Client:
    """Get Supabase client using Streamlit secrets."""
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
    except Exception:
        url = st.secrets.get("SUPABASE_URL", "https://your-project.supabase.co")
        key = st.secrets.get("SUPABASE_KEY", "your-anon-key")
    return create_client(url, key)
