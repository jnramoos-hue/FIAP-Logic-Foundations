# Write “Enter the sale value: ”
# Read sale
sale = float(input("Enter the sale amount: "))

# If sale > 300 then
if sale > 300:

    # discount = sale * 10 / 100
    discount = sale * 10 / 100

    # sale = sale - discount
    sale = sale - discount

# Write “New value = ”, sale
print("New value: ", sale)