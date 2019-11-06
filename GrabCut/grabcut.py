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

# Create a copy of the image
show_image = np.copy(image)

# Mouse callback variables
mouse_pressed = False
y = x = w = h = 0

# Mouse callback function
def mouse_callback(event, _x, _y, flags, param):
    global show_image, x, y, w, h, mouse_pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        x, y = _x, _y
        show_image = np.copy(image)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            show_image = np.copy(image)
            cv2.rectangle(show_image, (x,y), (_x,_y),
                          (0,255,0),3)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        w, h = _x -x, _y - y

# Show image and set callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

# Loop to get rectangle. When A is pressed, close the window
while True:
    cv2.imshow('image', show_image)
    key = cv2.waitKey(1)

    if key == ord('a') and not mouse_pressed:
        if w*h > 0:
            break

cv2.destroyAllWindows()

# Create object mask based on rectangle drawn
labels = np.zeros(image.shape[:2], np.uint8)
labels, bgdModel, fgdModel = cv2.grabCut(image, labels, (x,y,w,h), None,
                                         None, 5, cv2.GC_INIT_WITH_RECT)

show_image = np.copy(image)
show_image[(labels == cv2.GC_PR_BGD) | (labels == cv2.GC_BGD)] //= 3

cv2.imshow('image', show_image)
cv2.waitKey()
cv2.destroyAllWindows()

# Set mouse callback to draw mask
label = cv2.GC_BGD
label_clrs = {cv2.GC_BGD: (0,0,0), cv2.GC_FGD: (255,255,255)}

def mouse_callback(event, x, y, flags, param):
    global mouse_pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        cv2.circle(labels, (x,y), 5, label, cv2.FILLED)
        cv2.circle(show_image, (x,y), 5, label_clrs[label], cv2.FILLED)
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            cv2.circle(labels, (x,y), 5, label, cv2.FILLED)
            cv2.circle(show_image, (x,y), 5, label_clrs[label], cv2.FILLED)
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False

# Create the window and set mouse funcion callback for displaying mask
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

# White draws backgound labeled pixels, black is for object pixels
while True:
    cv2.imshow('image', show_image)
    key = cv2.waitKey(1)

    if key == ord('a') and not mouse_pressed:
        break
    elif key == ord('l'):
        label = cv2.GC_FGD - label

cv2.destroyAllWindows()

labels, bgdModel, fgdModel = cv2.grabCut(image, labels, None, bgdModel, fgdModel,
                                         5, cv2.GC_INIT_WITH_MASK)

show_image = np.copy(image)
show_image[(labels == cv2.GC_PR_BGD) | (labels == cv2.GC_BGD)] //= 3

cv2.imshow('image', show_image)
cv2.waitKey()
cv2.destroyAllWindows()