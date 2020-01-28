import pandas as pd
import numpy as np

df = pd.read_excel('Sales.xlsx')


df['Rank'] = df['Total Sales'].rank(method='dense', ascending=False)

print(df)

df.to_excel('Rank.xlsx')




