# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import cv2
import numpy as np

# Creates a window
cv2.namedWindow('Fill Color')

# Variable that contains fill color value in BGR
fill_val = np.array([255, 255, 255], np.uint8)

# Callback function that will be called by the trackbar.
# Updates the color index with value
def trackbar_callback(idx, value):
    fill_val[idx] = value

# Creates trackbar and assign callback function as first-class parameters for each color channel
cv2.createTrackbar('R', 'Fill Color', 255, 255, lambda v: trackbar_callback(2, v))
cv2.createTrackbar('G', 'Fill Color', 255, 255, lambda v: trackbar_callback(1, v))
cv2.createTrackbar('B', 'Fill Color', 255, 255, lambda v: trackbar_callback(0, v))

# While the user not hit ESC...
while True:
    # Creates an image with 500x500 and fill value
    image = np.full((500, 500, 3), fill_val)

    # Show the image
    cv2.imshow('Fill Color', image)

    # Receives input key
    key = cv2.waitKey(3)

    # And checks if input key is ESC
    if key == 27:
        break

cv2.destroyAllWindows()