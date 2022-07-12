
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

    if selection == "b" or selection == "d":
        mainfunct._find_customer(customers)
    elif selection == "c":
        mainfunct._add_customer(customers)
    elif selection == "e":
        mainfunct._show_all_customers(customers)
    elif selection == "q":
        continue
    else:
        print("That's not an option. Try again.")

    input("Press any key to return to the main menu")
    system("clear")

print("Exiting application... Bye!")
