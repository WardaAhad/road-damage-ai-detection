"""
=========================================================
AI Road Damage Detection System
Professional Navbar
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
from datetime import datetime

from config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    MODEL_NAME
)


# ==========================================================
# Top Navbar
# ==========================================================

def show_navbar():

    current_date = datetime.now().strftime("%d %B %Y")
    current_time = datetime.now().strftime("%I:%M %p")

    st.markdown(
        f"""
        <div style="
            background:linear-gradient(90deg,#1E3A8A,#2563EB);
            padding:20px;
            border-radius:18px;
            margin-bottom:25px;
            color:white;
            box-shadow:0 8px 20px rgba(0,0,0,.25);
        ">

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            flex-wrap:wrap;
        ">

        <div>

        <h2 style="margin:0;color:white;">
        🚧 {PROJECT_NAME}
        </h2>

        <p style="
        margin-top:5px;
        color:#E2E8F0;
        ">

        YOLOv11 • FastAPI • Streamlit

        </p>

        </div>

        <div style="
        text-align:right;
        ">

        <b>📅 {current_date}</b><br>

        🕒 {current_time}<br>

        🤖 {MODEL_NAME}

        </div>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# Welcome Banner
# ==========================================================

def welcome_banner():

    st.markdown(
        """
        <div style="
        background:#1E293B;
        border-left:6px solid #2563EB;
        padding:20px;
        border-radius:15px;
        margin-bottom:20px;
        ">

        <h3 style="color:white;margin-bottom:10px;">

        👋 Welcome

        </h3>

        <p style="color:#CBD5E1;">

        Upload a road image and detect potholes,
        cracks and road damages using the
        YOLOv11 Deep Learning Model.

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# Project Information
# ==========================================================

def project_info():

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Model",
            MODEL_NAME
        )

    with col2:

        st.metric(
            "Version",
            PROJECT_VERSION
        )

    with col3:

        st.metric(
            "Framework",
            "YOLO"
        )
