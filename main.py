
from os import system
from seed import customer_seed
import mainfunct
import help
from sys import argv


name = argv[1]

# create a new customers object and seed it
customers = customer_seed()

# while loop to start main menu

selection = ""

while selection != "q":

    system("clear")
    mainfunct.welcome(name)

    selection = mainfunct.main_menu()

    if selection == "a":
        mainfunct.find_customer(customers, "a")
    elif selection == "b":
        mainfunct.find_customer(customers, "b")
    elif selection == "c":
        mainfunct.add_customer(customers)
    elif selection == "d":
        mainfunct.show_all_customers(customers)
    elif selection == "e":
        mainfunct.view_total_credit(customers)
    elif selection == "f":
        mainfunct.update_credit_value(customers)
    elif selection == "h":
        help.help_doc()
    elif selection == "q":
        continue
    else:
        print("That's not an option. Try again.")

    input("Press any key to continue")
    system("clear")

print("Exiting application... Bye!")
