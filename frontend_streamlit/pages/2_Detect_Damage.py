"""
=========================================================
AI Road Damage Detection System
Detect Road Damage
Developer : Warda Ahad
=========================================================
"""

import streamlit as st
import os


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
from components.uploader import (
    image_uploader,
    preview_image,
    predict_button,
    predict_image
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
# Hero
# ==========================================================

hero_title(
    "🚧 Detect Road Damage",
    "Upload a road image and detect cracks, potholes and road damage using YOLOv11."
)


st.divider()



# ==========================================================
# Upload Image
# ==========================================================

section_title("📤 Upload Road Image")


uploaded_file = image_uploader()


result = None


if uploaded_file:

    section_title("🖼️ Original Image")

    preview_image(uploaded_file)



st.divider()



# ==========================================================
# Prediction
# ==========================================================

section_title("🤖 AI Detection")



if uploaded_file:


    if predict_button():


        result = predict_image(uploaded_file)



        if result:


            st.success(
                "✅ Detection Completed Successfully"
            )

            st.json(result)




# ==========================================================
# Detection Result
# ==========================================================

if result:


    prediction = result["result"]


    st.divider()


    section_title("📊 Detection Summary")



    col1, col2 = st.columns(2)



    with col1:


        st.metric(
            "Total Damages",
            prediction["total_damages"]
        )


        st.metric(
            "Image Name",
            result["filename"]
        )



    with col2:


        if prediction["detections"]:


            highest_conf = max(
                d["confidence"]
                for d in prediction["detections"]
            )


            st.metric(
                "Highest Confidence",
                f"{highest_conf*100:.2f}%"
            )


            st.metric(
                "Detected Classes",
                len(prediction["detections"])
            )



    st.divider()




# ==========================================================
# Detection Table
# ==========================================================


    section_title("🚧 Detection Details")


    detection_data = []



    for item in prediction["detections"]:


        detection_data.append({

            "Class": item["class"],

            "Confidence":
            f"{item['confidence']*100:.2f}%",

            "Bounding Box":
            str(item["bbox"])

        })



    if detection_data:


        st.dataframe(

            detection_data,

            width="stretch",

            hide_index=True

        )


    else:


        st.info(
            "No road damage detected."
        )



    st.divider()



# ==========================================================
# Output Image (FIXED)
# ==========================================================


    section_title("🖼️ Detected Image")



    output_path = prediction["output_image"]



    # Replace Windows slash
    output_path = output_path.replace("\\", "/")



    # Get project root
    current_file = os.path.abspath(__file__)


    frontend_folder = os.path.dirname(
        os.path.dirname(current_file)
    )


    project_folder = os.path.dirname(
        frontend_folder
    )



    image_path = os.path.join(

        project_folder,

        "backend",

        output_path

    )



    if os.path.exists(image_path):


        st.image(

            image_path,

            caption="Prediction Result",

            width="stretch"

        )


    else:


        st.error(

            f"Detected image not found: {image_path}"

        )



    st.divider()




# ==========================================================
# Raw JSON
# ==========================================================


    with st.expander("📄 API Response"):


        st.json(result)



else:


    st.info(
        "👆 Upload an image to start detection."
    )



st.divider()



# ==========================================================
# Footer
# ==========================================================

show_footer()
