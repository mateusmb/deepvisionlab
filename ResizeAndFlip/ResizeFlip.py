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

print("Original image shape: ", image.shape)

# Witdth and height which the image will be resized
width, height = 128, 256
resized_image = cv2.resize(image, (width, height))
print("Resized to 128x256 image shape: ", resized_image)

# Resizing with multipliers
width_mult, height_mult = 0.25, 0.5
resized_image = cv2.resize(image, (0, 0), resized_image, width_mult, height_mult)
print("Image shape: ", resized_image.shape)

# Resizing using nearest-neighbor interpolation
width_mult, height_mult = 2, 4
resized_image = cv2.resize(image, (0, 0), resized_image, width_mult, height_mult, cv2.INTER_NEAREST)
print("Half sized image shape: ", resized_image.shape)

# Flip the image along its horizontal x-axis
image_flip_along_x = cv2.flip(image, 0)

# Flip the image along its vertical y-axis
image_flip_along_y = cv2.flip(image, 1)

# Flip the image in both x and y axis
image_flip_xy = cv2.flip(image, -1)