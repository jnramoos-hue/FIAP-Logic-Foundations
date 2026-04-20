# Asl the user to enter Y for yes or N for no
# Input 1:
    # Enter [Y]yes or [N]no:
# Output 1
    # You entered Y or N

# Ask the user to enter Y for yes or N for no
# Input 1:
    # Enter [Y]yes [N]no: H
# Output 1
    # You entered 'H', enter Y or N

option = input("Enter [Y]yes or [N]o: ")
while option != "Y" and option != "y" and option != "N" and option != "n":
    print("You entered ", option, "enter Y or N!")
    option = input("Enter [Y]yes or [N]No: ")
print("You entered ", option)