# Multilevel Inheritance Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Customer(Person):   # inherits Person
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.customer_id = customer_id

    def show_customer(self):
        print(f"Customer ID: {self.customer_id}")


class Account(Customer):  # inherits Customer (which already inherits Person)
    def __init__(self, name, age, customer_id, acc_no, balance):
        super().__init__(name, age, customer_id)
        self.acc_no = acc_no
        self.balance = balance

    def show_account(self):
        print(f"Account Number: {self.acc_no}, Balance: ₹{self.balance}")


# Testing Multilevel
print("---- Multilevel Inheritance ----")
acc = Account("Bilal", 20, "CUST101", "ACC12345", 5000)
acc.show_person()     # From Person
acc.show_customer()   # From Customer
acc.show_account()    # From Account