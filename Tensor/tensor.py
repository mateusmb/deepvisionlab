# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import cv2
import argparse
import numpy as np

# Create an object for parsing argument from command line
parser = argparse.ArgumentParser()

# Defines the argument --image and -i for setting image path. Default is 
# bw.png which is included in this repository
parser.add_argument('--path', '-p', default='../res/tokyo.jpg', help='Image path.')
params = parser.parse_args()

# Read image as 3-color channel
image = cv2.imread(params.path, cv2.IMREAD_COLOR)

# Check wether the image was successfully loaded
assert image is not None

# Print image shape
print(image.shape)

# Transform to four dimensional tensor
image_float = image.astype(np.float32)
image_rgb = image_float[..., ::-1]
tensor_chw = np.transpose(image_rgb, (2,0,1))
tensor_nchw = tensor_chw[np.newaxis, ...]

# Print tensor
print(tensor_nchw.shape)
