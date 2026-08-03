"""
=========================================================
AI Road Damage Detection System
Frontend Dashboard
Developer : Warda Ahad
=========================================================
"""

# =========================================================
# Imports
# =========================================================

import streamlit as st
import requests
from PIL import Image

from config import *

from styles.theme import (
    set_page_config,
    apply_theme,
    section_title,
    divider,
    space
)


# =========================================================
# Page Configuration
# =========================================================

set_page_config()

apply_theme()



# =========================================================
# Load Assets
# =========================================================

def load_assets():

    try:

        assets = {

            "logo": Image.open(LOGO),

            "banner": Image.open(BANNER),

            "upload": Image.open(UPLOAD_ICON),

            "detection": Image.open(DETECTION_ICON),

            "analytics": Image.open(ANALYTICS_ICON),

            "road": Image.open(ROAD_ICON),

            "github": Image.open(GITHUB_ICON)

        }

        return assets


    except Exception as e:

        st.error(

            f"❌ Failed to load assets.\n\n{e}"

        )

        st.stop()


assets = load_assets()



# =========================================================
# Backend Health Check
# =========================================================

def check_backend():

    try:

        response = requests.get(

            HEALTH_ENDPOINT,

            timeout=2

        )

        if response.status_code == 200:

            return True

        return False

    except requests.exceptions.RequestException:

        return False


backend_online = check_backend()


backend_status = (

    "🟢 Online"

    if backend_online

    else

    "🔴 Offline"

)



# =========================================================
# Project Information
# =========================================================

PROJECT_INFO = {

    "name": PROJECT_NAME,

    "developer": DEVELOPER,

    "model": MODEL_NAME,

    "framework": FRAMEWORK,

    "version": PROJECT_VERSION,

    "backend": "FastAPI",

    "frontend": "Streamlit",

    "deployment": "Railway"

}



# =========================================================
# GitHub Repository
# =========================================================

GITHUB_REPOSITORY = (

    "https://github.com/WardaAhad/ai-road-damage-detection-system"

)
# =========================================================
# Sidebar
# =========================================================

with st.sidebar:

    st.image(
        assets["logo"],
        width=170
    )

    st.markdown(
        """
        <h2 style="text-align:center;">
            🚧 AI Road Damage
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center;color:#CBD5E1;">
            Intelligent Road Inspection System
        </p>
        """,
        unsafe_allow_html=True
    )

    divider()


    # =====================================================
    # System Status
    # =====================================================

    st.subheader("🖥 System Status")

    if backend_online:

        st.success(
            f"Backend : {backend_status}"
        )

    else:

        st.error(
            f"Backend : {backend_status}"
        )

    st.success(
        f"Model : {MODEL_NAME}"
    )

    divider()


    # =====================================================
    # Technology Stack
    # =====================================================

    st.subheader("🛠 Technology Stack")

    st.markdown(
        f"""
- 🤖 **Model:** {MODEL_NAME}
- ⚡ **Backend:** FastAPI
- 🌐 **Frontend:** Streamlit
- 🚂 **Deployment:** Railway
- 🐍 **Language:** Python
"""
    )

    divider()


    # =====================================================
    # Supported Classes
    # =====================================================

    st.subheader("📂 Damage Classes")

    for cls in DAMAGE_CLASSES:

        st.write(f"• {cls}")

    divider()


    # =====================================================
    # Version Information
    # =====================================================

    st.caption(
        f"Version : {PROJECT_VERSION}"
    )

    st.caption(
        f"Developer : {DEVELOPER}"
    )


# =========================================================
# Banner
# =========================================================

st.image(
    assets["banner"],
    width="stretch"
)


space()


# =========================================================
# Hero Section
# =========================================================

