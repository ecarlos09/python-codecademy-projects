hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Define a total price of all haircuts
total_price = 0

# Calculate the total price by looping through prices
for p in prices:
  total_price += p
print(total_price, "\n")

# Calculate average price
average_price = total_price / len(prices)
print("Average Haircut Price: $", round(average_price, 2), "\n")

# Amend prices:
new_prices = [p - 5 for p in prices]
print(new_prices, "\n")

# Define a total revenue from last week
total_revenue = 0

# Calculate last week's revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print('Total Revenue: ${:,.2f}'.format(total_revenue), "\n")

# Calculate average daily revenue from last week
average_daily_revenue = total_revenue/7
print("Average Daily Revenue: ${:,.2f}".format(average_daily_revenue), "\n")

# Filter out haircuts that cost more than 30 dollars under new pricing scheme
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
