import pandas as pd

df = pd.read_csv('Sales.csv')

df['Revenue'] = df['Quantity'] * df['Price']

total_revenue_pp = df.groupby('Product')['Revenue'].sum()

print("Total revenue per product:\n")
print(total_revenue_pp)
