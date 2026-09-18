class User:
    count = 0
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.count+=1
        
    def display(self):
        print(f"Username: {self.username} and Email: {self.email} ")
        
        
        
User1=User("Ali","Ali@.com")
User2=User("dave","dave@.com")
User3=User("bob","bob@.com")

User_array = []

User_array.append(User1)
User_array.append(User2)
User_array.append(User3)


print(f"{User.count}")

for users in User_array:
  print(users.username, users.email)