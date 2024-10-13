import cv2

img_path="araba.jpg"

save_path="yeni_araba.jpg"

new_width=800
new_height=600
img=cv2.imread(img_path)
resized_image=cv2.resize(img ,(new_width,new_height))



cv2.imshow("pencere", img)

cv2.imshow("penceres", resized_image)


cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite(save_path, img)

print(f"dosya kaydedildi {save_path}")