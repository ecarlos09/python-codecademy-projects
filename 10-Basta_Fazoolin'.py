# Create menu class
class Menu:

  # Define constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  # Define string representation of class
  def __repr__(self):
    start_time_formatted = None
    end_time_formatted = None
    if self.start_time > 1200:
      start_time_formatted = f"{self.start_time/100-12}pm"
    else:
      start_time_formatted = f"{self.start_time/100}am"
    if self.start_time > 1200:
      end_time_formatted = f"{self.end_time/100-12}pm"
    else:
      end_time_formatted = f"{self.end_time/100}am"
    return f"You are viewing our '{self.name}' menu, which is available from {start_time_formatted} until {end_time_formatted}."

  # Define bill calculation method
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
      total_bill += self.items[item]

    return "The total bill is £{:,.2f}.".format(total_bill)



# Create brunch menu
brunch = Menu(
  "Brunch",
  {
    'pancakes': 7.50, 
    'waffles': 9.00, 
    'burger': 11.00, 
    'home fries': 4.50, 
    'coffee': 1.50, 
    'espresso': 3.00, 
    'tea': 1.00, 
    'mimosa': 10.50, 
    'orange juice': 3.50
  },
  1100,
  1600
)

# Create ealry bird menu
early_bird = Menu(
  "Early-bird",
  {
    'salumeria plate': 8.00, 
    'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 
    'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 1.50, 
    'espresso': 3.00
  },
  1500,
  1800
)

# Create dinner menu
dinner = Menu(
  "Dinner",
  {
    'crostini with eggplant caponata': 13.00, 
    'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 
    'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 2.00, 
    'espresso': 3.00
  },
  1700,
  2300
)

# Create kids menu
kids = Menu(
  "Kids",
  {
    'chicken nuggets': 6.50, 
    'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
  },
  1100,
  2100
)

## Test string representation of class instances
# print(brunch)
# print(early_bird)
# print(kids)
# print(dinner)


# ## Test calculate_bill method

# #brunch purchase
# purchase1 = ["pancakes", "home fries", "coffee"]
# print(brunch.calculate_bill(purchase1))

# #early-bird purchase
# purchase2 = [
#   "salumeria plate", 
#   'mushroom ravioli (vegan)'
# ]
# print(early_bird.calculate_bill(purchase2))


## Creating the Franchises

class Franchise:
  
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"Welcome to Basta Fazoolin' at {self.address}!"

  def available_menus(self, time):
    valid_menus = []
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if 
    converted_time_str = ""
    for char in time:
      if char in "".join(digits):
        converted_time_str = converted_time_str + char
    converted_time = int(converted_time_str)*100
    for menu in self.menus:
      if converted_time >= menu.start_time and converted_time <= menu.end_time:
        valid_menus.append(menu.name)
    return f"Here are the available menus for {time}: {valid_menus}"



# Create flagship store
original_menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", original_menus)
new_installment = Franchise("12 East Mulberry Street", original_menus)

# Test string represnetation of both franchise stores
# print(flagship_store)
# print(new_installment)

# Test available menus method
print(flagship_store.available_menus("12 noon"))
print(flagship_store.available_menus("5pm"))
