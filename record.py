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

# Initialize webcam capture. If you have multiple
# devices, change the 0 to another number
cap = cv2.VideoCapture(0)

# This isn't quite right; the action seems sped up in the file
frames_per_second = 25
video_length = int(cfg['length']) * frames_per_second

print("Creating a video that is {0} frames long".format(video_length))

if(cfg['record']):
    video = np.empty([video_length, 480, 640, 4], dtype = np.uint8)
    video = video.astype(np.uint8)

i = 0
start_time = time.time()
current_time = 0

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    if(cfg['record']):
        # Add frame to video. All the frames will live in memory
        # until it's time to write to the output file
        #
        # A special shout out to @ravikt for this approach. There
        # aren't any docs on how to take output from CV and use it in
        # skvideo.io
        video[i] = color
        i += 1

    if(cfg['display_window']):
        # Display the resulting frame in a GUI window
        cv2.imshow('frame',color)

    pressed = cv2.waitKey(1);
    # If q key is pressed
    if pressed == 113:
        break

    # To find other key codes, use the waitkey script

    current_time = time.time()
    if (int(current_time) - int(start_time) >= int(cfg['length'])):
        elapsed = int(current_time) - int(start_time)
        print("Reached limit of {0} seconds".format(elapsed))
        break

if(cfg['record']):
    d = datetime.now()
    filename = "/repos/homeSurveillance/{0}-{1}-{2}-{3}-{4}-{5}.mp4".format(d.year, d.month, d.day, d.hour, d.minute, d.second)
    skvideo.io.vwrite(filename, video)
    print("Created file: {0}".format(filename))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
