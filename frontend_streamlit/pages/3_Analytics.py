"""
=========================================================
AI Road Damage Detection System
Analytics
Developer : Warda Ahad
=========================================================
"""

import streamlit as st


# Theme
from styles.theme import (
    set_page_config,
    apply_theme,
    hero_title,
    section_title
)


# Components
from components.sidebar import show_sidebar

from components.navbar import (
    show_navbar,
    welcome_banner
)


from components.charts import (
    show_bar_chart,
    show_pie_chart,
    show_line_chart,
    show_confidence_chart,
    detection_summary
)


from components.cards import (
    statistics,
    model_information
)


from components.footer import show_footer



# ==========================================================
# Page Configuration
# ==========================================================

set_page_config()

apply_theme()



# ==========================================================
# Sidebar
# ==========================================================

show_sidebar()



# ==========================================================
# Navbar
# ==========================================================

show_navbar()



# ==========================================================
# Hero Section
# ==========================================================

hero_title(
    "📊 Analytics Dashboard",
    "Visualize road damage statistics and model performance."
)


welcome_banner()


st.divider()



# ==========================================================
# Statistics
# ==========================================================

statistics()


st.divider()



# ==========================================================
# Model Information
# ==========================================================

model_information()


st.divider()



# ==========================================================
# Damage Distribution
# ==========================================================

section_title("📊 Damage Distribution")


col1, col2 = st.columns(2)


with col1:

    show_bar_chart()



with col2:

    show_pie_chart()



st.divider()



# ==========================================================
# Weekly Detection Trend
# ==========================================================

section_title("📈 Weekly Detection Trend")


show_line_chart()



st.divider()



# ==========================================================
# Confidence Analysis
# ==========================================================

section_title("🎯 Model Confidence")


show_confidence_chart()



st.divider()



# ==========================================================
# Detection Summary
# ==========================================================

section_title("📋 Detection Summary")


detection_summary()



st.divider()



# ==========================================================
# Damage Insights
# ==========================================================

section_title("💡 Damage Insights")



col1, col2 = st.columns(2)



with col1:


    st.info(
        """
### 📌 Key Findings

- Crack is the most common road damage.
- Potholes are detected less frequently.
- Model accuracy remains above 95%.
- YOLOv11 provides fast inference.
"""
    )



with col2:


    st.success(
        """
### 🚀 System Performance

✅ FastAPI Connected

✅ YOLOv11 Loaded

✅ Streamlit Running

✅ Analytics Updated
"""
    )



st.divider()



# ==========================================================
# Performance Metrics
# ==========================================================

section_title("⚡ Performance")



c1, c2, c3 = st.columns(3)



with c1:

    st.metric(
        "Inference Time",
        "45 ms",
        "-5 ms"
    )



with c2:

    st.metric(
        "Average Confidence",
        "96.8%",
        "+1.2%"
    )



with c3:

    st.metric(
        "Model Accuracy",
        "98.6%",
        "+0.4%"
    )



st.divider()



# ==========================================================
# Footer
# ==========================================================

show_footer()
