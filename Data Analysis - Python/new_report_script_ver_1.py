import pandas as pd
import numpy as np
import xlrd

# Import csvs & xlsx
client = pd.read_csv('client.csv', index_col='PRODUCT ID')
observe = pd.read_csv('Observe.csv', index_col='PRODUCT ID')
avail = pd.read_excel('Avail.xlsx', index_col='PRODUCT ID')
sales = pd.read_excel('Sales.xlsx', index_col='PRODUCT ID')

# Merging and sorting
df = client.merge(observe,on='PRODUCT ID', how='left', indicator=True)
df['Observation'].replace('', np.nan, inplace=True)
df['Observation'] = df['Observation'].fillna(-1).astype(int)
df = df.sort_values(['Observation'], ascending=True)
df = df[df['Observation'] == -1]
df= df.dropna(subset=['Observation'])


print(df)
df.to_csv('Temp.csv', index=True)


df2 = df.merge(avail,on='PRODUCT ID', how='left')
df2 = df2.sort_values(['avail'], ascending=False)
df2['avail'].replace('', np.nan, inplace=True)
df2.dropna(subset=['avail'], inplace=True)
df2 = df2[(df2['avail'] >= 0.4) & (df2['avail'] <= 1.0)]



df3 = df2.merge(rev,on='PRODUCT ID', how='left')
df3 = df3.sort_values(['Revenue'], ascending = False)
df3.groupby(['avail','Sales']).size().sort_values()
df3= df3.dropna(subset=['Revenue'])
df3.drop(['Observation','_merge','avail','Sales'], axis=1, inplace=True)
df3 = df3.head(500)


# Export to csv
df3.to_csv('client_report.csv', index=True)






