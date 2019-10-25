# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import argparse
import cv2
import random
import numpy as np

# Create an object for parsing argument from command line
parser = argparse.ArgumentParser()

# Defines the argument --image and -i for setting image path. Default is 
# tokyo.jpg which is included in this repository
parser.add_argument('--path', '-p', default='../res/tokyo.jpg', help='Image path.')
params = parser.parse_args()

# Read image from path in a NumPy array
image = cv2.imread(params.path)

# Check wether the image was successfully loaded
assert image is not None

# Get image width and height
width, height = image.shape[1], image.shape[0]

# Copy the image to show
img_show = np.copy(image)

# Mouse state
mouse_pressed = False
s_x = s_y = e_x = e_y = -1

# Handler for mouse events
def mouse_callback(event, x, y, flags, param):
    global img_show, s_x, s_y, e_x, e_y, mouse_pressed

    # If left mouse button pressed, get the x, y coordinates of mouse position
    # And clear image
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = x, y
        img_show = np.copy(image)

    # If mouse moved while pressed, draw green rectangle at previous coordinates stored
    # and current mouse position
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            img_show = np.copy(image)
            cv2.rectangle(img_show, (s_x, s_y), (x, y), (0, 255, 0), 1)

    # If button released, set pressed state to false and store mouse last position
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        e_x, e_y = x, y

# Create window with function callback
cv2.namedWindow("Tokyo")
cv2.setMouseCallback("Tokyo", mouse_callback)

# Drawing loop
while True:
    # Show image in window
    cv2.imshow("Tokyo", img_show)

    # Get user input
    key = cv2.waitKey(1)

    # C is for show only selected portion
    if key == ord('c'):
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        if s_x > e_x:
            s_x, e_x = e_x, s_x

        if e_y - s_y > 1 and e_x - s_x > 0:
            image = image[s_y: e_y, s_x: e_x]
            img_show = np.copy(image)
    
    # ESC for quit
    elif key == 27:
        break

cv2.destroyAllWindows()
