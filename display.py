#!/usr/bin/env python3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
current_flag = ''
index = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    cv2.imshow('frame',color)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('n'):
    	flag = flags[index]
    	color = cv2.cvtColor(frame, cv2.flag)
    	current_flag = flag
    	index += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print("Current flag on quit: {}".format(current_flag))