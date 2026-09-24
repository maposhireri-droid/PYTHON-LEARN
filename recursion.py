""" Recursion is
a technique in which a function calls itself
"""
def recursive_countdown(number):
    if number < 1: # base case
        return 
    print(number)
    # moves it toward base case
    recursive_countdown(number - 1) # recursive case

recursive_countdown(5)

# Ascending order 
def recursive_countdown(number):
    if number < 1:
        return # base case reached
    recursive_countdown(number - 1)
    print(number)

recursive_countdown(5)

def recursive_countdown(number):
    print(f'Function call started for number: {number}')
    if number < 1:
        print('Base case reached')
        return
    print(f'Calling recursive_countdown with number: {number - 1}')
    recursive_countdown(number - 1)
    print(f'Function call completed for number: {number}')

recursive_countdown(3)

def countup(number):
    if number < 1:
        return []
    count_list = countup(number - 1)
    count_list.append(number)
    return count_list

print(countup(5))

# range of number generator
"""
Base case: if start_num is bigger than end_num, there's nothing left to count — return an empty list. This is what eventually stops the recursion.
Recursive case: otherwise, call the function again with start_num + 1, working toward the base case. This builds up a list for everything after the current number first.
Assembling the result: once that inner call returns, l holds the list for the smaller range. l.insert(0, start_num) puts the current start_num at the front of that list, then it's returned.
Example with range_of_numbers(2, 5):
calls range_of_numbers(3, 5) → calls range_of_numbers(4, 5) → calls range_of_numbers(5, 5) → calls range_of_numbers(6, 5)
6 > 5 is true, so that innermost call returns []
unwinding back up: [5] → [4, 5] → [3, 4, 5] → [2, 3, 4, 5]
So it counts up from start_num to end_num, building the list from the back end first, then inserting each number at the front as the calls return.
"""
def range_of_numbers(start_num, end_num):
    if start_num > end_num:
        return []
    i = range_of_numbers(start_num + 1, end_num)
    i.insert(0, start_num)
    return i 

# factorial
"""
the find_factorial function is called recursively until n reaches 0. When n is 0, the base case is reached and the function returns 1. The function then returns the product of n and the result of the recursive call to find_factorial(n - 1).
"""
def find_factorial(n):
    if n == 0:
        return 1
    return n * find_factorial(n - 1)                   
                                    
                                        