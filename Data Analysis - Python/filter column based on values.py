import numpy as np
import pandas as pd

client = pd.read_csv('Customers.csv')

cities = client[client['CITY_NAME'].isin(['Tokyo', 'London'])]


print(cities)

cities.to_csv('Top_Cities.csv')

