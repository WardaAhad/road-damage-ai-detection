"""
=========================================================
AI Road Damage Detection System
Professional Footer
Developer : Warda Ahad
=========================================================
"""

import streamlit as st

from config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    DEVELOPER,
    MODEL_NAME
)


# ==========================================================
# Footer
# ==========================================================

def show_footer():

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <hr>

        <div style="
            text-align:center;
            padding:20px;
            color:#CBD5E1;
            font-size:15px;
        ">

            <h4 style="color:white;">
                🚧 {PROJECT_NAME}
            </h4>

            <p>
                Deep Learning Based Road Damage Detection
            </p>

            <p>
                🤖 Model : {MODEL_NAME}
            </p>

            <p>
                👩‍💻 Developed by
                <b>{DEVELOPER}</b>
            </p>

            <p>
                Version {PROJECT_VERSION}
            </p>

            <p>
                © 2026 All Rights Reserved
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# Technology Stack
# ==========================================================

def tech_stack():

    st.markdown("### 🛠 Technology Stack")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.success("YOLOv11")

    with col2:
        st.success("FastAPI")

    with col3:
        st.success("Streamlit")

    with col4:
        st.success("Python")


# ==========================================================
# Contact Information
# ==========================================================

def contact_info():

    st.markdown("### 📬 Contact")

    st.markdown("""
📧 Email : your_email@gmail.com

💻 GitHub : https://github.com/WardaAhad

🔗 LinkedIn :
https://linkedin.com/in/your-linkedin
""")


# ==========================================================
# Copyright
# ==========================================================

def copyright_text():

    st.caption(
        "© 2026 Warda Ahad | AI Road Damage Detection System"
    )
