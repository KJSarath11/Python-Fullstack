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
        
class whatsapp_v3(whatsapp_v2):
    def __init__(self,phno,username,profile,endcall):
        super().__init__(phno,username,profile)
        self.endcall=endcall
    def video_call(self):
        print(f"Video Calling {self.phno} => {self.username} => {self.profile}=> {self.endcall}")

obj=whatsapp_v3(9496981270,"Sarath","img"," Changing to videoCALL :)")
obj.video_call() 