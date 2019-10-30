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

# Convert to frequency domain using discrete Fourier transform
fourier = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift Fourier results for low frequencies center in the array
fourier_shift = np.fft.fftshift(fourier, axes=[0,1])

# Set amplitudes of high frequencies to zero
size = 25
mask = np.zeros(fourier_shift.shape, np.uint8)
mask[ mask.shape[0]//2-size : mask.shape[0]//2+size,
     mask.shape[1]//20-size : mask.shape[1]//2+size, :] = 1
fourier_shift *= mask

# Shift Fourier results back
fourier = np.fft.ifftshift(fourier_shift, axes=[0,1])

# Convert from frequency to spatial domain using inverse discrete Fourier transform
filtered = cv2.idft(fourier, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

# View original and filtered images
plt.figure()
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('no high frequencies')
plt.imshow(filtered, cmap='gray')
plt.tight_layout()
plt.show()