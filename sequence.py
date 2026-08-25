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

# append() method adds an element to the end of a list to a nested list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  #[1, 2, 3, 4, 5, 6]
print(numbers)  #[1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
even = [6, 8, 10]
numbers.extend(even)  #[1, 2, 3, 4, 5, [6, 8, 10]]
print(numbers)  #[1, 2, 3, 4, 5, [6, 8, 10]]

# extend() method adds multiple elements from ane list to another list
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.extend(even_numbers)  #[1, 2, 3, 4, 5, 6, 8, 10]
print(numbers)  #[1, 2, 3, 4, 5, 6, 8, 10]

# insert method inserts an element at a specific index in a list
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5) # inserts 2.5 at index 2
print(numbers)  #[1, 2, 2.5, 3, 4, 5]

# remove() removes an element from a list and takes value as argument
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)  # removes 3 from the list
print(numbers)  #[1, 2, 4, 5]

# pop() removes element at a specific index and returns the removed element. If no index is specified, it removes the last element.
numbers = [1, 2, 3, 4, 5]
removed_element = numbers.pop(2)  # removes element at index 2 (3)  
print(removed_element)  #3
print(numbers)  #[1, 2, 4, 5]

numbers = [1, 2, 3, 4, 5]
removed_element = numbers.pop()  # removes last element (5)
print(removed_element)  #5
print(numbers)  #[1, 2, 3, 4]

# clear() method removes all elements from a list
numbers = [1, 2, 3, 4, 5]   
numbers.clear()  # removes all elements from the list
print(numbers)  #[]

# sort() method sorts the elements of a list in ascending order by default. It can also take a reverse argument to sort in descending order.
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # sorts the list in ascending order
print(numbers)  #[1, 2, 5, 5, 6, 9]

numbers.sort(reverse=True)  # sorts the list in descending order
print(numbers)  #[9, 6, 5, 5, 2, 1]

# sorted() function returns a new sorted list from the elements of any iterable.
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # returns a new sorted list in ascending order
print(sorted_numbers)  #[1, 2, 5, 5, 6, 9]
print(numbers)  #[5, 2, 9, 1, 5, 6] # original list remains unchanged

# reverse() method reverses the elements of a list in place.
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()
print(numbers)  #[1, 2, 3, 4, 5, 6]

# index() method returns the index of the first occurrence of a specified value in a list.
programming_languages = ['Python', 'Java', 'C++', 'JavaScript']
index_of_java = programming_languages.index('Java')  # returns the index of 'Java'
print(index_of_java)  #1

''' Tuples are python data types that are similar to lists 
but are immutable. They are defined using parentheses () 
and can contain elements of different data types. 
Tuples support indexing and slicing, just like lists.'''

developer = ('Alice', 34, 'Rust Developer')
developer[1]  #34. Accessing the second element of the tuple using zero-based indexing
developer[-2] #34. Accessing the second element of the tuple using negative indexing

# create a tuple using the tuple() constructor
numbers = (1, 2, 3, 4, 5)   
tuple_from_list = tuple(numbers)  # creates a tuple from a list
print(tuple_from_list)  #(1, 2, 3, 4, 5)

developer = 'jessicca'
tuple(developer)  #('j', 'e', 's', 's', 'i', 'c', 'c', 'a') 

# check if an item is present in a tuple using 'in' operator
programming_languages = ('Python', 'Java', 'C++', 'JavaScript')
'Python' in programming_languages  #True
'Ruby' in programming_languages  #False 

# unpacking tuple elements into variables
developer = ('Alice', 34, 'Rust Developer')
name, age, profession = developer
print(name)  #'Alice'
print(age)
print(profession)  #'Rust Developer'

# collecting remaining elements of a tuple into a single variable using * operator
developer = ('Alice', 34, 'Rust Developer', 'Software Engineer')
name, age, *details = developer
print(name)  #'Alice'
print(age)  #34
print(details)  #['Rust Developer', 'Software Engineer']

# slicing operation on tuples
desserts = ('cake', 'ice cream', 'cookies', 'brownies', 'pie')
desserts[1:3]  #('ice cream', 'cookies')
desserts[:2]  #('cake', 'ice cream')
desserts[2:5]  #('cookies', 'brownies', 'pie')

# tuple methods
programming_languages = ('Python', 'Java', 'C++', 'JavaScript', 'Python')
programming_languages.count('Python')  #2. count() method returns the number of occurrences of a specified value in a tuple.
programming_languages.count('Go')  #0. count() method returns 0 if the specified value is not found in the tuple.
#programming_languages.count() #TypeError: count() takes exactly one argument (0 given). count() method requires one argument, which is the value to be counted in the tuple.
programming_languages.index('Java')  #1. index() method returns the index of the first occurrence of a specified value in a tuple.
#programming_languages.index('Go')  #ValueError: tuple.index(x): x not in tuple. index() method raises a ValueError if the specified value is not found in the tuple.
programming_languages.index('python', 3)  #4. index() method can take an optional start argument to specify the starting index for the search.
programming_languages.index
# sorted() function can be used to sort the elements of a tuple and return a new sorted list.
numbers = (5, 2, 9, 1, 5, 6)
sorted_numbers = sorted(numbers)  # returns a new sorted list in ascending order
print(sorted_numbers)  #[1, 2, 5, 5, 6, 9]
programming_languages = ('Python', 'Java', 'C++', 'JavaScript')
sorted(programming_languages, key=len)  # sorts the tuple elements based on their length and returns a new sorted list
print(sorted(programming_languages, reverse=True))  # sorts the tuple elements in reverse alphabetical order and returns a new sorted list