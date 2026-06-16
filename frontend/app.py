


import streamlit as st

if "user_email" not in st.session_state:

    st.session_state["user_email"] = (
        "partha@test.com"
    )


st.set_page_config(
    page_title="HireSense AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------------
# Session State
# ---------------------

if "user" not in st.session_state:
    st.session_state.user = None

# ---------------------
# Sidebar
# ---------------------

st.sidebar.title("🤖 HireSense AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Login",
        "Dashboard",
        "Resume Analyzer",
        "Semantic Search",
        "Recruiter Chatbot",
        "Analytics"
    ]
)

# ---------------------
# Home
# ---------------------

if page == "Home":

    st.title("🤖 HireSense AI")

    st.subheader(
        "AI Recruitment Intelligence Platform"
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Resumes Supported",
            "10,000+"
        )

    with col2:
        st.metric(
            "AI Modules",
            "8"
        )

    with col3:
        st.metric(
            "Search Type",
            "Semantic"
        )

    st.markdown("---")

    st.header("🚀 Core Features")

    st.write("✅ AI Resume Analysis")
    st.write("✅ Candidate Ranking")
    st.write("✅ Semantic Search")
    st.write("✅ RAG Recruiter Chatbot")
    st.write("✅ Voice Recruiter Assistant")
    st.write("✅ Duplicate Resume Detection")

# ---------------------
# Login
# ---------------------

elif page == "Login":

    st.title("🔐 Login")

    st.info(
        "Authenticate using your Google Account"
    )

    if st.button("Login with Google"):
        st.switch_page("pages/login.py")

# ---------------------
# Dashboard
# ---------------------

elif page == "Dashboard":

    if st.session_state.user is None:

        st.warning(
            "Please login first."
        )

        st.stop()

    st.title("📊 Dashboard")

    st.success(
        "Welcome Recruiter"
    )

# ---------------------
# Resume Analyzer
# ---------------------

elif page == "Resume Analyzer":

    st.title("📄 Resume Analyzer")

    st.info("Coming Soon")

# ---------------------
# Semantic Search
# ---------------------

elif page == "Semantic Search":

    st.title("🔍 Semantic Search")

    st.info("Coming Soon")

# ---------------------
# Recruiter Chatbot
# ---------------------

elif page == "Recruiter Chatbot":

    st.title("🤖 Recruiter Chatbot")

    st.info("Coming Soon")

# ---------------------
# Analytics
# ---------------------

elif page == "Analytics":

    st.title("📈 Analytics")

    st.info("Coming Soon")