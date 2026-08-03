"""
=========================================================
AI Road Damage Detection System
Configuration File
Developer : Warda Ahad
=========================================================
"""

import os

# =========================================================
# Base Directory
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================================================
# Project Information
# =========================================================

PROJECT_NAME = "AI Road Damage Detection System"

PROJECT_VERSION = "1.0.0"

DEVELOPER = "Warda Ahad"

DESCRIPTION = """
YOLOv11 based AI Road Damage Detection System
using FastAPI Backend and Streamlit Frontend.
"""

# =========================================================
# Backend API Configuration
# =========================================================

# Local Backend
API_BASE_URL = "http://127.0.0.1:8000"

# Production Backend
# API_BASE_URL = "https://your-backend-url.up.railway.app"

PREDICT_ENDPOINT = f"{API_BASE_URL}/predict"
HEALTH_ENDPOINT = f"{API_BASE_URL}/health"
REPORT_ENDPOINT = f"{API_BASE_URL}/report"
HISTORY_ENDPOINT = f"{API_BASE_URL}/history"

# =========================================================
# Upload Configuration
# =========================================================

ALLOWED_IMAGE_TYPES = [
    "jpg",
    "jpeg",
    "png"
]

MAX_UPLOAD_SIZE_MB = 10

# =========================================================
# YOLO Detection Settings
# =========================================================

MODEL_NAME = "YOLOv11"
MODEL_VERSION = "v11"
FRAMEWORK = "Ultralytics"

IMAGE_SIZE = 640

DEFAULT_CONFIDENCE = 0.25
DEFAULT_IOU = 0.45
MAX_DETECTIONS = 100

# =========================================================
# Streamlit Configuration
# =========================================================

PAGE_TITLE = PROJECT_NAME
PAGE_ICON = "🚧"
LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# =========================================================
# Theme Configuration
# =========================================================

PRIMARY_COLOR = "#2563EB"
PRIMARY_LIGHT = "#3B82F6"
PRIMARY_DARK = "#1D4ED8"

BACKGROUND_COLOR = "#0F172A"
SURFACE_COLOR = "#111827"
CARD_COLOR = "#1E293B"

TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#CBD5E1"

SUCCESS_COLOR = "#22C55E"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#EF4444"
INFO_COLOR = "#06B6D4"

# =========================================================
# Assets Configuration
# =========================================================

ASSETS_DIR = os.path.join(BASE_DIR, "assets")

LOGO = os.path.join(ASSETS_DIR, "logo.png")

BANNER = os.path.join(ASSETS_DIR, "banner.png")

FAVICON = os.path.join(ASSETS_DIR, "favicon.png")

# =========================================================
# Icons
# =========================================================

ICON_DIR = os.path.join(ASSETS_DIR, "icons")

UPLOAD_ICON = os.path.join(ICON_DIR, "upload.png")

DETECTION_ICON = os.path.join(ICON_DIR, "detection.png")

ROAD_ICON = os.path.join(ICON_DIR, "road.png")

ANALYTICS_ICON = os.path.join(ICON_DIR, "analytics.png")

GITHUB_ICON = os.path.join(ICON_DIR, "github.png")

# =========================================================
# Output Folder Configuration
# =========================================================

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

UPLOAD_DIR = os.path.join(OUTPUT_DIR, "uploaded_images")

PREDICTION_DIR = os.path.join(OUTPUT_DIR, "predictions")

REPORT_DIR = os.path.join(OUTPUT_DIR, "reports")

# =========================================================
# Analytics Settings
# =========================================================

SAVE_HISTORY = True

SAVE_REPORT = True

AUTO_REFRESH = False

# =========================================================
# Dashboard Settings
# =========================================================

SHOW_TOTAL_IMAGES = True

SHOW_TOTAL_DETECTIONS = True

SHOW_MODEL_ACCURACY = True

SHOW_BACKEND_STATUS = True

# =========================================================
# Damage Classes
# =========================================================

DAMAGE_CLASSES = [
    "D00",   # Crack
    "D10",   # Pothole
    "D20",   # Repair / Patch
    "D40"    # Other Damage
]

# =========================================================
# Create Required Directories
# =========================================================

os.makedirs(UPLOAD_DIR, exist_ok=True)

os.makedirs(PREDICTION_DIR, exist_ok=True)

os.makedirs(REPORT_DIR, exist_ok=True)