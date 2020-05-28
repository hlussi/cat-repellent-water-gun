#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()

for i in range(9):
    sleep(5)
    camera.capture('images/image%s.jpg' % i)

