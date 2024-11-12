import cv2
import numpy as np
image = cv2.imread("C:/Users/mbavy/CV/data1.jpg",0)
_,binary_image = cv2.threshold(image , 127, 255, cv2.THRESH_BINARY)
kernel=np.ones((5,5), np.uint8)
erode = cv2.erode(binary_image, kernel , iterations = 1)
cv2.imshow("Erode" , erode)
