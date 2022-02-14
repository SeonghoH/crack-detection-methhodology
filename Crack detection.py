import cv2
import numpy as np


#cracktrained = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cracktrained = cv2.CascadeClassifier('cascade6.xml')

#image = cv2.imread('facetest.jpg')
image = cv2.imread('5.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cracks = cracktrained.detectMultiScale(gray,
         scaleFactor=1.1,
         minNeighbors=4,
         minSize=(3,3),
         maxSize=(5,5))

for (x,y,w,h) in cracks:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',image)
cv2.imwrite('image1.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows
