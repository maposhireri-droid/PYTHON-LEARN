class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.amount = amount
        self.description = description
        self.ledger.append
        ('amount': self.amount, 'description ': self.descriptio})
        
    def withdraw(self, amount, description=''):
        self.amount = - amount
        if amount:
            self.ledger.append(self.amount)
            return True
        False
        self.ledger.append(self.withdrawals)

    def get_balance(self):
        return self.ledger['amount']

    def transfer(self, amount, catogory):
        self.withdraw(self.amount, "Transfer to {category}")
        self.deposit(self.amount, "Transfer from {category}")

    def check_funds(self, amount):
        if self.transfer:
            if amount < self.get_balance:
                return False
            True

def create_spend_chart(categories):
    print('Percentage spent by category')
    valp = sum(self.withdrawals.values())
    for y in range(0, 101, 10):
        print(y,'|\n')
        if valp == y:
            print('o')
    for category in categories:
        for c in category:
            print(c,'\n')

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)




