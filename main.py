
from os import system

from seed import customer_seed
import mainfunct
# Maybe import math

# create a new customers object and seed it
customers = customer_seed()


# while loop to start main menu

selection = ""

while selection != "q":

    system("clear")
    mainfunct._welcome()

    selection = mainfunct._main_menu()

    if selection == "a":
        mainfunct._find_customer(customers, "a")
    elif selection == "b":
        mainfunct._find_customer(customers, "b")
    elif selection == "c":
        mainfunct._add_customer(customers)
    elif selection == "d":
        mainfunct._show_all_customers(customers)
    elif selection == "e":
        pass #show store credit debt
    elif selection == "q":
        continue
    else:
        print("That's not an option. Try again.")

    input("Press any key to return to the main menu")
    system("clear")

print("Exiting application... Bye!")
