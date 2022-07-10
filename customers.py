from customer import Customer
from os import system

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

            for customer in self.customer_list:
                if customer == customer:
                   
                    response = ""
                    while response not in ["1","2","3","4"]:
                        system("clear")
                        response = input("\nSelect a field to update\n1. first name\n2. last name\n3. phone\n4. email?\n(Enter 1-4 only): ").strip()
                        
                        if response == "1":
                            update = "first name"
                        elif response == "2":
                            update = "last name"
                        elif response == "3":
                            update = "phone"
                        elif response == "4":
                            update = "email"
                        else:
                            print("That's not a valid response. Try again.")
                            input("Please enter to continue...")

                    new_value = input(f"\nEnter new {update}: ")
                    
                    # add if statement here
                    customer.phone = new_value

                   

                    return  print(f"The customer's {update} was successfully updated in system.")



            

            





    # def remove_customer(self, phone, email):

    #     #iterate over customer list searching for customer
    #     #only look using phone or email as these are unique ids

    #     for customer in self.customer_list:

    #         if customer.phone == phone or customer.email == email:
