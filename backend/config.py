"""
=========================================================
AI Road Damage Detection System
Configuration File
Developer : Warda Ahad
=========================================================
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# =========================================================
# Load Environment Variables
# =========================================================

load_dotenv()

# =========================================================
# Project Paths
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"
UPLOAD_DIR = BASE_DIR / "uploads"
RESULT_DIR = BASE_DIR / "results"
LOG_DIR = BASE_DIR / "logs"
HISTORY_DIR = BASE_DIR / "history"

MODEL_PATH = MODEL_DIR / "best.pt"

# =========================================================
# Create Required Folders
# =========================================================

for folder in [
    MODEL_DIR,
    UPLOAD_DIR,
    RESULT_DIR,
    LOG_DIR,
    HISTORY_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

# =========================================================
# Application Settings
# =========================================================

APP_NAME = os.getenv(
    "APP_NAME",
    "AI Road Damage Detection API"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

# =========================================================
# Server Settings
# =========================================================

HOST = os.getenv(
    "HOST",
    "0.0.0.0"
)

PORT = int(
    os.getenv(
        "PORT",
        8000
    )
)

# =========================================================
# YOLO Settings
# =========================================================

CONFIDENCE_THRESHOLD = float(
    os.getenv(
        "CONFIDENCE_THRESHOLD",
        0.25
    )
)

IOU_THRESHOLD = float(
    os.getenv(
        "IOU_THRESHOLD",
        0.45
    )
)

MAX_IMAGE_SIZE = int(
    os.getenv(
        "MAX_IMAGE_SIZE",
        10 * 1024 * 1024
    )
)

# =========================================================
# Allowed Image Extensions
# =========================================================

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}

# =========================================================
# API Information
# =========================================================

API_DESCRIPTION = """
Professional AI Road Damage Detection API

Features:
- YOLOv11 Object Detection
- Road Crack Detection
- Pothole Detection
- Surface Damage Detection
- Confidence Score
- Result Image Generation
- Detection History
"""