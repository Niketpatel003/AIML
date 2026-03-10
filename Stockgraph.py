import random
import matplotlib.pyplot as plt

days = list(range(1,31))
stock_prices = [random.randint(100,500) for _ in range(30)]
max_price = max(stock_prices)
max_day = days[stock_prices.index(max_price)]
plt.plot(days, stock_prices, label="Stock Price")
plt.scatter(max_day, max_price, color='red', s=100, label="Highest Price")
plt.xlabel("Days")
plt.ylabel("Stock Price ($)")
plt.title("30 Day Stock Price Graph")
plt.legend()
plt.grid(True)
plt.show()