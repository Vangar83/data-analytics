import pandas as pd
import numpy as np
import xlrd
from datetime import date
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_excel('Bookings.xlsx',index='Product Code')


#select columns required from dataframe
df = df[['Product Code', 'Product Name', 'Supplier', 'Cancellation Date']]

#filter between dates
df = df[(df['Cancellation Date'] > '2019-02-19') & (df['Cancellation Date'] <= '2019-09-19')]

#groupby and aggregation
df = df.groupby('Product Code').agg({'Product Name':'first','City':'first','Cancellation Date':'count'}).reset_index()

#sorting
df=df.sort_values('Cancellation Date',ascending=False)

#rename column
df.rename(columns={'Cancellation Date': 'Cancellations'},inplace=True)

df1 = df.head(10)

print (df1)

df1.to_csv('Test.csv')

#single plot with matplotlib
plt.plot(df1.City , df1.Cancellations)
plt.xlabel('Cities')
plt.ylabel('No of Cancellations')

plt.plot()
plt.show()

