import cv2
import numpy as np
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
cap = cv2.VideoCapture("C:/Users/mbavy/CV/chocolate.mp4")
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
matrix = cv2.getPerspectiveTransform(source_points, destination_points)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    transformed_frame = cv2.warpPerspective(frame, matrix, (frame.shape[1], frame.shape[0]))
    cv2.imshow('Perspective Transformed Video', transformed_frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
