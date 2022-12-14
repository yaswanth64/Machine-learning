# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xsvX24WfxaBi3aj58pOGWCdplUuqxgya
"""

import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as mlp
import seaborn as sb
import sklearn as sk

from google.colab import files
uploaded=files.upload()

mynet=pd.read_csv("Salary_Data.csv")
mynet

mynet.head()

mynet

mlp.scatter(m_train,n_train,color='red')
mlp.plot(m_train,regressor.predict(m_train),color='blue')
mlp.title("Salary vs Experience (Training set)")

mlp.xlabel("Years of experience")
mlp.ylabel("Salaries")
mlp.show()

m=mynet.iloc[:, :-1].values
n=mynet.iloc[:,1].values

from sklearn.model_selection import train_test_split
m_train,m_test,n_train,n_test=train_test_split(m,n,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(m_train,n_train)

n_pred=regressor.predict(m_test)
n_pred
