"""#fast Motion
import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/mbavy/CV/chocolate.mp4")
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Fast Motion', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()

#slow motion
cap = cv2.VideoCapture("C:/Users/mbavy/CV/chocolate.mp4")
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Slow Motion', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()"""
"""import cv2
video_path = "C:/Users/mbavy/CV/chocolate.mp4" 
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video file.")
normal_speed = 33  # About 30 fps
slow_motion_speed = 250  # About half the speed (slower)
fast_motion_speed = 1  # About twice the speed (faster)
# Start with normal playback speed
current_speed = normal_speed
print("Press 'n' for normal speed, 's' for slow motion, 'f' for fast motion, 'q' to quit.")
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 # If frame was not captured correctly, break the loop
    if not ret:
        print("End of video reached or failed to read the frame.")
        break
    # Display the frame
    cv2.imshow("Video Playback", frame)
    # Wait for the specified delay and check for key presses
    key = cv2.waitKey(current_speed) 
    if key == 'n':
        current_speed = normal_speed
        print("Switched to normal speed.")
    elif key == ord('s'):
        current_speed = slow_motion_speed
        print("Switched to slow motion.")
    elif key == 'f':
        current_speed = fast_motion_speed
        print("Switched to fast motion.")
    elif key == ord('q'):
        print("Exiting...")
        break
# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
"""

import cv2
cap = cv2.VideoCapture("C:/Users/mbavy/CV/chocolate.mp4")
if not cap.isOpened():
    print("Error in loading the video")
    exit()
normal_speed = 33
fast_speed = 1
slow_speed = 250
current_speed = normal_speed
print("Press 'n' for normal speed, 's' for slow motion, 'f' for fast motion, 'q' to quit.")
while True :
    ret, frame = cap.read()
    if not ret:
        print("End of the video or failed to read a frame")
        break
    cv2.imshow("Video Playback",frame)
    key = cv2.waitKey(current_speed)
    if key == ord('n'):
        current_speed = normal_speed
        print("Switched to normal motion")
    elif key == ord('f'):
        current_speed = fast_speed
        print("Switched to fast motion")
    elif key == ord('s'):
        current_speed = slow_speed
        print("Switched to slow motion")
    elif key == ord('q'):
        print("Exiting")
        break
cv2.release()
cv2.DestroyAllWindows()

