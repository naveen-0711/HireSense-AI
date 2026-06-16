import streamlit as st

def get_current_user():

    return st.session_state.get(
        "user_email"
    )