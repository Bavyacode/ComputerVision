import cv2
import numpy as np
image = cv2.imread("C:/Users/mbavy/CV/ninjahattori.jpg")
source_points = np.float32([
    [50, 50],      # Top-left corner
    [200, 50],     # Top-right corner
    [50, 200],     # Bottom-left corner
    [200, 200]     # Bottom-right corner
])

destination_points = np.float32([
    [10, 100],     # New top-left corner
    [300, 50],     # New top-right corner
    [100, 250],    # New bottom-left corner
    [250, 300]     # New bottom-right corner
])

# Calculate the perspective transformation matrix
matrix = cv2.getPerspectiveTransform(source_points, destination_points)

# Apply perspective transformation
transformed_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))
cv2.imshow('Perspective Transformed Image', transformed_image)
