"""
=========================================================
AI Road Damage Detection System
Charts Component
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
import plotly.express as px
import pandas as pd


# ==========================================================
# Bar Chart
# ==========================================================

def show_bar_chart():

    data = pd.DataFrame({

        "Damage Type": [
            "Crack",
            "Pothole",
            "Patch"
        ],

        "Count": [
            120,
            65,
            40
        ]

    })

    fig = px.bar(

        data,

        x="Damage Type",

        y="Count",

        title="Road Damage Distribution",

        text="Count"

    )

    fig.update_layout(

        template="plotly_dark",

        height=450

    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# ==========================================================
# Pie Chart
# ==========================================================

def show_pie_chart():

    data = pd.DataFrame({

        "Damage": [
            "Crack",
            "Pothole",
            "Patch"
        ],

        "Value": [
            120,
            65,
            40
        ]

    })

    fig = px.pie(

        data,

        names="Damage",

        values="Value",

        hole=0.45,

        title="Damage Percentage"

    )

    fig.update_layout(

        template="plotly_dark",

        height=450

    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# ==========================================================
# Line Chart
# ==========================================================

def show_line_chart():

    data = pd.DataFrame({

        "Day":[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],

        "Detections":[
            20,
            35,
            28,
            42,
            51,
            38,
            60
        ]

    })

    fig = px.line(

        data,

        x="Day",

        y="Detections",

        markers=True,

        title="Weekly Detection Trend"

    )

    fig.update_layout(

        template="plotly_dark",

        height=450

    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


# ==========================================================
# Confidence Chart
# ==========================================================

def show_confidence_chart():

    confidence = 96

    st.subheader("🎯 Model Confidence")

    st.progress(confidence / 100)

    st.success(f"Average Confidence : {confidence}%")



# ==========================================================
# Detection Summary
# ==========================================================

def detection_summary():

    st.subheader("📋 Detection Summary")

    summary = pd.DataFrame({

        "Damage":[
            "Crack",
            "Pothole",
            "Patch"
        ],

        "Detected":[
            120,
            65,
            40
        ]

    })

    st.dataframe(

        summary,

        width="stretch",

        hide_index=True

    )


# ==========================================================
# Dashboard Analytics
# ==========================================================

def dashboard_charts():

    col1, col2 = st.columns(2)

    with col1:

        show_bar_chart()

    with col2:

        show_pie_chart()

    st.divider()

    show_line_chart()

    st.divider()

    show_confidence_chart()

    st.divider()

    detection_summary()
