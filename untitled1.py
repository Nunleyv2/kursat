import cv2

import numpy as np

width,height=800,600

black_canvas=np.zeros((width,height,3),dtype=np.uint8)+255

cv2.line(black_canvas,(50,50),(200,50),(0,0,0),5)

cv2.imshow("pencere",black_canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()