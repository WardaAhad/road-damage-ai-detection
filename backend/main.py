"""
=========================================================
AI Road Damage Detection System
FastAPI Backend
Developer : Warda Ahad
=========================================================
"""

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)

from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from config import (
    APP_NAME,
    APP_VERSION,
    API_DESCRIPTION,
    RESULT_DIR,
    UPLOAD_DIR,
)

from logger import app_logger

from utils import (
    allowed_file,
    save_upload,
    save_detection_history,
    current_time
)

from predictor import Predictor
from model_loader import model


# =========================================================
# FastAPI Application
# =========================================================

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=API_DESCRIPTION
)


# =========================================================
# CORS Configuration
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# Root Endpoint
# =========================================================

@app.get("/")
def root():
    return {
        "message": "AI Road Damage Detection API",
        "version": APP_VERSION,
        "status": "Running"
    }


# =========================================================
# Health Check
# =========================================================

@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "model_loaded": model is not None,
        "version": APP_VERSION
    }


# =========================================================
# Model Information
# =========================================================

@app.get("/model-info")
def model_info():
    return {
        "model": "YOLOv11",
        "framework": "Ultralytics",
        "version": APP_VERSION
    }


# =========================================================
# Prediction Endpoint
# =========================================================

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    # -----------------------------------------------------
    # Validate File
    # -----------------------------------------------------

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file provided."
        )

    if not allowed_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail="Unsupported Image Format"
        )

    # -----------------------------------------------------
    # Save Uploaded Image
    # -----------------------------------------------------

    image_path = save_upload(file)

    app_logger.info(
        f"Image Uploaded : {file.filename}"
    )

    # -----------------------------------------------------
    # Run YOLO Prediction
    # -----------------------------------------------------

    prediction = Predictor.predict(
        image_path
    )

    # -----------------------------------------------------
    # Save Detection History
    # -----------------------------------------------------

    history_data = {
        "timestamp": current_time(),
        "original_filename": file.filename,
        "result_filename": prediction["filename"],
        "total_objects": prediction["total_objects"],
        "detections": prediction["detections"],
        "processing_time": prediction["processing_time"]
    }

    save_detection_history(
        history_data
    )

    app_logger.info(
        "Detection history saved."
    )

    return prediction


# =========================================================
# Download Detection Result
# =========================================================

@app.get("/download/{filename}")
def download_result(filename: str):

    path = RESULT_DIR / filename

    if not path.exists():
        raise HTTPException(
            status_code=404,
            detail="Result not found"
        )

    return FileResponse(
        path
    )


# =========================================================
# Delete Uploaded File
# =========================================================

@app.delete("/delete/{filename}")
def delete_file(filename: str):

    path = UPLOAD_DIR / filename

    if path.exists():
        path.unlink()

    return {
        "message": "Deleted Successfully"
    }


# =========================================================
# Startup Event
# =========================================================

@app.on_event("startup")
def startup():

    app_logger.success(
        "Backend Started Successfully."
    )


# =========================================================
# Shutdown Event
# =========================================================

@app.on_event("shutdown")
def shutdown():

    app_logger.info(
        "Backend Stopped."
    )