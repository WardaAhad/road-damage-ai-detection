"""
=========================================================
AI Road Damage Detection System
FastAPI Client
Developer : Warda Ahad
=========================================================
"""

import requests
import streamlit as st

from config import (
    API_BASE_URL,
    HEALTH_ENDPOINT,
    PREDICT_ENDPOINT,
    HISTORY_ENDPOINT,
    REPORT_ENDPOINT
)


# ==========================================================
# Health Check
# ==========================================================

def check_backend():

    try:

        response = requests.get(
            HEALTH_ENDPOINT,
            timeout=5
        )

        if response.status_code == 200:

            return True

        return False

    except Exception:

        return False


# ==========================================================
# Predict Image
# ==========================================================

def predict(uploaded_file):

    try:

        files = {

            "file": (

                uploaded_file.name,

                uploaded_file.getvalue(),

                uploaded_file.type

            )

        }

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

        st.error(e)

        return None


# ==========================================================
# History
# ==========================================================

def get_history():

    try:

        response = requests.get(

            HISTORY_ENDPOINT,

            timeout=10

        )

        if response.status_code == 200:

            return response.json()

        return []

    except Exception:

        return []


# ==========================================================
# Download Report
# ==========================================================

def download_report(report_id):

    try:

        response = requests.get(

            f"{REPORT_ENDPOINT}/{report_id}",

            timeout=20

        )

        if response.status_code == 200:

            return response.content

        return None

    except Exception:

        return None


# ==========================================================
# API Status Card
# ==========================================================

def api_status():

    if check_backend():

        st.success("🟢 Backend Connected")

    else:

        st.error("🔴 Backend Offline")


# ==========================================================
# Display Prediction
# ==========================================================

def display_prediction(result):

    if result is None:

        return

    st.success("Detection Completed")

    st.json(result)


# ==========================================================
# Error Message
# ==========================================================

def api_error(message):

    st.error(message)


# ==========================================================
# Success Message
# ==========================================================

def api_success(message):

    st.success(message)
