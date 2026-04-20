# Ask for the amount
amount = int(input("Enter the amount:"))

# Perform the calculation of the banknote quantities
note_50 = amount // 50
amount = amount % 50
note_20 = amount // 20
amount = amount % 20
note_10 = amount // 10
amount = amount % 10

# Display the quantities of banknotes
print("Quantity of 50 banknotes: ", note_50)
print("Quantity of 20 banknotes: ", note_20)
print("Quantity of 10 banknotes: ", note_10)