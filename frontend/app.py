"""
=========================================================
AI Road Damage Detection System
Streamlit Frontend
Developer : Warda Ahad
Backend   : FastAPI + YOLOv11
=========================================================
"""

import io
from datetime import datetime

import requests
import pandas as pd
import streamlit as st
from PIL import Image


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="AI Road Damage Detection",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# Local Backend API
# =========================================================

API_URL = "http://127.0.0.1:8000"


# =========================================================
# Custom CSS
# =========================================================

st.markdown(
    """
    <style>

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    .stApp {
        background: linear-gradient(
            180deg,
            #0f172a 0%,
            #111827 100%
        );
    }

    .main-title {
        font-size: 2.6rem;
        font-weight: 800;

        background: linear-gradient(
            90deg,
            #38bdf8,
            #818cf8
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-bottom: 0.2rem;
    }

    .sub-title {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-bottom: 1.5rem;
    }

    .card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1.2rem;
    }

    .metric-box {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 1rem;
        text-align: center;
    }

    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #38bdf8;
    }

    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .badge-online {
        background: #064e3b;
        color: #34d399;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .badge-offline {
        background: #450a0a;
        color: #f87171;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .stButton > button {
        background: linear-gradient(
            90deg,
            #38bdf8,
            #818cf8
        );

        color: #0f172a;
        font-weight: 700;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.4rem;
    }

    .stButton > button:hover {
        opacity: 0.9;
        color: #0f172a;
    }

    section[data-testid="stSidebar"] {
        background: #0b1220;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Session State
# =========================================================

if "history" not in st.session_state:
    st.session_state.history = []


# =========================================================
# Backend Health Check
# =========================================================

def check_backend_health():

    try:

        response = requests.get(
            f"{API_URL}/health",
            timeout=8
        )

        if response.status_code == 200:

            return True, response.json()

        return False, None

    except requests.exceptions.RequestException:

        return False, None


# =========================================================
# Prediction Function
# =========================================================

def run_prediction(
    image_bytes: bytes,
    filename: str
):

    files = {
        "file": (
            filename,
            image_bytes,
            "image/jpeg"
        )
    }

    response = requests.post(
        f"{API_URL}/predict",
        files=files,
        timeout=120
    )

    response.raise_for_status()

    return response.json()


# =========================================================
# Fetch Result Image
# =========================================================

def fetch_result_image(
    result_filename: str
):

    response = requests.get(
        f"{API_URL}/download/{result_filename}",
        timeout=30
    )

    response.raise_for_status()

    return Image.open(
        io.BytesIO(response.content)
    )


# =========================================================
# Backend Status
# =========================================================

is_online, health_data = check_backend_health()


# =========================================================
# Sidebar
# =========================================================

with st.sidebar:

    st.markdown(
        "## 🛣️ Road Damage AI"
    )

    st.caption(
        "YOLOv11-powered road damage detector"
    )

    st.divider()

    # -----------------------------------------------------
    # Backend Status
    # -----------------------------------------------------

    if is_online:

        st.markdown(
            '<span class="badge-online">'
            '● Backend Online'
            '</span>',
            unsafe_allow_html=True,
        )

        if health_data:

            st.caption(
                f"Model loaded: "
                f"{health_data.get('model_loaded')}"
            )

            st.caption(
                f"API version: "
                f"{health_data.get('version')}"
            )

    else:

        st.markdown(
            '<span class="badge-offline">'
            '● Backend Offline'
            '</span>',
            unsafe_allow_html=True,
        )

        st.caption(
            "Start the FastAPI backend first."
        )

        st.code(
            "python -m uvicorn "
            "backend.main:app "
            "--reload "
            "--host 127.0.0.1 "
            "--port 8000"
        )

    st.divider()

    # -----------------------------------------------------
    # About
    # -----------------------------------------------------

    st.markdown(
        "### ⚙️ About"
    )

    st.write(
        "Upload a road image and the model will "
        "detect cracks, potholes and other surface "
        "damage with bounding boxes and confidence "
        "scores."
    )

    st.divider()

    # -----------------------------------------------------
    # Links
    # -----------------------------------------------------

    st.markdown(
        "### 🔗 Links"
    )

    st.markdown(
        "[GitHub Repository]"
        "(https://github.com/WardaAhad/"
        "ai-road-damage-detection-system)"
    )

    st.markdown(
        f"[Backend API]({API_URL})"
    )

    st.markdown(
        f"[API Documentation]"
        f"({API_URL}/docs)"
    )

    st.divider()

    st.caption(
        "Developed by Warda Ahad"
    )


# =========================================================
# Main Header
# =========================================================

st.markdown(
    """
    <div class="main-title">
        AI Road Damage Detection
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="sub-title">
        Upload a road/pavement image to automatically
        detect cracks, potholes and surface damage
        using a YOLOv11 deep learning model.
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Tabs
# =========================================================

tab_detect, tab_history, tab_about = st.tabs(
    [
        "🔍 Detect",
        "🕘 History",
        "ℹ️ About the Project",
    ]
)


# =========================================================
# TAB 1 : Detection
# =========================================================

with tab_detect:

    left, right = st.columns(
        [1, 1],
        gap="large"
    )

    # =====================================================
    # LEFT COLUMN
    # =====================================================

    with left:

        st.markdown(
            "#### 1. Upload Image"
        )

        uploaded_file = st.file_uploader(
            "Choose a road image",
            type=[
                "jpg",
                "jpeg",
                "png",
                "bmp",
                "webp",
            ],
            help=(
                "Supported formats: "
                "JPG, JPEG, PNG, BMP, WEBP"
            ),
        )

        if uploaded_file is not None:

            image = Image.open(
                uploaded_file
            )

            st.image(
                image,
                caption="Uploaded Image",
                use_container_width=True,
            )

            run_btn = st.button(
                "🚀 Run Detection",
                use_container_width=True,
            )

        else:

            run_btn = False

            st.info(
                "👆 Please upload an image to begin."
            )


    # =====================================================
    # RIGHT COLUMN
    # =====================================================

    with right:

        st.markdown(
            "#### 2. Detection Result"
        )

        if uploaded_file is not None and run_btn:

            if not is_online:

                st.error(
                    "Backend server is not running. "
                    "Please start FastAPI first."
                )

            else:

                with st.spinner(
                    "Analyzing image with YOLOv11..."
                ):

                    try:

                        # ---------------------------------
                        # Read Image
                        # ---------------------------------

                        uploaded_file.seek(0)

                        image_bytes = (
                            uploaded_file.read()
                        )

                        # ---------------------------------
                        # Prediction
                        # ---------------------------------

                        result = run_prediction(
                            image_bytes,
                            uploaded_file.name
                        )

                        # ---------------------------------
                        # Result Image
                        # ---------------------------------

                        result_img = fetch_result_image(
                            result["filename"]
                        )

                        st.image(
                            result_img,
                            caption="Detected Damage",
                            use_container_width=True,
                        )

                        # ---------------------------------
                        # Metrics
                        # ---------------------------------

                        st.markdown(
                            "### 📊 Detection Summary"
                        )

                        c1, c2 = st.columns(2)

                        c1.metric(
                            "Objects Detected",
                            result["total_objects"]
                        )

                        c2.metric(
                            "Processing Time",
                            f"{result['processing_time']}s"
                        )

                        # ---------------------------------
                        # Detection Details
                        # ---------------------------------

                        if result["detections"]:

                            st.markdown(
                                "### 🔎 Detection Details"
                            )

                            df = pd.DataFrame(
                                result["detections"]
                            )

                            df["confidence"] = (
                                df["confidence"]
                                * 100
                            ).round(
                                1
                            ).astype(
                                str
                            ) + "%"

                            st.dataframe(
                                df,
                                use_container_width=True,
                                hide_index=True,
                            )

                        else:

                            st.info(
                                "No road damage detected."
                            )

                        # ---------------------------------
                        # Save History
                        # ---------------------------------

                        st.session_state.history.insert(
                            0,
                            {
                                "time":
                                    datetime.now().strftime(
                                        "%Y-%m-%d %H:%M:%S"
                                    ),

                                "filename":
                                    uploaded_file.name,

                                "total_objects":
                                    result["total_objects"],

                                "processing_time":
                                    result["processing_time"],

                                "detections":
                                    result["detections"],
                            }
                        )

                        st.success(
                            "✅ Detection completed successfully."
                        )

                    except requests.exceptions.HTTPError as e:

                        st.error(
                            f"Backend returned an error: {e}"
                        )

                    except requests.exceptions.RequestException as e:

                        st.error(
                            f"Request to backend failed: {e}"
                        )

                    except Exception as e:

                        st.error(
                            f"Something went wrong: {e}"
                        )

        else:

            st.markdown(
                """
                <div class="card">

                Detection result will appear here
                after you upload an image and click
                <b>Run Detection</b>.

                </div>
                """,
                unsafe_allow_html=True,
            )


# =========================================================
# TAB 2 : History
# =========================================================

with tab_history:

    st.markdown(
        "#### 🕘 Session Detection History"
    )

    if not st.session_state.history:

        st.info(
            "No detections yet in this session. "
            "Run a detection from the **Detect** tab."
        )

    else:

        for item in st.session_state.history:

            with st.expander(
                f"📄 {item['filename']} — "
                f"{item['time']}"
            ):

                c1, c2 = st.columns(2)

                c1.metric(
                    "Objects Detected",
                    item["total_objects"]
                )

                c2.metric(
                    "Processing Time",
                    f"{item['processing_time']}s"
                )

                if item["detections"]:

                    df = pd.DataFrame(
                        item["detections"]
                    )

                    df["confidence"] = (
                        df["confidence"]
                        * 100
                    ).round(
                        1
                    ).astype(
                        str
                    ) + "%"

                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True,
                    )

        if st.button(
            "🗑️ Clear History"
        ):

            st.session_state.history = []

            st.rerun()


