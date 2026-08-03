from ultralytics import YOLO
import os


MODEL_PATH = "model/best.pt"

OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


model = YOLO(MODEL_PATH)


def predict_image(image_path):

    results = model(
        image_path,
        conf=0.5
    )


    detections = []

    output_path = None


    for result in results:

        # Save image with bounding boxes
        plotted_image = result.plot()

        filename = os.path.basename(image_path)

        output_path = os.path.join(
            OUTPUT_FOLDER,
            "result_" + filename
        )

        import cv2

        cv2.imwrite(
            output_path,
            plotted_image
        )


        boxes = result.boxes


        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])


            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )


            detections.append(
                {
                    "class": model.names[class_id],
                    "confidence": round(confidence, 3),
                    "bbox": [
                        x1,
                        y1,
                        x2,
                        y2
                    ]
                }
            )


    return {
        "total_damages": len(detections),
        "detections": detections,
        "output_image": output_path
    }