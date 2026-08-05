"""
=========================================================
AI Road Damage Detection System
FastAPI Backend

Developer : Warda Ahad
=========================================================
"""


from pathlib import Path


from fastapi import (

    FastAPI,

    UploadFile,

    File,

    HTTPException

)


from fastapi.responses import FileResponse


from fastapi.middleware.cors import CORSMiddleware



from backend.config import (

    APP_NAME,

    APP_VERSION,

    API_DESCRIPTION,

)



from backend.logger import app_logger



from backend.utils import (

    allowed_file,

    save_upload,

    save_detection_history,

    current_time

)



from backend.predictor import Predictor


from backend.model_loader import model





app = FastAPI(

    title=APP_NAME,

    version=APP_VERSION,

    description=API_DESCRIPTION

)





app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)





@app.get("/")

def root():

    return {

        "message": "AI Road Damage Detection API",

        "version": APP_VERSION,

        "status": "Running"

    }





@app.get("/health")

def health():

    return {

        "status": "Healthy",

        "model_loaded": model is not None,

        "version": APP_VERSION

    }





@app.get("/model-info")

def model_info():

    return {

        "model": "YOLOv11",

        "framework": "Ultralytics",

        "version": APP_VERSION

    }





@app.post("/predict")

async def predict(

        file: UploadFile = File(...)

):


    if not allowed_file(file.filename):

        raise HTTPException(

            status_code=400,

            detail="Unsupported Image Format"

        )



    image_path = save_upload(file)



    app_logger.info(

        f"Image Uploaded : {file.filename}"

    )




    prediction = Predictor.predict(

        image_path

    )




    # ================================
    # Save Detection History
    # ================================


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





@app.get("/download/{filename}")

def download_result(filename: str):


    path = Path("results") / filename



    if not path.exists():

        raise HTTPException(

            status_code=404,

            detail="Result not found"

        )



    return FileResponse(path)





@app.delete("/delete/{filename}")

def delete_file(filename: str):


    path = Path("uploads") / filename



    if path.exists():

        path.unlink()



    return {


        "message": "Deleted Successfully"

    }





@app.on_event("startup")

def startup():


    app_logger.success(

        "Backend Started Successfully."

    )





@app.on_event("shutdown")

def shutdown():


    app_logger.info(

        "Backend Stopped."

    )