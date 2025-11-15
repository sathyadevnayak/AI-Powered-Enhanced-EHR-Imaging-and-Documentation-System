# AI-Powered Enhanced EHR Imaging & Documentation System

## Project Overview

This project enhances Electronic Health Records (EHR) by integrating Generative AI for medical image analysis and clinical documentation automation. The system improves medical imaging clarity, automates clinical note generation, and streamlines ICD-10 coding to reduce clinician workload and support faster decision-making.

---

## Expected Outcomes

- **Improved medical image interpretation** through AI-driven enhancement
- **75% reduction** in manual documentation time
- **Streamlined ICD-10 coding** with 90% accuracy
- **Enhanced patient care** through reduced administrative burden

---

## Repository Structure



```
├── Data/
│ ├── csv datasets/ # Patient, clinical notes, lab results, prescriptions
│ ├── ICD-10 Coding Data/ # ICD-10-CM 2023 codes
│ ├── Raw images/ # CT, MRI, X-Ray samples
│ └── Processed images/ # Enhanced images, trained models
├── clinical_note_automation/ # Clinical note generation scripts
├── Module_4/ # Streamlit web application
│ ├── app.py
│ ├── pages/
│ └── requirements.txt
├── Agile documentation/
└── README.md
```

---

## Module 1: Data Collection and Preprocessing 

### Objective
Prepare imaging and clinical data for AI model training and application.

### Tasks Completed
• **Medical imaging datasets collected**: X-ray, MRI, CT scan samples organized by modality  
• **Structured and unstructured EHR content gathered**: Patient notes, lab results, prescriptions, and clinical documentation  
• **ICD-10 coding data integrated**: Complete ICD-10-CM codes for 2023 and custom ICDCodeSet  
• **Data cleaning and standardization**: Automated preprocessing for GenAI model compatibility  

### Key Files & Datasets
- **`Data/csv datasets/`**: 
  - `clinical_notes_dataset.csv` - Structured clinical notes for training
  - `patients_dataset.csv` - Patient demographics and information
  - `lab_results_dataset.csv` - Laboratory test results and values  
  - `prescriptions_dataset.csv` - Medication and prescription data
  - `Image_captions.csv` - AI-generated captions for medical images
- **`Data/ICD-10 Coding Data/ICDCode/`**:
  - `icd10cm_codes_2023.txt` - Official ICD-10-CM classification codes
  - `ICDCodeSet.csv` - Custom ICD code mappings for automation
- **`Data/Data_cleaning.py`** - Automated data cleaning and preprocessing script

### How to Run Data Preprocessing
```bash
python Data/Data_cleaning.py
```

### Outcomes
✅ Clean, labeled, and standardized datasets ready for AI model training  
✅ Comprehensive EHR data structure established  
✅ ICD-10 coding reference system integrated  

---

## Module 2: Medical Imaging Enhancement

### Objective  
Use GenAI to enhance image quality and support diagnosis through advanced image processing and AI-driven reconstruction.

### Tasks Completed
• **GenAI applied for denoising and realistic reconstruction** of medical images  
• **Advanced image processing pipeline** with MONAI framework integration  
• **AI model training** for X-ray enhancement using U-Net architecture  
• **Improved visualization support** for clinicians with enhanced resolution and clarity  

### Key Files & Models
- **`Data/Processed images/`**:
  - `train_xray_enhancer_monai.py` - MONAI-based U-Net training script for X-ray enhancement
  - `enhance_xray_batch_monai.py` - Batch processing script for X-ray enhancement  
  - `image_processing.py` - Core image preprocessing and enhancement pipeline
  - `xray_denoiser_unet.pth` - Trained U-Net model for X-ray denoising
  - `Training and validation loss over Epochs.png` - Model training metrics visualization
  - `Output.png` - Sample enhanced image output
- **`Data/image_processing_visuals.py`** - Before/after comparison visualization tool
- **`Data/csv datasets/generate_image_captions.py`** - AI-powered image caption generation

### Advanced Features Implemented
• **MONAI Framework Integration**: Medical imaging-specific deep learning framework  
• **U-Net Architecture**: Advanced neural network for medical image denoising  
• **Batch Processing**: Efficient processing of multiple medical images  
• **Training Metrics**: Comprehensive loss tracking and model performance evaluation  
• **Multi-modal Support**: CT Scan, MRI, and X-Ray processing capabilities  

