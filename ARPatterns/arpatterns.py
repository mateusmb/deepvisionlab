# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import cv2
import cv2.aruco as aruco
import numpy as np

# Create an image with different AruCo markers
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
image = np.full((700,700), 255, np.uint8)

image[100:300, 100:300] = aruco.drawMarker(aruco_dict, 2, 200)
image[100:300, 400:600] = aruco.drawMarker(aruco_dict, 76, 200)
image[400:600, 100:300] = aruco.drawMarker(aruco_dict, 42, 200)
image[400:600, 400:600] = aruco.drawMarker(aruco_dict, 123, 200)

# Blur the image
image = cv2.GaussianBlur(image, (11, 11), 0)

# Display
cv2.imshow('Created AruCo markers', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detect the markers and draw them
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
corners, ids, _ = aruco.detectMarkers(image, aruco_dict)
image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
aruco.drawDetectedMarkers(image_color, corners, ids)

# Show results
cv2.imshow('Detected AruCo markers', image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()