from customer import Customer

class Customers:
    
    def __init__(self, customer_list):
        self.custumer_list = customer_list

    def show_customers(self):
        print("List of customers in the system")
        for customer in self.customer_list:
            customer.show_customer()



