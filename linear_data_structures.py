""" Big O notation. worst case performance regardless of input."""

# 0(1) constant time complexity.
""" Takes same amount of time to run, regardless of input size.
"""
def check_even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

""" Pseudocode
is a high level description of the algorithms logic that is generic in nature and is not based on any programming language"""

# reverse string
GET original_string

SET reversed_string = ''

For EACH character IN original_string:
    ADD charater TO THE BEGINNING OF THE reversed_string

DISPLAY THE reversed_string

""" Dynamic array can grow and 
shrink automatically.
"""
# built-in list works as a dynamic array.

numbers = [3, 4, 5, 6]
print(numbers[0])
print(numbers[3])

numbers[2] = 16 # Update a value
numbers.append(7) # updating elements
numbers.insert(3, 15) # Inserting element at specic index(3 is index)
numbers.pop(2) # Removing element at specific index. if no index, remove first element. 

# Hash Tables

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, Str):
        return sum(ord(char) for char in Str)

    def add(self, k, v):
        h = self.hash(k)
        if h not in self.collection:
            self.collection[h] = {}
            self.collection[h][k] = v

    def remove(self, k):
        h = self.hash(k)
        if h in self.collection and k in self.collection[h]:
            del self.collection[h][k]

    def lookup(self, k):
        h = self.hash(k)
        if h not in self.collection:
            return Noreturn self.collection[h].get(k)