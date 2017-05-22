#!/usr/bin/env python3

from datetime import datetime

import cv2
import numpy as np
import sys
import time

cap = cv2.VideoCapture(0)

frames_per_second = 25
video_length = 10 * frames_per_second

# Define color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
index = 29
i = 0
current_flag = flags[index]

start_time = time.time()
current_time = 0

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    flag = getattr(cv2, flags[index])
    color = cv2.cvtColor(frame, flag)

    # Display the resulting frame
    cv2.imshow('frame',color)

    pressed = cv2.waitKey(1);
    if pressed == 113:
        break
    
    if pressed == 110:
        index += 1
        current_flag = flags[index]
        print("Current flag: {0}".format(current_flag))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print("Current flag on quit: {}".format(current_flag))