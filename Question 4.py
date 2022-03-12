import cv2


img1 = cv2.imread("D:/pics/spaniel.jpg")
img2 = cv2.imread("D:/pics/golden.jpg")
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))

cv2.imshow("Size",img1)

cv2.imshow("size2",img2)

cv2.waitKey(0)