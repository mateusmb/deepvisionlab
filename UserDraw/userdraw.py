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

# Create window
cv2.namedWindow("Tokyo")

# Get image width and height
width, height = image.shape[1], image.shape[0]

# Copy the image to show
img_show = np.copy(image)

# Function to get random points
def rand_pt():
    return (random.randrange(width), random.randrange(height))

# Drawing loop
# Flag for finished program
finish = False

while not finish:
    # Show the image
    cv2.imshow("Tokyo", img_show)

    # Get user input key
    key = cv2.waitKey(0)

    # P is for drawing points
    if key == ord('p'):
        for pt in [rand_pt() for _ in range(10)]:
            cv2.circle(img_show, pt, 3, (255, 0, 0), -1)
    
    # L is for drawing lines
    elif key == ord('l'):
        cv2.line(img_show, rand_pt(), rand_pt(), (0, 255, 0), 3)

    # R is for drawing rectangles
    elif key == ord('r'):
        cv2.rectangle(img_show, rand_pt(), rand_pt(), (0, 0, 255), 3)

    # E is for drawing ellipses
    elif key == ord('e'):
        cv2.ellipse(img_show, rand_pt(), rand_pt(), random.randrange(360), 0, 360, (255, 255, 0), 3)

    # T is for drawing text
    elif key == ord('t'):
        cv2.putText(img_show, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

    # C is for clear image
    elif key == ord('c'):
        img_show = np.copy(image)

    # ESC for exit
    elif key == 27:
        finish = True