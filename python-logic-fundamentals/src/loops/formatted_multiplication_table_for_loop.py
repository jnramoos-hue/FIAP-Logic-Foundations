n = int(input("Enter a number: "))

multiplication = 1

# Loop configured for 10 iteration
for i in range(1, 11, 1):
    multiplication = i * n
    print(f"{n} x {i} = {multiplication}")
    