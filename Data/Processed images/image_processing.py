import cv2
import os

# Process CT Scan Cancerous images: resize to 256x256 and normalize pixel values
input_folder = '..\\Raw images\\CT Scan\\Cancerous raw images'
output_folder = 'CT Scan\\Cancerous images'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))
print("Processing of CT Scan Cancerous images completed.")


# Process CT Scan Non-Cancerous images: resize to 256x256 and normalize pixel values
input_folder = '..\\Raw images\\CT Scan\\Non-Cancerous raw images'
output_folder = 'CT Scan\\Non-Cancerous images'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))
print("Processing of CT Scan Non-Cancerous images completed.")


# Process MRI images: resize to 256x256 and normalize pixel values
input_folder = '..\\Raw images\\MRI'
output_folder = 'MRI'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))
print("Processing of MRI images completed.")

# Process X-Ray Bone fractured images: resize to 256x256 and normalize pixel values
input_folder = '..\\Raw images\\X-Ray\\Bone fractured'
output_folder = 'X-Ray\\Bone fractured'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))
print("Processing of X-Ray Bone fractured images completed.")

# Process X-Ray Bone not fractured images: resize to 256x256 and normalize pixel values
input_folder = '..\\Raw images\\X-Ray\\Bone not fractured'
output_folder = 'X-Ray\\Bone not fractured'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))
print("Processing of X-Ray Bone not fractured images completed.")
