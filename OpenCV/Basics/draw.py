import cv2 as cv

import numpy as np

print(np.zeros((4,2,3), dtype='uint8'))

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

# 1 . paint the image a certain colour
# blank[235:431,180:300] = 0,0,255
# cv.imshow('Red',blank)


# 2. Draw a Rectangle 
# cv.rectangle(blank, (250,250), (blank.shape[1]//2+200,blank.shape[0]//2+200), (0,255,0), thickness=-1)
# cv.imshow('Rectangle' , blank)

# 3. Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),5,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)
 
# 4. Draw a line
# cv.line(blank,(100,0),(blank.shape[1]//2,0),(255,255,255),thickness=5)
# cv.imshow('Line',blank)

cv.putText(blank, 'My name is marcdewa1111',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),2)
cv.imshow('Text',blank)

cv.waitKey(0)