import numpy as np
import matplotlib.pyplot as plt


days = [ 'Friday', 'Saturday', 'Sunday','Monday', 'Tuesday', 'Wednesday','Thursday']
temperatures = [18, 21, 19, 22, 24, 26, 25]


plt.plot(days, temperatures, marker='o', color='green', linestyle='-', linewidth=2, markersize=8)
plt.title("Temperature Variation Over a Week")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
