import pandas as pd

df=pd.read_csv("sales_subset.csv")

# Print the head of the sales DataFrame
print("sales_subset".head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())