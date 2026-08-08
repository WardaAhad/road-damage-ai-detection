"""
=========================================================
AI Road Damage Detection System
Backend : FastAPI + YOLOv11
Developer : Warda Ahad
=========================================================
"""

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException,
)

from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


# =========================================================
# Backend Imports
# =========================================================

from backend.config import (
    APP_NAME,
    APP_VERSION,
    API_DESCRIPTION,
    RESULT_DIR,
    UPLOAD_DIR,
)

from backend.logger import app_logger

from backend.utils import (
    allowed_file,
    save_upload,
    save_detection_history,
    current_time,
)

from backend.predictor import Predictor
from backend.model_loader import model


# =========================================================
# FastAPI Application
# =========================================================

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=API_DESCRIPTION,
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
        "status": "Running",
    }


# =========================================================
# Health Check
# =========================================================

@app.get("/health")
def health():

    return {
        "status": "Healthy",
        "model_loaded": model is not None,
        "version": APP_VERSION,
    }


# =========================================================
# Model Information
# =========================================================

@app.get("/model-info")
def model_info():

    return {
        "model": "YOLOv11",
        "framework": "Ultralytics",
        "version": APP_VERSION,
    }


# =========================================================
# Prediction Endpoint
# =========================================================

@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
):

    # -----------------------------------------------------
    # Validate File
    # -----------------------------------------------------

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="No file provided.",
        )

    if not allowed_file(file.filename):

        raise HTTPException(
            status_code=400,
            detail="Unsupported Image Format.",
        )

    # -----------------------------------------------------
    # Save Uploaded Image
    # -----------------------------------------------------

    try:

        image_path = save_upload(file)

        app_logger.info(
            f"Image Uploaded : {file.filename}"
        )

    except Exception as e:

        app_logger.error(
            f"Failed to save uploaded image: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to save uploaded image.",
        )

    # -----------------------------------------------------
    # Run YOLO Prediction
    # -----------------------------------------------------

    try:

        prediction = Predictor.predict(
            image_path
        )

    except Exception as e:

        app_logger.error(
            f"Prediction failed: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}",
        )

    # -----------------------------------------------------
    # Save Detection History
    # -----------------------------------------------------

    try:

        history_data = {
            "timestamp": current_time(),
            "original_filename": file.filename,
            "result_filename": prediction["filename"],
            "total_objects": prediction["total_objects"],
            "detections": prediction["detections"],
            "processing_time": prediction["processing_time"],
        }

        save_detection_history(
            history_data
        )

        app_logger.info(
            "Detection history saved."
        )

    except Exception as e:

        app_logger.error(
            f"Failed to save detection history: {e}"
        )

    # -----------------------------------------------------
    # Return Prediction
    # -----------------------------------------------------

    return prediction


# =========================================================
# Download Detection Result
# =========================================================

@app.get("/download/{filename}")
def download_result(
    filename: str,
):

    path = RESULT_DIR / filename

    if not path.exists():

        raise HTTPException(
            status_code=404,
            detail="Result not found.",
        )

    return FileResponse(
        path
    )


# =========================================================
# Delete Uploaded File
# =========================================================

@app.delete("/delete/{filename}")
def delete_file(
    filename: str,
):

    path = UPLOAD_DIR / filename

    if path.exists():

        path.unlink()

        return {
            "message": "Deleted Successfully",
        }

    raise HTTPException(
        status_code=404,
        detail="File not found.",
    )


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