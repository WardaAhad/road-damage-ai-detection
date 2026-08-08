"""
=========================================================
AI Road Damage Detection System
Backend Configuration
Developer : Warda Ahad
=========================================================
"""

import os
import tempfile
from pathlib import Path

from dotenv import load_dotenv


# =========================================================
# Load Environment Variables
# =========================================================

load_dotenv()


# =========================================================
# Project Paths
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

TMP_DIR = Path(tempfile.gettempdir())


# =========================================================
# Model Paths
# =========================================================

# Actual structure:
#
# backend/
# ├── config.py
# ├── main.py
# └── models/
#     └── best.pt

MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "best.pt"


# =========================================================
# Temporary Directories
# =========================================================

UPLOAD_DIR = TMP_DIR / "uploads"

RESULT_DIR = TMP_DIR / "results"

LOG_DIR = TMP_DIR / "logs"

HISTORY_DIR = TMP_DIR / "history"


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
    folder.mkdir(
        parents=True,
        exist_ok=True,
    )


# =========================================================
# Application Settings
# =========================================================

APP_NAME = os.getenv(
    "APP_NAME",
    "AI Road Damage Detection API",
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0",
)


# =========================================================
# Server Settings
# =========================================================

HOST = os.getenv(
    "HOST",
    "0.0.0.0",
)

PORT = int(
    os.getenv(
        "PORT",
        "8000",
    )
)


# =========================================================
# YOLO Settings
# =========================================================

CONFIDENCE_THRESHOLD = float(
    os.getenv(
        "CONFIDENCE_THRESHOLD",
        "0.25",
    )
)

IOU_THRESHOLD = float(
    os.getenv(
        "IOU_THRESHOLD",
        "0.45",
    )
)

MAX_IMAGE_SIZE = int(
    os.getenv(
        "MAX_IMAGE_SIZE",
        str(10 * 1024 * 1024),
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
    ".webp",
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