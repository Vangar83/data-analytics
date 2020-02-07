import pandas as pd
import numpy as np
import xlrd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt


df = pd.read_excel('Sales Forecast.xlsx')



X = df['January'].values.reshape(-1,1)
y = df['January'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm

print(regressor.intercept_)

print(regressor.coef_)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

print(df)
