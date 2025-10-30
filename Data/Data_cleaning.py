import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# patients_dataset.csv
patients = pd.read_csv("csv datasets/patients_dataset.csv")

print(patients.head())

print(patients.info())

print(patients.describe())

print(patients.isnull().sum())

print(patients.duplicated().sum())

print(patients)

patients['gender'] = patients['gender'].map({'Male':0, 'Female':1})

plt.figure(figsize=(10, 5))
sns.histplot(patients['age'], bins=30, kde=True)
plt.title('Patient Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='gender', data=patients)
plt.title('Gender Distribution')
plt.show()

plt.figure(figsize=(12, 6))
top_conditions = patients['primary_condition'].value_counts().nlargest(10)
sns.barplot(x=top_conditions.index, y=top_conditions.values)
plt.title('Top 10 Primary Conditions')
plt.xticks(rotation=45)
plt.xlabel('Condition')
plt.ylabel('Number of Patients')
plt.show()

numeric_patients = patients.select_dtypes(include=[np.number])
plt.figure(figsize=(10,8))
sns.heatmap(numeric_patients.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (with Encoded Categories)")
plt.show()

# clinical_notes_dataset.csv
notes = pd.read_csv("csv datasets/clinical_notes_dataset.csv")

print(notes.head())

print(notes.info())

print(notes.describe())

print(notes.isnull().sum())

print(notes.duplicated().sum())

plt.figure(figsize=(8, 5))
sns.countplot(x='note_type', data=notes)
plt.title('Clinical Notes by Type')
plt.xlabel('Note Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

notes_per_patient = notes.groupby('patient_id').size()

plt.figure(figsize=(10, 5))
sns.histplot(notes_per_patient, bins=20, kde=False)
plt.title('Distribution of Number of Clinical Notes per Patient')
plt.xlabel('Number of Notes')
plt.ylabel('Number of Patients')
plt.show()

# lab_results_dataset.csv
lab = pd.read_csv("csv datasets/lab_results_dataset.csv")

print(lab.head())

print(lab.info())

print(lab.describe())

print(lab.isnull().sum())

print(lab.duplicated().sum())

lab['flag'] = lab['flag'].map({'H':1, 'N':0, 'L':-1})

plt.figure(figsize=(10,6))
wbc = lab[lab['test_name']=='WBC']
sns.histplot(data=wbc, x='result_value', hue='flag', multiple='stack', bins=30)
plt.title('White Blood Cell Count Distribution by Flag')
plt.xlabel('WBC (cells/mcL)')
plt.show()

cbc = lab[lab['panel_name']=='Complete Blood Count (CBC)']
avg_cbc = cbc.groupby('test_name')['result_value'].mean().sort_values()
plt.figure(figsize=(10,6))
sns.barplot(x=avg_cbc.values, y=avg_cbc.index)
plt.title('Average CBC Test Values')
plt.xlabel('Average Value')
plt.show()

# prescriptions_dataset.csv
prescription = pd.read_csv("csv datasets/prescriptions_dataset.csv")

print(prescription.head())

print(prescription.info())

print(prescription.describe())

print(prescription.isnull().sum())

print(prescription.duplicated().sum())

prescription['generic_available'] = prescription['generic_available'].map({'No':0, 'Yes':1})
prescription['controlled_substance'] = prescription['controlled_substance'].map({'No':0, 'Yes':1})

top_meds = prescription['medication_name'].value_counts().nlargest(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_meds.index, y=top_meds.values)
plt.title('Top 10 Prescribed Medications')
plt.xticks(rotation=45)
plt.ylabel('Prescription Count')
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(y='frequency', data=prescription, order=prescription['frequency'].value_counts().index)
plt.title('Medication Frequency Distribution')
plt.xlabel('Count')
plt.show()
