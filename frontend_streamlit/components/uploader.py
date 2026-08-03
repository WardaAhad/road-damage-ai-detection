"""
=========================================================
AI Road Damage Detection System
Image Uploader Component
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
from PIL import Image
import requests
import io

from config import (
    PREDICT_ENDPOINT,
    ALLOWED_IMAGE_TYPES
)


# ==========================================================
# Upload Image
# ==========================================================

def image_uploader():

    st.subheader("📤 Upload Road Image")

    uploaded_file = st.file_uploader(
        "Choose a road image",
        type=ALLOWED_IMAGE_TYPES
    )

    return uploaded_file


# ==========================================================
# Preview Image
# ==========================================================

def preview_image(uploaded_file):

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        width="stretch"
    )


# ==========================================================
# Send Image to FastAPI
# ==========================================================

def predict_image(uploaded_file):

    if uploaded_file is None:

        st.warning("Please upload an image.")

        return None

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    try:

        with st.spinner("Detecting Road Damage..."):

            response = requests.post(
                PREDICT_ENDPOINT,
                files=files,
                timeout=120
            )

        if response.status_code == 200:

            return response.json()

        st.error("Prediction Failed")

        return None

    except Exception as e:

        st.error(f"Connection Error\n\n{e}")

        return None


# ==========================================================
# Predict Button
# ==========================================================

def predict_button():

    return st.button(
        "🚧 Detect Damage",
        width="stretch"
    )


# ==========================================================
# Show Prediction Result
# ==========================================================

def show_prediction(result):

    if result is None:

        return

    st.success("Detection Completed")

    st.json(result)


# ==========================================================
# Download Result Image
# ==========================================================

def download_result(image_bytes):

    st.download_button(

        label="📥 Download Result",

        data=image_bytes,

        file_name="prediction.jpg",

        mime="image/jpeg",

        width="stretch"
    )
