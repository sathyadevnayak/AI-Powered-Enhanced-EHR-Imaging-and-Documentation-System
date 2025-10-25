import cv2
import os

# Process CT Scan Cancerous images: resize to 256x256 and normalize pixel values
input_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Raw images\\CT Scan\\Cancerous raw images'
output_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Processed images\\CT Scan\\Cancerous images'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))


# Process CT Scan Non-Cancerous images: resize to 256x256 and normalize pixel values
input_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Raw images\\CT Scan\\Non-Cancerous raw images'
output_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Processed images\\CT Scan\\Non-Cancerous images'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))


# Process MRI images: resize to 256x256 and normalize pixel values
input_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Raw images\\MRI'
output_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Processed images\\MRI'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))

# Process X-Ray Bone fractured images: resize to 256x256 and normalize pixel values
input_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Raw images\\X-Ray\\Bone fractured'
output_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Processed images\\X-Ray\\Bone fractured'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))

# Process X-Ray Bone not fractured images: resize to 256x256 and normalize pixel values
input_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Raw images\\X-Ray\\Bone not fractured'
output_folder = 'C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Processed images\\X-Ray\\Bone not fractured'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    cv2.imwrite(os.path.join(output_folder, filename), (img * 255).astype('uint8'))
