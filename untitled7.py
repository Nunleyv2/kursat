import cv2
img_path="yüz.jpg"

cascade_path=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
face_cascade=cv2.CascadeClassifier(cascade_path)

cascade_eye_path=cv2.data.haarcascades+"haarcascade_eye.xml"
eye_cascade=cv2.CascadeClassifier(cascade_eye_path)

img=cv2.imread(img_path)

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=gray[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.1,minNeighbors=5)
cv2.imshow("asd",img)
cv2.waitKey(0)