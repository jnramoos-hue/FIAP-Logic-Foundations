start = int(input("Enter the starting number"))
end = int(input("Enter the final value"))

for count in range(start, end + 1, 1):
    print(count, " ")

while True:
    print(start, " ")
    start = start + 1
    if start > end:
        break