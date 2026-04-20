n = int(input("Enter a number: "))

interation = n
factorial = 1

for iteration in range(n, 1, -1):
    factorial = factorial * iteration

print("Factorial: ", factorial)

