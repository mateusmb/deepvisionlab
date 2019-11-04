# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Create an object for parsing argument from command line
parser = argparse.ArgumentParser()

# Defines the argument --image and -i for setting image path. Default is 
# bw.png which is included in this repository
parser.add_argument('--path', '-p', default='../res/bw.png', help='Image path.')
params = parser.parse_args()

# Read image as gray
image = cv2.imread(params.path, cv2.COLOR_GRAY2BGR)

# Check wether the image was successfully loaded
assert image is not None

# Find contours and display
contours, image2 = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(color, contours, -1, (0, 255, 0), 3)
cv2.imshow('contours', color)
cv2.waitKey()
cv2.destroyAllWindows()

# Callback function to handle user click.
# Draw a small circle at click position, and paints it green when inside
# and red when outside
contour = contours[0]
image_to_show = np.copy(color)
measure = True

def mouse_callback(event, x, y, flags, param):
    global contour, image_to_show

    if event == cv2.EVENT_LBUTTONUP:
        distance = cv2.pointPolygonTest(contour, (x,y), measure)
        image_to_show = np.copy(color)
        if distance > 0:
            point_color = (0, 255, 0)
        elif distance < 0:
            point_color = (0, 0, 255)
        else:
            point_color = (128, 0, 128)
        cv2.circle(image_to_show, (x,y), 5, point_color, -1)
        cv2.putText(image_to_show, '%.2f' % distance, (0, image_to_show.shape[1] - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

# Show image with mouse click handler. M button switches mode of pointPolygonTest result
cv2.namedWindow('contours')
cv2.setMouseCallback('contours', mouse_callback)

while(True):
    cv2.imshow('contours', image_to_show)
    key = cv2.waitKey(1)

    if key == ord('m'):
        measure = not measure
    elif key == 27:
        break

cv2.destroyAllWindows()
