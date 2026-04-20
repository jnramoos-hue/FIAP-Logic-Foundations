# Ask for the user's age
age = input("Enter your age: ")
age = int(age)

# Check if the age meets the condition and display a message
if age >= 18:
    print("Adult")
else:
    print("Minor")