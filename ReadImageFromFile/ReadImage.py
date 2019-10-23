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

# Print image path
print('read {}'.format(params.path))

# Print width, height and color channels
print('shape: ', image.shape)

# Print undelying image data type
print('dtype: ', image.dtype)

# Load the image in grayscale mode
image = cv2.imread(params.path, cv2.IMREAD_GRAYSCALE)
assert image is not None

print('read {} as grayscale'.format(params.path))

print('shape: ', image.shape)

print('dtype: ', image.dtype)
