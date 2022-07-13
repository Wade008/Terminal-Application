
from datetime import datetime
from os import system

# Welcome message with current date


def welcome():
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
def main_menu():
    print("Main menu. Select from the options below:\n")
    print("[a] Update or view a customer's credit")
    print("[b] Update or view a customer's details")
    print("[c] Add a new customer")
    print("[d] View all store customers")
    print("[e] View total outstanding credit for the store")
    print("[q] Exit application\n")
    # add help here

    selection = input(
        "What would you like to do? (Enter [a-e] or [q] to exit): ").strip()
    return selection


# Add a customer
def add_customer(customers):
    # add validation here -- do not allow blanks
    print("Enter customer details below")
    fname = input("Customer first name: ").strip()
    lname = input("Customer last name: ").strip()
    phone = input("Customer Phone number: ").strip()
    email = input("Customer Email address: ").strip()

    customers.add_customer(fname, lname, phone, email)

    print(f"{fname} {lname} has been added to the system")


def _invalid_response():
    print("That's not a valid response. Try again.")
    input("Please enter to continue...")


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


def find_customer(customers, option):
    try:
        lookup = input(
            "Search for a customer by entering either their email or phone: ").strip()

        customer = customers.find_customer(lookup)

        if option == "a":
            print(
                f"\nCurrent credit balance for {customer.firstname} {customer.lastname} is: {customer.credit}")
            print("[a] add credit")
            print("[s] subtract credit")

            action = input(
                "\nWhat would you like to do? (Enter [a] or [s] or any other key to return to the main menu: ").strip()

            if action == "a" or action == "s":
                # value error captured if entry not an integer
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
            "No customer found. Try again? (type [y] to search again or press any other key to exit) ")
        if again == "y":
            find_customer(customers, option)
        else:
            print("Exiting customer search...")


def show_all_customers(customers):
    customers.show_customers()
