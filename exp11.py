import cv2
import numpy as np
image = cv2.imread("C:/Users/mbavy/CV/ninjahattori.jpg")
if image is None:
    print("Error loading image.")
    exit()
#  Define source points (three corners or arbitrary points in the image)
height, width = image.shape[:2]
source = np.float32([[50, 50], [200, 50], [50, 200]])
# Define destination points (desired new positions of the points)
destination = np.float32([[10, 100], [200, 50], [100, 250]])
#  Get the Affine Transformation matrix
matrix = cv2.getAffineTransform(source, destination)
# Apply the Affine Transformation
transformed_image = cv2.warpAffine(image, matrix, (width, height))
#  Display the original and transformed images
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", transformed_image)

