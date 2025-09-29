class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name}, Age: {self.age}")
# -----------------------------
# Multilevel: Person → Customer
# -----------------------------
class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.customer_id = customer_id

    def show_customer(self):
        print(f"Customer ID: {self.customer_id}")
# -----------------------------
# Multiple Inheritance Parents
# -----------------------------
class BankFeatures:
    def deposit(self, amount):
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        print(f"Withdrew ₹{amount}")

class LoanFeatures:
    def apply_loan(self, amount):
        print(f"Applied for loan of ₹{amount}")

    def repay_loan(self, amount):
        print(f"Repaid loan of ₹{amount}")
# -----------------------------
# Multilevel + Multiple Combined
# CustomerAccount inherits:
#   - Customer (multilevel from Person)
#   - BankFeatures & LoanFeatures (multiple inheritance)
# -----------------------------
class CustomerAccount(Customer, BankFeatures, LoanFeatures):
    def __init__(self, name, age, customer_id, acc_no, balance):
        Customer.__init__(self, name, age, customer_id)  # from multilevel
        self.acc_no = acc_no
        self.balance = balance

    def show_account(self):
        print(f"Account Number: {self.acc_no}, Balance: ₹{self.balance}")
# -----------------------------
# Testing
# -----------------------------
print("---- Multilevel + Multiple Inheritance ----")
acc = CustomerAccount("Bilal", 21, "CUST101", "ACC12345", 5000)
# From Person
acc.show_person()
# From Customer
acc.show_customer()
# From CustomerAccount
acc.show_account()
# From BankFeatures
acc.deposit(2000)
acc.withdraw(1000)
# From LoanFeatures
acc.apply_loan(10000)
acc.repay_loan(2000)