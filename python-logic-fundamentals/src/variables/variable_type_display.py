# USING DIFFERENT VARIABLES AND DISCOVERING THEIR TYPES
from variables.variable_types_and_casting import number_of_children

name = "Jhon" # Text type (string)
print(f"The variable name = {name} is of type {type(name)}")

salary = 2500.75 # Real number type (float)
print(f"The variable salary = {salary} is of type {type(salary)}")

number_of_children = 3 # Integer number type (int)
print(f"The variable number_of_children = {number_of_children} is of type {type(number_of_children)}")

option = "N" #Character type (char)
print(f"The variable option = {option} is of type {type(option)}")

is_adult = False # Logical type (boolean)
print(f"The variable is_adult = {is_adult} is tyoe {type(is_adult)}")