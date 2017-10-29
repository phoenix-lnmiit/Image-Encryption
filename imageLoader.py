import cv2

img = cv2.imread('E:/OpenCV/Images/maxresdefault.jpg')  #path and name of the image

#To choose a pixel with co-ordinates (x,y) type 
#px = img[x][y]

cv2.imshow('ImageWindow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
