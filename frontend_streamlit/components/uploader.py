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
# Upload Image
# ==========================================================

def image_uploader():

    uploaded_file = st.file_uploader(
        "Choose Road Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    return uploaded_file



# ==========================================================
# Preview Uploaded Image
# ==========================================================

def preview_image(uploaded_file):

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Uploaded Road Image",
            use_container_width=True
        )



# ==========================================================
# Detect Button
# ==========================================================

def predict_button():

    return st.button(
        "🚧 Detect Damage"
    )



# ==========================================================
# Predict Image
# ==========================================================

def predict_image(uploaded_file):

    if uploaded_file is None:

        st.warning(
            "Please upload an image."
        )

        return None



    files = {

        "file": (

            uploaded_file.name,

            uploaded_file.getvalue(),

            uploaded_file.type

        )

    }



    try:

        with st.spinner(
            "🚧 Detecting Road Damage..."
        ):


            response = requests.post(

                PREDICT_ENDPOINT,

                files=files,

                timeout=120

            )



        # Debug

        st.write(
            "### Backend Response"
        )


        st.write(
            "Status Code:",
            response.status_code
        )


        st.code(
            response.text
        )



        if response.status_code == 200:

            return response.json()



        else:

            st.error(
                f"Prediction Failed: {response.status_code}"
            )

            return None



    except requests.exceptions.ConnectionError:


        st.error(
            """
            ❌ Backend Connection Failed

            Start FastAPI backend first.
            """
        )

        return None



    except Exception as e:


        st.error(
            f"Error: {e}"
        )

        return None