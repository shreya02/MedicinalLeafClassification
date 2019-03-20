import cv2

img = cv2.imread('C:/Users/HP/Desktop/LEAVES11/60.PNG',0)  #pass 0 to convert into gray level 
ret,thr = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('win1', thr)
cv2.waitKey(0)  
cv2.destroyAllWindows()