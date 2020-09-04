import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = open('UV.txt', 'r')          # Open file
column0=[]                       # Data of time
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


df=pd.DataFrame(column1,column0)
df1=pd.DataFrame(column2,column0)
df2=pd.concat([df,df1],axis=1)



df2.to_excel('UV.xlsx')
print(df2)
print('OK')
