import cv2


def preprocess_image(image_path):

    image = cv2.imread(image_path)


    if image is None:
        raise ValueError(
            "Image not found"
        )


    image = cv2.resize(
        image,
        (640,640)
    )


    return image