print("Enter 0 to finish")

# Reset the variable that accumulates the sum
total_sum = 0

# To enter the loop for the first time
number = 1

# Start of the while loop
while number != 0:
    # Repetition block
    number = float(input("Enter a number: "))
    total_sum = total_sum + number

# Flow after the end of the loop: Display the total sum value
print("Summation = ", total_sum)
