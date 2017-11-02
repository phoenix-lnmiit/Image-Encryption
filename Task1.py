import cv2
img = cv2.imread('goku.jpg')                #Read an image
cv2.imshow('image',img)                     #Display image
cv2.waitKey()
cv2.destroyAllWindows()
