import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
blank = np.zeros((img.shape[0],img.shape[1]), dtype='uint8')

b ,g ,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,red])

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge = cv.merge([b,g,r])
cv.imshow('merged',merge)

cv.waitKey(0)