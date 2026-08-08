"""
=========================================================
AI Road Damage Detection System
Frontend (Streamlit)
Developer : Warda Ahad
=========================================================
"""

import os
import requests
import streamlit as st
from PIL import Image
from io import BytesIO


# ==========================================================
# BASE DIRECTORY
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

PAGE_TITLE = "AI Road Damage Detection System"
PAGE_ICON = "🚧"
LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)


# ==========================================================
# BACKEND API CONFIGURATION
# ==========================================================

API_BASE_URL = st.secrets.get(
    "API_URL",
    "https://road-damage-ai-detection-production.up.railway.app",
)

PREDICT_ENDPOINT = f"{API_BASE_URL}/predict"
HEALTH_ENDPOINT = f"{API_BASE_URL}/health"
MODEL_INFO_ENDPOINT = f"{API_BASE_URL}/model-info"
DOWNLOAD_ENDPOINT = f"{API_BASE_URL}/download"


# ==========================================================
# FILE CONFIGURATION
# ==========================================================

ALLOWED_IMAGE_TYPES = ["jpg", "jpeg", "png", "webp"]
MAX_UPLOAD_SIZE_MB = 10


# ==========================================================
# ASSETS (optional)
# ==========================================================

ASSETS_DIR = os.path.join(BASE_DIR, "assets")
LOGO_PATH = os.path.join(ASSETS_DIR, "logo.png")
BANNER_PATH = os.path.join(ASSETS_DIR, "banner.png")


# ==========================================================
# APP SETTINGS
# ==========================================================

APP_NAME = "AI Road Damage Detection System"
APP_VERSION = "1.0.0"
MODEL_NAME = "YOLOv11"
CONFIDENCE_THRESHOLD = 0.25
BACKEND_TIMEOUT = 120


