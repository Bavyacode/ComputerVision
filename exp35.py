import cv2
import numpy as np

# Load an image in grayscale mode
image = cv2.imread('data1.jpg', 0)  # Replace 'image_path' with the actual path to your image

# Define the kernel for the morphological operation
kernel = np.ones((15, 15), np.uint8)  # Adjust size based on the scale of features

# Apply the Black Hat operation
black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Black Top Hat",black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
