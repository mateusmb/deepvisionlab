# Source from Alexey Spizhevoy and Aleksandr Rybnikov OpenCV 3 Computer Vision with Python Cookbook

import cv2

# Create a camera capture
capture = cv2.VideoCapture(0)

# Get frame width and height
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame width: ', frame_width)
print('Frame height: ', frame_height)

# Create a video writer
video = cv2.VideoWriter('captured_video.avi', cv2.VideoWriter_fourcc(*'X264'), 25, (frame_width, frame_height))

# Capture loop
while True:
    has_frame, frame = capture.read()

    if not has_frame:
        print("Can't get frame")
        break

    # Save each frame on stream file
    video.write(frame)

    # Show camera
    cv2.imshow('Camera', frame)

    # Wait for ESC
    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed ESC')
        break

# Release memory from capture, stream file and window
capture.release()
video.release()
cv2.destroyAllWindows()