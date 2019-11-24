# -*- coding: utf-8 -*-

"""

Project: Alpha Random - Alpha Particles Random Number Generator - Random Picture Generator
Version: 1.0
Author: Leo Plese
e-mail: plese.leo@gmail.com
Web: alpharandom.info

Abstract:
This script is used for generating random picture which are used by Alpha Particles Random Number Generator Simulation program (AlphaRandom_numGen.py). 

Note:
Set number of generated pictures in variable with name numberOfPictures.
Before using simulation script set absolute file path to your image folder in variable imagePath and number of images in variable numberOfPictures.
In the program is example of file path /home/pi/Image/ and ordinal number of last image 501.

"""
import numpy as np
from random import randint
import cv2

def main():
    # here set number (>0) of generated pictures in next variable (here: 501)
    numberOfPictures = 501

    # flash pictures
    shapeOne = np.array([1, 1, 638, 1, 1, 1, 636, 1, 1, 1, 1, 636, 1, 1, 1, 638, 1])
    shapeTwo = np.array([1, 1, 1, 1, 636, 1, 1, 1, 1, 636, 1, 1, 1, 1, 637, 1, 1, 1, 638, 1])
    shapeThree = np.array([1, 1, 1, 1, 637, 1, 1, 1, 637, 1, 1, 1, 637, 1, 1, 1])
    shapeFour = np.array([1, 1, 1, 637, 1, 1, 1, 1, 636, 1, 1, 1, 1, 637, 1, 1, 638, 1, 1, 639])
    shapeFive = np.array([1, 1, 638, 1, 1, 1, 636, 1, 1, 1, 1, 636, 1, 1, 1, 1, 1, 1, 635, 1, 3, 1, 1279, 1])
    shapeSix = np.array([1, 1, 1, 1, 1, 636, 1, 1, 1, 1, 637, 1, 1, 637, 1, 1, 1, 638, 1])
    shapeSeven = np.array([1, 1, 1, 1, 637, 1, 1, 1, 637, 1, 1, 1, 637, 1, 1, 1, 637, 3, 638])

    for nop in range(numberOfPictures):
        
        randPicture = np.zeros(307200, dtype=int)
        flashNum = randint(0, 35)

        for x in range(0, flashNum):
            positionX = randint(0, 307199)
            shapeNumber = randint(1, 7)
            dicX = {1:shapeOne, 2:shapeTwo, 3:shapeThree, 4:shapeFour, 5:shapeFive, 6:shapeSix, 7:shapeSeven}
            shapeFlash = dicX[shapeNumber]
            for y in range(0, shapeFlash.size):
                positionX += shapeFlash[y]
                if positionX > 307199:
                    y = shapeFlash.size
                else:
                    randPicture[positionX] = 255

        randPicture = randPicture.reshape(480, 640)
        # here set absolute file path to images (here: /home/pi/Image/)
        imagePath = "/home/pi/Image/"
        cv2.imwrite(imagePath + "Img_" + str(nop+1) + ".png", randPicture)


main()

