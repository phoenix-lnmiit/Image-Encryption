import cv2

img = cv2.imread('E:/OpenCV/Images/maxresdefault.jpg')  #path and name of the image
cv2.imshow('ImageWindow', img)
cv2.waitKey()
