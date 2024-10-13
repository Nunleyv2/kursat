import cv2

img_path="araba.jpg"

img=cv2.imread(img_path)

gaussian_blur=cv2.GaussianBlur(img, (15,15), 0)

#rotate=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("asd",gaussian_blur)

cv2.waitKey(0)