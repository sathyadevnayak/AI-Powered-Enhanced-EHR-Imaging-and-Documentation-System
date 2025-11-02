import pandas as pd

PATIENTS_CSV = "../data/csv datasets/patients_dataset.csv"
CLINICAL_CSV = "../data/csv datasets/clinical_notes_dataset.csv"
PRESCRIPTIONS_CSV = "../data/csv datasets/prescriptions_dataset.csv"

def get_patient_row(patients, patientid):
    row = patients.loc[patients["patient_id"] == patientid]
    return row.iloc[0] if not row.empty else None

def get_demo_and_diagnosis(patient_row):
    age = patient_row.get("age", "N/A")
    gender = patient_row.get("gender", "N/A")
    diagnosis = patient_row.get("primary_condition", "N/A")
    icd10 = patient_row.get("primary_icd10_code", "N/A")
    name_str = f"{patient_row.get('first_name','')} {patient_row.get('last_name','')}".strip()
    admission_date = patient_row.get("admission_date", "N/A")
    admission_time = patient_row.get("admission_time", "N/A")
    insurance = patient_row.get("insurance_provider","N/A")
    bloodtype = patient_row.get("blood_type","N/A")
    emergency_contact = patient_row.get("emergency_contact_name","N/A")
    return age, gender, diagnosis, icd10, name_str, admission_date, admission_time, insurance, bloodtype, emergency_contact

def get_recent_clinical(clinical, pid):
    notes = clinical[clinical['patient_id'] == pid].copy()
    if notes.empty:
        return "N/A", "N/A", "N/A", "N/A", "N/A"
    notes['datetime'] = notes['note_date'].astype(str) + " " + notes['note_time'].astype(str)
    recent = notes.sort_values('datetime', ascending=False).iloc[0]
    note_type = recent.get("note_type", "N/A")
    note_text = recent.get("note_text", "N/A")
    physician = recent.get("physician","N/A")
    note_date = recent.get("note_date","N/A")
    note_time = recent.get("note_time","N/A")
    return note_type, note_text, physician, note_date, note_time

def get_latest_prescription(prescriptions, pid):
    meds = prescriptions[prescriptions["patient_id"] == pid].copy()
    if meds.empty:
        return "N/A"
    meds['datetime'] = meds["prescription_date"].astype(str) + " " + meds["prescription_time"].astype(str)
    latest = meds.sort_values('datetime', ascending=False).iloc[0]
    med_info = (
        f"{latest.get('medication_name','N/A')} {latest.get('strength','')}, "
        f"Qty: {latest.get('quantity','N/A')}, "
        f"Frequency: {latest.get('frequency','N/A')}, "
        f"Route: {latest.get('route','N/A')}, "
        f"Prescribed by: {latest.get('prescribing_physician','N/A')}, "
        f"Pharmacy: {latest.get('pharmacy','N/A')}"
    )
    return med_info

def main():
    patients = pd.read_csv(PATIENTS_CSV, dtype=str)
    clinical = pd.read_csv(CLINICAL_CSV, dtype=str)
    prescriptions = pd.read_csv(PRESCRIPTIONS_CSV, dtype=str)

    pid = input("Enter patient id: ").strip().upper()
    patient_row = get_patient_row(patients, pid)

    if patient_row is None:
        print(f"No details found for patient ID: {pid}")
        return

    age, gender, diagnosis, icd10, name_str, admission_date, admission_time, insurance, bloodtype, emergency_contact = get_demo_and_diagnosis(patient_row)
    note_type, note_text, physician, note_date, note_time = get_recent_clinical(clinical, pid)
    treatment = get_latest_prescription(prescriptions, pid)

    print(f"\n--- Patient Clinical Summary ---")
    print(f"Patient: {pid} ({name_str})")
    print(f"Age/Gender: {age} years old, {gender}")
    print(f"Diagnosis: {diagnosis} (ICD-10: {icd10})")
    print(f"Admission Date/Time: {admission_date} {admission_time}")
    print(f"Insurance: {insurance} | Blood Type: {bloodtype}")
    print(f"Emergency Contact: {emergency_contact}")

    print(f"\nLatest Clinical Note:")
    print(f"- Date/Time: {note_date} {note_time}")
    print(f"- Type: {note_type}")
    print(f"- Physician: {physician}")
    print(f"- Note: {note_text}")

    print(f"\nLatest Prescription/Treatment:")
    print(f"- {treatment}")

    print("\nRecommended regular follow-up and monitoring.\n")

if __name__ == "__main__":
    main()
