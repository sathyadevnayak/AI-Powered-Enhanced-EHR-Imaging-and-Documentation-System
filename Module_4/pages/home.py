import streamlit as st

import streamlit as st

def render():
    # Hero Section
    st.markdown("---")
    
    # Project Overview
    st.header("📋 Project Overview")
    st.markdown("""
    This comprehensive healthcare AI platform integrates **Generative AI** capabilities to revolutionize 
    Electronic Health Records (EHR) management through advanced medical image analysis and intelligent 
    clinical documentation automation.
    
    Our system leverages deep learning models and natural language processing to:
    - Enhance medical imaging quality for improved diagnostic accuracy
    - Automate clinical documentation to reduce administrative burden
    - Streamline ICD-10 coding workflows
    - Enable faster, data-driven clinical decision-making
    """)
    
    # Key Features
    st.header("✨ Key Features")
    
    st.markdown("- 🖼️ Medical Image Enhancement")
    st.markdown("- 📝 Clinical Documentation Automation")
    st.markdown("- 🔍 Patient Lookup & Management")
    st.markdown("- 🏷️ ICD-10 Coding Automation")
    
    st.markdown("""
    ### Key Benefits:
    - **Improved Diagnostic Accuracy**: Enhanced medical images support better clinical decisions
    - **Reduced Administrative Burden**: Automated documentation saves 2-3 hours per clinician daily
    - **Streamlined Workflows**: Integrated ICD-10 coding reduces billing errors
    - **Enhanced Patient Care**: More time for patient interaction, less on paperwork
    - **Cost Efficiency**: Reduced operational costs through automation
    - **Scalability**: Cloud-ready architecture for hospital-wide deployment
    """)
    
    # Use Cases
    st.header("💡 Use Cases")
    
    use_cases = [
        {
            "title": "🏥 Hospital Emergency Departments",
            "description": "Quick patient lookup, instant medical history access, and automated triage documentation"
        },
        {
            "title": "🩺 Radiology Departments",
            "description": "Enhanced image quality for better diagnosis, automated report generation, and DICOM integration"
        },
        {
            "title": "👨‍⚕️ Primary Care Clinics",
            "description": "Streamlined patient documentation, prescription management, and ICD-10 coding for billing"
        },
        {
            "title": "🔬 Research Institutions",
            "description": "Medical image datasets, clinical data analytics, and AI model training infrastructure"
        }
    ]
    
    cols = st.columns(2)
    for idx, use_case in enumerate(use_cases):
        with cols[idx % 2]:
            st.markdown(f"""
            **{use_case['title']}**
            
            {use_case['description']}
            """)
    
    # Getting Started
    st.header("🚀 Getting Started")
    st.markdown("""
    Navigate through the sidebar to explore different features:
    
    1. **👤 Patient Lookup**: Search patient records by ID
    2. **🖼️ Image Enhancement**: Upload and enhance medical images
    3. **📝 Clinical Documentation**: Generate automated clinical notes
    4. **🏷️ ICD-10 Coding**: Get automated diagnosis code suggestions
    """)
    
    st.info("💡 **Tip:** Use the sidebar to navigate between different modules.")

    st.markdown('<h1 class="main-header">Thank you 🙏</h1>',unsafe_allow_html=True)
