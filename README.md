# AI Road Damage Detection System

**Deep Learning | YOLOv11 | Streamlit**

An AI-powered Road Damage Detection System that automatically detects and localizes different types of road damage from images using the RDD2022 Dataset and YOLOv11.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-v11-red?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge\&logo=pytorch\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)

---

# Overview

Road damage inspection is traditionally performed manually, making the process time-consuming and difficult to scale.

This project presents an AI-powered Computer Vision application that automatically detects road damage from images using a trained YOLOv11 object detection model.

The application provides an interactive Streamlit interface where users can upload road images and view detected damage with bounding boxes and confidence scores.

---

# Features

* Road Damage Detection
* Crack Detection
* Pothole Detection
* Detection of Multiple Road Damage Categories
* Bounding Box Visualization
* Confidence Score Analysis
* Image Upload
* YOLOv11 Object Detection
* Interactive Streamlit Dashboard
* Analytics Dashboard
* Detection History
* Annotated Detection Results
* User-Friendly Interface

---

# Damage Classes

| Class | Description        |
| ----- | ------------------ |
| D00   | Longitudinal Crack |
| D10   | Transverse Crack   |
| D20   | Alligator Crack    |
| D40   | Pothole            |

---

# System Workflow

```text
Road Image
     |
     v
Image Upload
     |
     v
Image Preprocessing
     |
     v
YOLOv11 Detection Model
     |
     v
Damage Detection
     |
     v
Bounding Boxes + Confidence Scores
     |
     v
Detection Results
```

---

# Technology Stack

## Programming Language

* Python

## Deep Learning

* YOLOv11
* PyTorch
* Ultralytics

## Computer Vision

* OpenCV
* Pillow

## Data Processing

* NumPy
* Pandas

## Visualization

* Matplotlib

## Web Application

* Streamlit

## Development Tools

* Git
* GitHub
* VS Code
* Jupyter Notebook

---

# Project Structure

```text
road-damage-ai-detection/
|
├── frontend/
│   ├── app.py
│   ├── assets/
│   │   └── logo.png
│   └── ...
│
├── notebooks/
│   └── ...
│
├── requirements.txt
├── packages.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

# Dataset

## RDD2022 - Road Damage Detection 2022

The project is based on the Road Damage Detection 2022 (RDD2022) dataset.

The dataset contains annotated road images collected from multiple countries and includes different types of road surface damage.

The model is trained to detect the following road damage categories:

* D00 - Longitudinal Crack
* D10 - Transverse Crack
* D20 - Alligator Crack
* D40 - Pothole

---

# Installation

## Clone Repository

```bash
git clone https://github.com/WardaAhad/road-damage-ai-detection.git
cd road-damage-ai-detection
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run frontend/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# Application Sections

## Dashboard

Provides an overview of the Road Damage Detection System and project information.

## Detect Damage

Upload a road image and use the trained YOLOv11 model to detect road damage.

## Analytics

Provides visual insights and statistics related to detection results.

## History

Allows users to review previously processed detection results.

---

# Application Screenshots

## Dashboard

Add Dashboard Screenshot here.

## Detection

Add Detection Screenshot here.

## Analytics

Add Analytics Screenshot here.

## History

Add History Screenshot here.

---

# Live Demo

Try the deployed Streamlit application:

https://road-damage-ai-detection-zlum5wd8ojrh6toetrnlqb.streamlit.app/

---

# Project Objectives

* Automate road damage detection using Computer Vision.
* Apply YOLOv11 object detection to real-world road images.
* Detect and localize multiple types of road damage.
* Build an interactive AI application using Streamlit.
* Visualize detection results using bounding boxes and confidence scores.
* Gain practical experience in Deep Learning and Computer Vision.

---

# Future Improvements

* Video Road Damage Detection
* Live Camera Detection
* GPS Integration
* Automated PDF Reports
* Damage Severity Analysis
* Interactive Road Damage Maps
* Mobile Application
* Cloud-Based Storage
* Real-Time Monitoring

---

# Developer

## Warda Ahad

Bachelor of Artificial Intelligence

The Islamia University of Bahawalpur

GitHub:

https://github.com/WardaAhad

---

# Show Your Support

If you find this project useful, consider giving the repository a star on GitHub.

Your support helps encourage further development and learning.

---

# License

This project is licensed under the MIT License.

---

# AI for Safer Roads

Built with Python, YOLOv11, and Streamlit.
