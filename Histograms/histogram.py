# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Create an object for parsing argument from command line
parser = argparse.ArgumentParser()

# Defines the argument --image and -i for setting image path. Default is 
# tokyo.jpg which is included in this repository
parser.add_argument('--path', '-p', default='../res/tokyo.jpg', help='Image path.')
params = parser.parse_args()

# Read image as grey from path in a NumPy array
image = cv2.imread(params.path, 0)

# Check wether the image was successfully loaded
assert image is not None
cv2.imshow('Original image', image)
cv2.waitKey()
cv2.destroyAllWindows()

# Compute histogram function
hist, bins = np.histogram(image, 256, [0,255])

# Plot histogram
plt.fill(hist)
plt.xlabel('Pixel value')
plt.show()