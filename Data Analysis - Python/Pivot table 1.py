import pandas as pd
import numpy as np
from datetime import date
import xlrd

df = pd.read_excel('Monthly Sales.xlsx')

df = pd.pivot_table(df,index=["Customercode"], values=['Sales'],aggfunc=np.sum)


df.to_csv('Test_pivot.csv')


