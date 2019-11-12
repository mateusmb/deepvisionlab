import cv2
import numpy as np

roi_pts = []
mouse_listen = False
frame = None
iterations = 10
capture = cv2.VideoCapture(0)

def selectROI(event, x, y, flags, param):
    global frame, roi_pts, mouse_listen

    if mouse_listen and event == cv2.EVENT_LBUTTONDOWN and len(roi_pts) < 4:
        roi_pts.append((x,y))
        cv2.circle(frame, (x,y), 4, (0,255,0), 2)
        cv2.imshow('Track', frame)

cv2.namedWindow('Track')
cv2.setMouseCallback('Track', selectROI)

finish = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, iterations, 1)
roi_box = None

while True:
    has_frame, frame = capture.read()

    if not has_frame:
        break

    if roi_box is not None:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        histogram_backproj = cv2.calcBackProject([hsv], [0], roiHist, [0,180], 1)

        (r, roi_box) = cv2.CamShift(histogram_backproj, roi_box, finish)
        pts = np.int0(cv2.boxPoints(r))
        cv2.polylines(frame, [pts], True, (0,255,0), 2)

    cv2.imshow('Track', frame)
    key = cv2.waitKey(1)

    if key == ord('t') and len(roi_pts) < 4:
        mouse_listen = True
        original = frame.copy()

        while len(roi_pts) < 4:
            cv2.imshow('Track', frame)
            cv2.waitKey(0)

        roi_pts = np.array(roi_pts)
        s = roi_pts.sum(axis=1)
        tl = roi_pts[np.argmin(s)]
        br = roi_pts[np.argmax(s)]

        roi = original[tl[1]:br[1], tl[0]:br[0]]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        roiHist = cv2.calcHist([roi], [0], None, [16], [0,180])
        roi_box = (tl[0], tl[1], br[0], br[1])

    elif key == 27:
        break

capture.release()
cv2.destroyAllWindows()
