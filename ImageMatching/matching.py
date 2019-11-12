# @author Mateus Bueno
# Source from @author

import cv2
import numpy as np

# Load the reference image
reference = cv2.imread('../res/ar-marker.png', 0)

# Get width and height from reference image
width, height = reference.shape
image_border = np.float32([[[0,0],[0,height-1],[width-1,height-1],[width-1,0]]])

# Create SIFT detector and extract keypoints, descriptor and compute features
detector = cv2.ORB_create()
keypoints = detector.detect(reference,None)
keypoints, descriptors = detector.detect(reference,keypoints)

# Create FLANN feature matcher
KDITREE = 0
TREE = 5
NEIGHBOURS = 2
flann_dict = dict(algorithm=KDITREE, tree=TREE)
flann = cv2.FlannBasedMatcher(flann_dict, {})

# Number of matches to be considered
MATCH_NUMBER = 30

# Capture from camera
capture = cv2.VideoCapture(0)

# For eache frame
while True:
    has_frame, frame = capture.read()
    if not has_frame:
        break

    # Convert to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract keypoints and descriptors of eache frame
    frame_kp, frame_desc = detector.detectAndCompute(frame_gray, None)

    # Matches descriptors
    matches = flann.knnMatch(frame_desc, descriptors,k=NEIGHBOURS)

    # Filter the matches
    match = []
    for i,j in matches:
        if(i.distance<0.75 * j.distance):
            match.append(i)

    if len(match) >= MATCH_NUMBER:
        reference_points = []
        frame_points = []

        for i in match:
            reference_points.append(keypoints[i.trainIdx].pt)
            frame_points.append(frame_kp[i.queryIdx].pt)

        reference_points,frame_points = np.float32((reference_points,frame_points))

        homography, _ = cv2.findHomography(reference_points, frame_points, cv2.RANSAC, 3.0)

        frame_border = cv2.perspectiveTransform(image_border, homography)

        cv2.polylines(frame, [np.int32(frame_border)], True, (0,255,0), 5)
    
    cv2.imshow('Track', frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()