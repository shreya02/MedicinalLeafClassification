import cv2 
image=cv2.imread('C:/Users/HP/Desktop/LEAVES11/60.PNG')
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Original image', image) 
cv2.imshow('Gray Image',gray) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

