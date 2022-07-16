from os import system
from termcolor import colored


def help_doc():
    col = "white"
    exit = ""
    while exit != "y":
        system("clear")
        print(colored("The Store Credit App - Help Documentation\n",
              col, attrs=["bold"]))

        print("The Store Credit App allows retail staff in any store to easily track customer store credit and comes with a number of key features.\n")

        print("Feature: Main menu:\n")
        print(
            "- The main menu lists all possible actions. To perform a specific action enter the letter shown inside [ ] at the prompt.\n")

        print("Feature: Update or view a customer's store credit:\n")
        print(
            "- This feature can be accessed by entering the letter [a] in the main menu.")
        print("- You'll then be asked to enter the phone number or email address of the relevant custumer.")
        print("- If the customer exists in the system, the customer's name, credit balance and credit value in dollars will be shown.")
        print(
            "- Follow the prompts to either [a] add credit, [b] subtract credit or return to the main menu.")
        print("- If adding or subtracting credit, enter the amount of credit to be added or removed.")
        print("- The new credit balance and value with be displayed.\n")

        print("Feature: Update or view a customer's details:\n")
        print(
            "- This feature can be accessed by entering the letter [b] in the main menu.")
        print("- You'll then be asked to enter the phone number or email address of the relevant custumer.")
        print("- If the customer exists in the system, the customer's name, phone number and email address will be shown.")
        print(
            "- Follow the prompts to either [1] edit the customer's details, [2] delete the customer from the system or return to the main menu.")
        print(
            "- If editing the customer's details, select which field requires updating: [1] first name, [2] last name,[3] phone, [4] email. Note, only one field can be updated at a time.")
        print("- The program will advise if the field has been updated successfully.")
        print("- WARNING: If deleting a customer, the customer's details will be permanently removed from the system.\n")
        print(
            "- This feature also includes adding a new customer to the system. Simply enter [c] in the main menu and follow the prompts. And by entering [d] in the main menu you can view all customers in the system.\n")

        print("Feature: Assign a dollar value to store credit:\n")
        print(
            "- This feature can be accessed by entering the letter [f] in the main menu.")
        print("- Initially, the current value of one credit will shown.")
        print(
            "- To update the value of a credit enter the letter [y] at the prompt. Then enter the new value in whole numbers only.\n")

        print("Feature: Calculate and view total outstanding credit and dollar value for the store:\n")
        print(
            "- This feature is accessed by entering the [e] in the main menu.")
        print("- The current balance for outstanding store credit will be shown along with the current total value of the outstanding store credit.\n")

        exit = input("\nExit help? (Enter [y] to exit): ")
