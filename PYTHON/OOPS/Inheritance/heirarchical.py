# Parent class
class Instagram:
    def __init__(self, uname):
        self.uname = uname

# Child class 1 inheriting from Instagram
class Email(Instagram):
    def __init__(self, uname, email_id):
        super().__init__(uname)  # Calling parent class constructor
        self.email_id = email_id

# Child class 2 inheriting from Instagram
class Phone(Instagram):
    def __init__(self, uname, phone_no):
        super().__init__(uname)  # Calling parent class constructor
        self.phone_no = phone_no

# Creating objects of the child classes
obj1 = Email("skj", "skj@example.com")
obj2 = Phone("skj", 9496981270)

# Displaying the attributes
print(f"Username: {obj1.uname}, Email ID: {obj1.email_id}")
print(f"Username: {obj2.uname}, Phone No: {obj2.phone_no}")
