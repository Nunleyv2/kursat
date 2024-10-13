import cv2
import numpy as np

img_path="araba.jpg"

img=cv2.imread(img_path)

rgb_img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("sad",grey_img)

cv2.waitKey(0)