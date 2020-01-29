import pandas as pd
import numpy as np
import xlrd

client = pd.read_csv('ABCDE01.csv', index_col = 'PRODUCT ID')
pdata = pd.read_csv('InfoCSV.csv', index_col = 'PRODUCT ID')
observe = pd.read_csv('Observation.csv', index_col = 'PRODUCT ID')



df = observe.merge(client,on='PRODUCT ID', how = 'left', indicator=True)
df = df.sort_values(by = ['_merge', 'Observation'],ascending = [True, False])
df = df[df._merge !='both']

df.drop(df.iloc[:, 1:14], inplace = True, axis = 1) 


df1 = pd.merge(df,pdata[['PRODUCT NAME', 'CITY NAME','COUNTRY NAME']], on = 'PRODUCT ID', how = 'left')
df1.dropna(subset=['PRODUCT NAME'],inplace=True)



#print(df)

df1.to_csv('Test-Succesful.csv', index=True)
