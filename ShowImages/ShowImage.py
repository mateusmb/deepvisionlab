# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import argparse
import cv2

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

# Get image size
image_size = image.shape[0:2]

# Display the image and wait for key to close or 2 seconds
cv2.imshow("Original image", image)
cv2.waitKey(2000)