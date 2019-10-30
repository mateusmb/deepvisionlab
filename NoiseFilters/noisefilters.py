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

# Read image, convert to float and scale to [0,1] range
image = cv2.imread(params.path).astype(np.float32) / 255

# Check wether the image was successfully loaded
assert image is not None

# Create noise adding random pixels and plot it
noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0, 1)
plt.imshow(noised[:,:,[2,1,0]])
plt.show()

# Gaussian blur
gauss_blur = cv2.GaussianBlur(noised, (7, 7), 0)
plt.imshow(gauss_blur[:,:,[2,1,0]])
plt.show()

# Median filter
median_blur = cv2.medianBlur((noised * 255).astype(np.uint8), 7)
plt.imshow(median_blur[:,:,[2,1,0]])
plt.show()

# Bilateral filter
bilateral = cv2.bilateralFilter(noised, -1, 0.3, 10)
plt.imshow(bilateral[:,:,[2,1,0]])
plt.show()