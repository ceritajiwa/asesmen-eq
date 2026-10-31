import streamlit as st
from supabase import create_client, Client


class SupabaseNotConfigured(Exception):
    pass


@st.cache_resource(show_spinner=False)
def get_supabase() -> Client:
    url = st.secrets.get("SUPABASE_URL")
    key = st.secrets.get("SUPABASE_KEY")
    if not url or not key:
        raise SupabaseNotConfigured(
            "SUPABASE_URL / SUPABASE_KEY belum diisi di Secrets Streamlit."
        )
    return create_client(url, key)
