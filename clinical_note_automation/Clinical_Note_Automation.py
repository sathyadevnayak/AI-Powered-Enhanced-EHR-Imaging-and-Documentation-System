import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# Paths – adapt if needed
CLINICAL_CSV = "../data/csv datasets/clinical_notes_dataset.csv"
OUTPUT_CSV = "../data/csv datasets/generated_clinical_notes_advanced.csv"

# 1. Load the CSV
try:
    df = pd.read_csv(CLINICAL_CSV)
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)

# 2. Prepare the Hugging Face pipeline
model_name = "google/medgemma-4b-it"  # Use local or HF Hub
device = 0 if torch.cuda.is_available() else -1  # Auto-use GPU if present

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    gen_pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)
except Exception as e:
    print(f"Error loading model/pipeline: {e}")
    exit(2)

# 3. Define the prompt template
def build_prompt(row):
    return (f"Patient details:\n"
            f"- ID: {row.get('PatientID', 'N/A')}\n"
            f"- Age: {row.get('Age', 'N/A')}\n"
            f"- Gender: {row.get('Gender', 'N/A')}\n"
            f"- Diagnosis: {row.get('Diagnosis', 'N/A')}\n"
            f"- Observations: {row.get('Observations', 'N/A')}\n"
            f"- Lab Results: {row.get('LabResults', 'N/A')}\n"
            f"- Prescriptions: {row.get('Prescriptions', 'N/A')}\n"
            f"Write a concise, clear clinical note for this patient:"
           )

# 4. Generate notes (batch or row-by-row for memory)
generated_notes = []
for idx, row in df.iterrows():
    try:
        prompt = build_prompt(row)
        # Adjust max_new_tokens/temperature as needed for your model
        output = gen_pipe(prompt, max_new_tokens=120, do_sample=True, temperature=0.7)[0]['generated_text']
        # Extract only the answer after the prompt if the model repeats the input
        answer = output.split("Write a concise, clear clinical note for this patient:")[-1].strip()
        generated_notes.append(answer)
    except Exception as e:
        print(f"Error generating note for row {idx}: {e}")
        generated_notes.append("ERROR: Generation failed")

df['Generated_Advanced_Note'] = generated_notes

# 5. Save to output CSV
try:
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved results to {OUTPUT_CSV}")
except Exception as e:
    print(f"Error saving to CSV: {e}")

# (Optional) Print first 3 notes for sanity check
print(df[['PatientID','Generated_Advanced_Note']].head(3))
