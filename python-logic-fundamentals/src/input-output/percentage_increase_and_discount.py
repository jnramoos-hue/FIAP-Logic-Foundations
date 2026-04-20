# Read value
value = input("Enter the value: £")
value = float(value)

# Write “Enter the percentage: ”
percentage = input("Enter the percentage: ")
percentage = float(percentage)

# Calculate the percentage
percent_value = value * percentage / 100

# Calculate the increase
increase = value + percent_value

# Calculate the discount
discount = value - percent_value

# Write “Percentage: ”, percent_value
print("Percentage: ", percent_value)

# Write ”Increase: ”, increase
print("Increase: ", increase)

# Write ”Discount: ”, discount
print("Discount: ", discount)
