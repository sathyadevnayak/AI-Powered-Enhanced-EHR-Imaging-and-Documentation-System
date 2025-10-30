import glob
import torch
import os
import matplotlib.pyplot as plt
from monai.networks.nets import UNet
from monai.data import Dataset, DataLoader
from monai.transforms import Compose, LoadImage, EnsureChannelFirst, ScaleIntensity, ToTensor, RandGaussianNoise

# --- Step 1: Prepare data loaders for training and validation ---
# Find all image paths
img_list = glob.glob(os.path.join("X-Ray/Bone fractured/", "*.jpg")) + \
           glob.glob(os.path.join("X-Ray/Bone not fractured/", "*.jpg")) + \
           glob.glob(os.path.join("MRI/", "*.jpg")) + \
           glob.glob(os.path.join("CT Scan/Cancerous images/", "*.jpg")) + \
           glob.glob(os.path.join("CT Scan/Non-Cancerous images/", "*.jpg"))

# Split data for training and validation
split_ratio = 0.8
split_index = int(len(img_list) * split_ratio)
train_files = img_list[:split_index]
val_files = img_list[split_index:]

# --- Step 2: Define transforms ---
train_transforms = Compose([
    LoadImage(image_only=True),
    EnsureChannelFirst(),
    ScaleIntensity(),
    RandGaussianNoise(prob=1.0, mean=0.0, std=0.08),
    ToTensor()
])
val_transforms = Compose([
    LoadImage(image_only=True),
    EnsureChannelFirst(),
    ScaleIntensity(),
    ToTensor()
])

# Use separate transforms for ground truth images (without noise)
target_transforms = Compose([
    LoadImage(image_only=True),
    EnsureChannelFirst(),
    ScaleIntensity(),
    ToTensor()
])

# --- Step 3: Create Datasets and DataLoaders ---
train_ds = Dataset(data=train_files, transform=train_transforms)
train_target_ds = Dataset(data=train_files, transform=target_transforms)
train_loader = DataLoader(list(zip(train_ds, train_target_ds)), batch_size=2, shuffle=True)

val_ds = Dataset(data=val_files, transform=train_transforms)
val_target_ds = Dataset(data=val_files, transform=target_transforms)
val_loader = DataLoader(list(zip(val_ds, val_target_ds)), batch_size=2, shuffle=False)

# --- Step 4: Define Model, Loss, Optimizer ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet(
    spatial_dims=2,
    in_channels=1,
    out_channels=1,
    channels=(16, 32, 64, 128, 256),
    strides=(2, 2, 2, 2),
    num_res_units=2,
).to(device)

loss_function = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

# Lists to store losses for plotting
train_losses = []
val_losses = []

# --- Step 5: Training Loop with Validation ---
EPOCHS = 30
for epoch in range(EPOCHS):
    model.train()
    epoch_train_loss = 0
    for noisy_batch, clean_batch in train_loader:
        noisy_batch, clean_batch = noisy_batch.to(device), clean_batch.to(device)
        output = model(noisy_batch)
        loss = loss_function(output, clean_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_train_loss += loss.item()

    avg_train_loss = epoch_train_loss / len(train_loader)
    train_losses.append(avg_train_loss)

    # Validation loop
    model.eval()
    epoch_val_loss = 0
    with torch.no_grad():
        for noisy_batch, clean_batch in val_loader:
            noisy_batch, clean_batch = noisy_batch.to(device), clean_batch.to(device)
            output = model(noisy_batch)
            loss = loss_function(output, clean_batch)
            epoch_val_loss += loss.item()

    avg_val_loss = epoch_val_loss / len(val_loader)
    val_losses.append(avg_val_loss)

    print(f"Epoch {epoch+1}/{EPOCHS}, Train Loss: {avg_train_loss:.4f}, Val Loss: {avg_val_loss:.4f}")

# --- Step 6: Plotting the loss curve ---
plt.figure(figsize=(10, 6))
plt.plot(train_losses, label="Training Loss")
plt.plot(val_losses, label="Validation Loss")
plt.title("Training and Validation Loss over Epochs")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()

# --- Step 7: Visualize a sample from the validation set ---
model.eval()
sample_noisy, sample_clean = next(iter(val_loader))
sample_noisy, sample_clean = sample_noisy.to(device), sample_clean.to(device)
with torch.no_grad():
    sample_denoised = model(sample_noisy)

# Detach from GPU and convert to numpy for plotting
sample_noisy = sample_noisy.cpu().numpy()[0, 0]
sample_clean = sample_clean.cpu().numpy()[0, 0]
sample_denoised = sample_denoised.cpu().numpy()[0, 0]

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(sample_clean, cmap="gray")
plt.title("Original Clean Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(sample_noisy, cmap="gray")
plt.title("Noisy Input Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(sample_denoised, cmap="gray")
plt.title("Denoised Output")
plt.axis("off")

plt.show()

# --- Step 8: Save Model ---
torch.save(model.state_dict(), "xray_denoiser_unet.pth")
print("Model saved as xray_denoiser_unet.pth")
