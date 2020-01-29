import pandas as pd
import numpy as np
import xlrd
from datetime import date
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_excel('Properties.xlsx',index='Product ID')


#select columns required from dataframe
df = df[['Product ID', 'Product Name', 'Supplier', 'Date']]

#filter between dates
df = df[(df['Date'] > '2019-02-19') & (df['Date'] <= '2019-09-19')]

#groupby and aggregation
df = df.groupby('Product ID').agg({'Product Name':'first','City':'first','Date':'count'}).reset_index()

#sorting
df=df.sort_values('Date',ascending=False)

#rename column
df.rename(columns={'Date': 'New Date'},inplace=True)

df1 = df.head(10)

print (df1)

df1.to_csv('Test.csv')

#single plot with matplotlib
plt.plot(df1.City , df1.Cancellations)
plt.xlabel('Cities')
plt.ylabel('Dates')

plt.plot()
plt.show()

