last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create new gradebook
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]
print(gradebook, "\n")

# Append extra classes with accompanying grades
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
# Amend Visual Arts grade
gradebook[5][1] += 5
# Remove poetry grade
gradebook[2].remove(85)
# Add "pass" value to poetry sublist
gradebook[2].append("Pass")
# Combine gradebooks:
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
