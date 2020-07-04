#!/usr/bin/env python3
"""
	Draw a boxing frame in an image using OpenCV
"""

import subprocess

import pytest
import yaml
import logging
import cv2 as cv
import sys

LOG = logging.getLogger('testrun')

@pytest.fixture(scope="module")
def read_config(config_file):
    with open(config_file) as config_file_content:
        config = yaml.load(config_file_content, Loader=yaml.FullLoader)
        LOG.debug('Configuration read........')

def test_boxing_frame(read_config):
    config = read_config

    LOG.debug('Calling OpenCV........')

    img = cv.imread("resources/test1.jpg")

    if img is None:
      sys.exit("Couldn't read the image")

    cv.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 2)

    # interactive mode only
    # cv.imshow("Display window", img)
    # k = cv.waitKey(0)
    #
    # if k == ord("s"):
    #   cv.imwrite("resources/test1-boxed.jpg", img)

    cv.imwrite("resources/test1-boxed.jpg", img)
