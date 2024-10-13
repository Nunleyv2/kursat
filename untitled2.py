import cv2

import numpy as np

width,height=800,600

black_canvas=np.zeros((width,height,3),dtype=np.uint8)*255

cv2.rectangle(black_canvas,(150,100), (400,400), (242,152,235),-1)
cv2.imshow("pencere",black_canvas)

cv2.waitKey(0)

cv2.destroyAllWindows()
