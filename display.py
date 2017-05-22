#!/usr/bin/env python3

from datetime import datetime

import cv2
import numpy as np
import sys
import skvideo.io
import time
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

cap = cv2.VideoCapture(0)

video_length = int(cfg['length']) * 24;

print("Creating a video that is {0} frames long".format(video_length))

video = np.empty([video_length, 480, 640, 4], dtype = np.uint8)
video = video.astype(np.uint8)

# Define color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
index = 30
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

    # Add to video
    video[i] = color
    i += 1

    if(cfg['display_window']):
        # Display the resulting frame
        cv2.imshow('frame',color)
        
    pressed = cv2.waitKey(1);
    if pressed == 113:
        break
    
    if pressed == 110:
        index += 1
        current_flag = flags[index]
        print("Current flag: {0}".format(current_flag))

    current_time = time.time()
    if (int(current_time) - start_time >= int(cfg['length'])):
        zzz = int(current_time) - start_time
        print("Reached limit of {0} seconds".format(zzz))
        break

if(cfg['record']):
    d = datetime.now()
    filename = "/repos/homeSurveillance/{0}-{1}-{2}-{3}-{4}-{5}.mp4".format(d.year, d.month, d.day, d.hour, d.minute, d.second)
    skvideo.io.vwrite(filename, video)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print("Current flag on quit: {}".format(current_flag))