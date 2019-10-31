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

# Read image as grey
image = cv2.imread(params.path, 0)

# Check wether the image was successfully loaded
assert image is not None

# Apply binary threshold
threshold, mask = cv2.threshold(image, 200, 1, cv2.THRESH_BINARY)
print('Threshold used: ', threshold)

# Apply adaptive threshold
adapt_mask = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY_INV, 11, 10)

# View images
plt.figure(figsize=(10,3))
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('binary threshold')
plt.imshow(mask, cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title('adaptive threshold')
plt.imshow(adapt_mask, cmap='gray')
plt.tight_layout()
plt.show()