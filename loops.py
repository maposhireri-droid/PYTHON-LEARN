'''They are used to repeat a block of code multiple times.
In Python, there are two main types of loops:
 for loops and while loops.'''

# for loop is used to iterate over a sequence (like a list, tuple, or string)
# and execute a block of code for each item in the sequence.

programming_languages = ['Python', 'Java', 'C++', 'JavaScript']
for language in programming_languages:
    print(language)  # prints each programming language in the list

# iterating over a string
for char in 'Hello':
    print(char)  # prints each character in the string

# nested for loop
'''the inner loop will run completely for each iteration of the outer loop.'''
categories = ['Fruits', 'Vegetables']
foods = ['Apple', 'Banana', 'Carrot', 'Broccoli']
for category in categories:
    for food in foods:
        print(category, food)  # prints each food item for each category

# while loop is used to execute a block of code 
# as long as a specified condition is true
# or until the condition becomes false.

secret_number = 3
guess = 0 # initialize guess to a value that is not equal to secret_number
while guess != secret_number:
    guess = int(input('Guess the number (1-5):')) # prompt the user to enter a guess
    if guess != secret_number:
        print('Wrong guess, try again!') # otherwise, if the guess is incorrect, print a message and continue the loop

print('You got it right! The secret number is', secret_number) # breaks out of the loop when the guess is correct

# Break statement is used to exit a loop prematurely, before the loop condition is false.   
developer_names = ['Alice', 'Bob', 'Charlie', 'David']

for developer in developer_names:
    if developer == 'Charlie':
        break  # exit the loop when the developer is 'Charlie'
    print(developer)  # prints the names of developers until 'Charlie' is encountered

# continue statement is used to skip the current iteration of a loop and move on to the next iteration.
developer_names = ['Alice', 'Bob', 'Charlie', 'David']

for developer in developer_names:
    if developer == 'Charlie':
        continue  # skip the current iteration when the developer is 'Charlie'
    print(developer)  # prints the names of developers, skipping 'Charlie'

# else clauses can be used with loops to specify a block of code that will be executed when the loop condition becomes false.
#or when the loop is exited normally (without a break statement).

words = ['sky', 'blue', 'green', 'red', 'yellow']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains a vowel: '{letter}'")
            break  # exit the inner loop when a vowel is found
    else:
        print(f"'{word}' has no vowels.")  # executed when the inner loop completes without finding a vowel

'''The range() function is used to generate a sequence of numbers/integers,
 which can be used in for loops to iterate a specific number of times.'''
# basic syntax of the range() function is:
#range(start, stop, step)  # generates a sequence of numbers from start to stop (exclusive), incrementing by ste

for num in range(3): # default start is 0, default step is 1
    print(num)  # prints numbers from 0 to 2

for num in range(1, 5):  # start is 1, stop is 5 (exclusive)
    print(num)  # prints numbers from 1 to 4

for num in range(2, 10, 2):  # start is 2, stop is 10 (exclusive), step is 2
    print(num)  # prints even numbers from 2 to 8

for num in range(40, 0, -10):  # start is 40, stop is 0 (exclusive), step is -10
    print(num)  # prints numbers from 40 to 10 in decrements of 10

numbers = list(range(2, 11, 2))
print(numbers)  # prints a list of even numbers from 2 to 10

# keep track of the index for each element
#one option is to create an index variable(counter) and increment it by 1 in each iteration of the loop.

languages = ['spanish', 'french', 'german', 'italian']

index = 0  # initialize index variable

for language in languages:
    print(f'index {index} and language {language}')  # prints the index and corresponding language
    index += 1  # increment the index variable by 1

# another option is to use the enumerate() function, 
# which returns both the index and the value of each item in the sequence as a tuple (index, value) during iteration.

languages = ['spanish', 'french', 'german', 'italian']

print(list(enumerate(languages)))  # returns a list of tuples containing the index and corresponding language

# refactoring the previous example using enumerate() function
languages = ['spanish', 'french', 'german', 'italian']

for index, language in enumerate(languages):
    print(f'index {index} and language {language}')  # prints the index and corresponding language

# enumerate() function also accepts an optional start parameter, which allows you to specify the starting index for enumeration.
languages = ['spanish', 'french', 'german', 'italian']

for index, language in enumerate(languages, start=1):  # start enumeration from 1
    print(f'index {index} and language {language}')  # prints the index and corresponding language

''' zip function is used to combine two or more sequences (like lists, tuples, or strings)
 into a single iterable object.'''

developers = ['Alice', 'Bob', 'Charlie']
ids = [101, 102, 103]

# zip() function with for loop to iterate over the combined sequences
# to iterate over developers and ids simultaneously, we can use the zip() function to combine the two lists into pairs of (developer, id).

developers = ['Alice', 'Bob', 'Charlie']
ids = [101, 102, 103]

for name, dev_id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')  # prints the name and corresponding ID of each 

# list comprehension is a concise way to create lists in Python using a single line of code.
# It consists of an expression followed by a for loop, and optionally, one or more if conditions. 
# The result is a new list containing the values generated by the expression for each item in the input sequence that satisfies the conditions.

even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)  # appends even numbers to the list
print(even_numbers)  # prints the list of even numbers from 0 to 20

# list comprehension can be used to achieve the same result in a more concise way:
even_numbers = [num for num in range(21) if num % 2 ==0]
print(even_numbers)  # prints the list of even numbers from 0 to 20

numbers = [1, 2, 3, 4, 5]
results = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(results)  # prints a list of tuples indicating whether each number is even or odd

# filter() function is used to filter elements from a sequence based on a specified condition.
# or creates a list starting from an existing iterable (like a list, tuple, or string) 
# and includes only those elements that satisfy the condition defined by a function.

words = ['sky', 'blue', 'green', 'red', 'yellow']

def is_long_word(word):
    return len(word) > 4  # returns True if the length of the word is greater than 4, otherwise returns False

long_words = list(filter(is_long_word, words))  # filters the words based on the condition defined in is_long_word function
print(long_words)  # prints the list of long words (words with more than 4

# map() function is used to apply a specified function to each item in a sequence (like a list, tuple, or string) 
# and return a new iterable with the results.

celcious = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32  # converts Celsius to Fahrenheit

fahrenheit = list(map(to_fahrenheit, celcious))  # applies the to_fahrenheit function to each item in the celcious list
print(fahrenheit)  # prints the list of temperatures in Fahrenheit

'''sum() function is used to calculate the sum of all the elements
 in a sequence (like a list, tuple, or set)
 or get the sum from an iterable object.'''

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # calculates the sum of all elements in the numbers list
print(total)  # prints the sum of the numbers (15)

# use can use startargument which sets the initial value for summation
# using start as positional argument
numbers = [5, 10, 15, 20]
total = sum(numbers, 10)  # calculates the sum of all elements in the numbers list, starting from 10 positional argument
print(total)  # prints the sum of the numbers (60)

# Using start as keyword argument
numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total)

'''Lambda functions'''
# upto now this is how i have been defining functions
def square(num):
    return num ** 2

print(square(4)) # 16

# an anonymous inline function
# refactoring the square function

lambda num: num ** 2 # no longer name square associated with the function

# using lambda in higher order function like this one
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

