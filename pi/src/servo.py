#!/usr/bin/env python3

from gpiozero import Servo
from time import sleep

pan = Servo(17)
tilt = Servo(18)

while True:
    print("pan.min")
    pan.min()
    sleep(2)
    print("pan.mid")
    pan.mid()
    sleep(2)
    print("pan.max")
    pan.max()
    sleep(2)

    print("tilt.min")
    tilt.min()
    sleep(2)
    print("tilt.mid")
    tilt.mid()
    sleep(2)
    print("tilt.max")
    tilt.max()
    sleep(2)
