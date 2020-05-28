#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()

id = 0
shotIntervalSec = 3

while True:
    sleep(shotIntervalSec)
    camera.capture('images/image%s.jpg' % id)
    id = id + 1

