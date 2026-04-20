sum_value = 0

while True:
    number = int(input("Enter a number: "))
    if number >= 0:
        sum_value = sum_value + number
    else:
        break

print("Sum = ", sum_value)