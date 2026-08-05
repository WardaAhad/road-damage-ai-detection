"""
=========================================================
AI Road Damage Detection System
Utility Functions
=========================================================
"""


from pathlib import Path

from uuid import uuid4

import shutil

from datetime import datetime


from fastapi import UploadFile


from backend.config import (

    UPLOAD_DIR,

    RESULT_DIR,

    ALLOWED_EXTENSIONS

)



def allowed_file(filename:str)->bool:


    suffix = Path(filename).suffix.lower()


    return suffix in ALLOWED_EXTENSIONS





def generate_filename(filename:str)->str:


    extension = Path(filename).suffix


    return f"{uuid4().hex}{extension}"






def save_upload(file:UploadFile):


    filename = generate_filename(
        file.filename
    )


    path = Path(UPLOAD_DIR) / filename



    with open(path,"wb") as buffer:


        shutil.copyfileobj(

            file.file,

            buffer

        )


    return path






def result_path(filename:str):


    return Path(RESULT_DIR)/filename






def current_time():

    return datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )