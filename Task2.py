import cv2
img = cv2.imread('goku.jpg',cv2.IMREAD_GRAYSCALE)

iMatrix = img[0:,0:]
cv2.imwrite('goku1i.jpg',img)

img[0:,0:]=2*iMatrix
print(iMatrix)

cv2.imshow('image',img)
cv2.imwrite('goku2i.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()