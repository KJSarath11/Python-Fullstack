class whatsapp_v1:
    def __init__(self,phno,username):
        self.phno=phno
        self.username=username
    def chat(self):
        print("Enter the message")
        
class whatsapp_v2(whatsapp_v1):
    def __init__(self,phno,username,profile):
        super().__init__(phno,username)
        self.profile=profile
    def voice_call(self):
        print(f"Calling {self.phno} => {self.username} => {self.profile}")

obj=whatsapp_v2(9496981270,"Sarath","img")
obj.voice_call() 