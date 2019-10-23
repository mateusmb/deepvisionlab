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

# Save image with lower compression
# Bigger file size but faster decoding
cv2.imwrite('tokyo-compressed.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 0])

# Check that image saved and loaded again is the same as original one
saved_image = cv2.imread('tokyo-compressed.png')
assert saved_image.all() == image.all()

# Save image with lower quality
# Smaller file size
cv2.imwrite('tokyo-compressed.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 50])
