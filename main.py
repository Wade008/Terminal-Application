
from seed import customer_seed
# Maybe import math


customers = customer_seed()

customers.show_customers()


def add_customer():
    fname = input("Customer first name: ")
    lname = input("Customer last name: ")
    phone = input("Customer Phone number: ")
    email = input("Customer Email address: ")

    customers.add_customer(fname, lname, phone, email)

    print(f"{fname} {lname} has been added to the system")


def find_customer():

    lookup = input(
        "Search for a customer by entering either their email or phone: ")

    customer = customers.find_customer(lookup)

    try: 
        print(f"\nCustomer details below:\n Name: {customer.firstname} {customer.lastname}\n Phone: {customer.phone}\n Email: {customer.email}")
    except AttributeError:
        again = input("No customer found. Try again? (type y to search again pr any other key to exit) ")
        if again == "y":
            find_customer()
        else:
            print("Exiting customer search... Bye!")



find_customer()


# add_customer()
# customers.show_customers()
