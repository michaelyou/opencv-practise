import numpy as np
import cv2

image = cv2.imread('image/dinosaur.jpg')
cv2.imshow("Original", image)

cropped = image[30:120, 240:335]
cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)
