
from datetime import datetime
from os import system
from termcolor import colored


# Welcome message with current date


def welcome(name):
    col = "white"
    date_time = datetime.now()
    today_name = date_time.strftime("%A")
    today = date_time.strftime("%d %B, %Y")
    if date_time.hour < 12:
        greeting = "Good morning"
    if date_time.hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(colored(f"{greeting}, {name}! Welcome to The Store Credit App.", col, attrs=["bold"]))
    print(colored(f"It's {today_name} {today}\n", col))


# Main menu for retail staff
def main_menu():
    col = "white"
    print(colored("Main menu. Select from the options below:\n", col))
    print(colored("[a] Update or view a customer's credit", col))
    print(colored("[b] Update or view a customer's details", col))
    print(colored("[c] Add a new customer", col))
    print(colored("[d] View all store customers", col))
    print(colored("[e] View total outstanding credit for the store", col))
    print(colored("[f] View or update the value of a credit (default $1)", col))
    print(colored("[h] Help", col))
    print(colored("[q] Exit application\n", col))

    selection = input(colored(
        "What would you like to do? (Enter [a-f], [h] for help  or [q] to exit): ", col, attrs=["bold"])).strip()
    return selection

# Generic invalid response function


def _invalid_response():
    print("That's not a valid response. Try again.")
    input("Please enter to continue...")

# Add a customer


def add_customer(customers):
    # add validation here -- do not allow blanks
    print("Enter customer details below")
    fname = input("Customer first name: ").strip()
    lname = input("Customer last name: ").strip()
    phone = input("Customer Phone number: ").strip()
    email = input("Customer Email address: ").strip()

    if not(fname == "" or lname == "" or phone == "" or email == ""):
        customers.add_customer(fname, lname, phone, email)
        print(f"{fname} {lname} has been added to the system")
        return
    system("clear")
    _invalid_response()
    add_customer(customers)


# handing the edit options
def _handle_edit():
    response = ""
    while response not in ["1", "2", "3", "4"]:
        system("clear")
        response = input(
            "\nSelect a field to update\n[1] first name\n[2] last name\n[3] phone\n[4] email\n(Enter [1-4] only): ").strip()

        if response == "1":
            update = "first name"
        elif response == "2":
            update = "last name"
        elif response == "3":
            update = "phone"
        elif response == "4":
            update = "email"
        else:
            _invalid_response()

    return update

# handle the edit input


def _handle_edit_input(update):

    new_value = ""
    while new_value == "":
        system("clear")
        new_value = input(f"\nEnter new {update}: ").strip()
        if new_value == "":
            _invalid_response()

    return new_value


# handle credit amount
def _handle_credit_amount():
    amount = ""
    while amount == "":
        try:
            amount = int(input("Enter amount of credit: ").strip())
        except ValueError:
            _invalid_response()
            amount == ""
    return amount

# Find customer function linking main menu and Customers find_customer method


def find_customer(customers, option):
    try:
        lookup = input(
            "Search for a customer by entering either their email or phone: ").strip()

        customer = customers.find_customer(lookup)

        if option == "a":
            worth = customer.credit*customer.worth
            print(
                f"\nCurrent credit balance for {customer.firstname} {customer.lastname} is: {customer.credit}, worth ${worth}")
            print("[a] add credit")
            print("[s] subtract credit")

            action = input(
                "\nWhat would you like to do? (Enter [a] or [s] or any other key to return to the main menu: ").strip()

            if action == "a" or action == "s":

                amount = _handle_credit_amount()
                customers.update_credit(customer, action, amount)
            else:
                print("Exiting customer credit menu...")

        elif option == "b":
            print(
                f"\nCustomer details below:\n Name: {customer.firstname} {customer.lastname}\n Phone: {customer.phone}\n Email: {customer.email}\n")
            print("[1] Edit customer")
            print("[2] Delete customer")
            response = input(
                "\nWhat would you like to do? (Enter [1-2] or any other key to return to the main menu): ").strip()

            if response == "1":
                update = _handle_edit()
                new_value = _handle_edit_input(update)
                customers.update_customer(customer, update, new_value)
            elif response == "2":
                customers.delete_customer(customer)
            else:
                print("Exiting customer details menu...")

    except AttributeError:
        again = input(
            "No customer found. Try again? (Enter [y] to search again or press any other key to exit) ")
        if again == "y":
            find_customer(customers, option)
        else:
            print("Exiting customer search...")


# Show all customers function linking main menu and Customer show_customer method
def show_all_customers(customers):
    customers.show_customers()


# dollar value per credit
def update_credit_value(customers):
    customer = customers.customer_list[0]
    current_worth = customer.worth

    print(f"The current value of one credit is: ${current_worth}")

    action = input(
        "Do you want to update credit value? (Enter [y] to update or any other key to return to the main menu): ")

    if action == "y":
        new_value = ""
        while new_value == "":
            system("clear")
            try:
                new_value = int(
                    input("Enter dollar value of one credit: ").strip())
            except ValueError:
                _invalid_response()
                new_value == ""

        customers.update_worth(new_value)
    else:
        return

# view total outstanding credit for the store


def view_total_credit(customers):
    customers.total_store_credit()
