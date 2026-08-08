"""
=========================================================
AI Road Damage Detection System
Frontend (Streamlit)
Developer : Warda Ahad
=========================================================
"""

import os
import requests
import streamlit as st
from PIL import Image
from io import BytesIO


# ==========================================================
# BASE DIRECTORY
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

PAGE_TITLE = "AI Road Damage Detection System"
PAGE_ICON = "🚧"
LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)


# ==========================================================
# BACKEND API CONFIGURATION
# ==========================================================

# Prefer Streamlit secrets (set in Streamlit Cloud -> App settings -> Secrets),
# fall back to the hardcoded Railway URL if no secret is set.
API_BASE_URL = st.secrets.get(
    "API_URL",
    "https://road-damage-ai-detection-production.up.railway.app",
)

PREDICT_ENDPOINT = f"{API_BASE_URL}/predict"
HEALTH_ENDPOINT = f"{API_BASE_URL}/health"
MODEL_INFO_ENDPOINT = f"{API_BASE_URL}/model-info"
DOWNLOAD_ENDPOINT = f"{API_BASE_URL}/download"


# ==========================================================
# FILE CONFIGURATION
# ==========================================================

ALLOWED_IMAGE_TYPES = ["jpg", "jpeg", "png", "webp"]
MAX_UPLOAD_SIZE_MB = 10


# ==========================================================
# ASSETS (optional — only used if the files exist)
# ==========================================================

ASSETS_DIR = os.path.join(BASE_DIR, "assets")
LOGO_PATH = os.path.join(ASSETS_DIR, "logo.png")
BANNER_PATH = os.path.join(ASSETS_DIR, "banner.png")


# ==========================================================
# APP SETTINGS
# ==========================================================

APP_NAME = "AI Road Damage Detection System"
APP_VERSION = "1.0.0"
MODEL_NAME = "YOLOv11"
CONFIDENCE_THRESHOLD = 0.25
BACKEND_TIMEOUT = 120


# ==========================================================
# HELPERS
# ==========================================================

def check_backend_health() -> dict | None:
    try:
        res = requests.get(HEALTH_ENDPOINT, timeout=10)
        if res.status_code == 200:
            return res.json()
    except requests.exceptions.RequestException:
        return None
    return None


def run_prediction(image_bytes: bytes, filename: str) -> dict | None:
    try:
        files = {"file": (filename, image_bytes)}
        res = requests.post(PREDICT_ENDPOINT, files=files, timeout=BACKEND_TIMEOUT)
        if res.status_code == 200:
            return res.json()
        st.error(f"Backend Error ({res.status_code}): {res.text}")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"Could not reach backend: {e}")
        return None


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, use_container_width=True)

    st.title(APP_NAME)
    st.caption(f"v{APP_VERSION} · {MODEL_NAME}")

    st.divider()

    st.subheader("Backend Status")
    health = check_backend_health()

    if health:
        st.success("Backend Online")
        st.json(health)
    else:
        st.error("Backend Unreachable")
        st.caption(f"Tried: {HEALTH_ENDPOINT}")

    st.divider()
    st.caption(f"API Base URL:\n{API_BASE_URL}")


# ==========================================================
# MAIN PAGE
# ==========================================================

if os.path.exists(BANNER_PATH):
    st.image(BANNER_PATH, use_container_width=True)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.write(
    "Upload a road image and the YOLOv11 model will detect and highlight "
    "road damage (potholes, cracks, etc.)."
)

uploaded_file = st.file_uploader(
    "Upload a road image",
    type=ALLOWED_IMAGE_TYPES,
    help=f"Max file size: {MAX_UPLOAD_SIZE_MB} MB",
)

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    size_mb = len(file_bytes) / (1024 * 1024)

    if size_mb > MAX_UPLOAD_SIZE_MB:
        st.error(f"File too large ({size_mb:.1f} MB). Max is {MAX_UPLOAD_SIZE_MB} MB.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(Image.open(BytesIO(file_bytes)), use_container_width=True)

        if st.button("🔍 Detect Road Damage", type="primary", use_container_width=True):
            with st.spinner("Running YOLOv11 detection..."):
                result = run_prediction(file_bytes, uploaded_file.name)

            if result and result.get("success"):
                with col2:
                    st.subheader("Detection Result")
                    result_filename = result.get("filename")
                    try:
                        img_res = requests.get(
                            f"{DOWNLOAD_ENDPOINT}/{result_filename}", timeout=30
                        )
                        if img_res.status_code == 200:
                            st.image(
                                Image.open(BytesIO(img_res.content)),
                                use_container_width=True,
                            )
                            st.download_button(
                                "⬇️ Download Result Image",
                                data=img_res.content,
                                file_name=f"detected_{result_filename}",
                                mime="image/jpeg",
                                use_container_width=True,
                            )
                    except requests.exceptions.RequestException:
                        st.warning("Could not load the annotated result image.")

                st.divider()

                m1, m2 = st.columns(2)
                m1.metric("Objects Detected", result.get("total_objects", 0))
                m2.metric("Processing Time", f"{result.get('processing_time', 0)} s")

                detections = result.get("detections", [])
                if detections:
                    st.subheader("Detections")
                    st.dataframe(detections, use_container_width=True)
                else:
                    st.info("No damage detected in this image.")
else:
    st.info("👆 Upload an image to get started.")