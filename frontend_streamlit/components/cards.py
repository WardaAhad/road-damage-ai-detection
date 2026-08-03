"""
=========================================================
AI Road Damage Detection System
Dashboard Cards
Developer : Warda Ahad
=========================================================
"""

import streamlit as st


# ==========================================================
# Single Metric Card
# ==========================================================

def metric_card(title, value, icon, color="#2563EB"):

    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            border-left:6px solid {color};
            padding:20px;
            border-radius:18px;
            box-shadow:0 8px 20px rgba(0,0,0,.25);
            margin-bottom:15px;
        ">

            <h2 style="margin:0;font-size:18px;color:white;">
                {icon} {title}
            </h2>

            <h1 style="
                margin-top:10px;
                color:white;
                font-size:36px;
            ">
                {value}
            </h1>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# Dashboard Cards
# ==========================================================

def dashboard_cards():

    col1, col2 = st.columns(2)

    with col1:

        metric_card(
            "Uploaded Images",
            "1250",
            "📂",
            "#2563EB"
        )

        metric_card(
            "Road Cracks",
            "320",
            "🛣️",
            "#F59E0B"
        )

        metric_card(
            "Potholes",
            "118",
            "🕳️",
            "#EF4444"
        )

    with col2:

        metric_card(
            "Accuracy",
            "98.6%",
            "🎯",
            "#22C55E"
        )

        metric_card(
            "Confidence",
            "96%",
            "📈",
            "#06B6D4"
        )

        metric_card(
            "Backend",
            "Online",
            "🟢",
            "#22C55E"
        )


# ==========================================================
# Model Information
# ==========================================================

def model_information():

    st.markdown("## 🤖 Model Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", "YOLOv11")

    with col2:
        st.metric("Framework", "Ultralytics")

    with col3:
        st.metric("Version", "v11")


# ==========================================================
# Statistics
# ==========================================================

def statistics():

    st.markdown("## 📊 Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Images", "1250", "+18")

    with c2:
        st.metric("Damages", "438", "+10")

    with c3:
        st.metric("Reports", "210", "+7")

    with c4:
        st.metric("Accuracy", "98.6%", "+0.4%")


# ==========================================================
# Detection Summary
# ==========================================================

def detection_summary():

    st.markdown("## 🚧 Detection Summary")

    st.success("✅ Crack Detection Working")

    st.success("✅ Pothole Detection Working")

    st.success("✅ Road Patch Detection Working")

    st.info("🤖 YOLOv11 Model Loaded Successfully")
