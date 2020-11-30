import cv2 as cv

#Resacle Image,Video,Live Video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions =(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#For Live Video Only
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

#Reading Image + Rescale
img = cv.imread('../Resources/Photos/cat.jpg')
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)


#Reading Video + Rescale
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    #Rescale performed
    frame_resized = rescaleFrame(frame,scale=0.2)
    cv.imshow('Video Resized',frame_resized)
    #

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)