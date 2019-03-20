import cv2
import numpy as np
import pandas as pd
import glob
path="C:/Users/HP/Desktop/MLPROJECT/Grey/*.*"
for file in glob.glob(path):
    #print(file)
    a=cv2.imread(file)
    #print(a)
    img_data = np.asarray(a)
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
            df.to_csv('C:/Users/HP/Desktop/MLPROJECT/new matrix.csv',index=None)

