number = int(input("Enter 5 numbers: "))
largest = number

for cont in range(1, 5, 1):
    number = int(input())
    if number > largest:
        largest = number

print("Largest value = ", largest)