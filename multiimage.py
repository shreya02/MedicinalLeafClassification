import numpy as np
import pandas as pd
import cv2
ss="C:/Users/HP/Desktop/MLPROJECT/Grey"
r=1
df=pd.DataFrame()
for r in range(30):
    t=str(r)
    fullpath=ss+t+".jpg"
    img = cv2.imread(fullpath)
    abc = np.array(img)
    a=[]
    b=[]
    c=[]
    for i in range(len(abc)):
        for j in range(len(abc[0])):
             a.append(abc[i][j][0])
             b.append(abc[i][j][1])
             c.append(abc[i][j][2])
    df[str(r)]=a
    df[str(r+1)]=b
    df[str(r+2)]=c
print(df)
