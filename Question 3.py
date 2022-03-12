import cv2
import numpy as np

img1 = cv2.imread("D:/pics/spaniel.jpg")
img2 = cv2.imread("D:/pics/golden.jpg")
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))

image = cv2.add(img1,img2)

cv2.imshow("image",image)


cv2.waitKey(0)