#importing necessary libraries
import cv2
import numpy as np 

#Reading the image and its matrix
img = cv2.imread('messi.jpg',cv2.IMREAD_GRAYSCALE)
m = img[0:,0:]
print(m)
img[0:,0:] = 2*m

#Show and save the image
cv2.imshow('new_image',img)
cv2.imwrite('output_image.jpg',img)

#exit the code
cv2.waitKey(0)
cv2.destroyAllWindows()

