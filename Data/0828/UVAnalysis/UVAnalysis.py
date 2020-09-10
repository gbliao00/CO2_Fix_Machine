import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = open('UV.txt', 'r')          # Open file
column0=[]                       # Data of time
columnT=[]
column1=[]                       # Data of UV300
column2=[]                       # Data of UV340


for line in iter(f):
    data=line.split()            # Data 用 space 隔開
    str0=float(data[5])          # Time (Sec)
    str1=float(data[2])          
    str2=float(data[1])

    column0.append(str0)         # Data of Time
    column1.append(str1)         # Data of UV300
    column2.append(str2)         # Data of UV340

T=column0[0]
print(T)

for line in column0:
    columnT.append(line-T)       # Data of Time from 0

df0=pd.DataFrame(columnT,column0)
df=pd.DataFrame(column1,column0)
df1=pd.DataFrame(column2,column0)
df2=pd.concat([df0,df,df1],axis=1)



df2.to_excel('UV.xlsx')
print(df2)
print('OK')
