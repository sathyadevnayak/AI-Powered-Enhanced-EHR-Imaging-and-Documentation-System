# AI-Powered-Enhanced EHR Imaging & Documentation System

## Project Overview

This project enhances Electronic Health Records (EHR) using Generative AI for advanced medical image analysis and automated clinical note documentation. The goal is to improve image clarity, automate documentation and ICD-10 coding, reduce non-clinical workload, and support better, faster clinical decision-making.

---

## Repository Structure



```markdown
Data/
  ├── csv datasets/
  │     ├── clinical_notes_dataset.csv
  │     ├── lab_results_dataset.csv
  │     ├── patients_dataset.csv
  │     └── prescriptions_dataset.csv
  ├── ICD-10 Coding Data/
  │     └── ICDCode/
  ├── Raw images/
  │     ├── CT Scan/
  │     ├── MRI/
  │     ├── X-Ray/
  │     └── rename.py
  ├── Processed images/
  │     ├── CT Scan/
  │     ├── MRI/
  │     ├── X-Ray/
  │     └── image_processing.py
  ├── Data_cleaning.py
  ├── image_processing_visuals.py
README.md

```

---

## Module 1: Data Collection and Preprocessing

**Objective:**  
Prepare clinical and imaging data for AI analysis.

**Progress:**  
- EHR data in four main CSVs (clinical notes, lab results, patients, prescriptions) under `csv datasets`
- ICD-10 reference data provided under `ICD-10 Coding Data/ICDCode`
- Sample images for CT, MRI, and X-ray modalities added and managed via `rename.py`
- `Data_cleaning.py` script for basic EHR CSV cleaning and preprocessing

**How to Run Data Cleaning**
```markdown
python Data/Data_cleaning.py
```

---

## Module 2: Medical Imaging Enhancement

**Objective:**  
Apply AI-based preprocessing and enhancement to medical images.

**Progress:**  
- Raw sample CT, MRI, and X-ray images organized in `Raw images` directory
- Image enhancement and preprocessing implemented in `image_processing.py`:
    - Steps: resizing, grayscale conversion, normalization, denoising
    - Output organized in respective modality subfolders of `Processed images`
- Visualization supported by `image_processing_visuals.py` for before-after comparisons

**How to Process Medical Images**
```markdown
python Data/Processed images/image_processing.py
```

**How to Visualize Results**
```markdown
python Data/image_processing_visuals.py
```


---

## Status Summary

| Module                     | Status  | Key Output                                    |
|----------------------------|---------|-----------------------------------------------|
| 1. Data Collection/Prep    | ✔       | Cleaned CSVs, organized sample images         |
| 2. Imaging Enhancement     | ✔       | Processed/enhanced sample medical images      |
| 3. Documentation/Coding    | —       | To be started (next module)                   |
| 4. Integration/Deployment  | —       | To be started after module 3                  |

---

## Next Steps

- Train image enhancement models using Azure OpenAI tools
- Generate clinical notes from structured data and doctor observations
- Automate ICD-10 coding by mapping EHR input to standard classifications
- Decrease documentation workload through seamless integration of GenAI tools



