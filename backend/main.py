from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os

from utils.predictor import predict_image

app = FastAPI(
    title="AI Road Damage Detection API",
    description="YOLO based Road Damage Detection System",
    version="1.0"
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "AI Road Damage Detection API is Running"
    }


# ==============================
# Health Check API
# ==============================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "message": "Backend is running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    try:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = predict_image(file_path)

        return JSONResponse(
            status_code=200,
            content={
                "filename": file.filename,
                "result": result
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )