# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import cv2
import argparse
import numpy as np
from random import randint

# Create an object for parsing argument from command line
parser = argparse.ArgumentParser()

# Defines the argument --image and -i for setting image path. Default is 
# bw.png which is included in this repository
parser.add_argument('--path', '-p', default='../res/tokyo.jpg', help='Image path.')
params = parser.parse_args()

# Read image as gray
image = cv2.imread(params.path)

# Check wether the image was successfully loaded
assert image is not None

# Copy, seeds and segmentation images
show_image = np.copy(image)
seeds = np.full(image.shape[0:2], 0, np.int32)
segmentation = np.full(image.shape, 0, np.uint8)

# Set number and color of seed types
n_seeds = 9
colors = []
for m in range(n_seeds):
    colors.append((255 * m/n_seeds, randint(0, 255), randint(0,255)))

# Mouse events variables
mouse_pressed = False
current_seed = 1
seeds_updated = False

# Mouse callback function. Draw seeds dragging the mouse while pressed
def mouse_callback(event, x, y, flags, param):
    global mouse_pressed, seeds_updated

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        cv2.circle(seeds, (x, y), 5, (current_seed), cv2.FILLED)
        cv2.circle(show_image, (x,y), 5, colors[current_seed - 1],
                   cv2.FILLED)
        seeds_updated = True
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            cv2.circle(seeds, (x,y), 5, (current_seed), cv2.FILLED)
            cv2.circle(show_image, (x,y), 5, colors[current_seed -
                       1], cv2.FILLED)
            seeds_updated = True

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False

# Create window and set callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

# Callback loop. C set changes to the current seed by pressing numbers.
# Segment image with watershed algorithm when finished
while True:
    cv2.imshow('segmentation', segmentation)
    cv2.imshow('image', show_image)

    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord('c'):
        show_image = np.copy(image)
        seeds = np.full(image.shape[0:2], 0, np.int32)
        segmentation = np.full(image.shape, 0, np.uint8)
    elif key > 0 and chr(key).isdigit():
        n = int(chr(key))
        if 1 <= n <= n_seeds and not mouse_pressed:
            current_seed = n

    if seeds_updated and not mouse_pressed:
        seeds_copy = np.copy(seeds)
        cv2.watershed(image, seeds_copy)
        segmentation = np.full(image.shape, 0, np.uint8)
        for m in range(n_seeds):
            segmentation[seeds_copy == (m+1)] = colors[m]

        seeds_updated

cv2.destroyAllWindows()