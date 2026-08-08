"""
=========================================================
AI Road Damage Detection System
Frontend Configuration
Developer : Warda Ahad
=========================================================
"""

import os


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


# ==========================================================
# BACKEND API CONFIGURATION
# ==========================================================

# Railway Production Backend
API_BASE_URL = "https://road-damage-ai-detection-production.up.railway.app"


# API Endpoints
PREDICT_ENDPOINT = f"{API_BASE_URL}/predict"
HEALTH_ENDPOINT = f"{API_BASE_URL}/health"
MODEL_INFO_ENDPOINT = f"{API_BASE_URL}/model-info"


# ==========================================================
# FILE CONFIGURATION
# ==========================================================

ALLOWED_IMAGE_TYPES = [
    "jpg",
    "jpeg",
    "png",
    "webp"
]

MAX_UPLOAD_SIZE_MB = 10


# ==========================================================
# ASSETS
# ==========================================================

ASSETS_DIR = os.path.join(BASE_DIR, "assets")

LOGO_PATH = os.path.join(ASSETS_DIR, "logo.png")
BANNER_PATH = os.path.join(ASSETS_DIR, "banner.png")
FAVICON_PATH = os.path.join(ASSETS_DIR, "favicon.png")


# ==========================================================
# APP SETTINGS
# ==========================================================

APP_NAME = "AI Road Damage Detection System"
APP_VERSION = "1.0.0"


# ==========================================================
# DETECTION SETTINGS
# ==========================================================

MODEL_NAME = "YOLOv11"

CONFIDENCE_THRESHOLD = 0.25


# ==========================================================
# BACKEND STATUS
# ==========================================================

BACKEND_TIMEOUT = 120