#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

# Create directory
imgDir = '../images'
 
try:
    # Create target Directory
    os.mkdir(imgDir)
    print("Directory " , imgDir ,  " Created ") 
except FileExistsError:
    print("Directory " , imgDir ,  " already exists")
    
camera = PiCamera()

id = 0
shotIntervalSec = 3

while True:
    sleep(shotIntervalSec)
    camera.capture('%s/image%s.jpg' % imgDir, id)
    id = id + 1

