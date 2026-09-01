"""
=========================================================
AI Road Damage Detection System
Frontend (Streamlit) — Standalone (no backend)
Developer : Warda Ahad
=========================================================
"""

import os
import time
from io import BytesIO

import streamlit as st
from PIL import Image

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
# MODEL CONFIGURATION
# ==========================================================

MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pt")

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
APP_VERSION = "2.0.0"
MODEL_NAME = "YOLOv11"
CONFIDENCE_THRESHOLD = 0.25


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

    section[data-testid="stSidebar"]{
        background: var(--panel);
        border-right: 1px solid var(--panel-border);
    }
    section[data-testid="stSidebar"] * { color: var(--text); }

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

    .rd-divider{
        height:0; border:0; border-top:3px dashed var(--panel-border);
        margin:1.6rem 0;
    }

    .rd-status{
        display:flex; align-items:center; gap:.55rem;
        background:var(--panel); border:1px solid var(--panel-border);
        border-radius:6px; padding:.65rem .9rem; font-family:'JetBrains Mono', monospace;
        font-size:.85rem;
    }
    .rd-dot{ width:10px; height:10px; border-radius:50%; flex-shrink:0; }
    .rd-dot.on{ background:var(--green); box-shadow:0 0 8px var(--green); }
    .rd-dot.off{ background:var(--red); box-shadow:0 0 8px var(--red); }

    [data-testid="stFileUploaderDropzone"]{
        background:var(--panel) !important;
        border:2px dashed var(--panel-border) !important;
        border-radius:8px !important;
    }
    [data-testid="stFileUploaderDropzone"]:hover{
        border-color:var(--amber) !important;
    }

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

    div[data-testid="stImage"]{
        position:relative;
        border:1px solid var(--panel-border);
        border-radius:4px;
        padding:10px;
        background:var(--panel);
    }
    div[data-testid="stImage"]::before, div[data-testid="stImage"]::after{
        content:''; position:absolute; width:22px; height:22px;
        border:3px solid var(--amber); pointer-events:none;
    }
    div[data-testid="stImage"]::before{ top:8px; left:8px; border-right:none; border-bottom:none; }
    div[data-testid="stImage"]::after{ top:8px; right:8px; border-left:none; border-bottom:none; }
    .rd-label{
        font-family:'JetBrains Mono', monospace; font-size:.72rem;
        color:var(--amber); letter-spacing:.12em; text-transform:uppercase;
        margin-bottom:.5rem;
    }

    [data-testid="stMetric"]{
        background:var(--panel); border:1px solid var(--panel-border);
        border-radius:6px; padding:.8rem 1rem;
    }
    [data-testid="stMetricValue"]{ color:var(--amber); font-family:'JetBrains Mono', monospace; }

    .rd-table{ width:100%; border-collapse:collapse; font-family:'JetBrains Mono', monospace; font-size:.85rem; }
    .rd-table th{
        text-align:left; text-transform:uppercase; letter-spacing:.08em;
        font-size:.72rem; color:var(--muted); padding:.5rem .6rem;
        border-bottom:1px solid var(--panel-border);
    }
    .rd-table td{ padding:.55rem .6rem; border-bottom:1px solid var(--panel-border); }
    .rd-bar-track{ background:#2a2d35; border-radius:3px; height:6px; width:100%; overflow:hidden; }
    .rd-bar-fill{ height:100%; background:var(--amber); }

    .rd-footer{
        margin-top:2.5rem; padding-top:1rem; border-top:1px solid var(--panel-border);
        color:var(--muted); font-size:.8rem; font-family:'JetBrains Mono', monospace;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==========================================================
# MODEL LOADING (cached — loads once per session)
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_model():
    from ultralytics import YOLO
    if not os.path.exists(MODEL_PATH):
        return None
    return YOLO(MODEL_PATH)


def confidence_color(conf: float) -> str:
    if conf >= 0.75:
        return "var(--green)"
    if conf >= 0.5:
        return "var(--amber)"
    return "var(--red)"


def render_detections_table(detections: list) -> str:
    # NOTE: every line below starts at column 0 with no leading spaces.
    # Streamlit's markdown renderer treats 4+ leading spaces as a code
    # block even with unsafe_allow_html=True, which was breaking the
    # table into raw visible HTML. Keep this whole block unindented.
    row_html = []
    for d in detections:
        conf = d.get("confidence", 0)
        bar = (
            f'<div style="display:flex;align-items:center;gap:.5rem;">'
            f'<div class="rd-bar-track" style="max-width:90px;">'
            f'<div class="rd-bar-fill" style="width:{conf*100:.0f}%;background:{confidence_color(conf)};"></div>'
            f'</div><span>{conf:.2f}</span></div>'
        )
        row_html.append(
            f'<tr><td>{d.get("class_name","—")}</td><td>{bar}</td>'
            f'<td>({d.get("xmin","-")}, {d.get("ymin","-")})</td>'
            f'<td>({d.get("xmax","-")}, {d.get("ymax","-")})</td></tr>'
        )
    rows = "".join(row_html)
    header = "<tr><th>Class</th><th>Confidence</th><th>Top-Left</th><th>Bottom-Right</th></tr>"
    return f'<table class="rd-table"><thead>{header}</thead><tbody>{rows}</tbody></table>'


def run_local_prediction(model, pil_image: Image.Image):
    """Runs YOLO inference directly (no backend/API call) and returns
    an annotated PIL image plus a list of detection dicts."""
    start = time.time()
    results = model.predict(pil_image, conf=CONFIDENCE_THRESHOLD, verbose=False)
    elapsed = round(time.time() - start, 2)

    result = results[0]
    annotated_bgr = result.plot()  # numpy array, BGR
    annotated_rgb = annotated_bgr[:, :, ::-1]
    annotated_image = Image.fromarray(annotated_rgb)

    detections = []
    names = result.names
    if result.boxes is not None:
        for box in result.boxes:
            xyxy = box.xyxy[0].tolist()
            cls_id = int(box.cls[0].item())
            conf = float(box.conf[0].item())
            detections.append({
                "class_name": names.get(cls_id, str(cls_id)),
                "confidence": conf,
                "xmin": round(xyxy[0]),
                "ymin": round(xyxy[1]),
                "xmax": round(xyxy[2]),
                "ymax": round(xyxy[3]),
            })

    return annotated_image, detections, elapsed


# ==========================================================
# LOAD MODEL
# ==========================================================

model = load_model()

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

    st.markdown("**Model Status**")
    if model is not None:
        st.markdown(
            """<div class="rd-status"><div class="rd-dot on"></div> MODEL LOADED</div>""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """<div class="rd-status"><div class="rd-dot off"></div> MODEL NOT FOUND</div>""",
            unsafe_allow_html=True,
        )
        st.caption(f"Expected at: `models/best.pt`")

    st.markdown("<hr class='rd-divider'>", unsafe_allow_html=True)
    st.caption("RUNNING FULLY IN-APP — NO BACKEND")


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

if model is None:
    st.error(
        "Model file not found. Make sure `models/last.pt` is included in the "
        "deployed app folder."
    )

uploaded_file = st.file_uploader(
    "Upload a road image",
    type=ALLOWED_IMAGE_TYPES,
    help=f"Max file size: {MAX_UPLOAD_SIZE_MB} MB",
    label_visibility="collapsed",
    disabled=model is None,
)

if uploaded_file is not None and model is not None:
    file_bytes = uploaded_file.getvalue()
    size_mb = len(file_bytes) / (1024 * 1024)

    if size_mb > MAX_UPLOAD_SIZE_MB:
        st.error(f"File too large ({size_mb:.1f} MB). Max is {MAX_UPLOAD_SIZE_MB} MB.")
    else:
        col1, col2 = st.columns(2)
        input_image = Image.open(BytesIO(file_bytes)).convert("RGB")

        with col1:
            st.markdown("<div class='rd-label'>Input</div>", unsafe_allow_html=True)
            st.image(input_image, use_container_width=True)

        detect_clicked = st.button("🔍  Detect Road Damage", type="primary", use_container_width=True)

        if detect_clicked:
            with st.spinner("Running YOLOv11 detection..."):
                annotated_image, detections, elapsed = run_local_prediction(model, input_image)

            with col2:
                st.markdown("<div class='rd-label'>Detected</div>", unsafe_allow_html=True)
                st.image(annotated_image, use_container_width=True)

                out_buffer = BytesIO()
                annotated_image.save(out_buffer, format="JPEG")
                st.download_button(
                    "⬇  Download Result",
                    data=out_buffer.getvalue(),
                    file_name=f"detected_{uploaded_file.name}",
                    mime="image/jpeg",
                    use_container_width=True,
                )

            st.markdown("<hr class='rd-divider'>", unsafe_allow_html=True)

            m1, m2 = st.columns(2)
            m1.metric("Objects Detected", len(detections))
            m2.metric("Processing Time", f"{elapsed} s")

            if detections:
                st.markdown('<div class="rd-label" style="margin-top:1rem;">Detections</div>', unsafe_allow_html=True)
                st.markdown(render_detections_table(detections), unsafe_allow_html=True)
            else:
                st.info("No damage detected in this image.")
else:
    if model is not None:
        st.markdown(
            """<div class="rd-status"><div class="rd-dot on"></div> Upload an image to begin scanning</div>""",
            unsafe_allow_html=True,
        )

st.markdown(
    f"<div class='rd-footer'>{APP_NAME} · {MODEL_NAME} · Built by Warda Ahad</div>",
    unsafe_allow_html=True,
)
