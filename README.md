# 🚧 AI Road Damage Detection System

<div align="center">

<img src="frontend_streamlit/assets/logo.png" width="140">

# AI Road Damage Detection System

### 🚀 Deep Learning • YOLOv11 • FastAPI • Streamlit

An End-to-End AI-powered Road Damage Detection System capable of detecting cracks, potholes, and road surface damage using the **RDD2022 Dataset** and **YOLOv11**.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-v11-red?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge\&logo=pytorch\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)

</div>

---

# 📖 Overview

Road damage inspection is traditionally performed manually, making it slow, expensive, and prone to human error.

This project presents an **AI-powered Road Damage Detection System** that automatically detects road damage using **YOLOv11**.

The application provides a modern **Streamlit Dashboard** connected to a **FastAPI Backend**, allowing users to upload road images and instantly receive detection results.

---

# ✨ Features

* 🚧 Road Damage Detection
* 🛣️ Crack Detection
* 🕳️ Pothole Detection
* 📍 Bounding Box Visualization
* 📊 Confidence Scores
* ⚡ FastAPI REST API
* 🎨 Modern Streamlit Dashboard
* 📈 Analytics Dashboard
* 📜 Detection History
* 📷 Image Upload
* 🧠 YOLOv11 Deep Learning Model
* 💻 Responsive UI
* ☁️ Ready for Railway Deployment

---

# 🎯 Damage Classes

| Class | Description        |
| ----- | ------------------ |
| D00   | Longitudinal Crack |
| D10   | Transverse Crack   |
| D20   | Alligator Crack    |
| D40   | Pothole            |

---

# 🏗️ System Architecture

```text
Road Image
      │
      ▼
Streamlit Frontend
      │
      ▼
FastAPI REST API
      │
      ▼
YOLOv11 Detection Model
      │
      ▼
Prediction Results
      │
      ▼
Bounding Boxes + Confidence Score
```

---

# 🛠️ Technology Stack

## Programming Language

* Python

## Deep Learning

* YOLOv11
* PyTorch

## Backend

* FastAPI
* Uvicorn

## Frontend

* Streamlit

## Computer Vision

* OpenCV
* Pillow

## Data Processing

* NumPy
* Pandas

## Visualization

* Matplotlib

---

# 📂 Project Structure

```text
AI-Road-Damage-Detection-System
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── best.pt
│   ├── uploads/
│   ├── outputs/
│   ├── utils/
│   │   ├── predictor.py
│   │   ├── image_processing.py
│   │   └── helper.py
│   └── __pycache__/
│
├── frontend_streamlit/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   │
│   ├── assets/
│   │   ├── logo.png
│   │   ├── banner.png
│   │   ├── favicon.png
│   │   └── icons/
│   │
│   ├── components/
│   │   ├── sidebar.py
│   │   ├── navbar.py
│   │   ├── footer.py
│   │   ├── cards.py
│   │   ├── charts.py
│   │   ├── uploader.py
│   │   ├── report.py
│   │   └── api.py
│   │
│   ├── pages/
│   │   ├── 1_Dashboard.py
│   │   ├── 2_Detect_Damage.py
│   │   ├── 3_Analytics.py
│   │   ├── 4_History.py
│   │   └── 5_About.py
│   │
│   ├── styles/
│   │   ├── colors.py
│   │   ├── theme.py
│   │   └── custom.css
│   │
│   └── utils/
│       ├── helper.py
│       ├── analytics.py
│       └── image_utils.py
│
├── notebooks/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# 📊 Dataset

**Dataset:** RDD2022 (Road Damage Detection 2022)

The dataset contains thousands of annotated road images collected from multiple countries and includes four road damage categories.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Road-Damage-Detection-System.git

cd AI-Road-Damage-Detection-System
```

---

# Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

# Frontend

```bash
cd frontend_streamlit

pip install -r requirements.txt

streamlit run app.py
```

Frontend URL

```
http://localhost:8501
```

---

# API Endpoints

## Home

```
GET /
```

## Health Check

```
GET /health
```

## Prediction

```
POST /predict
```

Returns

* Total Damages
* Detection Class
* Confidence Score
* Output Image

---

# 📷 Application Screenshots

## Dashboard

> Add Dashboard Screenshot

---

## Detection

> Add Detection Screenshot

---

## Analytics

> Add Analytics Screenshot

---

## History

> Add History Screenshot

---

# 🌍 Deployment

### Backend

* Railway

### Frontend

* Streamlit Community Cloud

---

# 🔮 Future Improvements

* Video Damage Detection
* Live Camera Detection
* GPS Integration
* PDF Report Generation
* User Authentication
* Cloud Storage
* Mobile Application
* Damage Severity Analysis
* Interactive Maps
* Real-Time Monitoring

---

# 👩‍💻 Developer

## Warda Ahad

**Bachelor of Artificial Intelligence**

The Islamia University of Bahawalpur

Machine Learning Engineer Apprentice

---

# ⭐ Show Your Support

If you like this project, please give it a ⭐ on GitHub.

It motivates future development and helps others discover the project.

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

## 🚀 AI for Safer Roads

### Made with ❤️ using Python, YOLOv11, FastAPI & Streamlit

</div>
