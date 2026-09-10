class Dog:
    def __init__(self,breed):
        self.breed=input("Enter breed:")
        print("woof woof")


class owner:
    def __init__(self,):
        self.name = input("Enter your name: ")


ownername= owner()
dog1= Dog(ownername.name)
