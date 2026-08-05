'''
sequence data types include strings, lists and tuples.
list
ordered sequence of elements that can be comprised of 
strings, numbers or other strings.
they are mutable and have zero-based indexing.'''

cities = ['Los Angeles', 'New York', 'Chicago', 'Houston', 'Phoenix']
# Accessing first element of cities list using zero-based indexing
cities[0]  #'Los Angeles'. 
cities[-1]  #'Phoenix'. last element of cities list using negative indexing

# creating list from list() constructor
# used to covert an iterable into a list
develop = 'Jessica'
list(develop)  #['J', 'e', 's', 's', 'i', 'c', 'a']

# no. of items in a list can be found using len() function
len(cities)  #5

#updating a value at a particular index in a list
cities[1] = 'San Francisco'  #['Los Angeles', 'San Francisco', 'Chicago', 'Houston', 'Phoenix']

# remove an item from a list using del() function
del cities[2]  #['Los Angeles', 'San Francisco', 'Houston', 'Phoenix']

# checking if an item is present in a list using 'in' operator
'Los Angeles' in cities  #True
'Seattle' in cities  #False

# Accessing nested list elements using indexing
nested_list = [1, 2, [3, 4, 5], 6]
nested_list[2]  #[3, 4, 5]
nested_list[2][1]  #4

# unpacking list elements into variables
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  #1 2 3

numbers = [1, 2, 3]
a, *rest = numbers
print(a)  #1
print(rest)  #[2, 3]

# Slice operation on lists
numbers = [1, 2, 3, 4, 5]
numbers[1:4]  #[2, 3, 4]
numbers[:3]  #[1, 2, 3]
numbers[3:5]  #[4, 5]
numbers[::2]  #[1, 3, 5] # optional step argument interval
numbers[::-1]  #[5, 4, 3, 2, 1] # default step argument is 1, negative step argument reverses the list
