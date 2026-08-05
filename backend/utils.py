"""
=========================================================
AI Road Damage Detection System
Utility Functions
=========================================================
"""


from pathlib import Path

from uuid import uuid4

import shutil

import json

from datetime import datetime

from fastapi import UploadFile


from backend.config import (

    UPLOAD_DIR,

    RESULT_DIR,

    HISTORY_DIR,

    ALLOWED_EXTENSIONS

)



# =========================================================
# File Validation
# =========================================================


def allowed_file(filename: str) -> bool:

    suffix = Path(filename).suffix.lower()

    return suffix in ALLOWED_EXTENSIONS





# =========================================================
# Generate Unique Filename
# =========================================================


def generate_filename(filename: str) -> str:

    extension = Path(filename).suffix

    return f"{uuid4().hex}{extension}"





# =========================================================
# Save Uploaded Image
# =========================================================


def save_upload(file: UploadFile):

    filename = generate_filename(
        file.filename
    )


    path = Path(UPLOAD_DIR) / filename



    with open(path, "wb") as buffer:

        shutil.copyfileobj(

            file.file,

            buffer

        )


    return path





# =========================================================
# Result Image Path
# =========================================================


def result_path(filename: str):

    return Path(RESULT_DIR) / filename





# =========================================================
# Current Time
# =========================================================


def current_time():

    return datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )





# =========================================================
# Save Detection History
# =========================================================


def save_detection_history(data: dict):


    history_file = Path(HISTORY_DIR) / "detection_history.json"



    # Create file if not exists

    if not history_file.exists():

        history = []



    # Handle empty file

    elif history_file.stat().st_size == 0:

        history = []



    else:


        with open(history_file, "r") as f:

            try:

                history = json.load(f)


            except json.JSONDecodeError:

                history = []




    history.append(data)




    with open(history_file, "w") as f:


        json.dump(

            history,

            f,

            indent=4

        )