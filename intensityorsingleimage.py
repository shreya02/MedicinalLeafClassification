import cv2
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

#path='C:/Users/HP/Desktop/MLPROJECT/Grey'
images=[]
#for imagepath in os.listdir(path):
paths="C:/Users/HP/Desktop/MLPROJECT/Grey/"
for r in range(3):
   t=str(r)
   full=t+".jpg"
   fullpath=paths+full
  # img=mpimg.imread(fullpath)
   img=cv2.imread(fullpath)
   plt.imshow(img)
   #im=Image.open(fullpath)
   #im.show()