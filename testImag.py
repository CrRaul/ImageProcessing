import cv2 as cv
import numpy as np
import sys

opt = sys.argv[1]
inImg = sys.argv[2]
ouImg = sys.argv[3]

if not(opt == "-rot" or opt=="-swp" or opt=="-red"):
    print("error: command")
    quit()

try:
    im = cv.imread(inImg)
except:
    print("error: read image")
    quit()

shape = im.shape
print(shape)

im2 = np.zeros((shape[0],shape[1],shape[2]), np.uint8)

if opt == "-rot":
    for i in range(0,shape[0]):
        for j in range(0,shape[1]):
            for k in range(0,shape[2]):
                im2.itemset((i,shape[1]-j-1,k),(im.item(i,j,k)))
            
            if opt == "-red":
                R = im.item(i,j,0)
                G = im.item(i,j,1)
                B = im.item(i,j,2)
                
                r = R * 1.5
                if r > 255: 
                    r = 255
                r = int(r)
                im2.itemset((i, j, 0), r)
                im2.itemset((i, k, 1), G//2)
                im2.itemset((i, j, 2), B//2)
if opt == "-swp":
    for i in range(0,shape[0]):
        for j in range(0, shape[1]):
            im2.itemset((i,j,0),im.item((i,j,2)))
            im2.itemset((i,j,1),im.item((i,j,1)))
            im2.itemset((i,j,2),im.item((i,j,0)))

if opt == "-red":
    for i in range(0,shape[0]):
        for j in range(0, shape[1]):
            R = im.item(i,j,0)
            G = im.item(i,j,1)
            B = im.item(i,j,2)
                                
            r = R * 1.5   
            if r > 255:
                r = 255 
            r = int(r)
            im2.itemset((i, j, 0), r)
            im2.itemset((i, j, 1), G//2)
            im2.itemset((i, j, 2), B//2)

try:
    cv.imwrite(ouImg,im2)
except:
    print("error: write image")


