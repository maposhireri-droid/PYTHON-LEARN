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
           pass # raise ValueError('Amount must be positive')

    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            pass #raise ValueError('Insufficient funds')
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

# Properties are what tie these getters and setters together so you can write logic while still using dot notation
''' Getter @property
Ther retrieve a value or
even compute a value on the fly
'''
class Circle:
    def __init__(self, radius):
        # _ is a common python convention to show that an attribute is ment to private. should not be accesed outside a class
        self._radius = radius

    @property 
    def radius(self): # A getter to get the radius
        return self._radius

    @property
    def area(self): # A getter to calculate the area
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)

print(my_circle.radius)
print(my_circle.area)

''' setter @ property sets the value. you have to define another method with the same property name as getter and use <property_name.setter> above it.
They let you modify the value safely by running checks before assignment 
'''
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property 
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value): # A setter to set the radius
        if value <= 0:
            raise ValueError('radius must be positive')
        # You cannot use the same name as property name (self.radius = value) when assinging the value. the setter will call itself within the setter leading to infinite recursion. 
        self._radius = value

my_circle = Circle(3)

print('initial radius:',my_circle.radius) # Intial radius: 3
my_circle.radius = 8
print('After modifying the radius', my_circle.radius) # After modifying the radius: 8

# Deleters lets you define what will happen when a property is deleted
''' A deleter @property decorator runs a custon logic when you use a del statement on a property.
'''
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property 
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Value must be positive')
        # you can also call the getter self.radius instead of directly accessing the attribute
        
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print('Deleting radius .....')
        del self._radius

# Create circle object with a radius
my_circle = Circle(13)
print('Initial radius:', my_circle.radius)

# Delete the radius
# His calls the deleter
del my_circle.radius
print('radius deleted')

# Try to access radius after deletion
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error", e) # Error: 'circle' object has no attribute has no attribute _radius
