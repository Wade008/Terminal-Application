from os import system

def help_doc():
    exit =""
    while exit != "y":
        system("clear")
        print("The Store Credit App - Help Documentation\n")

        print("The Store Credit App allows retail staff in any store to easily track customer store credit and comes with a number of key features.\n")

        print("Feature 1: Update or view a customer's store credit:\n")
        print("- This feature can be accessed by entering the letter [a] in the main menu.")
        print("- You'll then be asked to enter the phone number or email address of the relevant custumer.")
        print("- If the customer exists in the system, the customer's name, credit balance and credit value in dollars will be shown.")
        print("- Follow the prompts to either [a] add credit, [b] subtract credit or return to the main menu.")
        print("- If adding or subtracting credit, enter the amount of credit to be added or removed.")
        print("- The new credit balance and value with be displayed.\n")
    
        print("Feature 2: Update or view a customer's details:\n")
        print("- This feature can be accessed by entering the letter [b] in the main menu.")
        print("- You'll then be asked to enter the phone number or email address of the relevant custumer.")
        print("- If the customer exists in the system, the customer's name, phone number and email address will be shown.")
        print("- Follow the prompts to either [1] edit the customer's details, [2] delete the customer from the system or return to the main menu.")
        print("- If editing the customer's details, select which field requires updating: [1] first name, [2] last name,[3] phone, [4] email. Note, only one field can be updated at a time.")
        print("- The program will advise if the field has been updated successfully.")
        print("- WARNING: If deleting a customer, the customer's details will be permanently removed from the system.\n")
        print("- Feature 2 also includes adding a new customer to the system. Simply enter [c] in the main menu and follow the prompts. And by entering [d] in the main menu you can view all customers in the system\n")

        print("Feature 3: Update or view a customer's store credit:\n")


        exit = input("\nExit help? (Enter [y] to exit): ")

      
