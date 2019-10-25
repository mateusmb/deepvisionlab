# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import argparse
import cv2
import random

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

# Create window
cv2.namedWindow("Tokyo")

# Get image width and height
width, height = image.shape[1], image.shape[0]

# Function to create random points
def rand_pt(mult=1.):
    return (random.randrange(int(width*mult)),
            random.randrange(int(height*mult)))

# Drawing circles
cv2.circle(image, rand_pt(), 40, (255, 0, 0))
cv2.circle(image, rand_pt(), 5, (255, 0, 0), cv2.FILLED)
cv2.circle(image, rand_pt(), 40, (255, 85, 85), 2)
cv2.circle(image, rand_pt(), 40, (255, 170, 170), 2, cv2.LINE_AA)

# Draw lines
cv2.line(image, rand_pt(), rand_pt(), (0, 255, 0))
cv2.line(image, rand_pt(), rand_pt(), (255, 255, 0), 3)
cv2.line(image, rand_pt(), rand_pt(), (170, 255, 170), 3, cv2.LINE_AA)

# Draw an arrow
cv2.arrowedLine(image, rand_pt(), rand_pt(), (0, 0, 255), 3, cv2.LINE_AA)

# Draw rectangle
cv2.rectangle(image, rand_pt(), rand_pt(), (255, 255, 0), 3)

# Draw ellipse
cv2.ellipse(image, rand_pt(), rand_pt(0.3), random.randrange(360), 0, 360, (255, 255, 255), 3)

# Draw text
cv2.putText(image, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

while True:
    cv2.imshow('Tokyo', image)

    # Receives input key
    key = cv2.waitKey(3)

    # And checks if input key is ESC
    if key == 27:
        break

cv2.destroyAllWindows()