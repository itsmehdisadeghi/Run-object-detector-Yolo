import cv2

from ultralytics import YOLO

img = 'koko.jpg'
imag = cv2.imread(img)
image = cv2.resize(imag , (480 , 480))
cv2.imwrite('D:\GITHUB\Run object detector  Yolo' , image)
model = YOLO('../Yolo_Weights/yolov8l.pt')
result = model('koko.jpg' , show=True) 
cv2.waitKey(0)