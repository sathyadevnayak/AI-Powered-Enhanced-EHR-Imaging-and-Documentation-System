import cv2
import matplotlib.pyplot as plt

# Visual comparison of a raw and processed image of CT Scan
img_raw = cv2.imread('C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Raw images\\CT Scan\\Cancerous raw images\\CT_001.jpg', cv2.IMREAD_GRAYSCALE)
img_processed = cv2.imread('C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Processed images\\CT Scan\\Cancerous images\\CT_001.jpg', cv2.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1)
plt.title("Raw")
plt.imshow(img_raw, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Processed")
plt.imshow(img_processed, cmap='gray')
plt.show()


# Visual comparison of a raw and processed image of MRI
img_raw = cv2.imread('C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Raw images\\MRI\\MRI_001.jpg', cv2.IMREAD_GRAYSCALE)
img_processed = cv2.imread('C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Processed images\\MRI\\MRI_001.jpg', cv2.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1)
plt.title("Raw")
plt.imshow(img_raw, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Processed")
plt.imshow(img_processed, cmap='gray')
plt.show()


# Visual comparison of a raw and processed image of X-Ray
img_raw = cv2.imread('C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Raw images\\X-Ray\\Bone fractured\\XRay_001.png', cv2.IMREAD_GRAYSCALE)
img_processed = cv2.imread('C:\\Users\\Sathyadev\\OneDrive\\Desktop\\Infosys\\AI-Powered-Enhanced-EHR-Imaging-and-Documentation-System\\Data\\Processed images\\X-Ray\\Bone fractured\\XRay_001.png', cv2.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1)
plt.title("Raw")
plt.imshow(img_raw, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Processed")
plt.imshow(img_processed, cmap='gray')
plt.show()
