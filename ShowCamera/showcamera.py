import cv2

# Creates a video capture
capture = cv2.VideoCapture(0)

# Video loop
while True:
    # Read frames and state from camera
    has_frame, frame = capture.read()

    if not has_frame:
        print('Cannot get frame')
        break

    # Show live camera frames
    cv2.imshow('Camera', frame)

    # Waits for ESC key to exit
    key = cv2.waitKey(3)
    if key == 27:
        print('Quit')
        break

# Release video capture and destroy window
capture.release()
cv2.destroyAllWindows()