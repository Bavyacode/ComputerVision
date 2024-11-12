"""import cv2
image = cv2.imread("C:/Users/mbavy/CV/data1.jpg")
if image is None:
    print("Error loading image.")
    exit()
print(image.shape)
height, width = image.shape[:2]
smaller_image = cv2.resize(image, (int(width * 0.5), int(height * 0.5)))
bigger_image = cv2.resize(image, (int(width * 2), int(height * 2)))
cv2.imshow("Original Image", image)
cv2.imshow("Smaller Image", smaller_image)
cv2.imshow("Bigger Image", bigger_image)
"""
import cv2
image = cv2.imread("C:/Users/mbavy/CV/data1.jpg")
if image is None:
    print("Error loading image.")
    exit()
scaling = 23
image_height = int(image.shape[0]*scaling/100)
image_width = int(image.shape[1]*scaling/100)
resized = cv2.resize(image, (image_height,image_width))
cv2.imshow("Original image",image)
cv2.imshow("Resized ",resized)
    
