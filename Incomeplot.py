import random
import matplotlib.pyplot as plt

days = list(range(1,31))
incomes = [random.randint(1000,5000) for _ in range(30)]
expenses = [random.randint(500,5000) for _ in range(30)]
plt.plot(days, incomes, label="Income",color="green")
plt.plot(days, expenses, label="Expenses",color="red")
plt.xlabel("Day")
plt.ylabel("Amount ($)")
plt.title("30 Day Income and Expenses")
plt.legend()
plt.grid(True)
plt.show()
