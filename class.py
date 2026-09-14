class Person:
    def __init__(self, email , password):
        self._email = email
        self.password = password
        print(f"Profile Created for {email}")

    @property
    def email(self):
            return self._email
    

person1 = Person("dan@gmail.com", "danny123@")

print(person1.email)




