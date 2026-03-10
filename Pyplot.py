import random
import matplotlib.pyplot as plt

days = list(range(1, 31))

temperatures = [random.randint(20, 40) for _ in range(30)]

max_temp = max(temperatures)
max_day = days[temperatures.index(max_temp)]

plt.plot(days, temperatures, marker='o', label="Temperature")

plt.scatter(max_day, max_temp, color='red', s=100, label="Highest Temperature")

plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("30 Day Temperature Graph")
plt.legend()

plt.grid(True)

plt.show()