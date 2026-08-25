developer = 'Devin'
print(type(developer)) # class string

my_integer = 10
print(type(my_integer)) # class int

my_float = 4.5
print(type(my_float)) # class float

my_string = "Hello, World!"
print(type(my_string)) # class string

my_boolean = True
print(type(my_boolean)) # class bool

my_set = {7, 'hello', 8.5}
print(type(my_set)) # class set

my_tuple = (7, 'hello', 8.5)
print(type(my_tuple)) # class tuple

my_range = range(5)
print(type(my_range)) # class range

my_list = [22, 'hello, world!', 3.14, True]
print(type(my_list)) # class list

my_dict = {'name': 'john', 'Age': 28}
print(type(my_dict)) # class dict

my_none = None
print(type(my_none)) # class NoneType

# checking the type of a variable using isinstance() function
print(isinstance(developer, str)) # True
print(isinstance(my_integer, int)) # True
print(isinstance(my_float, float)) # True
print(isinstance(my_boolean, bool)) # True
print(isinstance(my_set, set)) # True
print(isinstance(my_tuple, tuple)) # True
print(isinstance(my_range, range)) # True
print(isinstance(my_list, list)) # True
print(isinstance(my_dict, dict)) # True
print(isinstance(my_none, type(None))) # True

account_balance = 'hello    '
print(isinstance(account_balance, (int, float)))
