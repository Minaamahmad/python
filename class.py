class EmailService:  
    
    def _connect(self):
         print("Connecting to server")
            
    def _authenticate(self , name ):
         self.name = name
         admin = "bob"
         
         if self.name != admin:
            print("Failed to Authenticate")
            
            return False
         else:
             print("Authenticated")
             return True
             
            
        
    def send_email(self):
        self._connect()
        if self._authenticate("bob1"):
         print("Sending Email")
       


email = EmailService()

email.send_email()