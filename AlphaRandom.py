# -*- coding: utf-8 -*-

"""

Project: Alpha Random - Alpha Particles Random Number Generator
Version: 1.0
Author: Leo Plese
e-mail: plese.leo@gmail.com
Web: alpharandom.info

Abstract:
This script is used to generate a random number of one of the next types:
true(1)/false(0), number from 0 to 1 (range [0,1]), integer number from input range [min,max] or floating point number from input range [min,max]. 

Note:
If option outtype is not defined, output will be --out=to1 by default.
If option from and/or option to values are not defined, used values will be --from=0 and --to=100

Options:
-o or --out= following argument <tf|to1|numint|numflt>  Choose output: true(1)/false(0)|number to 1|integer|float
-f or --from= following argument <fromnumber>           Integer min in range. Required for output numint/numflt
-t or --to= following argument <tonumber>               Integer max in range. Required for output numint/numflt
-h or --help                                            Show help.

Defaults:
--out=to1
--from=0
--to=100

Example of use:
AlphaRandom.py -o tf
AlphaRandom.py --out=to1
AlphaRandom.py -o numint -f 100 -t 200
AlphaRandom.py --out=numflt --from=100 --to=200

"""

import time
import cv2
import numpy as np
import sys
import getopt


def fnImageCaptureAndTransform():
    """ Capture image from Alpha Random camera """
    try:
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)

        # camera settings
        ARcamera.set(3, 640) # width
        ARcamera.set(4, 480) # height
        ARcamera.set(12, 0) # saturation
        ARcamera.set(11, 1) # contrast
        ARcamera.set(10, 0) # brightness
        
        time.sleep(0.1)  # wait for camera to stabilize itself
        isOk, capturedImage = ARcamera.read()
        del(ARcamera)

        """ Transform image to grayscale and give high contrast """
        # transformation to grayscale image
        grayImage = cv2.cvtColor(capturedImage, cv2.COLOR_BGR2GRAY)
        # high contrast image - set with treshold number to treshold hot and stuck pixels
        grayImage[grayImage<5] = 0
        grayImage[grayImage>=5] = 255
        return grayImage
    except:
        fnException("Unexpected error!\nPlese check Alpha Random Camera and perform calibration of system if problem persists.", 0)

    
def fnImageArrayToNumber():
    """ Image data transformation to 100 rectangular sections in 2-D array """
    # retrieve image from fnImageCaptureAndTransform()
    inputImageArray = fnImageCaptureAndTransform()
    # reorder values of images into rectangles 64x48 pixels and then into lists with 100x3072 values 
    dataSplit = np.hsplit(inputImageArray, 64)
    dataStack = np.stack(dataSplit, axis=0)
    dataResult = np.reshape(dataStack, (100,3072))

    """ Conversion 100 sections to 100 bit sequence """
    # give value 0 or 1 to image rectangle section and add to bitseq variable
    bitSeq = "" # 100-bit sequence
    for i in range(100):
        if np.count_nonzero(dataResult[i]) > 1:
            bitSeq += "1"
        else:
            bitSeq += "0"

    """ Convert 100-bit string to float """
    bitSeq = bitSeq.lstrip("0") # remove leading zeros
    bitSeqRev = bitSeq[::-1] # reverse bitSeq sequence
    
    intBitSeq = int(bitSeq, 2)
    intBitSeqRev = int(bitSeqRev, 2)
    if intBitSeq <= intBitSeqRev != 0:
        randNum = intBitSeq / intBitSeqRev
    elif intBitSeqRev < intBitSeq != 0:
        randNum = intBitSeqRev / intBitSeq
    else:
        randNum = 0
    
    return randNum


def fnRandNumGen(outType, inMin=0, inMax=100):
    """ Generate number of requested type """     
    if outType == "tf":
        outputResult = round(fnImageArrayToNumber())
    elif outType == "to1":
        outputResult = fnImageArrayToNumber()
    elif outType == "numflt" or outType == "numint":
        try:
            inMin = int(inMin)
            inMax = int(inMax)
        except:
            fnException("Incorrect min or/and max number!", 1)
        
        if inMax <= inMin:
           fnException("Min number is greater than or equal to max number!", 1)

        numMinMax = fnImageArrayToNumber()
        outputResult = ((inMax - inMin) * numMinMax) + inMin
        
        if outType == "numint":
            outputResult = round(outputResult)
    else:
        fnException("Incorrect output option in the script argument!", 1)
            
    return outputResult


def fnException(excMsg, prtHelp):
    """ Exception print with short help manual """
    print(excMsg)
    if prtHelp == 1:
        print("""AlphaRandom.py -o <tf|to1|numint|numflt> [-f <fromnumber> -t <tonumber>]
        Options:
        -h --help                        Show help.
        -o --out=<tf|to1|numint|numflt>  Choose output: 1=true/0=false|number to 1|integer|float
        -f --from=<fromnumber>           Integer min in range. Required for output numint/numflt
        -t --to=<tonumber>               Integer max in range. Required for output numint/numflt""")
    sys.exit(1)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:f:t:", ["help","out=","from=","to="])
    except getopt.GetoptError:
        fnException("Correct use of script is:", 1)

    # set default values
    outType = "to1"
    fromNum = 0
    toNum = 100
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            fnException("Correct use of script is:", 1)
        elif opt in ("-o", "--out"):
            outType = arg
        elif opt in ("-f", "--from"):
            fromNum = arg
        elif opt in ("-t", "--to"):
            toNum = arg

    if outType =="tf":
        outValue = fnRandNumGen(outType)
    elif outType =="to1":
        outValue = fnRandNumGen(outType)
    elif outType =="numint" or outType=="numflt":
            outValue = fnRandNumGen(outType, fromNum, toNum)
    else:
        fnException("Incorrect output option in the script argument!", 1)

    print (outValue)


if __name__ == "__main__":
    main()

