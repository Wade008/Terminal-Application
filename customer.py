
class Customer:
    # A class to instantiate a customer object
    def __init__(self, fname, lname, phone, email, credit=0, worth=1):
        self.firstname = fname
        self.lastname = lname
        self.phone = phone
        self.email = email
        self.credit = credit
        self.worth = worth

    def show_customer(self):

        value = self.credit*self.worth
        print(
            f"Customer: {self.firstname} {self.lastname}, Phone: {self.phone}, Email: {self.email}, Credit: {self.credit}, worth: ${value}")
   
