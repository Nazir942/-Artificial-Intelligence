import numpy as np

x = np.random.randint(1, 20, size=(5, 5))
row_sums = np.sum(x, axis=1)

print("Matrix:\n", x)
print("\nRow-wise sums:", row_sums)
