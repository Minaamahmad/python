class BankAccount:
    
    def __init__(self,user,balance):
        self.user = user
        self._balance = balance
        
        
    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self,amount):
        if amount < 0:
            raise ValueError("Insufficient Balance")
        
        self._balance = amount
        
account = BankAccount("Bob", 500)

account.balance += 500

print(f"{account.balance}")