''' Dictionaries are python built in datastructures
that store a collection of key-value pairs.
Similar to real dictionaries where you find a word to
find its corresponding meaning.'''

# general syntax
dictionary = {
    #key1: value1,
    #key2: Value2
}

pizzas = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'topping': ['mozzarella', 'basil']
}

# dict() constructor builds a dictionarY FROM  a sequence of key-value pairs
# These tuples contains the key as the first element and value as second
pizza = dict([('name', 'Magherita Pizza'), ('Price', 8.9), ('calories_per_slice', 250), ('toppings', ['Mozzarella', 'basil'])])
print(pizza['name'])

# update dictionaries
pizza['name'] = 'Magherita'
print(pizza['name'])

# get() method retrieves a value associated with the key
pizza.get('toppings', [])

# .key() and .values() returns a view object with all keys and values 
#in the dictionary respectively
pizza.keys()
pizza.values()

# .items()returns a view object with all key-value pairs
# in the dictionary. including both the keys and the values
print(pizza.items())

# clear() removes items in the dictionary
pizza.clear()

# pop
pizza.pop('price', 10)
#pizza.pop('total_price ') #keyerror

# popitem()
#pizza.popitem() # remove last inserted item

# update()
pizza.update({'price': 15, 'totl_times': 25})

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

# iterate over dictionary view object with for loop
# Iterate over values
for price in products.values():
    print(price)

#iterate over keys
for product in products.keys():
    print(product)

# or
for product in products:
    print(product)

# Iterate over key and their corresonding values simultaneously.
for product in products.items():
    print(product)

# storing keys and values in separate loop variables.
#Each holds its corresponding value
# key first and then the value

for product, price in products.items():
    print(product, price)

# offering 20% discount for products
for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

# enumerator function iterates over the key value pairs while
#keeping track of the counter.

for product in enumerate(products):
    print(product)

# assign the keys to separate loop variables.
for index, product in enumerate(products):
    print(index, product)

# iterate over values
for price in enumerate(products.values()):
    print(price)

# you can also assign them to separate loop variables
for index, price in enumerate(products.values()):
    print(index, price)

# you can get the entire key value pair in addition to
# counter or index with product.items()

for index, product in enumerate(products.items()):
    print(index, product)

# customize initial value of count
for index, product in enumerate(products.items(), 1):
    print(index, product)
