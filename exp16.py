import cv2
image = cv2.imread("C:/Users/mbavy/CV/ninjahattori.jpg")
print(image.shape)
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gray,(5,5),0)
canny = cv2.Canny(blur,100,100)
cv2.imshow("Canny edge detection", canny)