# =========================================================
# TAB 3 : About
# =========================================================

with tab_about:

    st.markdown(
        """
        <div class="card">

        <h4>
            🛣️ AI Road Damage Detection System
        </h4>

        <p>
            This project uses a
            <b>YOLOv11</b> object detection model
            trained to identify road surface damage
            such as cracks and potholes from images.
        </p>

        <b>Architecture</b>

        <ul>

            <li>
                <b>Backend:</b>
                FastAPI + Ultralytics YOLOv11
            </li>

            <li>
                <b>Frontend:</b>
                Streamlit
            </li>

            <li>
                <b>Model:</b>
                Custom-trained YOLOv11 (best.pt)
            </li>

        </ul>

        <b>Detection Classes</b>

        <p>
            Road cracks, potholes and other surface
            damage types, each returned with a
            bounding box and confidence score.
        </p>

        <b>How it works</b>

        <ol>

            <li>
                Upload a road image
            </li>

            <li>
                Image is sent to the FastAPI backend
            </li>

            <li>
                YOLOv11 model runs inference
            </li>

            <li>
                Annotated image and detection details
                are returned and displayed
            </li>

        </ol>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "[⭐ View Source Code on GitHub]"
        "(https://github.com/WardaAhad/"
        "ai-road-damage-detection-system)"
    )


# =========================================================
# Footer
# =========================================================

st.divider()

st.caption(
    "© 2026 AI Road Damage Detection System — "
    "Built with FastAPI, YOLOv11 & Streamlit"
)