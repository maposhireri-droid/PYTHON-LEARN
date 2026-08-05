'''
These are reusable pieces of code that run when you call them
'''

# Inpunt function prompts the user for input.
name = input('What is your name?')
print('Hello', name)

# This is a custom function that prints hello to the terminal
def hello():
    print('Hello World')

hello()  # function call, otside the function

# Prints the sum of two numbers in the terminal
def calculator_sum(a, b):
    print(a + b)

calculator_sum(3, 1)

''' Return keyword in functions,
exits the function and returns none.
python defaults to return None if you dont explicitly use 
return in your function'''

def calculator_sum(a, b):
    print(a + b)

my_sum = calculator_sum(3, 1) # Return value is None. NO return explicitly.
print(my_sum)

# Use the return keyward to send back the results
def calculator_sum(a, b):
    return a + b # calculator_sum func returns the sum of a and, which get stored in my sum

my_sum = calculator_sum(3, 1)
print(my_sum)

''' Local scope
variables declared inside a function or class can oly 
be accessed within that function or class'''

def my_func():
    my_var = 10
    print(my_var)

my_func()

''' Enclosing Scope
A function that is nested inside another function 
cAN access the vsriables of the function it
is nested within
'''

def outer_func():
    msg = 'Hello there'

    def inner_func():
        print(msg)
    inner_func()
outer_func()

'''Outer functions cannot access variables defined 
within any nested functin
'''

def outer_func():
    msg = 'hello world'
    #print(res) not defined in enclosing scope

    def inner_function():
        res = 'How are you'
        print(msg)

    inner_function()

outer_func() # NameError: name 'res' is not defined

''' solution one
initialize res in enclosing scope or outer function as an empty string
Then within the inner function make res a non 
local variable with nonlocal keyword'''

def outer_func():
    msg = 'Hello there!'
    res = "" #declare res in the enclosing scope

    def inner_func():
        nonlocal res # Allow modifiaction of an enclosing variable
        res = 'How are you'
        print(msg) # accessing msg from outer_func()

    inner_func()
    print(res)

outer_func()

'''Gobal variables
they are declared outside any function or class
can be accessed from anywhere in the program'''

my_var = 100

def show_var():
    print(my_var)

show_var()  # 100
print(my_var) # 100

'''
using global veriable to make a functions locally
defined variable globally accessible'''

my_var_1 = 7

def show_vars():
    global my_var_2 
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars()  #7 10

print(my_var_2) # its now a global var and can be accessed from anywhere

'''modify global variables with global keyword'''
my_var = 10

def change_var():
    global my_var # alllow gv modifications
    my_var = 20

change_var()

print(my_var) # my var is now modified globally to 20

'''string translation
returns table that matches char in corresponding places
pos one sA with pos one sb'''
lower_chars = 'abc'
upper_chars = 'ABC'

table = str.maketrans(lower_chars, upper_chars)
# chars are stored as unicode ordinal, 
#i.e numbers that uniquely identifies the character
print(table)

'''translate method
takes as argument the translation table generated
by maketrans()
it is called on a string and returns a copy of the 
original string where the chars have been replaced 
based on the translation tables'''
t = str.maketrans('1k', 'br')
sentence = 'The tent gave in to the leaks'

print(sentence.maketrans(t))
# output: The tent gave in to the bears
