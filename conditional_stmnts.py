print(3 > 4)# False
print(3 < 4)# True
print(3 ==4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) #  True

# if conditional basic syntax
if condition:
    pass # code to execute if condition is true

age = 18

if age >= 18:
    print('You are an adult') # You are an adult

# if...else syntax
if condition:
    pass # code to execute if condition is true
else:
    pass # code to execute if condition is false

# else condition
age = 12

if age >= 18:
    print('You are an adult')
#print('Almost there!)     # you cannot place a statement between if and else
else: # results in syntaxerror: invalid syntax if done so
    print('You are not an adult')

# elif condition
if condition1:
    pass # code to execute if condition is true
elif condition2:
    pass # code to execute if condition1 is false and condition2 is true
else:
    pass # code to execute if all conditions are false

age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child

'''Nested conditional statements
comapres multiple values at once.'''

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vot') # you are eligible to vote
else:
    print('You are not eligible to vote')

# checking for truthy or falsy value
# they either evaluate to true or false

print(bool(False)) # False
print(bool(0)) # False
print(bool('')) #false

print(bool(True)) # True
print(bool(1)) # True
print(bool('hello')) # Ture

''' The and operator
results in a truthy value if both operands are True'''

is_citizen = True
age = 25

print(is_citizen and age) # 25. # truthy, returns second operand

'''refactoring using and operator and if
instead of nested if statements'''

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # you are eligible to vote
else:
    print('You are not eligible to vote')

''' The or operator
results in a truthy value if atleast one operand is true'''
age = 19
is_employed = False

print(age or is_employed) #19

# checking if one or more expressions is true
age = 19
is_student = False

if age < 18 or is_student:
    print('You are eligible for a student discount')
else:
    print('you are not eligible for a student discount')

''' The not operator
takes a single operand and inverts its boolean value.
it always returns True or False.'''

print(not '') #True, becouse empty strings are falsy
print(ot 'Hello') # False, becouse non empty strings are tru
print(not 0) # True, becouse 0 is falsy
print(not 1) # False, bacause 1 is truthy
print(not False) # True, because false is falsy
print(not True) # False, because True is truthy

is_admin = False

if not is_admin:
    print('Access denied for non-administrators')
else:
    print('Welcome, Administrator')

