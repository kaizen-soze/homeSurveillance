#!/usr/bin/env python3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
filename = 'rawr.xvid'
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
video = cv2.VideoWriter.open(filename, fourcc, 24.0, (1920,1080))

if(video.isOpened() is False):
    print("Oops! Unable to initialize {0}".format(filename))
    exit()

# Define color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
index = 30
current_flag = flags[index]

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    rawr = video.write(frame)
    print(rawr)

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
        print("Current flag: {}".format(current_flag))

# When everything done, release the capture
video.release()
cap.release()
cv2.destroyAllWindows()
print("Current flag on quit: {}".format(current_flag))