import cv2

img=cv2.imread("araba.jpg")

roi=img[300:325,450:550]

cv2.imshow("araba",img)
cv2.imshow("roi",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()