# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:05:10 2020

@author: MDhamani
"""
import pandas as pd
vlx = []
data1 = pd.read_csv("newdata1.csv",header=None)#key-value pairs csv
data2 = pd.read_csv("cnewdata2.csv",header=None)#csv file for changes
new_col = data2.shape
new_col = new_col[1]
data2.insert(new_col,str(new_col),None)
#print(data1)
#print(data2)
key = data1.iloc[:,0:1]
#print(key[0][1])
value = data1.iloc[:,1:]
#print(value[1][0])
#an = data1.count()
for i in range(0,len(key)):
    val = value[1][i]
    val[1:-1]
    vlx.append(val[1:-1])

#%%
for xkey in range(0,len(key)):#key:
    temp = []
    temp = vlx[xkey]
    tt = temp.split(" ")
    print(tt)
    for xval in tt:
        print(xval)
        row = (data2.loc[int(xval),:])
        print(row)
        r = row.isnull()
        for f in range(0,len(r)-1):
            if r[f] == True:
                TF = int(f)
                print(TF)
                break
            else:
                continue
        print(row[TF])
        row[TF] = int(xkey)
        data2.loc[int(xval),:] = row
