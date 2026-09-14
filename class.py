class Person:
    def __init__(self, email , password):
        self._email = email
        self.password = password
        print(f"Profile Created for {email}")

    @property
    def email(self):
            return self._email
    @email.setter
    def email(self, new_email):
            print("Updated Email")
            if "@" in new_email:
                self._email = new_email
            else:
                print("Invalid Email")

person1 = Person("dan@gmail.com", "danny123@")

print(person1.email)

person1.email ="123@.com"

print(person1.email)


