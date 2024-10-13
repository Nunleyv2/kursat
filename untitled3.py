import cv2

import numpy as np

width,height=800,600

black_canvas=np.zeros((width,height,3),dtype=np.uint8)*255

text="hello"
org=(50,50)
font=cv2.FONT_HERSHEY_DUPLEX
font_scale=1.5
color=(234,223,123)
thickness=5
line_aa=cv2.LINE_AA

cv2.putText(black_canvas,text,org,font,font_scale,(123,234,200),thickness,line_aa)

cv2.imshow("pencere",black_canvas)

cv2.waitKey(0)

cv2.destroyAllWindows()