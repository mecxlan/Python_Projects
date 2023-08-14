# Merge Sort & Filter
* Libraries Used
  * `pandas` - read DataFrames 
  * `matplotlib`- `pyplot` - 
  * `seaborn`
  
Two different documents - Yearly data: rainYearly.csv and tempYearly.csv`
_Filter_ the _DataFrames_ based on certain criteria.
* pandas `query()` method for removing outliers 

Merge the two dataframes.
* `pd.merge(df_var1, df_var2, on = 'Year', how = 'outer '` outer involves `Nan`
  
Sort the merged dataframes, first by rainfall, then by temperature.
`var.sort_values(by = 'column_name', ascending = 'bool' )`

Call the function to plot the merged data: rainfall vs temperature.
* `kind = reg` seaborn joint regression plot
