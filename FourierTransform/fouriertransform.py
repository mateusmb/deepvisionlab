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

# Read image as grey and convert it to float32
image = cv2.imread(params.path, 0).astype(np.float32) / 255

# Check wether the image was successfully loaded
assert image is not None

# Apply discrete fourier transform
fourier = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

# View image spectrum
shifted = np.fft.fftshift(fourier, axes=[0,1])
magnitude = cv2.magnitude(shifted[:,:,0], shifted[:,:,1])
magnitude = np.log(magnitude)

plt.axis('off')
plt.imshow(magnitude, cmap='gray')
plt.tight_layout()
plt.show()

# convert back from the frequency representation to spatial representation
restored = cv2.idft(fourier, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)