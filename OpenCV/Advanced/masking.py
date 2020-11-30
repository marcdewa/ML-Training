import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats 2.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank',blank)

mask = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

print(img.shape)
print(mask.shape)

masking = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masking)

cv.waitKey(0)