import pandas as pd
import numpy as np

data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Quantity': [10, 5, np.nan, 8],
    'Price': [5.0, np.nan, 5.0, 8.0]
}

df = pd.DataFrame(data)
print("Original DataFrame with missing values:")
print(df)

df_filled = df.copy()
df_filled['Quantity'] = df_filled['Quantity'].fillna(df_filled['Quantity'].mean())
df_filled['Price'] = df_filled['Price'].fillna(df_filled['Price'].mean())

print("\nDataFrame after filling missing values with column-wise means:")
print(df_filled)
