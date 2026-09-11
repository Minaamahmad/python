class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

    def greet(self):
        print(f"hello my name is {self.name}")

person1=Person()

print(person1.name,person1.age)