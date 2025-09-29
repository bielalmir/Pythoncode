class Cust:
    type = 'customer'   # class variable

    def __init__(self, n, mbn, adr, age):
        self.name = n 
        self.mobile = mbn
        self.address = adr
        self.__age = age   # private attribute

    # Getter
    def get_age(self):
        return self.__age    

    # Setter
    def set_age(self, age):
        if int(age) > 0:  
            self.__age = age
        else:
            print("Invalid age. Must be greater than 0.")

    def __str__(self):
        return f"Mr {self.name} lives at {self.address}, contact: {self.mobile}, Age: {self.__age}"


# -------------------------
# Derived Class: Account
# -------------------------
class Account(Cust):
    def __init__(self, n, mbn, adr, age, acc_no, acc_type="Savings", balance=0.0):
        # Inherit from Cust
        super().__init__(n, mbn, adr, age)
        
        # Account-specific attributes
        self.account_number = acc_no
        self.account_type = acc_type
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    # Withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")

    # Check balance
    def check_balance(self):
        return f"Account Balance for {self.name}: ₹{self.balance}"

    # String representation
    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Account Type: {self.account_type}\n"
                f"Balance: ₹{self.balance}\n"
                f"Contact: {self.mobile}, Address: {self.address}\n")


# -------------------------
# Example usage
# -------------------------
acc1 = Account("Bilal", "9797552622", "Chouadhi", 20, "ACC12345", "Savings", 5000)
print(acc1)

acc1.deposit(2000)
acc1.withdraw(1000)
print(acc1.check_balance())

acc2 = Account("Owais", "7070707070", "Polooṇṇda", 19, "ACC67890", "Current", 10000)
print("\nAnother account:\n", acc2)