from customer import Customer
from customers import Customers


def customer_seed():
    customer1 = Customer("John", "Mayer", "1987456321", "jmayer@legend.com")
    customer2 = Customer("Vance", "Joy", "1987567321", "vance@singer.com")
    customer3 = Customer("James", "Bay", "1987567895", "jbay@singer.com")
    customer4 = Customer("Adam", "Spark", "19874879321", "aspark@guitar.com")
    customer5 = Customer("Brian", "Griffin", "1956456321", "b_ri@famguy.com")
    customer6 = Customer("John", "Anderson", "1234", "1@2.com")

    customers = Customers([customer1, customer2, customer3, customer4, customer5, customer6])
    return customers

    