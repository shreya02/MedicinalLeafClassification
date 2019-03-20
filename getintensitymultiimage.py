import numpy as np
import pandas as pd
import cv2
#import os
#import glob
from PIL import Image
#img_dir = "C:/Users/HP/Desktop/Grey"  
#data_path = os.path.join(img_dir,'*g')
#files = glob.glob(data_path)
#data = []
#for f1 in files:
 #3   img = cv2.imread(f1)
   # data.append(img)    
img = cv2.imread('C:/Users/HP/Desktop/LEAVES11/60.PNG',0) 
img_data = np.asarray(img)
#print(img_data[1][1][1])
a=[]
b=[]
c=[]
for i in range(len(img_data)):
 for j in range(len(img_data[0])):
     a.append(img_data[i][j][0])
     b.append(img_data[i][j][1])
     c.append(img_data[i][j][2])
df=pd.DataFrame()
df['a']=a
df['b']=b
df['c']=c
df.to_csv('C:/Users/HP/Desktop/MLPROJECT/hi.csv',index=None)

#print(a)
#print(b)
#print(c)      
#ser=pd.Series([a,b,c])
#print(ser)
#datas = pd.DataFrame(ser)
#print(datas)
