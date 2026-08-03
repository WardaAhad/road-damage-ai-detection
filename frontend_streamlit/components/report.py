"""
=========================================================
AI Road Damage Detection System
Report Component
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
from datetime import datetime
import json


# ==========================================================
# Show Detection Report
# ==========================================================

def show_report(result):

    if result is None:

        st.warning("No report available.")

        return

    st.subheader("📄 Detection Report")

    st.write("### Detection Details")

    st.write(result)


# ==========================================================
# Report Summary
# ==========================================================

def report_summary(

    image_name,
    damage_type,
    confidence

):

    st.info(f"""

📷 Image : {image_name}

🚧 Damage : {damage_type}

🎯 Confidence : {confidence} %

📅 Date : {datetime.now().strftime('%d-%m-%Y')}

🕒 Time : {datetime.now().strftime('%I:%M %p')}

""")


# ==========================================================
# JSON Download
# ==========================================================

def download_json(result):

    json_data = json.dumps(

        result,

        indent=4

    )

    st.download_button(

        label="📥 Download JSON Report",

        data=json_data,

        file_name="road_damage_report.json",

        mime="application/json",

        width="stretch"

    )


# ==========================================================
# Text Report
# ==========================================================

def download_text(

    image_name,

    damage,

    confidence

):

    report = f"""
=======================================

AI ROAD DAMAGE DETECTION REPORT

=======================================

Image Name : {image_name}

Damage Type : {damage}

Confidence : {confidence} %

Date : {datetime.now().strftime('%d-%m-%Y')}

Time : {datetime.now().strftime('%I:%M %p')}

=======================================
"""

    st.download_button(

        label="📄 Download Text Report",

        data=report,

        file_name="Detection_Report.txt",

        mime="text/plain",

        width="stretch"

    )


# ==========================================================
# Detection Statistics
# ==========================================================

def report_statistics():

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Images",

            "1250"

        )

    with col2:

        st.metric(

            "Damages",

            "438"

        )

    with col3:

        st.metric(

            "Accuracy",

            "98.6%"

        )


# ==========================================================
# Complete Report
# ==========================================================

def complete_report(

    image_name,

    damage,

    confidence,

    result

):

    report_summary(

        image_name,

        damage,

        confidence

    )

    st.divider()

    show_report(result)

    st.divider()

    download_json(result)

    download_text(

        image_name,

        damage,

        confidence

    )
