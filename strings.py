my_str_1 = "it is a sunny day" # single line string
my_str_2 = 'it is a sunny day' # single line string
my_str_3 = """multiline
string""" # multiline string
my_str_4 = "it's a sunny day" # single line string with apostrophe
my_str_5 = '"hello world"' # single line string with double quotes
mystr_6 = 'it\'s a sunny day' # single line string with escaped apostrophe
my_str_7 = "\"hello world\"" # single line string with escaped double quotes

# if strin contains one or more characters.
my_str = "Hello, World"

print('Hello' in my_str) # True
print('hey' in my_str) # False
print('hi' in my_str) # False
print('e' in my_str) # True
print('e' in my_str) # True
print('f' in my_str) # False

my_st = 'Hello world'
print(len(my_st)) # 11
print(my_st[0]) # H
print(my_st[6]) # w
print(my_st[-1]) # d
print(my_st[-2]) # l

# strings are immutable in python programming language.
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

greeting = 'hi'
#greeting[0] = 'H' # TypeError: 'str' object does not

# string concatenation in python programming language.
my_str_1 = 'Hello'
my_str_2 = 'World'

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# repeating a string in python programming language.
sound = 'ha'
repeated_sound = sound * 3

# concatenating a string with a number in python programming language
name = 'John'
age = 25

name_and_age = name + ' ' + str(age)
print(name_and_age) 

# augmented assignment operator
name = 'richard'
age = 28

name_and_age =name
name_and_age += str(age)

print(name_and_age)

# string interpolation
name = 'john doe'
age = 28
name_and_age = f'My name is {name} and I am {age} years old.'
print(name_and_age)

num1 = 10
num2 = 20
print(f'The sum of {num1} and {num2} is {num1 + num2}.') # The sum of 10 and 20 is 30.

#string slicing in python programming language.
my_str = 'Hello World!'
print(my_str[1:4]) # ell
print(my_str[:7])
print(my_str[8:]) # orld!
print(my_str[:]) 
print(my_str[0:11:2]) # HloWrd
print(my_str[::2]) # HloWrd
print(my_str[::-1]) # !dlroW olleH and reverse the string.

# string methods in python programming language.
my_str = 'Hello World!'
uppercase_my_str = my_str.upper()
print(uppercase_my_str) # HELLO WORLD!

my_str = 'HELLO WORLD!'
lowercase_my_str = my_str.lower()
print(lowercase_my_str) # hello world!

my_str = '  Hello World!    '
trimmed_my_str = my_str.strip() # remove leading and trailing whitespace
print(trimmed_my_str) # Hello World!

my_str = 'Hello World!'
replaced_my_str = my_str.replace('hello', 'hi') # replace 'hello' with 'hi'
print(replaced_my_str) # hi World!

my_str = 'Hello World!'
split_words = my_str.split() # split the string into a list of words
print(split_words) # ['Hello', 'World!']

my_list = ['Hello', 'World!']
joined_my_str = ' '.join(my_list) # join the list of words into a string
print(joined_my_str) # Hello World!

my_str = 'Hello World!'
starts_with_hello = my_str.startswith('Hello') # check if the string starts with 'Hello'
print(starts_with_hello) # True

my_str = 'Hello World!'
ends_with_world = my_str.endswith('World!') # check if the string ends with 'World!'
print(ends_with_world) # True

my_str = 'Hello World'
world_index = my_str.find('World') # find the index of 'World' in the string
print(world_index)

my_str = 'Hello World'
o_count = my_str.count('o') # count the number of occurrences of 'o' in the string
print(o_count) # 2

my_str = 'Hello World'
capitalized_my_str = my_str.capitalize() # capitalize the first letter of the string
print(capitalized_my_str) # Hello world

my_str = 'hello world'
is_all_upper = my_str.isupper() # check if all characters in the string are uppercase
print(is_all_upper) # False

my_str = 'hello world'
is_all_lower = my_str.islower() # check if all characters in the string are lowercase
print(is_all_lower) # True

my_str = 'hello world'
tittle_case_my_str = my_str.title() # convert the first letter of each word to uppercase
print(tittle_case_my_str) # Hello World 

# Add content to end of an existing string variable
greetings = 'Hello'
greetings += 'world'
print(greetings) # Helloworld