''' OOP
is a programming style in which developers treat everything in their code like real world objects.'''

class Wallet:
    def __init__(self, balance):
        self.balance = balance # for internal use by convention

    def deposit(self, amount):
        if amount > 0:
           self.balance += amount # Add to the balance safely.

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount # Remove from the balance safely

'''Private attributes and methods
cannot be accessed outside their class.'''
class Wallet:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount # Add to the balance safely

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount # Remove from the balance safely

account = Wallet(500)
#print(account.__balance) # AttributeError: 'Wallet' object has no attribute '__balance'

'''To get the current value of balance you can define a get_balance method'''
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance 
        
acct_one = Wallet(100)
acct_one.deposit(50)
print(acct_one.get_balance()) # 150
acct_two = Wallet(450)
acct_two.withdraw(28)
print(acct_two.get_balance()) # 422 
acct_two.deposit(150)
print(acct_two.get_balance()) # 572

''' You can also define a private __validate method to check if every deposit or withdrawal amount is a positive number:'''

class Wallet:
    def __init__(self):
        self.__balance = 0

    def __validate(self, amount):
        if amount < 0:
           raise ValueError('Amount must be positive')

    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError('Insufficient funds')
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

acct_one = Wallet()
acct_one.deposit(3)
print(acct_one.get_balance()) # 3

acct_one.deposit(50)
print(acct_one.get_balance()) # 53

acct_one.deposit(-4)  # ValueError: Amount must be positive
acct_one.withdraw(-8) # ValueError: Amount must be positive
acct_one.withdraw(58) # ValueError: Insufficient funds
