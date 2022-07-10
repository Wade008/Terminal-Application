from customer import Customer


class Customers:

    def __init__(self, customer_list):
        self.customer_list = customer_list

    def show_customers(self):
        print("List of customers in the system")
        for customer in self.customer_list:
            customer.show_customer()

    def add_customer(self, fname, lname, phone, email):
        self.customer_list.append(Customer(fname, lname, phone, email))

    def find_customer(self, search):
        # iterate over customer list searching for customer
        # only look using phone or email as these are unique ids

        for customer in self.customer_list:
            if customer.phone == search or customer.email == search:
                return customer

    def delete_customer(self, customer):
        # using the find method above pass in the current customer
        self.customer_list.remove(customer)

        return print(f"{customer.firstname} {customer.lastname} was successfully removed from the system.")

    def update_customer(self, customer):
        pass






    # def remove_customer(self, phone, email):

    #     #iterate over customer list searching for customer
    #     #only look using phone or email as these are unique ids

    #     for customer in self.customer_list:

    #         if customer.phone == phone or customer.email == email:
