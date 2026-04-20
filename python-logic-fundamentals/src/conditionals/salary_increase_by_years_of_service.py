# Write "Enter your years of service: "
# Read years_of_service
years_of_service = int(input("Enter your tears of service: "))

# Write "Enter your salary: "
# Read salary
salary = float(input("Enter your salary: "))

# If years_of_service < 3 then
if years_of_service <= 3:
    # increase = salary * 0.05
    incriase = salary * 0.05

# Otherwise
#increase = salary * 0.1
else:
    incriase = salary * 0.1
#end_if

#new_salary = salary + increase
new_salary = salary + incriase

# Write "Your salary changed from", salary, "to", new_salary
print("Your salary changed from: ", salary, " to ", new_salary)