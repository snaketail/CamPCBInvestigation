# Importing the Opencv2 library
import cv2
import numpy as np
import matplotlib.pyplot as plt

from ImgReg import alignImages

# Reading the image using imread() function
img1loc = "C:\\Users\\yuhu0001.KEYSIGHT\\OneDrive - Keysight Technologies\\Harry\\__Projects\\[[[Temp]]]\\Python\\img1.jpg"
img2loc = "C:\\Users\\yuhu0001.KEYSIGHT\\OneDrive - Keysight Technologies\\Harry\\__Projects\\[[[Temp]]]\\Python\\img2.jpg"
#img1loc = "C:\\Users\\yuhu0001.KEYSIGHT\\OneDrive - Keysight Technologies\\Harry\\__Projects\\[[[Temp]]]\\Python\\p1.png"
#img2loc = "C:\\Users\\yuhu0001.KEYSIGHT\\OneDrive - Keysight Technologies\\Harry\\__Projects\\[[[Temp]]]\\Python\\p2.png"
image1 = cv2.imread(img1loc)
image2 = cv2.imread(img2loc)

  
# Extracting the height and width of an image
h1, w1 = image1.shape[:2]

# Displaying the height and width
print("Height = {},  Width = {}".format(h1, w1))

# Extracting the height and width of an image
h2, w2 = image2.shape[:2]

# Displaying the height and width
print("Height = {},  Width = {}".format(h2, w2))

im1 = cv2.resize(image1, (960, 720))
#im1 = image1
#im2 = image2
cv2.imshow('image1',im1)

im2 = cv2.resize(image2, (960, 720))

cv2.imwrite("im2reg.jpg", im2)
cv2.imshow('image2',im2)

im1reg, h = alignImages(im1, im2)

cv2.imwrite("im1reg.jpg", im1reg)

cv2.imshow('im1reg',im1reg)

# Extracting the height and width of an image
hreg, wreg = im1reg.shape[:2]

# Displaying the height and width
print("Height = {},  Width = {}".format(hreg, wreg))

cv2.waitKey(0)