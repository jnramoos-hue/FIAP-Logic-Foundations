contact_list = [] # Creating an empty list.

# FUNCTION DEFINITIONS

# Description: This procedure creates a new contact in the contact list.

# Name: new()
# Type: procedure

def new():
    global contact_list # Defining variable as Global.
    name = p_name()
    phone = input("Phone.........:")
    email = input("E-mail........:")
    contact_list.append([name, phone, email]) # Adding the data to the contact list

    print("""
            ---------------------------
             Record saved successfully!!!
            ---------------------------""")

# Description: This procedure reads a name.
# Name: p_name()
# Type: procedure
def p_name():
    return (input("Name..........: "))

# Description: This procedure list one record
# Name: list_data(name, phone, email)
# Type: procedure
def list_data(name, phone, email):
    print("Name: %s Phone: %s Email: %s" % (name, phone, email))
    print("---------------------------")

# Description: This procedure list all records in the matrix.
# Name: list_all()
# Type: procedure
def list_all(): # Function to show the contact list.
    print("CONTACT LIST #############")
    for e in contact_list:
        list_data(e[0], e[1], e[2])
    print("END OF THE LIST ##############")

# Description: This function searches for a contact by name.
# Name: search(name): int
# Type: function
def search(name): # Function to search contacts.
    search_name = name.lower()
    for d, e in enumerate(contact_list): # Goes through the whole matrix
        if e[0]. lower() == search_name: # Looks for the desired name
            return d # Returns the index of the found name
        return None
#Description: This procedure displays the record or an unsuccessful message
# Name: search_contact():
# Type: procedure
def search_contact():
    # Search the name
    p = search(p_name()) #Data input.
    if p != None:
        print("Record found!")
        # Update the variables if found
        name = contact_list[p][0]
        phone = contact_list[p][1]
        email = contact_list[p][2]
        # Show the record
        list_data(name, phone, email)
    else:
        #Display the unsuccessful message when searching for the record
        print("Record not found!")

# Description: This procedure deletes a contact
# Name: delete():
#Type: procedure
def delete():
    global contact_list
    name = p_name()
    # Returns the index of mu name or empty
    p = search(name)
    if p != None: # If the contact was found
        del contact_list[p] # Deletes the contact
        print("""------------------------
              Record DELETED successfully!!!
              ------------------------""")
    else:
        # Did not find the record tod delete
        print("Record not found!")

# Description: This procedure edits a contact
# Name: edit():
# Type: procedure
def edit():
    p = search(p_name()) # Data input
    # If the record was found
    if p != None:
        # Show the name and ask for the others
        name = contact_list[p][0]
        print("Name........:", name)
        phone = input("Phone........:")
        email = input("E-mail........:")
        contact_list[p] = [name, phone, email] # Storing the new data.
        print("""------------------------
              Record EDITED successfully!!!
              ------------------------""")
    else:
        print("Record not found!") # Executes if the condition is false.

# Description: This function validades IF THE ENTERED ITEM IS VALID
# Name: validate(questions, start, end): int
# Type: function
def validade(question, start, end): # Function to validade integer numbers.
    while True: # Creating an infinite loop.
        try: # Creating an agreement/condition.
            value = int(input(question)) # Data input
            if start <= value <= end:
                return (value)
            else:
                return (0)
        except ValueError: # Executes if false.
            print("Invalid value, please enter between %d and %d"  % (start, end))

# Description: This function returns the menu item or 0 if invalid
# Name: menu(question, start, end): int
# Type: Function
def menu(): # Function that displays the options menu.
    print("""
    1 - Add new contact
    2 - Edit a contact
    3 - Search contact
    4 - Contact list
    5 - Delete contact
    6 - Exit
    """)
    return validade("Choose an option: ", 1, 6)

# MAIN PROGRAM
while True:
    option = menu()
    if option == 0:
        print("Invalid option!")
    elif option == 6:
        break
    elif option == 1:
        new()
    elif option == 2:
        edit()
    elif option == 3:
        search_contact()
    elif option == 4:
        list_all()
    elif option == 5:
        delete()



