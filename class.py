class Person:
    def __init__(self, email , password):
        self._email = email
        self.password = password
        print(f"Profile Created for {email}")

    def get_email(self):
            return self._email

    def set_email(self, new_email):
            if "@" in new_email:
                self._email = new_email
            else:
                print("Invalid Email")

person1 = Person("dan@gmail.com", "danny123@")

print(person1.get_email())

person1.set_email("Person@gmail.com")

print(person1.get_email())


