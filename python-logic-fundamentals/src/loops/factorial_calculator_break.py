n = int(input("Enter a number: "))

factorial = 1

while True:
    factorial = factorial * n
    n = n - 1
    if n < 1:
        break
print("Factorial = ",factorial)