st.markdown(
    f"""
    <div class="hero-container">

        <h1 class="hero-title">
            🚧 {PROJECT_NAME}
        </h1>

        <p class="hero-subtitle">

            AI-Powered Road Damage Detection using
            <b>YOLOv11</b>, <b>FastAPI</b> and
            <b>Streamlit</b>.

        </p>

        <div class="hero-badges">

            <span>⚡ Real-Time Detection</span>

            <span>🎯 High Accuracy</span>

            <span>📊 Smart Analytics</span>

            <span>🛣 Infrastructure Monitoring</span>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


space()
# =========================================================
# About Project
# =========================================================

section_title("📌 About Project")

st.write(
f"""
{DESCRIPTION}

This AI-powered application automatically detects road
damages using the **YOLOv11 Object Detection Model**.

The system is designed to assist municipalities,
engineers, and transportation departments by providing
fast, accurate, and intelligent road inspections.
"""
)

space()


# =========================================================
# Key Features
# =========================================================

section_title("🚀 Key Features")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.image(
        assets["upload"],
        width=70
    )

    st.markdown("### Upload")

    st.caption(
        "Upload Road Images"
    )


with col2:

    st.image(
        assets["detection"],
        width=70
    )

    st.markdown("### Detection")

    st.caption(
        "YOLOv11 AI Detection"
    )


with col3:

    st.image(
        assets["analytics"],
        width=70
    )

    st.markdown("### Analytics")

    st.caption(
        "Detection Statistics"
    )


with col4:

    st.image(
        assets["road"],
        width=70
    )

    st.markdown("### Smart Roads")

    st.caption(
        "Infrastructure Monitoring"
    )


divider()


# =========================================================
# Dashboard Overview
# =========================================================

section_title("📊 Dashboard Overview")

m1, m2, m3, m4 = st.columns(4)

with m1:

    st.metric(
        "🤖 Model",
        PROJECT_INFO["model"]
    )


with m2:

    st.metric(
        "⚡ Framework",
        PROJECT_INFO["framework"]
    )


with m3:

    st.metric(
        "🌐 Frontend",
        PROJECT_INFO["frontend"]
    )


with m4:

    st.metric(
        "🚀 Backend",
        PROJECT_INFO["backend"]
    )


divider()


# =========================================================
# System Status
# =========================================================

section_title("🖥 System Status")

if backend_online:

    st.success(
        "✅ Backend is running successfully. The AI Road Damage Detection System is ready to perform predictions."
    )

else:

    st.error(
        "❌ Backend server is currently offline. Please start the FastAPI server before running detections."
    )


st.info(
"""
👈 Use the sidebar to navigate through:

• Dashboard

• Detect Damage

• Analytics

• History

• About
"""
)


divider()
# =========================================================
# Project Statistics
# =========================================================

section_title("📈 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Supported Classes",
        len(DAMAGE_CLASSES)
    )

with c2:

    st.metric(
        "Image Formats",
        ", ".join(ALLOWED_IMAGE_TYPES).upper()
    )

with c3:

    st.metric(
        "Maximum Upload",
        f"{MAX_UPLOAD_SIZE_MB} MB"
    )

with c4:

    st.metric(
        "Confidence",
        f"{DEFAULT_CONFIDENCE:.2f}"
    )

divider()



# =========================================================
# Model Information
# =========================================================

section_title("🤖 AI Model Information")

left, right = st.columns([2, 1])

with left:

    st.markdown(
        f"""
### Model Details

**Model Name**
: {MODEL_NAME}

**Framework**
: {FRAMEWORK}

**Model Version**
: {MODEL_VERSION}

**Deployment**
: Railway

**Frontend**
: Streamlit

**Backend**
: FastAPI
"""
    )

    st.markdown(
        """
### Model Description

The system uses the **YOLOv11 Deep Learning Model**
to automatically detect road damages from uploaded
road images.

The model identifies multiple types of pavement
defects with high speed and accuracy, making it
suitable for intelligent transportation and
smart city applications.
"""
    )


with right:

    st.image(
        assets["detection"],
        width="stretch"
    )



divider()



# =========================================================
# Supported Damage Classes
# =========================================================

section_title("🚧 Supported Damage Classes")

class1, class2 = st.columns(2)

with class1:

    for cls in DAMAGE_CLASSES[:len(DAMAGE_CLASSES)//2]:

        st.success(f"✅ {cls}")

with class2:

    for cls in DAMAGE_CLASSES[len(DAMAGE_CLASSES)//2:]:

        st.success(f"✅ {cls}")



divider()



# =========================================================
# Detection Workflow
# =========================================================

section_title("⚙️ Detection Workflow")

st.markdown(
"""
### How the System Works

1️⃣ Upload a road image.

⬇️

2️⃣ The image is sent to the FastAPI backend.

⬇️

3️⃣ YOLOv11 processes the image.

⬇️

4️⃣ Damages are detected with bounding boxes.

⬇️

5️⃣ Confidence scores are calculated.

⬇️

6️⃣ The final annotated image and prediction
results are displayed on the dashboard.
"""
)

divider()
# =========================================================
# Backend API Information
# =========================================================

section_title("🌐 Backend API")

st.markdown(
f"""
### API Configuration

**Base URL**

`{API_BASE_URL}`

**Prediction Endpoint**

`{PREDICT_ENDPOINT}`

**Health Endpoint**

`{HEALTH_ENDPOINT}`
"""
)

divider()



# =========================================================
# GitHub Repository
# =========================================================

section_title("💻 Source Code")

left, right = st.columns([1, 5])

with left:

    st.image(
        assets["github"],
        width=60
    )

with right:

    st.markdown(
        """
### GitHub Repository

The complete source code of this project is available on GitHub.
"""
    )

    st.link_button(
        "🚀 View GitHub Repository",
        GITHUB_REPOSITORY,
        width="stretch"
    )


divider()



# =========================================================
# Developer Information
# =========================================================

section_title("👩‍💻 Developer")

st.markdown(
f"""
### Developer Profile

**Name:** {DEVELOPER}

**Project:** {PROJECT_NAME}

**AI Model:** {MODEL_NAME}

**Frontend:** Streamlit

**Backend:** FastAPI

**Deployment:** Railway

**Programming Language:** Python

**Version:** {PROJECT_VERSION}
"""
)

st.success(
"""
Thank you for using the AI Road Damage Detection System.

This application was developed as an Artificial Intelligence
Final Year Project to assist in automatic road damage
inspection using Deep Learning.
"""
)

divider()



# =========================================================
# Footer
# =========================================================

st.markdown(
f"""
<div class="footer">

<h3>🚧 {PROJECT_NAME}</h3>

<p>
AI-Powered Road Damage Detection using
<b>YOLOv11</b>
</p>

<br>

<p>

⚡ FastAPI &nbsp; | &nbsp;

🌐 Streamlit &nbsp; | &nbsp;

🚂 Railway &nbsp; | &nbsp;

🤖 {MODEL_NAME}

</p>

<br>

<p>

Version <b>{PROJECT_VERSION}</b>

</p>

<p>

© 2026 {DEVELOPER}

</p>

</div>
""",
unsafe_allow_html=True
)

