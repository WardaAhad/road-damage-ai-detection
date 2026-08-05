"""
=========================================================
AI Road Damage Detection System
YOLOv11 Predictor

Developer : Warda Ahad
=========================================================
"""


import time

from pathlib import Path

import cv2


from backend.model_loader import model

from backend.config import (

    RESULT_DIR,

    CONFIDENCE_THRESHOLD,

    IOU_THRESHOLD

)

from backend.logger import app_logger




class Predictor:


    @staticmethod
    def predict(image_path: Path):


        start_time = time.time()



        app_logger.info(
            "Running YOLOv11 prediction..."
        )


        results = model.predict(

            source=str(image_path),

            conf=CONFIDENCE_THRESHOLD,

            iou=IOU_THRESHOLD,

            save=False,

            verbose=False

        )



        result = results[0]


        detections = []



        image = cv2.imread(
            str(image_path)
        )


        names = model.names



        for box in result.boxes:


            cls_id = int(box.cls[0])


            class_name = names[cls_id]


            confidence = float(
                box.conf[0]
            )


            x1,y1,x2,y2 = map(

                int,

                box.xyxy[0]

            )



            detections.append({

                "class_name": class_name,

                "confidence": round(
                    confidence,
                    4
                ),

                "xmin": x1,

                "ymin": y1,

                "xmax": x2,

                "ymax": y2

            })



            cv2.rectangle(

                image,

                (x1,y1),

                (x2,y2),

                (0,255,0),

                2

            )


            cv2.putText(

                image,

                f"{class_name} {confidence:.2f}",

                (x1,y1-10),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.6,

                (0,255,0),

                2

            )




        result_path = Path(RESULT_DIR) / image_path.name



        cv2.imwrite(

            str(result_path),

            image

        )



        processing_time = round(

            time.time()-start_time,

            3

        )



        app_logger.success(

            "Prediction completed"

        )



        return {


            "success": True,

            "filename": image_path.name,

            "total_objects": len(detections),

            "detections": detections,

            "result_image": str(result_path),

            "processing_time": processing_time


        }