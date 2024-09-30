# Parent class 1
class whatsapp_v1:
    def __init__(self, phno):
        self.phno = phno

# Parent class 2
class whatsapp_v2:
    def __init__(self, username):
        self.username = username

# Child class inheriting from both whatsapp_v1 and whatsapp_v2
class application(whatsapp_v1, whatsapp_v2):
    def __init__(self, phno, username):
        whatsapp_v1.__init__(self, phno)  # Initializing whatsapp_v1
        whatsapp_v2.__init__(self, username)  # Initializing whatsapp_v2

    def chat(self):
        return "Enter the message"

    def voice_call(self):
        return f"Calling {self.phno} => {self.username}"

# Creating object of application class
obj = application(9496981270, "Sarath")

# Testing the methods
print(obj.phno)       # Phone number from whatsapp_v1
print(obj.username)   # Username from whatsapp_v2
print(obj.voice_call())  # Using voice_call method
