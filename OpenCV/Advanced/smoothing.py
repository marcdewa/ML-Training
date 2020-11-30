import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

# Averaging

average = cv.blur(img,(3,3))
cv.imshow('Average',average)

#Gaussina Blur

gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian',gaussian)

# Median blur
median = cv.medianBlur(img,3)
cv.imshow('Median',median)

# Bilateral
bilateral = cv.bilateralFilter(img , 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)