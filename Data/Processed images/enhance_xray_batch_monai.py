import glob
import torch
from monai.networks.nets import UNet
from monai.transforms import Compose, LoadImage, EnsureChannelFirst, ScaleIntensity, ToTensor
from PIL import Image
import numpy as np
import os

# --- Step 1: Load Model ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet(
    spatial_dims=2,
    in_channels=1,
    out_channels=1,
    channels=(16, 32, 64, 128, 256),
    strides=(2, 2, 2, 2),
    num_res_units=2,
).to(device)
model.load_state_dict(torch.load("xray_denoiser_unet.pth", map_location=device))
model.eval()

# --- Step 2: Image Paths ---
DATA_DIR = "MRI/"
img_list = glob.glob(os.path.join(DATA_DIR, "*.jpg"))

# --- Step 3: Inference Preparation ---
val_transforms = Compose([
    LoadImage(image_only=True),
    EnsureChannelFirst(),
    ScaleIntensity(),
    ToTensor()
])

OUT_DIR = os.path.join(DATA_DIR, "enhanced")
os.makedirs(OUT_DIR, exist_ok=True)

# --- Step 4: Batch Enhancement ---
for img_path in img_list:
    img = val_transforms(img_path)
    with torch.no_grad():
        pred = model(img.unsqueeze(0).to(device))
    result = pred.squeeze().cpu().numpy()
    # If result.shape is (H,W) or (1,H,W)
    if result.ndim == 3:
        result = result[0]
    fname = os.path.basename(img_path)
    save_path = os.path.join(OUT_DIR, fname.replace(".png", "_enhanced.png").replace(".jpg", "_enhanced.png"))
    # Save as 8-bit PNG
    # Scale to 0-255; clip to range to avoid wrapping
    result_img = np.clip(result * 255, 0, 255).astype(np.uint8)
    Image.fromarray(result_img).save(save_path)
    print(f"Enhanced: {save_path}")

print("Batch enhancement completed. Check the 'enhanced' subfolder.")
