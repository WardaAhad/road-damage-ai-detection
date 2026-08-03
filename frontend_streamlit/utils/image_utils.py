"""
=========================================================
AI Road Damage Detection System
Image Utilities
Developer : Warda Ahad
=========================================================
"""

import cv2
import numpy as np
from PIL import Image
import io
import os


# ==========================================================
# Load Image
# ==========================================================

def load_image(uploaded_file):
    """
    Load uploaded image using PIL.
    """

    if uploaded_file is None:
        return None

    return Image.open(uploaded_file)


# ==========================================================
# PIL to NumPy
# ==========================================================

def pil_to_numpy(image):
    """
    Convert PIL Image to NumPy array.
    """

    if image is None:
        return None

    return np.array(image)


# ==========================================================
# NumPy to PIL
# ==========================================================

def numpy_to_pil(image):
    """
    Convert NumPy array to PIL Image.
    """

    if image is None:
        return None

    return Image.fromarray(image)


# ==========================================================
# Resize Image
# ==========================================================

def resize_image(image, width=640, height=640):
    """
    Resize image.
    """

    if image is None:
        return None

    return image.resize((width, height))


# ==========================================================
# Get Image Size
# ==========================================================

def image_size(image):
    """
    Return image width and height.
    """

    if image is None:
        return (0, 0)

    return image.size


# ==========================================================
# Image Mode
# ==========================================================

def image_mode(image):
    """
    Return image mode.
    """

    if image is None:
        return ""

    return image.mode
# ==========================================================
# RGB to BGR Conversion
# ==========================================================

def rgb_to_bgr(image):
    """
    Convert RGB image to BGR format for OpenCV.
    """

    if image is None:
        return None

    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


# ==========================================================
# BGR to RGB Conversion
# ==========================================================

def bgr_to_rgb(image):
    """
    Convert BGR image to RGB format.
    """

    if image is None:
        return None

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# ==========================================================
# Save Image
# ==========================================================

def save_image(image, path):
    """
    Save image to given path.
    """

    if image is None:
        return False

    try:
        image.save(path)
        return True

    except Exception:
        return False


# ==========================================================
# Image to Bytes
# ==========================================================

def image_to_bytes(image, format="PNG"):
    """
    Convert PIL image into bytes.
    """

    if image is None:
        return None

    img_bytes = io.BytesIO()

    image.save(
        img_bytes,
        format=format
    )

    return img_bytes.getvalue()


# ==========================================================
# Bytes to Image
# ==========================================================

def bytes_to_image(image_bytes):
    """
    Convert bytes back to PIL image.
    """

    if image_bytes is None:
        return None

    return Image.open(
        io.BytesIO(image_bytes)
    )


# ==========================================================
# Image Dimensions
# ==========================================================

def image_dimensions(image):
    """
    Return image dimensions.
    """

    if image is None:
        return {
            "width": 0,
            "height": 0
        }

    width, height = image.size

    return {
        "width": width,
        "height": height
    }


# ==========================================================
# Delete Image
# ==========================================================

def delete_image(path):
    """
    Delete image from system.
    """

    if not os.path.exists(path):
        return False

    try:
        os.remove(path)
        return True

    except Exception:
        return False


# ==========================================================
# Image Information
# ==========================================================

def image_info(image):
    """
    Return complete image information.
    """

    if image is None:
        return {}

    width, height = image.size

    return {
        "format": image.format,
        "mode": image.mode,
        "width": width,
        "height": height,
        "size": f"{width}x{height}"
    }
