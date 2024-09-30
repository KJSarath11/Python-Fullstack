class instagram:
    def __init__(self,uname):
        self.uname=uname

class Email(instagram):
    def __init__(self, uname,email_id):
        super().__init__(uname)
        self.email_id=email_id

class Phone(instagram):
    def __init__(self, uname,phno):
        super().__init__(uname)
        self.phno=phno
    
class instagram_v1(Email,Phone):
    def __init__(self, uname, email_id,phno):
        Email.__init__(uname, email_id)
        Phone.__init__(uname, phno)

    def chat(self):
        return "Enter the message"

    def voice_call(self):
        return f"Calling {self.phno} => {self.uname} => {self.email_id}"

obj = instagram_v1("Sarath","kjsarath76@gmail.com","9496981270")

# Testing the methods
print(obj.phno)       # Phone number from whatsapp_v1
print(obj.uname)
print(obj.email_id)   # Username from whatsapp_v2
print(obj.voice_call())