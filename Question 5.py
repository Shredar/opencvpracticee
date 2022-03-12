import cv2


img1 = cv2.imread("D:/pics/spaniel.jpg")
imgGray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2 = cv2.imread("D:/pics/golden.jpg")
imgGray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))

#cv2.imshow("Size",img1)
cv2.imshow("Sizeee",imgGray1)
cv2.imshow("Sizee",imgGray2)

#cv2.imshow("size2",img2)

cv2.waitKey(0)