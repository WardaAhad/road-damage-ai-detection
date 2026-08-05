"""
=========================================================
AI Road Damage Detection System
Pydantic Schemas

Developer : Warda Ahad
=========================================================
"""


from pydantic import BaseModel, Field

from typing import List



# =========================================================
# Detection Response Schema
# =========================================================

class Detection(BaseModel):

    class_name: str = Field(
        ...,
        description="Detected damage class name"
    )

    confidence: float = Field(
        ...,
        description="Detection confidence score"
    )

    xmin: float

    ymin: float

    xmax: float

    ymax: float



# =========================================================
# Prediction Response Schema
# =========================================================

class PredictionResponse(BaseModel):

    success: bool

    filename: str

    total_objects: int

    detections: List[Detection]

    result_image: str

    processing_time: float



# =========================================================
# Health Response Schema
# =========================================================

class HealthResponse(BaseModel):

    status: str

    model_loaded: bool

    version: str