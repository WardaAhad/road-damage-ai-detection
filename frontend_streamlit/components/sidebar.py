"""
=========================================================
AI Road Damage Detection System
Professional Sidebar
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
import requests

from config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    DEVELOPER,
    MODEL_NAME,
    HEALTH_ENDPOINT
)


# ==========================================================
# Backend Status
# ==========================================================

def get_backend_status():
    """
    Check FastAPI Backend
    """

    try:

        response = requests.get(
            HEALTH_ENDPOINT,
            timeout=3
        )

        if response.status_code == 200:
            return "🟢 Online"

        return "🔴 Offline"

    except Exception:

        return "🔴 Offline"


# ==========================================================
# Sidebar
# ==========================================================

def show_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div style='text-align:center;'>

            <h1 style='font-size:65px;margin-bottom:5px;'>
            🚧
            </h1>

            <h2 style='margin-bottom:0px;'>
            AI Road Damage
            </h2>

            <p style='color:#CBD5E1;'>
            Detection System
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.markdown("### 📌 Navigation")

        st.page_link(
            "app.py",
            label="🏠 Home"
        )

        st.page_link(
            "pages/1_Dashboard.py",
            label="📊 Dashboard"
        )

        st.page_link(
            "pages/2_Detect_Damage.py",
            label="🚧 Detect Damage"
        )

        st.page_link(
            "pages/3_Analytics.py",
            label="📈 Analytics"
        )

        st.page_link(
            "pages/4_History.py",
            label="🕓 History"
        )

        st.page_link(
            "pages/5_About.py",
            label="ℹ About"
        )

        st.divider()

        st.markdown("### 🤖 Model")

        st.info(MODEL_NAME)

        st.markdown("### 🌐 Backend")

        st.success(get_backend_status())

        st.markdown("### 📦 Version")

        st.write(PROJECT_VERSION)

        st.markdown("### 👩‍💻 Developer")

        st.write(DEVELOPER)

        st.divider()

        st.caption("© 2026 AI Road Damage Detection")


# ==========================================================
# Sidebar Footer
# ==========================================================

def sidebar_footer():

    st.sidebar.markdown(
        """
        ---
        ❤️ Built with Streamlit & FastAPI
        """,
        unsafe_allow_html=True
    )
