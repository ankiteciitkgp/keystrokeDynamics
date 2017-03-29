# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:53:58 2015

@author: Naman
"""

import pandas as pd


df1=pd.read_csv('final_mean_Raunak.csv')
df1=df1.drop('index',axis=1)
df2=pd.read_csv('final_mean_Amrut.csv')
df2=df2.drop('index',axis=1)
df3=pd.read_csv('final_mean_Vikram.csv')
df3=df3.drop('index',axis=1)
df4=pd.read_csv('final_mean_Ankit.csv')
df4=df4.drop('index',axis=1)

df5=pd.read_csv('final_mean_Naman.csv')
df5=df5.drop('index',axis=1)

df=df1.append(df2,ignore_index=True)
df=df.append(df3,ignore_index=True)
df=df.append(df4,ignore_index=True)

df=df.append(df5,ignore_index=True)

df1=df[['lr','rl','Lr','Rl','ll','rr','l','r','L','R','Space','Enter','cpm','y']]

df1.to_csv('data_final.csv',index=False)