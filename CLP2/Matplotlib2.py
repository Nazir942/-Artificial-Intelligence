import matplotlib.pyplot as plt
import numpy as np

regions = ['Central', 'North-East', 'South-West', 'West-Coast']
sales_revenue = [32000, 28000, 35000, 29000]

plt.bar(regions, sales_revenue, color='Green', width=0.6)
plt.title("Sales Revenue Across Different Regions")
plt.xlabel("Regions")
plt.ylabel("Sales Revenue (in $)")
plt.show()

