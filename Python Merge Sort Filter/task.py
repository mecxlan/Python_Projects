#Author: [Muhammad Arslan](https://www.linkedin.com/in/mecxlan/)
'''
Python Pandas: Merge Sort Filter
Application memory space using python

Install required packages 
'''
import pandas as pd
import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt

# 1. Read the data into Pandas DataFrames
df_temp = pd.read_csv(r'tempYearly.csv')
df_rain = pd.read_csv(r'rainYearly.csv')

print(df_temp)
print(df_rain)

# 2. Use a filter to remove outliers in the data
# Pandas qurey method
df_temp_f = df_temp.query('Temperature < 40 & Temperature > 0')
print(df_temp_f)

df_rain_f = df_rain.query('Rainfall < 6 & Rainfall > 0')
print(df_temp_f)

# Scatter plot using seaborn
# df_temp_f.plot.scatter(x='Year', y='Temperature', label ='Temperature and Year')

# plt.show()

# df_rain_f.plot.scatter(x='Year', y='Rainfall', label='Rainfall and Year')

# plt.show()

# 3. Combine the data using Pandas Merge
# outer join the dataframes Nan includes
# inner remove the Nan
df_merge = pd.merge(df_temp_f, df_rain_f, on='Year', how='inner')
# print(df_merge.sort_values(by='Rainfall')) # Sort the data by rainfall and temperature

# 4. Sort the data of temperature in descending order
print(df_merge.sort_values(by='Temperature', ascending=False))

# 5. Use the Seaborn package to create a regression plot
sns.set(rc={'figure.figsize':(12,6)})

sns.jointplot(x ='Rainfall', y = 'Temperature', data = df_merge, kind = 'reg')

plt.show()

# Link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html