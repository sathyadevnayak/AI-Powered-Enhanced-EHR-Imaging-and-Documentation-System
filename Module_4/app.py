import streamlit as st
import sys
import os

# Add paths
sys.path.append(os.path.join(os.path.dirname(__file__), 'clinical_note_automation'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Data/Processed images'))

from pages import home, image_enhancement, patient_lookup, icd10_coding, clinical_documentation
# Import page modules




# Page configuration
st.set_page_config(
    page_title="AI-Powered EHR System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-top: 2rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🏥 AI-Powered Enhanced EHR Imaging & Documentation System</h1>', unsafe_allow_html=True)

# Sidebar
pg = st.navigation([
st.Page(home.render, title="Home", icon="🏠", default=True),
st.Page(patient_lookup.render, title="Patient Lookup", icon="🧑‍⚕️", url_path="patient_lookup"),
st.Page(image_enhancement.render, title="Image Enhancement", icon="🖼️", url_path="image_enhancement"),
st.Page(clinical_documentation.render, title="Clinical Documentation", icon="📝", url_path="clinical_documentation"),
st.Page(icd10_coding.render, title="ICD-10 Coding", icon="💉", url_path="icd10_coding")
])
pg.run()


# Route to appropriate page
