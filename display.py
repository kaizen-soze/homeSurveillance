#!/usr/bin/env python3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
index = 29
current_flag = flags[index]

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    cv2.imshow('frame',color)

    if cv2.waitKey(1) & ord('q'):
        break
    elif cv2.waitKey(1) & ord('n'):
        current_flag = flags[index]
        print("Current flag: {}".format(current_flag))
        flag = getattr(cv2, flags[index])
        color = cv2.cvtColor(frame, flag)
        #cv2.destroyAllWindows()
        index += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print("Current flag on quit: {}".format(current_flag))