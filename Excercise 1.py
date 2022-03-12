import cv2

img = cv2.imread("D:/pics/spaniel.jpg")
img2 = cv2.imread("D:/pics/golden.jpg")
#print(img.shape)
#print(img2.shape)
H,W,D = img.shape
H1,W2,D3 = img2.shape

print("Width={},Height={},Depth={}".format(H,W,D))
print("Width1={},Height1={},Depth1={}".format(H1,W2,D3))


cv2.imshow("Size",img)

cv2.imshow("size2",img2)

cv2.waitKey(0)