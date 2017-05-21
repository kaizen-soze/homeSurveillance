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
filename = "{0}-{1}-{2}-{3}-{4}-{5}.avi".format(d.year, d.month, d.day, d.hour, d.minute, d.second)

cap = cv2.VideoCapture(1)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        current_time = time.time()
        if (int(current_time) >= int(cfg['length'])):
            break

# Release everything if job is finished
cap.release()
out.release()
#cv2.destroyAllWindows()

print("Finished!")
