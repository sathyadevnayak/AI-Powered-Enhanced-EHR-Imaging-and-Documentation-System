import streamlit as st
import pandas as pd
from datetime import datetime
import time

def render():
    st.markdown('<h2 class="sub-header">📝 Automated Clinical Documentation</h2>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Generate New Note", "View Existing Notes"])
    
    with tab1:
        st.markdown("### Create Clinical Note")
        
        col1, col2 = st.columns(2)
        
        with col1:
            patient_id = st.text_input("Patient ID:", placeholder="PT000001")
            diagnosis = st.text_input("Diagnosis:", placeholder="Enter diagnosis")
            observations = st.text_area("Clinical Observations:", placeholder="Enter observations...", height=150)
        
        with col2:
            physician = st.text_input("Physician Name:", placeholder="Dr. Smith")
            note_type = st.selectbox("Note Type:", ["Progress Note", "Admission Note", "Discharge Summary", "Consultation", "Follow-up Note"])
            treatment = st.text_area("Treatment Plan:", placeholder="Enter treatment details...", height=150)
        
        if st.button("🤖 Generate Clinical Note", type="primary", use_container_width=True):
            if patient_id and diagnosis:
                with st.spinner("Generating clinical note....."):
                    time.sleep(2)
                    
                    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    note_lines = [
                        "CLINICAL NOTE",
                        "="*60,
                        f"Patient ID: {patient_id}",
                        f"Date & Time: {current_datetime}",
                        f"Physician: {physician}",
                        f"Note Type: {note_type}",
                        "",
                        "CHIEF COMPLAINT & DIAGNOSIS:",
                        diagnosis,
                        "",
                        "CLINICAL OBSERVATIONS:",
                        observations,
                        "",
                        "TREATMENT PLAN:",
                        treatment,
                        "",
                        "ASSESSMENT:",
                        f"The patient presents with {diagnosis}. Clinical observations indicate: {observations}.",
                        f"Based on comprehensive evaluation, recommended treatment includes: {treatment}.",
                        "",
                        "PLAN:",
                        "1. Continue current medication regimen as prescribed",
                        "2. Schedule follow-up appointment in 2 weeks",
                        "3. Monitor for any adverse reactions or complications",
                        "4. Patient education provided regarding condition management",
                        "",
                        "RECOMMENDATIONS:",
                        "- Regular monitoring of vital signs",
                        "- Adherence to prescribed treatment plan",
                        "- Immediate medical attention if symptoms worsen",
                        "",
                        f"\nPHYSICIAN SIGNATURE: {physician}",
                        f"Date: {current_datetime}"
                    ]
                    
                    generated_note = "\n".join(note_lines)
                    
                    st.success("✅ Clinical note generated successfully!")
                    st.markdown("### Generated Note:")
                    st.text_area("", value=generated_note, height=400, key="generated_note_display")
                    
                    st.download_button(
                        label="💾 Download Note",
                        data=generated_note,
                        file_name=f"clinical_note_{patient_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
            else:
                st.error("Please fill in Patient ID and Diagnosis fields.")
    
    with tab2:
        st.markdown("### Existing Clinical Notes")
        
        try:
            clinical_df = pd.read_csv("../Data/csv datasets/clinical_notes_dataset.csv", dtype=str)
            
            search_patient = st.text_input("Filter by Patient ID :", placeholder="PT000001")
            
            if search_patient:
                filtered_df = clinical_df[clinical_df['patient_id'] == search_patient.upper()]
            else:
                filtered_df = clinical_df.head(50)
            
            if not filtered_df.empty:
                st.dataframe(
                    filtered_df[['patient_id', 'note_date', 'note_time', 'note_type', 'physician', 'note_text']],
                    use_container_width=True,
                    height=400
                )
                
                st.info(f"📊 Showing {len(filtered_df)} clinical notes")
            else:
                st.warning("No clinical notes found.")
        
        except Exception as e:
            st.error(f"Error loading clinical notes: {e}")
