import numpy as np
import cv2

img = cv2.imread('Shubhipic.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() # If 0 is passed, it waits indefinitely for a key stroke.
