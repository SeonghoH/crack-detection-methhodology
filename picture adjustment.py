import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt
import os 

from skimage.filters import threshold_mean, threshold_otsu, threshold_local, threshold_minimum
from skimage import data, color
from skimage.morphology import skeletonize, remove_small_objects
from skimage.filters import try_all_threshold
from skimage import io
from skimage.util import invert
negrobajo1 = np.array([0, 0, 0],np.uint8)
negroalto1 = np.array([0, 0, 100],np.uint8)
negrobajo2 = np.array([250, 0, 40],np.uint8)
negroalto2 = np.array([250, 100, 40],np.uint8)

imagen = cv2.imread('Cracked_01.jpg')
gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray1',gray)
cv2.imwrite('1.jpg', gray)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.imshow('gray2',gray)
cv2.imwrite('2.jpg', gray)
hsv = cv2.cvtColor(gray, cv2.COLOR_BGR2HSV)
cv2.imshow('gray3',hsv)
cv2.imwrite('3.jpg', hsv)
#cv2.waitKey(0)

masknegro1 = cv2.inRange(hsv, negrobajo1, negroalto1)
masknegro2 = cv2.inRange(hsv, negrobajo2, negroalto2)
mask = cv2.add(masknegro1,masknegro2)
cv2.imshow('gray4',mask)
cv2.imwrite('4.jpg',mask)
#blur =cv2.medianBlur(mask, 7)
blur = cv2.blur(mask,(3,3))
cv2.imshow('gray5',blur)
cv2.imwrite('5.jpg', blur)
cv2.waitKey(0)
img_log = (np.log(blur+1)/(np.log(1+np.max(blur))))*255
img_log = np.array(img_log,dtype=np.uint8)
cv2.imshow('gray6',img_log)
cv2.imwrite('6.jpg',img_log)
cv2.imshow('gray7',blur)
cv2.imwrite('7.jpg', blur)
cv2.waitKey(0)
bilateral = cv2.bilateralFilter(img_log, 5, 75, 75)
cv2.imshow('gray8',bilateral)
cv2.imwrite('8.jpg', bilateral)
cv2.waitKey(0)
edges = cv2.Canny(bilateral,100,200)
cv2.imshow('gray9',edges)
cv2.imwrite('9.jpg', edges)
cv2.waitKey(0)
#_,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

#Para versiones OpenCV4:
contornos,hierarchy = cv2.findContours(edges, cv2.RETR_LIST,
           cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(imagen,contornos, -1, (0,0,255), 2)
perimeter=0
print ('hierarchy=',hierarchy)
for i in range (len(contornos)):
  cv2.drawContours(imagen, contornos, i, (0,255,0), 2)
  #cv2.imshow('imagen',imagen)
  #cv2.waitKey(0)
  perimeter= perimeter + cv2.arcLength(contornos[i],False)
#cv2.imshow('gray',imagen)

print ('perimeter=',perimeter/2)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('gray10',imagen)
cv2.imwrite('10.jpg', imagen)
cv2.waitKey(0)

# Invert the horse image
#image = invert(blur)
# perform skeletonization
#skeleton = skeletonize(blur)


# display results
#fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
#                         sharex=True, sharey=True)

#ax = axes.ravel()

#ax[0].imshow(image, cmap=plt.cm.gray)
#ax[0].axis('off')
#ax[0].set_title('original', fontsize=20)

#ax[1].imshow(skeleton, cmap=plt.cm.gray)
#ax[1].axis('off')
#ax[1].set_title('skeleton', fontsize=20)

#fig.tight_layout()
#plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows


cv2.destroyAllWindows()
