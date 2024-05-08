import cv2

import numpy as np

# Read the image in BGR format

img_path = "F:\python\cap.jpg"

img = cv2.imread(img_path, 1)

if img is None:

 print(f"Error: Unable to read image file '{img_path}'")

 exit()

# Convert the image from BGR to RGB format

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define the kernel

kernel = np.ones((5, 5), dtype="uint8")

# Apply erosion and dilation filters

img_erosion = cv2.erode(img, kernel, iterations=1)

img_dilation = cv2.dilate(img, kernel, iterations=1)

# Display the original and filtered images

cv2.imshow("input", img)

cv2.imshow("erosion", img_erosion)

cv2.imshow("dilation", img_dilation)

# Wait for the user to press any key before closing the windows

cv2.waitKey(0)
