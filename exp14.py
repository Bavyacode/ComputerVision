import cv2
import numpy as np

# Read the input image
image = cv2.imread("C:/Users/mbavy/CV/ninjahattori.jpg")
if image is None:
    print("Error loading image.")
    exit()

# Define source and destination points for homography transformation
source_points = np.float32([
    [50, 50],
    [200, 50],
    [50, 200],
    [200, 200]
])

destination_points = np.float32([
    [10, 100],
    [300, 50],
    [100, 250],
    [250, 300]
])

# Calculate the homography matrix
homography_matrix, _ = cv2.findHomography(source_points, destination_points)

# Apply homography transformation
transformed_image = cv2.warpPerspective(image, homography_matrix, (image.shape[1], image.shape[0]))

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformed Image", transformed_image)
