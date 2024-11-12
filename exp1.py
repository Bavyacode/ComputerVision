"""from PIL import Image
image = Image.open("C:/Users/mbavy/CV/flower.jpg")
gray_image = image.convert("L")
gray_image.save("output1.jpeg")
gray_image.show()


import cv2
image = cv2.imread("C:/Users/mbavy/CV/flower.jpg")
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image ",grayimage)
"""
import cv2
image = cv2.imread("C:/Users/mbavy/CV/data1.jpg")
print(image.shape)
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgbimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsvimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#resized_image = cv2.resize(grayimage, (800, 600))
cv2.imshow("Gray image ",grayimage)
cv2.imshow("rgb image ",rgbimage)
cv2.imshow("hsv image ",hsvimage)
cv2.imshow("Original image ",image)
cv2.waitKey()
cv2.destroyAllWindows()
