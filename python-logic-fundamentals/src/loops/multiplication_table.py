number = int(input("Enter a number: "))

counter = 1

while True:
    result = number * counter
    print(result)
    counter += 1 # Equivalent to counter = counter + 1
    if counter > 10:
        break