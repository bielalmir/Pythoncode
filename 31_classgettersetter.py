class Cust:
    type = 'customer'     
    def __init__(self, n, mbn, adr, age):
        self.name = n 
        self.mobile = mbn
        self.address = adr
        self.__age = age 

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
        return f'Mr {self.name} lives at {self.address} and you can contact them on {self.mobile} and he is {self.__age} years old\n'

test = Cust('Bilal', '9797552622', 'chouadhi', '10')
test2 = Cust('Owais', '7070707070', 'Polooṇṇda', '5')
test3 = Cust('Salik', '7078689398', 'israel', '5')

print("Default type:", Cust.type)

print("Before change:")
print(test.name, test.mobile, test.address, test.type)
print(test2.name, test2.mobile, test2.address, test2.type)
print(test3.name, test3.mobile, test3.address, test3.type)

# Change attributes
test.name, test.mobile, test.address, test.type = 'Agent', 'XXX-XXXX-XXX', 'Error 69', 'Stud'

print("\nAfter change:")
print(test.name, test.mobile, test.address, test.type)

# Using getter
print("\nGetting age of test:", test.get_age())

# Using setter
test.set_age(25)
print("After setting valid age:", test.get_age())

test.set_age(-5)
print("After trying invalid age:", test.get_age())

print("\nString output:\n", test)