# ==========================================================
# THEME — asphalt / hazard-amber / detection-HUD
# ==========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

    :root{
        --asphalt:#121317;
        --panel:#1b1d23;
        --panel-border:#2b2e37;
        --amber:#ffb020;
        --amber-dim:rgba(255,176,32,.14);
        --green:#3ddc84;
        --red:#ff5470;
        --text:#e9eaef;
        --muted:#9498a3;
    }

    html, body, [class*="css"], .stMarkdown, p, span, label, div {
        font-family:'Inter', sans-serif;
    }

    .stApp{
        background:
            repeating-linear-gradient(180deg, rgba(255,255,255,.015) 0 2px, transparent 2px 4px),
            var(--asphalt);
        color: var(--text);
    }

    /* ---- Sidebar: device-panel look ---- */
    section[data-testid="stSidebar"]{
        background: var(--panel);
        border-right: 1px solid var(--panel-border);
    }
    section[data-testid="stSidebar"] * { color: var(--text); }

    /* ---- Headings: condensed highway-sign type ---- */
    h1, h2, h3 {
        font-family:'Oswald', sans-serif !important;
        text-transform:uppercase;
        letter-spacing:.03em;
    }
    .rd-eyebrow{
        font-family:'JetBrains Mono', monospace;
        color:var(--amber);
        font-size:.78rem;
        letter-spacing:.18em;
        text-transform:uppercase;
        margin-bottom:.35rem;
    }
    .rd-title{
        font-family:'Oswald', sans-serif;
        font-weight:700;
        text-transform:uppercase;
        font-size:2.4rem;
        letter-spacing:.02em;
        margin:0 0 .3rem 0;
        border-left:6px solid var(--amber);
        padding-left:.6rem;
    }
    .rd-sub{ color:var(--muted); margin-bottom:1.2rem; }

    /* lane-marking divider */
    .rd-divider{
        height:0; border:0; border-top:3px dashed var(--panel-border);
        margin:1.6rem 0;
    }

    /* ---- Status pill ---- */
    .rd-status{
        display:flex; align-items:center; gap:.55rem;
        background:var(--panel); border:1px solid var(--panel-border);
        border-radius:6px; padding:.65rem .9rem; font-family:'JetBrains Mono', monospace;
        font-size:.85rem;
    }
    .rd-dot{ width:10px; height:10px; border-radius:50%; flex-shrink:0; }
    .rd-dot.on{ background:var(--green); box-shadow:0 0 8px var(--green); }
    .rd-dot.off{ background:var(--red); box-shadow:0 0 8px var(--red); }

    /* ---- Uploader ---- */
    [data-testid="stFileUploaderDropzone"]{
        background:var(--panel) !important;
        border:2px dashed var(--panel-border) !important;
        border-radius:8px !important;
    }
    [data-testid="stFileUploaderDropzone"]:hover{
        border-color:var(--amber) !important;
    }

    /* ---- Buttons ---- */
    .stButton>button{
        font-family:'Oswald', sans-serif;
        text-transform:uppercase;
        letter-spacing:.06em;
        background:var(--amber) !important;
        color:#1a1300 !important;
        border:none !important;
        border-radius:4px !important;
        font-weight:600;
    }
    .stButton>button:hover{ filter:brightness(1.08); }
    .stDownloadButton>button{
        border:1px solid var(--amber) !important;
        color:var(--amber) !important;
        background:transparent !important;
        border-radius:4px !important;
        font-family:'JetBrains Mono', monospace !important;
    }

    /* ---- Viewfinder frame around images (signature element) ---- */
    .rd-frame{
        position:relative;
        border:1px solid var(--panel-border);
        border-radius:4px;
        padding:10px;
        background:var(--panel);
    }
    .rd-frame::before, .rd-frame::after{
        content:''; position:absolute; width:22px; height:22px;
        border:3px solid var(--amber);
    }
    .rd-frame::before{ top:-2px; left:-2px; border-right:none; border-bottom:none; }
    .rd-frame::after{ top:-2px; right:-2px; border-left:none; border-bottom:none; }
    .rd-label{
        font-family:'JetBrains Mono', monospace; font-size:.72rem;
        color:var(--amber); letter-spacing:.12em; text-transform:uppercase;
        margin-bottom:.5rem;
    }

    /* ---- Metrics ---- */
    [data-testid="stMetric"]{
        background:var(--panel); border:1px solid var(--panel-border);
        border-radius:6px; padding:.8rem 1rem;
    }
    [data-testid="stMetricValue"]{ color:var(--amber); font-family:'JetBrains Mono', monospace; }

    /* ---- Detection table ---- */
    .rd-table{ width:100%; border-collapse:collapse; font-family:'JetBrains Mono', monospace; font-size:.85rem; }
    .rd-table th{
        text-align:left; text-transform:uppercase; letter-spacing:.08em;
        font-size:.72rem; color:var(--muted); padding:.5rem .6rem;
        border-bottom:1px solid var(--panel-border);
    }
    .rd-table td{ padding:.55rem .6rem; border-bottom:1px solid var(--panel-border); }
    .rd-bar-track{ background:#2a2d35; border-radius:3px; height:6px; width:100%; overflow:hidden; }
    .rd-bar-fill{ height:100%; background:var(--amber); }

    /* ---- Footer ---- */
    .rd-footer{
        margin-top:2.5rem; padding-top:1rem; border-top:1px solid var(--panel-border);
        color:var(--muted); font-size:.8rem; font-family:'JetBrains Mono', monospace;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==========================================================
# HELPERS
# ==========================================================

def check_backend_health():
    try:
        res = requests.get(HEALTH_ENDPOINT, timeout=10)
        if res.status_code == 200:
            return res.json()
    except requests.exceptions.RequestException:
        return None
    return None


def run_prediction(image_bytes: bytes, filename: str):
    try:
        files = {"file": (filename, image_bytes)}
        res = requests.post(PREDICT_ENDPOINT, files=files, timeout=BACKEND_TIMEOUT)
        if res.status_code == 200:
            return res.json()
        st.error(f"Backend Error ({res.status_code}): {res.text}")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"Could not reach backend: {e}")
        return None


def confidence_color(conf: float) -> str:
    if conf >= 0.75:
        return "var(--green)"
    if conf >= 0.5:
        return "var(--amber)"
    return "var(--red)"


def render_detections_table(detections: list) -> str:
    rows = ""
    for d in detections:
        conf = d.get("confidence", 0)
        rows += f"""
        <tr>
            <td>{d.get('class_name','—')}</td>
            <td>
                <div style="display:flex; align-items:center; gap:.5rem;">
                    <div class="rd-bar-track" style="max-width:90px;">
                        <div class="rd-bar-fill" style="width:{conf*100:.0f}%; background:{confidence_color(conf)};"></div>
                    </div>
                    <span>{conf:.2f}</span>
                </div>
            </td>
            <td>({d.get('xmin','-')}, {d.get('ymin','-')})</td>
            <td>({d.get('xmax','-')}, {d.get('ymax','-')})</td>
        </tr>
        """
    return f"""
    <table class="rd-table">
        <thead>
            <tr><th>Class</th><th>Confidence</th><th>Top-Left</th><th>Bottom-Right</th></tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>
    """


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, use_container_width=True)

    st.markdown("<div class='rd-eyebrow'>Computer Vision · Infrastructure</div>", unsafe_allow_html=True)
    st.markdown(f"### {APP_NAME}")
    st.caption(f"v{APP_VERSION} · {MODEL_NAME}")

    st.markdown("<hr class='rd-divider'>", unsafe_allow_html=True)

    st.markdown("**Backend Status**")
    health = check_backend_health()

    if health:
        st.markdown(
            f"""<div class="rd-status"><div class="rd-dot on"></div>
            ONLINE · MODEL {"LOADED" if health.get("model_loaded") else "NOT LOADED"}</div>""",
            unsafe_allow_html=True,
        )
        with st.expander("Raw response"):
            st.json(health)
    else:
        st.markdown(
            """<div class="rd-status"><div class="rd-dot off"></div> UNREACHABLE</div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<hr class='rd-divider'>", unsafe_allow_html=True)
    st.caption("API BASE URL")
    st.code(API_BASE_URL, language=None)


# ==========================================================
# MAIN PAGE
# ==========================================================

if os.path.exists(BANNER_PATH):
    st.image(BANNER_PATH, use_container_width=True)

st.markdown("<div class='rd-eyebrow'>YOLOv11 · Real-Time Inference</div>", unsafe_allow_html=True)
st.markdown(f"<div class='rd-title'>{PAGE_ICON} {PAGE_TITLE}</div>", unsafe_allow_html=True)
st.markdown(
    "<p class='rd-sub'>Upload a road image — potholes, cracks and surface damage are detected and boxed automatically.</p>",
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "Upload a road image",
    type=ALLOWED_IMAGE_TYPES,
    help=f"Max file size: {MAX_UPLOAD_SIZE_MB} MB",
    label_visibility="collapsed",
)

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    size_mb = len(file_bytes) / (1024 * 1024)

    if size_mb > MAX_UPLOAD_SIZE_MB:
        st.error(f"File too large ({size_mb:.1f} MB). Max is {MAX_UPLOAD_SIZE_MB} MB.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='rd-frame'><div class='rd-label'>Input</div>", unsafe_allow_html=True)
            st.image(Image.open(BytesIO(file_bytes)), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        detect_clicked = st.button("🔍  Detect Road Damage", type="primary", use_container_width=True)

        if detect_clicked:
            with st.spinner("Running YOLOv11 detection..."):
                result = run_prediction(file_bytes, uploaded_file.name)

            if result and result.get("success"):
                with col2:
                    st.markdown("<div class='rd-frame'><div class='rd-label'>Detected</div>", unsafe_allow_html=True)
                    result_filename = result.get("filename")
                    img_bytes = None
                    try:
                        img_res = requests.get(f"{DOWNLOAD_ENDPOINT}/{result_filename}", timeout=30)
                        if img_res.status_code == 200:
                            img_bytes = img_res.content
                            st.image(Image.open(BytesIO(img_bytes)), use_container_width=True)
                    except requests.exceptions.RequestException:
                        st.warning("Could not load the annotated result image.")
                    st.markdown("</div>", unsafe_allow_html=True)

                    if img_bytes:
                        st.download_button(
                            "⬇  Download Result",
                            data=img_bytes,
                            file_name=f"detected_{result_filename}",
                            mime="image/jpeg",
                            use_container_width=True,
                        )

                st.markdown("<hr class='rd-divider'>", unsafe_allow_html=True)

                m1, m2 = st.columns(2)
                m1.metric("Objects Detected", result.get("total_objects", 0))
                m2.metric("Processing Time", f"{result.get('processing_time', 0)} s")

                detections = result.get("detections", [])
                if detections:
                    st.markdown("<div class='rd-label' style='margin-top:1rem;'>Detections</div>", unsafe_allow_html=True)
                    st.markdown(render_detections_table(detections), unsafe_allow_html=True)
                else:
                    st.info("No damage detected in this image.")
else:
    st.markdown(
        """<div class="rd-status"><div class="rd-dot on"></div> Upload an image to begin scanning</div>""",
        unsafe_allow_html=True,
    )

st.markdown(
    f"<div class='rd-footer'>{APP_NAME} · {MODEL_NAME} · Built by Warda Ahad</div>",
    unsafe_allow_html=True,
)
