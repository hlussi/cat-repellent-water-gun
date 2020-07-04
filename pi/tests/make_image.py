#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import os

# Create directory
IMG_DIR = '../../images'
 
try:
    # Create target Directory
    os.mkdir(IMG_DIR)
    print("Directory " , IMG_DIR ,  " Created ") 
except FileExistsError:
    print("Directory " , IMG_DIR ,  " already exists")
    
camera = PiCamera()

id = 0
shotIntervalSec = 3

while True:
    sleep(shotIntervalSec)
    camera.capture('%s/image%s.jpg' % IMG_DIR, id)
    id = id + 1

