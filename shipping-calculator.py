weight = 4.8

# Ground shipping costs
if weight <= 2:
  gs_cost = weight*1.5 + 20
elif weight <= 6:
  gs_cost = weight*3 + 20
elif weight <= 10:
  gs_cost = weight*4 + 20
elif weight > 10:
  gs_cost = weight*4.75 + 20
else:
  gs_cost = "Error!"

# Ground shipping premium costs
gsp_cost = 125

# Drone shipping costs
if weight <= 2:
  drone_cost = weight*4.5
elif weight <= 6:
  drone_cost = weight*9
elif weight <= 10:
  drone_cost = weight*12
elif weight > 10:
  drone_cost = weight*14.25
else:
  drone_cost = "Error!"

# Calculate cheapest method
cost_list = [
  ["Ground Shipping", gs_cost], 
  ["Ground Shipping Premium", gsp_cost],
  ["Drone Shipping", drone_cost]
]
lowest_cost = gs_cost
cheapest_option= ""

for x in cost_list:
  if x[1] <= lowest_cost:
    lowest_cost = x[1];
    cheapest_option = x[0]

# Format costs
gs_cost = '${:,.2f}'.format(gs_cost)
gsp_cost = '${:,.2f}'.format(gsp_cost)
drone_cost = '${:,.2f}'.format(drone_cost)
lowest_cost = '${:,.2f}'.format(lowest_cost)

print(f"Ground shipping for your package that weighs {weight} lbs will cost {gs_cost}.\n")

print(f"Ground shipping premium for your package that weighs {weight} lbs will cost {gsp_cost}.\n")

print(f"Drone shipping for your package that weighs {weight} lbs will cost {drone_cost}.\n")

print(f"The cheapest option for your package weighing {weight}lbs is {cheapest_option}.\nIt will cost you {lowest_cost}.")
