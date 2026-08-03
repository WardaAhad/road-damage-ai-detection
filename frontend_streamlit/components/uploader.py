"""
=========================================================
AI Road Damage Detection System
Image Uploader Component
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
import requests

from config import PREDICT_ENDPOINT


# ==========================================================
# Predict Image
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

        with st.spinner("🚧 Detecting Road Damage..."):

            response = requests.post(
                PREDICT_ENDPOINT,
                files=files,
                timeout=120
            )


        # ==============================
        # Debug Response
        # ==============================

        st.write("### Backend Response")

        st.write(
            "Status Code:",
            response.status_code
        )


        st.write("Response Text:")

        st.code(
            response.text
        )


        # ==============================
        # Success
        # ==============================

        if response.status_code == 200:

            result = response.json()

            return result


        else:

            st.error(
                f"Prediction Failed: {response.status_code}"
            )

            return None



    except requests.exceptions.ConnectionError:

        st.error(
            """
            ❌ Backend Connection Failed

            Make sure FastAPI backend is running:
            
            uvicorn main:app --reload
            """
        )

        return None



    except Exception as e:

        st.error(
            f"Error: {e}"
        )

        return None



# ==========================================================
# Image Upload UI
# ==========================================================

def image_uploader():

    st.subheader("📤 Upload Road Image")


    uploaded_file = st.file_uploader(
        "Choose Road Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )


    if uploaded_file:


        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )


        if st.button("🚧 Detect Damage"):


            result = predict_image(
                uploaded_file
            )


            if result:


                st.success(
                    "Detection Completed Successfully"
                )


                st.json(
                    result
                )