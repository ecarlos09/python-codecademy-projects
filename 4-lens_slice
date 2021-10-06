# List of pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# List of pizza slice prices
prices = [2, 6, 1, 3, 2, 7, 2]
# Counting number of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# Finding total number of toppings
num_pizzas = len(toppings)
print(f'We sell {num_pizzas} different kinds of pizza!')
# Creating a 2D list
pizza_and_prices = []
for x in range(len(prices)):
  price = prices[x]
  topping = toppings[x]
  pizza_and_prices.append([price, topping])
print(pizza_and_prices, "\n")
# Sort pizzas in order of increasing price
pizza_and_prices.sort()
print(pizza_and_prices, "\n")
# Find cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza, "\n")
# Find priciest pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza, "\n")
# Remove "anchovies from list"
pizza_and_prices.pop()
print(pizza_and_prices, "\n")
# Add new topping
new_topping = [ 2.5, "peppers"]
pizza_and_prices.insert(4, new_topping)
print(pizza_and_prices, "\n")
# Find cheapest three pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest, "\n")
