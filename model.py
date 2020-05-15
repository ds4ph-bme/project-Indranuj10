# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:47:02 2020

@author: INDRANUJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.metrics import mean_squared_error

df=pd.read_csv('Housing_data.csv')

X=df.drop('MEDV  ',axis=1)
y=df['MEDV  ']

X_train,X_test,y_train,y_test=train_test_split(X,y, stratify=df['CHAS'],test_size=0.2,random_state=1234)

X_final=X_train[['LSTAT','DIS ','NOX','RM ','CRIM','AGE ','PTRATIO','B ','TAX']]

model=RandomForestRegressor(random_state=1234)

model.fit(X_final,y_train)

pickle.dump(model,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))


