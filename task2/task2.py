import cv2

img = cv2.imread('/home/aashish/Downloads/wall-e.jpg',cv2.IMREAD_GRAYSCALE)

matrix = img[0:, 0:]
print(matrix)

img[0:, 0:] = 2*matrix

cv2.imshow('InputImage', img)
cv2.imwrite('outputImage.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
