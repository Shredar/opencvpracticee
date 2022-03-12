import cv2
import numpy as np

img1 = cv2.imread("D:/pics/spaniel.jpg")
img2 = cv2.imread("D:/pics/golden.jpg")

width,height = 480,720
pts1 = np.float32([[214,61],[592,60],[195,379],[603,380]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img1,matrix,(width,height))

width,height = 635,640
pts3 = np.float32([[318,69],[548,63],[331,270],[564,282]])
pts4 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts3,pts4)
imgOutput2 = cv2.warpPerspective(img2,matrix,(width,height))



cv2.imshow("image",img1)
cv2.imshow("image1",img2)
cv2.imshow("output",imgOutput)
cv2.imshow("output2",imgOutput2)
cv2.waitKey(0)

