"""
=========================================================
AI Road Damage Detection System
Dashboard
Developer : Warda Ahad
=========================================================
"""

import streamlit as st

# Theme
from styles.theme import (
    set_page_config,
    apply_theme,
    hero_title,
    section_title
)

# Components
from components.sidebar import show_sidebar
from components.navbar import (
    show_navbar,
    welcome_banner,
    project_info
)
from components.cards import (
    dashboard_cards,
    statistics,
    model_information
)
from components.charts import dashboard_charts
from components.footer import show_footer

# ==========================================================
# Page Configuration
# ==========================================================

set_page_config()
apply_theme()

# ==========================================================
# Sidebar
# ==========================================================

show_sidebar()

# ==========================================================
# Navbar
# ==========================================================

show_navbar()

# ==========================================================
# Hero Section
# ==========================================================

hero_title(
    "🚧 AI Road Damage Detection",
    "Detect Road Cracks, Potholes and Surface Damage using YOLOv11 Deep Learning"
)

# ==========================================================
# Welcome Banner
# ==========================================================

welcome_banner()

# ==========================================================
# Project Information
# ==========================================================

project_info()

st.divider()

# ==========================================================
# Dashboard Cards
# ==========================================================

section_title("📊 Dashboard Overview")

dashboard_cards()

st.divider()

# ==========================================================
# Statistics
# ==========================================================

statistics()

st.divider()

# ==========================================================
# Model Information
# ==========================================================

model_information()

st.divider()

# ==========================================================
# Analytics
# ==========================================================

section_title("📉 Analytics")

dashboard_charts()

st.divider()
# ==========================================================
# Recent Activity
# ==========================================================

section_title("🕒 Recent Detection Activity")

activity_data = [
    {
        "Image": "road_001.jpg",
        "Damage": "Crack",
        "Confidence": "98%"
    },
    {
        "Image": "road_002.jpg",
        "Damage": "Pothole",
        "Confidence": "95%"
    },
    {
        "Image": "road_003.jpg",
        "Damage": "Patch",
        "Confidence": "92%"
    },
    {
        "Image": "road_004.jpg",
        "Damage": "Crack",
        "Confidence": "97%"
    }
]

st.dataframe(
    activity_data,
    width="stretch",
    hide_index=True
)

st.divider()

# ==========================================================
# System Status
# ==========================================================

section_title("⚙️ System Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🟢 FastAPI Backend")

with col2:
    st.success("🟢 YOLOv11 Loaded")

with col3:
    st.success("🟢 Streamlit Running")

st.divider()

# ==========================================================
# Quick Actions
# ==========================================================

section_title("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "🚧 Detect Damage",
        width="stretch"
    ):
        st.switch_page("pages/2_Detect_Damage.py")

with col2:

    if st.button(
        "📊 Analytics",
        width="stretch"
    ):
        st.switch_page("pages/3_Analytics.py")

with col3:

    if st.button(
        "📜 History",
        width="stretch"
    ):
        st.switch_page("pages/4_History.py")

st.divider()

# ==========================================================
# About Project
# ==========================================================

section_title("ℹ️ About Project")

st.info("""
This AI Road Damage Detection System uses the
YOLOv11 Deep Learning Model to detect:

✅ Road Cracks

✅ Potholes

✅ Road Patches

The system is powered by:

• Streamlit Frontend

• FastAPI Backend

• YOLOv11 Model

• OpenCV Image Processing
""")

st.divider()

# ==========================================================
# Tips
# ==========================================================

section_title("💡 Tips")

st.markdown("""
- Upload a clear road image.
- Supported formats: JPG, JPEG, PNG.
- Keep image resolution high for better detection.
- Wait until prediction is completed before uploading another image.
""")

st.divider()

# ==========================================================
# Footer
# ==========================================================

show_footer()