### How to Run Image Enhancement
```bash
# Train the X-ray enhancement model
python Data/Processed\ images/train_xray_enhancer_monai.py

# Enhance X-ray images in batch
python Data/Processed\ images/enhance_xray_batch_monai.py

# Process individual medical images
python Data/Processed\ images/image_processing.py

# Visualize enhancement results
python Data/image_processing_visuals.py

# Generate image captions
python Data/csv\ datasets/generate_image_captions.py
```

### Outcomes
✅ **Trained AI model** for medical image enhancement (xray_denoiser_unet.pth)  
✅ **Improved image quality** through denoising and reconstruction algorithms  
✅ **Enhanced diagnostic support** with clearer, higher-resolution medical images  
✅ **Automated image captioning** for better documentation and accessibility  

---

## Module 3: Clinical Note Generation & ICD-10 Coding Automation 

### Objective
Automate routine documentation and coding tasks using GenAI to reduce administrative burden and improve clinical workflow efficiency.

### Tasks Completed
• **Automated clinical note generation** from structured data and doctor observations  
• **ICD-10 coding automation** by mapping EHR input to standard classifications  
• **Integration of GenAI tools** for seamless documentation workflow  
• **Clinical summary automation** for efficient patient record management  

### Key Files & Scripts
- **`clinical_note_automation/`**:
  - `Clinical_Note_Automation.py` - Main automation engine for clinical note generation
  - `clinical_summary.py` - Automated clinical summary generation from patient data

### Advanced Automation Features
• **AI-Powered Clinical Notes**: Automatic generation of comprehensive clinical notes from structured patient data  
• **ICD-10 Code Mapping**: Intelligent mapping of clinical conditions to appropriate ICD-10 codes  
• **Natural Language Processing**: Advanced text processing for medical terminology and documentation standards  
• **Workflow Integration**: Seamless integration with existing EHR data structures  
• **Quality Assurance**: Automated validation and formatting of generated documentation  

### How to Run Clinical Note Automation
```bash
# Generate automated clinical notes
python clinical_note_automation/Clinical_Note_Automation.py

# Create clinical summaries
python clinical_note_automation/clinical_summary.py
```


### Integration with Data Pipeline
The clinical note automation system integrates seamlessly with Module 1's preprocessed data:
- Uses `clinical_notes_dataset.csv` for training and reference
- Leverages `patients_dataset.csv` for patient-specific information
- Incorporates `lab_results_dataset.csv` for objective clinical data
- Applies `ICD-10 Coding Data/` for accurate medical coding

### Outcomes
✅ **Significant reduction** in manual documentation time  
✅ **Automated ICD-10 coding** with high accuracy and compliance  
✅ **Standardized clinical notes** following medical documentation best practices  
✅ **Improved clinical workflow** efficiency through AI-driven automation

---

## Module 4: Integration and Deployment

### Objective
Deploy and integrate the enhanced EHR features into a unified, production-ready clinical application with intuitive user interface and real-time processing capabilities.

### Tasks Completed
- **Streamlit multi-page application** with modular architecture
- **Unified dashboard** integrating all AI-powered modules
- **Real-time image enhancement** processing with Stable Diffusion
- **Interactive patient lookup** system with comprehensive clinical history
- **Clinical documentation generator** interface with AI assistance
- **ICD-10 coding assistant** with intelligent search capabilities
- **Responsive web interface** optimized for clinical workflows
- **Comprehensive deployment documentation**

### Application Structure
- **`Module_4/app.py`** - Main Streamlit application entry point
- **`Module_4/pages/`** - Multi-page application modules:
  - `home.py` - Project overview and system introduction
  - `patient_lookup.py` - Patient search and clinical history viewer
  - `image_enhancement.py` - Medical image upload and AI enhancement
  - `clinical_documentation.py` - Automated clinical note generation
  - `icd10_coding.py` - ICD-10 code lookup and mapping
- **`Module_4/requirements.txt`** - Python dependencies for deployment

