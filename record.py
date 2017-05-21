#!/usr/bin/env python3
from datetime import datetime

import cv2
import numpy as np
import time
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

start_time = time.time()
current_time = 0

d = datetime.now()
filename = "/repos/homeSurveillance/{0}-{1}-{2}-{3}-{4}-{5}.xvid".format(d.year, d.month, d.day, d.hour, d.minute, d.second)

cap = cv2.VideoCapture(1)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter(filename, fourcc, 24.0, (1920,1080))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        if(cfg['display_window'] == true):
        	cv2.imshow('frame',frame)

        # write the flipped frame
        out.write(frame)

        current_time = time.time()
        if (int(current_time) >= int(cfg['length'])):
            break
    else:
        print(ret)

# Release everything if job is finished
cap.release()
out.release()

if(cfg['display_window'] == true):
	cv2.destroyAllWindows()

print("Finished!")
print(filename)
