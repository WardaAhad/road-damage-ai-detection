"""
=========================================================
AI Road Damage Detection System
Theme Manager
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
from pathlib import Path
import sys
import os


# =========================================================
# Add frontend_streamlit Path
# =========================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


# =========================================================
# Config
# =========================================================

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE
)


# =========================================================
# Page Configuration
# =========================================================

def set_page_config():

    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=LAYOUT,
        initial_sidebar_state=SIDEBAR_STATE
    )


# =========================================================
# Google Fonts
# =========================================================

def load_fonts():

    st.markdown(
        """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
""",
        unsafe_allow_html=True
    )


# =========================================================
# Load Custom CSS
# =========================================================

def load_css():

    css_file = Path(__file__).parent / "custom.css"

    if css_file.exists():

        with open(css_file, "r", encoding="utf-8") as file:
            css = file.read()

        st.markdown(
            f"""
            <style>
            {css}
            </style>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("custom.css not found.")


# =========================================================
# Apply Theme
# =========================================================

def apply_theme():

    load_fonts()
    load_css()


# =========================================================
# Hero Title
# =========================================================

def hero_title(title, subtitle=""):

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg,#0F172A,#1E40AF);
            padding:35px;
            border-radius:18px;
            text-align:center;
            color:white;
            margin-bottom:25px;
            box-shadow:0 8px 20px rgba(0,0,0,.25);
        ">

            <h1 style="
                font-size:42px;
                margin-bottom:10px;
                font-weight:700;
            ">
                {title}
            </h1>

            <p style="
                font-size:18px;
                color:#E5E7EB;
                margin:0;
            ">
                {subtitle}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Section Title
# =========================================================

def section_title(title):

    st.markdown(
        f"""
        <h2 style="
            color:#1E3A8A;
            font-size:28px;
            font-weight:700;
            margin-top:20px;
            margin-bottom:15px;
        ">
            {title}
        </h2>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Divider
# =========================================================

def divider():

    st.markdown(
        """
        <hr style="
            border:none;
            height:1px;
            background:#d1d5db;
            margin-top:25px;
            margin-bottom:25px;
        ">
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Empty Space
# =========================================================

def space(lines=1):

    for _ in range(lines):
        st.write("")


# =========================================================
# Success Message
# =========================================================

def success_box(message):

    st.success(message)


# =========================================================
# Warning Message
# =========================================================

def warning_box(message):

    st.warning(message)


# =========================================================
# Error Message
# =========================================================

def error_box(message):

    st.error(message)


# =========================================================
# Info Message
# =========================================================

def info_box(message):

    st.info(message)
