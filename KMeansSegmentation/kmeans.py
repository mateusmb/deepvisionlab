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

# Read image as gray
image = cv2.imread(params.path).astype(np.float32)/255

# Check wether the image was successfully loaded
assert image is not None

# Convert image to Lab color space
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

# Reshape to vector
data = image_lab.reshape((-1,3))

# Set clusters and criteria. Then perform k-means clusterization
num_classes = 4
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.1)
_, labels, centers = cv2.kmeans(data, num_classes, None, criteria, 10,
                                cv2.KMEANS_RANDOM_CENTERS)

# Apply centroid colors to all relevant pixel to these centroids. Then reshape to original
segmented_lab = centers[labels.flatten()].reshape(image.shape)

# Convert to RGB color space
segmented = cv2.cvtColor(segmented_lab, cv2.COLOR_Lab2RGB)

# Display original and segmented images
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(image[:, :, [2, 1, 0]])
plt.subplot(122)
plt.axis('off')
plt.title('segmented')
plt.imshow(segmented)
plt.show()