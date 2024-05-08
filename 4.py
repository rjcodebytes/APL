import cv2

import numpy

def nothing(x):

 pass

# Creating a window with black image

img = numpy.zeros((512, 512, 3), numpy.uint8)

cv2.namedWindow('image')

# creating trackbars for red, blue, green color change 

cv2.createTrackbar ('R', 'image', 0, 255, nothing) 

cv2.createTrackbar ('G', 'image', 0, 255, nothing) 

cv2.createTrackbar ('B', 'image', 0, 255, nothing)

while (True):

 # show image

 cv2.imshow('image', img)

 

 # for button pressing and changing

 if cv2.waitKey (1) == 27:

 break

 

 # get current positions of all Three trackbars

 r = cv2.getTrackbarPos ('R', 'image')

 g = cv2.getTrackbarPos ('G', 'image')

 b = cv2.getTrackbarPos ('B', 'image')

 

 # display color mixture
img[:] = [b, g, r]

#close the window

cv2.destroyAllWindows ()
