import cv2
import numpy as np
from matplotlib import pyplot as plt
img= cv2.imread('C:/Users/HP/Desktop/Grey/60g.jpeg',0)
ret, thresh1= cv2.threshold(img,92,255,cv2.THRESH_BINARY)
cv2.imshow('GREY',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()