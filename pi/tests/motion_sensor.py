#!/usr/bin/env python3
"""
	Detects motion and outputs a sound via a piezo buzzer. 
"""

from gpiozero import MotionSensor
from time import sleep
from signal import pause

pir = MotionSensor(4, pull_up=True)

cnt = 0
def signal_motion():
  global cnt
  print("motion %s" % (cnt))
  cnt = cnt + 1
  sleep(0.1)

pir.when_motion = signal_motion

pause()

