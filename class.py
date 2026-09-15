class Person:
    def __init__(self):
        self._email = ""
        self.password = ""
        print(f"Profile Created for {self.email}")

    @property
    def email(self):
            return self._email


    
    @email.setter
    def email(self, new_email):
            print()
            if "@" in new_email and ".com" in new_email:
                self._email = new_email
            else:
                print("Invalid Email")


person1 = Person()

user_email = input("Enter Email: ")
user_pass = input("Enter Pass: ")
person1.password = user_pass
person1.email = user_email

if person1.email:
     forgotpass= input("Forgot Pass Y/N: ")
     if forgotpass == "Y":
          new_pass = input("Enter new Passord: ")
          person1.password= new_pass
     if new_pass ==user_pass:
          print("Old Password")

    

          
