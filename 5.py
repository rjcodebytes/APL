import cv2 

import numpy as np

img=cv2.imread("cap.jpg")

dst=cv2.fastNlMeansDenoisingColored(img,None,10,10,7,20)

cv2.imshow("original_image",img)

cv2.imshow("denoisng_image",dst)
