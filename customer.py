
class Customer:
    # A class to instantiate a customer object
    def __init__(self, fname, lname, phone, email):
        self.firstname = fname
        self.lastname = lname
        self.phone = phone
        self.email = email

    def show_customer(self):
        print(f"Customer: {self.firstname} {self.lastname}, Phone: {self.phone}, Email: {self.email}")


# customer1 = Customer("Wade", "Doolan", "0448175351", "wadedoolan@hotmail.com")

# customer1.show_customer()