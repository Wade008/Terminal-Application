from curses import longname
import email
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



add_customer()

customers.show_customers()






