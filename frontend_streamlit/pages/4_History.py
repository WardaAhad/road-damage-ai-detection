"""
=========================================================
AI Road Damage Detection System
History
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
import pandas as pd

# Theme
from styles.theme import (
    set_page_config,
    apply_theme,
    hero_title,
    section_title
)

# Components
from components.sidebar import show_sidebar
from components.navbar import show_navbar
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
    "🕒 Detection History",
    "View all previously detected road damages."
)

st.divider()

# ==========================================================
# Sample History
# ==========================================================

section_title("📋 Detection History")

history = pd.DataFrame({

    "Image":[
        "road_001.jpg",
        "road_002.jpg",
        "road_003.jpg",
        "road_004.jpg",
        "road_005.jpg"
    ],

    "Damage":[
        "Crack",
        "Pothole",
        "Patch",
        "Crack",
        "D00"
    ],

    "Confidence":[
        "98%",
        "95%",
        "91%",
        "97%",
        "96%"
    ],

    "Date":[
        "03-08-2026",
        "03-08-2026",
        "02-08-2026",
        "01-08-2026",
        "31-07-2026"
    ]

})

st.dataframe(

    history,

    width="stretch",

    hide_index=True

)

st.divider()

# ==========================================================
# Search
# ==========================================================

section_title("🔍 Search")

search = st.text_input(
    "Search by Image or Damage Type"
)
# ==========================================================
# Filter History
# ==========================================================

if search:

    filtered_history = history[
        history["Image"].str.contains(search, case=False) |
        history["Damage"].str.contains(search, case=False)
    ]

    st.dataframe(
        filtered_history,
        width="stretch",
        hide_index=True
    )

else:

    filtered_history = history

st.divider()

# ==========================================================
# History Statistics
# ==========================================================

section_title("📊 History Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Images",
        len(history)
    )

with col2:
    st.metric(
        "Damages",
        len(history)
    )

with col3:
    st.metric(
        "Highest Confidence",
        "98%"
    )

with col4:
    st.metric(
        "Today's Scans",
        "2"
    )

st.divider()

# ==========================================================
# Recent Detection
# ==========================================================

section_title("🚧 Latest Detection")

latest = history.iloc[0]

st.success(f"""
📷 Image : {latest['Image']}

🚧 Damage : {latest['Damage']}

🎯 Confidence : {latest['Confidence']}

📅 Date : {latest['Date']}
""")

st.divider()

# ==========================================================
# Download History
# ==========================================================

section_title("📥 Download History")

csv = filtered_history.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📄 Download History (CSV)",

    data=csv,

    file_name="road_damage_history.csv",

    mime="text/csv",

    width="stretch"

)

st.divider()

# ==========================================================
# History Timeline
# ==========================================================

section_title("🕒 Recent Activity")

for index, row in history.iterrows():

    st.info(
        f"""
📷 **{row['Image']}**

🚧 Damage : **{row['Damage']}**

🎯 Confidence : **{row['Confidence']}**

📅 Date : **{row['Date']}**
"""
    )

st.divider()

# ==========================================================
# Footer
# ==========================================================

show_footer()

