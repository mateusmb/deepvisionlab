# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Draw a test image with primitives (line and circle)
image = np.zeros((500,500), np.uint8)
cv2.circle(image, (200,200), 50, 255, 3)
cv2.line(image, (100,400), (400,350), 255, 3)

# Detect lines using Hough probabilistic transform
lines = cv2.HoughLinesP(image, 1, np.pi/180, 100, 100, 10)[0]

# Detect circles using Hough transform
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 15, param1=200, param2=30)[0]

# Draw detected lines and circles
dbg_image = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)
for x1, y1, x2, y2 in lines:
    print('Detected line: ({} {}) ({} {})'.format(x1,y1,x2,y2))
    cv2.line(dbg_image, (x1,y1), (x2,y2), (0,255,0), 2)

for c in circles:
    print('Detected circles: center=({} {}), radius={}'.format(c[0], c[1], c[2]))
    cv2.circle(dbg_image, (c[0], c[1]), c[2], (0,255,0), 2)

# Display images
plt.figure(figsize=(8,4))
plt.subplot(121)
plt.title('original')
plt.axis('off')
plt.imshow(image, cmap='gray')
plt.subplot(122)
plt.title('detected primitives')
plt.axis('off')
plt.imshow(dbg_image)
plt.show()