### Key Features Implemented
- **Multi-Page Navigation**: Intuitive sidebar navigation between modules
- **Real-Time Processing**: Live image enhancement and note generation
- **Interactive UI**: User-friendly interface with Streamlit components
- **Data Integration**: Seamless access to all preprocessed datasets
- **Model Integration**: Deployed AI models for image enhancement and NLP
- **Responsive Design**: Optimized for various screen sizes
- **Error Handling**: Robust exception handling and user feedback

### How to Run the Application
Navigate to Module 4
```bash
cd Module_4
```
Install dependencies
```bash
pip install -r requirements.txt
```
Run the Streamlit application
```bash
streamlit run app.py
```
Access the application at http://localhost:8501
---

### Application Pages Overview

#### 1. Home Page
- Project overview and system architecture
- Module status and achievements
- Quick start guide and navigation
- Technology stack information

#### 2. Patient Lookup
- Search patients by ID
- View comprehensive clinical history
- Display demographics, diagnoses, prescriptions, and lab results
- Show recent clinical notes and observations

#### 3. Image Enhancement
- Upload medical images (X-ray, MRI, CT)
- AI-powered image enhancement using Stable Diffusion
- Side-by-side comparison of original and enhanced images
- Download enhanced images for clinical use

#### 4. Clinical Documentation
- Generate automated clinical notes from patient data
- Template-based and AI-generated note options
- Edit and customize generated notes
- Export documentation in standard formats

#### 5. ICD-10 Coding
- Search diagnoses and get ICD-10 code suggestions
- Automated mapping from clinical terms to codes
- Fuzzy matching for similar conditions
- Browse complete ICD-10-CM 2023 codeset

### Technology Stack
- **Frontend**: Streamlit (Python-based web framework)
- **Backend**: Python 3.9+
- **AI/ML**: PyTorch, Diffusers (Stable Diffusion), Transformers
- **Data Processing**: Pandas, NumPy
- **Image Processing**: PIL/Pillow
- **Deployment**: Streamlit Cloud, Docker (optional)

### Outcomes
✅ **Production-ready application** with all modules integrated  
✅ **User-friendly interface** for healthcare professionals  
✅ **Real-time AI processing** for images and documentation  
✅ **Scalable architecture** ready for hospital-wide adoption  
✅ **Comprehensive documentation** for users and developers

---

## Technical Specifications

### Dependencies & Frameworks
- **MONAI**: Medical imaging framework for deep learning
- **PyTorch**: Deep learning framework for model training
- **Streamlit**: Web application framework for interactive UI
- **Diffusers**: Stable Diffusion models for image enhancement
- **Transformers**: NLP models for text generation
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing library
- **Pillow (PIL)**: Image processing library

### Model Architecture
- **U-Net**: Convolutional neural network for medical image segmentation and enhancement
- **Stable Diffusion**: Diffusion-based model for image upscaling and enhancement
- **Transformer Models**: For natural language processing in clinical note generation
- **Custom Neural Networks**: Specialized architectures for medical data processing

---

## Current Project Status

| Module | Status | Key Deliverables |
|--------|--------|-----------------|
| **Module 1: Data Collection/Prep** | ✅ **COMPLETED** | Cleaned datasets, organized medical images, ICD-10 integration |
| **Module 2: Imaging Enhancement** | ✅ **COMPLETED** | Trained AI models, enhanced medical images, MONAI integration |
| **Module 3: Clinical Note/ICD-10 Automation** | ✅ **COMPLETED** | Automated documentation, ICD-10 coding system |
| **Module 4: Integration/Deployment** | ✅ **COMPLETED** | Streamlit app, unified platform, production-ready system |

---

## Results & Impact

### Quantified Outcomes
- Reduction in manual documentation time through automated clinical note generation
- Accuracy in ICD-10 coding automation compared to manual coding
- Improvement in medical image clarity and diagnostic quality
- Enhanced workflow efficiency enabling clinicians to focus more on patient care

### Clinical Benefits
- Faster, more accurate clinical decision-making
- Reduced administrative burden on healthcare professionals
- Improved medical image interpretation capabilities
- Standardized and comprehensive clinical documentation
- Streamlined coding and billing processes

---

## Technical Requirements

**Prerequisites**:
- Python 3.9+
- (Optional) CUDA-capable GPU

**Dependencies** (see `Module_4/requirements.txt`)
---

**⭐ Star this repository if you find it helpful!**
