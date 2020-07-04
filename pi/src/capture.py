#!/usr/bin/env python3
"""
	Caputures images triggered by motion sensor
"""

#import the necessary packages
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause

IMAGE_PATH = '/home/pi/pictures/'

pir = MotionSensor(4, pull_up=True)
camera = PiCamera()

#start the camera
camera.rotation = 180
camera.start_preview()

img_num = 0

def take_photo():
    global img_num
    img_num = img_num + 1
    camera.capture(IMAGE_PATH + '/image_%s.jpg' % img_num)
    print('A photo has been taken')
    sleep(10)

pir.when_motion = take_photo

pause()

