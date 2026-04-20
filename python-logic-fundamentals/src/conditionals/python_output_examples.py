# Data output command in Python

# Write "Jose da Silva Ramos Junior"
print("Jose da Silva Ramos Junior")

# Write "28 years old"
print("28 years old")

name = "Junior Ramos"
age = 28
weight = 82.64

# Form 1
print("1. My name is", name, "I am ", age, "years old and", weight, "Kilograms")

# From 2
print("2. My name is {} I am {} years old and {} kilograms.".format(weight,name, age))
print("2. My name is {0} I am {1} years old and {2:.1f} kilograms.".format(weight,name, age))
print("2. My name is {n} I am {i} years old and {k:.2f} kilograms.".format(n=name,i=age,k=weight))

# From 3
print(f"3. My name is {name} I am {age} years old and {weight:.2f} kilograms.")
