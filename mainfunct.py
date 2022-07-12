
from datetime import datetime

# Welcome message with current date


def _welcome():
    date_time = datetime.now()
    today_name = date_time.strftime("%A")
    today = date_time.strftime("%d %B, %Y")
    if date_time.hour < 12:
        greeting = "Good morning"
    if date_time.hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}! Welcome to the store credit application.")
    print(f"It's {today_name} {today}\n")


# Main menu for retail staff
def _main_menu():
    print("Main menu. Select from the options below:\n")
    print("a. Update or view a customer's credit")
    print("b. Update or view a customer's details")
    print("c. Add a new customer")
    print("d. View all store customers")
    print("e. View total outstanding credit for the store")
    print("q. Exit application\n")

    selection = input(
        "What would you like to do? (Enter a-f or q to exit): ").strip()
    return selection


# Add a customer
def _add_customer(customers):
    # add validation here -- do not allow blanks
    print("Enter customer details below")
    fname = input("Customer first name: ").strip()
    lname = input("Customer last name: ").strip()
    phone = input("Customer Phone number: ").strip()
    email = input("Customer Email address: ").strip()

    customers.add_customer(fname, lname, phone, email)

    print(f"{fname} {lname} has been added to the system")


def _find_customer(customers, option):

    lookup = input(
        "Search for a customer by entering either their email or phone: ").strip()

    customer = customers.find_customer(lookup)

    try:
        if option == "a":
            print(f"Current credit balnce for {customer.firstname} {customer.lastname} is: {customer.credit}")
            
        elif option == "b":
            print(
                f"\nCustomer details below:\n Name: {customer.firstname} {customer.lastname}\n Phone: {customer.phone}\n Email: {customer.email}\n")
            print("1. Edit customer")
            print("2. Delete customer\n")
            response = input(
                "What would you like to do? (Enter 1-2 or any other key to return to the main menu).").strip()
            if response == "1":
                customers.update_customer(customer)

            elif response == "2":
                customers.delete_customer(customer)

    except AttributeError:
        again = input(
            "No customer found. Try again? (type y to search again or press any other key to exit) ")
        if again == "y":
            _find_customer(customers)
        else:
            print("Exiting customer search... Bye!")


def _show_all_customers(customers):
    customers.show_customers()
