"""
=========================================================
AI Road Damage Detection System
Helper Functions
Developer : Warda Ahad
=========================================================
"""

import os
from datetime import datetime
import streamlit as st


# ==========================================================
# Date & Time
# ==========================================================

def current_date():
    """
    Return current date.
    """
    return datetime.now().strftime("%d-%m-%Y")


def current_time():
    """
    Return current time.
    """
    return datetime.now().strftime("%I:%M %p")


# ==========================================================
# File Information
# ==========================================================

def get_file_name(uploaded_file):

    if uploaded_file is None:
        return ""

    return uploaded_file.name


def get_file_extension(uploaded_file):

    if uploaded_file is None:
        return ""

    return os.path.splitext(uploaded_file.name)[1].lower()


def get_file_size(uploaded_file):

    if uploaded_file is None:
        return "0 MB"

    size = uploaded_file.size / (1024 * 1024)

    return f"{size:.2f} MB"


# ==========================================================
# Image Validation
# ==========================================================

def validate_image(uploaded_file):

    if uploaded_file is None:
        return False

    allowed = [
        ".jpg",
        ".jpeg",
        ".png"
    ]

    extension = get_file_extension(uploaded_file)

    return extension in allowed


# ==========================================================
# Messages
# ==========================================================

def show_success(message):

    st.success(message)


def show_error(message):

    st.error(message)


def show_warning(message):

    st.warning(message)


def show_info(message):

    st.info(message)
# ==========================================================
# Detection Summary
# ==========================================================

def get_detection_summary(result):
    """
    Extract basic information from API response.
    """

    if not result:
        return {}

    prediction = result.get("result", {})

    return {
        "filename": result.get("filename", ""),
        "total_damages": prediction.get("total_damages", 0),
        "detections": prediction.get("detections", [])
    }


# ==========================================================
# Average Confidence
# ==========================================================

def average_confidence(result):
    """
    Calculate average confidence percentage.
    """

    prediction = result.get("result", {})
    detections = prediction.get("detections", [])

    if len(detections) == 0:
        return 0

    total = sum(item["confidence"] for item in detections)

    avg = (total / len(detections)) * 100

    return round(avg, 2)


# ==========================================================
# Highest Confidence
# ==========================================================

def highest_confidence(result):
    """
    Return highest confidence.
    """

    prediction = result.get("result", {})
    detections = prediction.get("detections", [])

    if len(detections) == 0:
        return 0

    highest = max(item["confidence"] for item in detections)

    return round(highest * 100, 2)


# ==========================================================
# Count Damage Classes
# ==========================================================

def count_damage_classes(result):
    """
    Count each detected damage class.
    """

    prediction = result.get("result", {})
    detections = prediction.get("detections", [])

    classes = {}

    for item in detections:

        damage = item["class"]

        if damage in classes:
            classes[damage] += 1
        else:
            classes[damage] = 1

    return classes


# ==========================================================
# Format Confidence
# ==========================================================

def format_confidence(value):
    """
    Convert confidence to percentage string.
    """

    return f"{value * 100:.2f}%"


# ==========================================================
# Bounding Box Formatter
# ==========================================================

def format_bbox(bbox):
    """
    Convert bounding box list to readable text.
    """

    if not bbox:
        return "-"

    return (
        f"X1:{bbox[0]} | "
        f"Y1:{bbox[1]} | "
        f"X2:{bbox[2]} | "
        f"Y2:{bbox[3]}"
    )


# ==========================================================
# Backend Status
# ==========================================================

def backend_status(is_online):

    if is_online:

        st.success("🟢 Backend Connected")

    else:

        st.error("🔴 Backend Offline")


# ==========================================================
# Reset Session
# ==========================================================

def clear_prediction():

    keys = [
        "prediction",
        "uploaded_file",
        "result"
    ]

    for key in keys:

        if key in st.session_state:

            del st.session_state[key]
