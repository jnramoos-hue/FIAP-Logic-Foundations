# Display "Ask the user for a number"
# Write "Enter a number: "
n = int(input("Enter a number: "))

#Decision command: Check if the number is negative
# if n < 0 then
# n= n * -1
if n < 0:
    n = n * -1
# End_if

# Display the positive nu,ber
# Write "Absolute value: ", n
print("Absolute value: ", n)