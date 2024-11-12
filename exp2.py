"""from PIL import Image, ImageFilter
image = Image.open("C:/Users/mbavy/CV/flower.jpg")
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))  # Adjust radius as needed
blurred_image.save("output_blurred.jpeg")
blurred_image.show()"""


import cv2
image = cv2.imread("C:/Users/mbavy/CV/flower.jpg")
blurred_image = cv2.GaussianBlur(image,(15,15),0)
cv2.imshow("Blurred Image", blurred_image)


