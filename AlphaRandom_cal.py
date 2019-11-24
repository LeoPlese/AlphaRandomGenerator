# -*- coding: utf-8 -*-

"""

Project: Alpha Random - Alpha Particles Random Number Generator
Version: 1.0
Author: Leo Plese
e-mail: plese.leo@gmail.com
Web: alpharandom.info

Abstract:
This script is used to calibrate system for Alpha Particles Random Number Generator.

Note:
Calibration reference image is saved in script path under name CalibImg.png

"""

import time
import cv2
import sys

def fnImageCaptureAndTransform():
    try:
        """ Capture image from Alpha Random camera """
        camera_port = 0
        ARcamera = cv2.VideoCapture(camera_port)

        # camera settings
        ARcamera.set(3, 640) # width
        ARcamera.set(4, 480) # height
        ARcamera.set(12, 0) # saturation
        ARcamera.set(11, 1) # contrast
        ARcamera.set(10, 0) # brightness
        
        time.sleep(0.1) # wait for camera to stabilize itself
        isOk, capturedImage = ARcamera.read()
        del(ARcamera)
        
        """ Transform image to grayscale and give high contrast """
        # transformation to grayscale image
        grayImage = cv2.cvtColor(capturedImage, cv2.COLOR_BGR2GRAY)

        """ CALIBRATION POINT - Change value 5 to lower to get brighter image or higher to get darker image"""
        grayImage[grayImage<5] = 0
        grayImage[grayImage>=5] = 255

        # save image to script path under name 
        cv2.imwrite("./CalibImg.png", grayImage)
    except:
        print ("Unexpected error:", sys.exc_info()[0],"\nPlese check:\n- camera_port value in calibration script\n- Alpha Random Camera\n- hardware connections")


fnImageCaptureAndTransform()
        
