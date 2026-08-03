"""
=========================================================
AI Road Damage Detection System
About
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
from components.navbar import show_navbar
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
    "ℹ️ About Project",
    "Learn more about the AI Road Damage Detection System."
)

st.divider()

# ==========================================================
# Project Overview
# ==========================================================

section_title("🚧 Project Overview")

st.markdown("""
The **AI Road Damage Detection System** is a Deep Learning based web
application that automatically detects road damages from images.

The project is developed using **YOLOv11**, **FastAPI** and
**Streamlit** to provide fast and accurate road damage detection.

The system can identify multiple types of road damages and generate
prediction results within a few seconds.
""")

st.divider()

# ==========================================================
# Project Features
# ==========================================================

section_title("✨ Features")

col1, col2 = st.columns(2)

with col1:

    st.success("✅ Road Crack Detection")

    st.success("✅ Pothole Detection")

    st.success("✅ Road Patch Detection")

    st.success("✅ Real-time Prediction")

with col2:

    st.success("✅ FastAPI Backend")

    st.success("✅ Streamlit Dashboard")

    st.success("✅ YOLOv11 Model")

    st.success("✅ Download Reports")

st.divider()

# ==========================================================
# Technology Stack
# ==========================================================

section_title("🛠 Technology Stack")

tech = {
    "Frontend": "Streamlit",
    "Backend": "FastAPI",
    "Model": "YOLOv11",
    "Language": "Python",
    "Deep Learning": "PyTorch",
    "Deployment": "Local / Cloud"
}

st.table(tech)

st.divider()
# ==========================================================
# Developer Information
# ==========================================================

section_title("👩‍💻 Developer")

col1, col2 = st.columns([1, 2])

with col1:

    st.markdown(
        """
# 👩‍💻

### Warda Ahad
AI Engineer
"""
    )

with col2:

    st.markdown("""
**Developer:** Warda Ahad

**Degree:** BS Artificial Intelligence

**Specialization:**
- Machine Learning
- Deep Learning
- Computer Vision
- FastAPI
- Streamlit
- Python

This project was developed as an AI-powered road damage detection
system using YOLOv11 for accurate and fast road surface analysis.
""")

st.divider()

# ==========================================================
# Project Workflow
# ==========================================================

section_title("🔄 Project Workflow")

st.markdown("""
### Step 1
📤 Upload Road Image

⬇️

### Step 2
🤖 YOLOv11 Detects Damage

⬇️

### Step 3
📊 Detection Results Generated

⬇️

### Step 4
📄 View Report & Analytics

⬇️

### Step 5
📥 Download Detection Report
""")

st.divider()

# ==========================================================
# Future Improvements
# ==========================================================

section_title("🚀 Future Improvements")

st.info("""
✅ Video Damage Detection

✅ Live Camera Detection

✅ GPS Integration

✅ Mobile Application

✅ Cloud Deployment

✅ User Authentication

✅ Database Integration

✅ AI Report Generation
""")

st.divider()

# ==========================================================
# Libraries Used
# ==========================================================

section_title("📚 Libraries")

libraries = [
    "Python",
    "Streamlit",
    "FastAPI",
    "Ultralytics YOLO",
    "OpenCV",
    "PyTorch",
    "NumPy",
    "Pandas",
    "Plotly",
    "Pillow",
    "Requests"
]

st.dataframe(
    libraries,
    width="stretch",
    hide_index=True
)

st.divider()

# ==========================================================
# Contact Information
# ==========================================================

section_title("📬 Contact")

st.markdown("""
📧 **Email:** your_email@example.com

💻 **GitHub:** https://github.com/WardaAhad

🔗 **LinkedIn:** https://linkedin.com/in/your-linkedin

🌍 **Project:** AI Road Damage Detection System
""")

st.divider()

# ==========================================================
# Project Version
# ==========================================================

section_title("📦 Version")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Version", "1.0")

with col2:
    st.metric("Model", "YOLOv11")

with col3:
    st.metric("Status", "Production")

st.divider()

# ==========================================================
# Acknowledgement
# ==========================================================

section_title("🙏 Acknowledgement")

st.success("""
This project was developed as part of an Artificial Intelligence
project to demonstrate real-time road damage detection using
Deep Learning and Computer Vision technologies.
""")

st.divider()

# ==========================================================
# Footer
# ==========================================================

show_footer()
