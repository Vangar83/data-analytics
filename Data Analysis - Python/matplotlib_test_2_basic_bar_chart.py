import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



#import excel

data = pd.read_excel('chart_for_matplotlib_test.xlsx')

plt.bar(data.Month , data.A2016)
plt.bar(data.Month , data.B2017)
plt.bar(data.Month , data.C2018)
plt.bar(data.Month , data.Forecasting2019)
plt.bar(data.Month , data.Actual2019)

plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales by month')
plt.legend(loc='upper left')


plt.plot()

plt.show()
