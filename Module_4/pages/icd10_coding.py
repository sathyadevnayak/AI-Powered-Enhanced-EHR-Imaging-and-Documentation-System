import streamlit as st
import pandas as pd

def render():
    st.markdown('<h2 class="sub-header">🏷️ ICD-10 Code Mapping</h2>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Search ICD-10 Codes", "Auto-Map Diagnosis"])
    
    with tab1:
        st.markdown("### Search ICD-10 Database")
        
        try:
            icd_df = pd.read_csv("../Data/ICD-10 Coding Data/ICDCode/ICDCodeSet.csv", dtype=str)
            
            search_term = st.text_input("Search by diagnosis or code:", placeholder="e.g., diabetes, J209")
            
            if search_term:
                search_results = icd_df[
                    icd_df.apply(lambda row: search_term.lower() in str(row).lower(), axis=1)
                ]
                
                if not search_results.empty:
                    st.success(f"✅ Found {len(search_results)} matching codes")
                    st.dataframe(search_results, use_container_width=True, height=400)
                else:
                    st.warning("No matching codes found. Try different search terms.")
            else:
                st.info("👆 Enter a diagnosis or ICD code to search the database")
                st.markdown("### Sample ICD-10 Codes:")
                st.dataframe(icd_df.head(20), use_container_width=True)
        
        except Exception as e:
            st.error(f"Error loading ICD-10 database: {e}")
    
    with tab2:
        st.markdown("### Automatic Diagnosis Mapping")
        
        col1, col2 = st.columns(2)
        
        with col1:
            patient_id = st.text_input("Patient ID:", placeholder="PT000001")
            diagnosis_input = st.text_area("Enter Diagnosis Description:", placeholder="Patient presents with...", height=150)
            map_button = st.button("🔍 Map to ICD-10", type="primary", use_container_width=True)
        
        with col2:
            if map_button and diagnosis_input:
                with st.spinner("Mapping diagnosis to ICD-10 codes..."):
                    try:
                        icd_df = pd.read_csv("../Data/ICD-10 Coding Data/ICDCode/ICDCodeSet.csv", dtype=str)
                        
                        matches = icd_df[
                            icd_df.apply(lambda row: any(word.lower() in str(row).lower() for word in diagnosis_input.split()), axis=1)
                        ].head(5)
                        
                        if not matches.empty:
                            st.success("✅ Suggested ICD-10 Codes:")
                            
                            for idx, row in matches.iterrows():
                                code = row.get('ICD10_Code', row.get('ICDCode', 'N/A'))
                                desc = row.get('Diagnosis', row.get('Description', 'N/A'))
                                
                                with st.expander(f"📌 {code} - {desc}"):
                                    st.markdown(f"""
                                    **Code:** {code}  
                                    **Description:** {desc}  
                                    """)
                                    
                                    if st.button(f"Select {code}", key=f"select_{idx}"):
                                        st.success(f"Selected: {code}")
                        else:
                            st.warning("No matching ICD-10 codes found. Try rephrasing the diagnosis.")
                    
                    except Exception as e:
                        st.error(f"Error during mapping: {e}")
            else:
                st.info("👈 Enter diagnosis details and click 'Map to ICD-10'")
        
        
