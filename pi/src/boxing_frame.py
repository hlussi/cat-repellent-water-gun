#!/usr/bin/env python3
"""
	Draw a boxing frame in an image using OpenCV
"""

import cv2 as cv
import sys

img = cv.imread("../../images/test1.jpg")

if img is None:
    sys.exit("Couldn't read the image")

cv.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 2)

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("../../images/test1-boxed.jpg", img)
