# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:43:50 2015

@author: Naman
"""

import pandas as pd
from sklearn.externals import joblib


#Feature Extraction part
#Output - array of input (n,N_features)
X_test=pd.read_csv('test_Amrut.csv',header=0)  #test file


X_test=X_test[['lr','rl','Lr','Rl','ll','rr','l','r','L','R','Space','Enter','cpm']]
X_test=X_test.values
GMM_classifier=joblib.load('GMMclassifier.pkl')
y_test=GMM_classifier.predict(X_test)

Person={0:'Raunak',1:'Amrut',2:'Vikram',3:'Ankit',4:'Naman'}

y_test_length=len(y_test)
y_=y_test.tolist()
mode=max(set(y_), key=y_.count)
frequency=y_.count(mode)
accuracy=float(frequency)/len(y_)*100

if  accuracy > 60:
    print "The Person identified typing is ", Person[mode],"with",round(accuracy,2),'% accuracy'
else:
    print "Impostor!"
        
    