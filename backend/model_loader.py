"""
=========================================================
AI Road Damage Detection System
YOLOv11 Model Loader

Developer : Warda Ahad
=========================================================
"""


from pathlib import Path

from ultralytics import YOLO


# =========================================================
# Backend Imports
# =========================================================

from backend.config import MODEL_PATH

from backend.logger import app_logger



# =========================================================
# Model Loader Class
# =========================================================

class ModelLoader:
    """
    Singleton YOLO Model Loader
    """

    _model = None


    @classmethod
    def load_model(cls):

        # Already loaded model return karein

        if cls._model is not None:

            return cls._model



        # Check model file exists

        model_file = Path(MODEL_PATH)


        if not model_file.exists():

            app_logger.error(
                f"Model not found: {MODEL_PATH}"
            )

            raise FileNotFoundError(
                f"Model not found: {MODEL_PATH}"
            )



        try:

            app_logger.info(
                "Loading YOLOv11 model..."
            )


            cls._model = YOLO(
                str(model_file)
            )


            app_logger.success(
                "YOLOv11 Model Loaded Successfully."
            )


            return cls._model



        except Exception as e:


            app_logger.error(
                f"Model loading failed: {str(e)}"
            )


            raise e



# =========================================================
# Export Loaded Model
# =========================================================

model = ModelLoader.load_model()