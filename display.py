#!/usr/bin/env python3

import numpy as np
import cv2
import sys
import skvideo.io

cap = cv2.VideoCapture(0)

video_length = 3 * 30;

video = np.empty([video_length, 480, 640, 4], dtype = np.uint8)
video = video.astype(np.uint8)

# Define color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
index = 30
i = 0
current_flag = flags[index]

while(i <= video_length):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    flag = getattr(cv2, flags[index])
    color = cv2.cvtColor(frame, flag)

    # Add to video
    video[i] = color
    i += 1

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
skvideo.io.vwrite("zrawr.mp4", video)
cap.release()
cv2.destroyAllWindows()
print("Current flag on quit: {}".format(current_flag))