"""#90 degree
import cv2
image = cv2.imread("C:/Users/mbavy/CV/ninjahattori.jpg")
rotatedimage = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
rotatedimageCC = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original image", image)
cv2.imshow("Rotated image ", rotatedimage)
cv2.imshow("Rotated imageCC", rotatedimageCC)

#180 degree
rotatedimage180 = cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow("Original image", image)
cv2.imshow("Rotated image 180", rotatedimage180)

rotatedimage270 = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Rotated image 270", rotatedimage270)
"""
import cv2
image = cv2.imread("C:/Users/mbavy/CV/ninjahattori.jpg")
rotate90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotate90cc = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
rotate180 = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("Original image",image)
cv2.imshow("90 - Clockwise ", rotate90)
cv2.imshow("90 - Counterclockwise ", rotate90cc)
cv2.imshow("180 ", rotate180)
