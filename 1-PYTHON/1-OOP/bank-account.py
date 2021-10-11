class BankAccount:
    def __init__(self,name):
        self.owner = name
        self.balance=0.0
    
    def getBalance(self):
        return self.balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        self.balance-=amount
        return self.balance
    
hesap = BankAccount("Murat")
print(hesap.getBalance())
hesap.deposit(5000)
print(hesap.getBalance())
hesap.withdraw(2000)
print(hesap.getBalance())
hesap.withdraw(7000)
print(hesap.getBalance())
