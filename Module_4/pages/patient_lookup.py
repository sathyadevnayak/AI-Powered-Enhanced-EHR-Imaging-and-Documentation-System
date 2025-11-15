import streamlit as st
import pandas as pd

def render():
    st.markdown('<h2 class="sub-header">👤 Patient Clinical Summary</h2>', unsafe_allow_html=True)
    
    try:
        patients_df = pd.read_csv("../Data/csv datasets/patients_dataset.csv", dtype=str)
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            patient_id = st.text_input("Enter Patient ID:", placeholder="PT000001")
            search_button = st.button("🔍 Search", type="primary", use_container_width=True)
        
        if search_button and patient_id:
            patient_row = patients_df.loc[patients_df["patient_id"] == patient_id.upper()]
            
            if not patient_row.empty:
                patient_data = patient_row.iloc[0]
                
                with col2:
                    st.success(f"✅ Patient Found: {patient_id.upper()}")
                
                st.markdown("### 📋 Patient Information")
                
                info_col1, info_col2, info_col3 = st.columns(3)
                
                with info_col1:
                    st.markdown(f"""
                    **Name:** {patient_data.get('first_name', 'N/A')} {patient_data.get('last_name', 'N/A')}  
                    **Age:** {patient_data.get('age', 'N/A')} years  
                    **Gender:** {patient_data.get('gender', 'N/A')}
                    """)
                
                with info_col2:
                    st.markdown(f"""
                    **Blood Type:** {patient_data.get('blood_type', 'N/A')}  
                    **Insurance:** {patient_data.get('insurance_provider', 'N/A')}  
                    **Admission:** {patient_data.get('admission_date', 'N/A')}
                    """)
                
                with info_col3:
                    st.markdown(f"""
                    **Diagnosis:** {patient_data.get('primary_condition', 'N/A')}  
                    **ICD-10:** {patient_data.get('primary_icd10_code', 'N/A')}  
                    **Emergency Contact:** {patient_data.get('emergency_contact_name', 'N/A')}
                    """)
                
                st.markdown("---")
                st.markdown("### 📝 Latest Clinical Notes")
                
                try:
                    clinical_df = pd.read_csv("../Data/csv datasets/clinical_notes_dataset.csv", dtype=str)
                    patient_notes = clinical_df[clinical_df['patient_id'] == patient_id.upper()]
                    
                    if not patient_notes.empty:
                        latest_note = patient_notes.sort_values(['note_date', 'note_time'], ascending=False).iloc[0]

                        st.markdown("""
                        <style>
                        .info-box {
                            background-color: #000000; /* Black background */
                            color: #ffffff;            /* White text */
                            border: 1px solid #444444; /* Subtle gray border */
                            padding: 15px;
                            border-radius: 10px;
                            box-shadow: 2px 2px 8px rgba(255,255,255,0.1);
                            margin-top: 10px;
                        }

                        .info-box strong {
                            color: #00bcd4; /* Cyan color for labels like Date, Type, etc. */
                        }
                        </style>
                        """, unsafe_allow_html=True)

                        
                        st.markdown(f"""
                        <div class="info-box">
                        <strong>Date:</strong> {latest_note.get('note_date', 'N/A')} {latest_note.get('note_time', 'N/A')}<br>
                        <strong>Type:</strong> {latest_note.get('note_type', 'N/A')}<br>
                        <strong>Physician:</strong> {latest_note.get('physician', 'N/A')}<br>
                        <strong>Note:</strong> {latest_note.get('note_text', 'N/A')}
                        </div>
                        """, unsafe_allow_html=True)

                    else:
                        st.warning("No clinical notes found for this patient.")
                except Exception as e:
                    st.error(f"Error loading clinical notes: {e}")
                
                st.markdown("---")
                st.markdown("### 💊 Latest Prescription")
                
                try:
                    prescriptions_df = pd.read_csv("../Data/csv datasets/prescriptions_dataset.csv", dtype=str)
                    patient_meds = prescriptions_df[prescriptions_df["patient_id"] == patient_id.upper()]
                    
                    if not patient_meds.empty:
                        latest_med = patient_meds.sort_values(['prescription_date', 'prescription_time'], ascending=False).iloc[0]
                        
                        med_col1, med_col2, med_col3 = st.columns(3)
                        
                        with med_col1:
                            st.markdown(f"""
                            **Medication:** {latest_med.get('medication_name', 'N/A')}  
                            **Strength:** {latest_med.get('strength', 'N/A')}  
                            **Quantity:** {latest_med.get('quantity', 'N/A')}
                            """)
                        
                        with med_col2:
                            st.markdown(f"""
                            **Frequency:** {latest_med.get('frequency', 'N/A')}  
                            **Route:** {latest_med.get('route', 'N/A')}  
                            **Duration:** {latest_med.get('duration', 'N/A')}
                            """)
                        
                        with med_col3:
                            st.markdown(f"""
                            **Prescribed By:** {latest_med.get('prescribing_physician', 'N/A')}  
                            **Pharmacy:** {latest_med.get('pharmacy', 'N/A')}  
                            **Date:** {latest_med.get('prescription_date', 'N/A')}
                            """)
                    else:
                        st.warning("No prescriptions found for this patient.")
                except Exception as e:
                    st.error(f"Error loading prescriptions: {e}")
                
            else:
                st.error(f"❌ Patient ID '{patient_id}' not found in the database.")
    
    except Exception as e:
        st.error(f"Error loading patient database: {e}")
