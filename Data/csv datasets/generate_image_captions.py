import os
from PIL import Image
import pandas as pd
import torch
from transformers import BlipForConditionalGeneration, AutoProcessor

# Paths
IMG_FOLDER = "../Processed images/X-Ray/Bone fractured/enhanced/"
OUTPUT_CSV = "image_caption.csv"
MODEL_ID = "umarigan/blip-image-captioning-base-chestxray-finetuned"

# Load the medical BLIP model and processor
model = BlipForConditionalGeneration.from_pretrained(MODEL_ID).to("cuda" if torch.cuda.is_available() else "cpu")
processor = AutoProcessor.from_pretrained(MODEL_ID)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
data = []

for fname in os.listdir(IMG_FOLDER):
    if fname.endswith('.png') or fname.endswith('.jpg'):
        path = os.path.join(IMG_FOLDER, fname)
        image = Image.open(path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt").to(device)
        pixel_values = inputs.pixel_values
        generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
        caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        data.append({"image_filename": fname, "caption": caption})
        print(f"{fname}: {caption}")

# Save results to CSV
pd.DataFrame(data).to_csv(OUTPUT_CSV, index=False)
print(f"Saved all BLIP-Med captions to {OUTPUT_CSV}")
