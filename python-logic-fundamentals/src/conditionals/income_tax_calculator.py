# Write "Enter the salary: "
# Read salary
salary = float(input("Enter your salary: "))

# If salary <= 1900 then
if salary <= 1900:
    # income_tax = 0
    income_tax = 0

# Otherwise
else:
    # If salarary <= 2800 then
    if salary <= 2800:
        # income_tax = salary * 0.15
        income_tax = salary * 0.15

        # Otherwise
    else:
        # income_tax = salary * 0.275
        income_tax = salary * 0.275
        # end_if
    # end_if

# net_salary = salary - income_tax
net_salary = salary - income_tax

# Write "Income Tax: ", income_tax
print(f"Income Tax: {income_tax:.2f}%")

# Write "Net Salary: ", net_salary
print(f"Net Salary: {net_salary:.2f}")



