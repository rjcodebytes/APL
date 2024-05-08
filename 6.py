import cv2

from matplotlib import pyplot as p 

image=cv2.imread("cap.jpg",0)

cv2.imshow("dshashira.jpg",image)

Hist=cv2.calcHist([image],[], None, [256], [0,256])

p.plot (Hist,color="r")

p.show()
