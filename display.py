#!/usr/bin/env python3

import numpy as np
import cv2

camera_index = 0
cap = cv2.VideoCapture(camera_index)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('n'):
    	camera_index += 1
    	cap = cv2.VideoCapture(camera_index)
    	if(!cap.isOpened):
    		print("CameraIndex {0} failed", format(camera_index))
    		cap = cv2.VideoCapture(0)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()