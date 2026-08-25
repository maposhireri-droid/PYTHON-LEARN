'''Sets are one of python built-in
data structures.'''

# Example of a set of numbers

my_set = {1, 2, 3, 4, 5}

# define empty set
set()

# Adding element to a set
my_set.add(6)
print(my_set)

# remove element from set
my_set.remove(4)
my_set.discard(4)

# remove all elements from sets
my_set.clear()

# subsets and supersets

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set))
print(my_set.issuperset(your_set))

# is disjoint() methods checks if they dont have elements in common.
print(my_set.isdisjoint(your_set))

# Union operator | returns a new set with all elements from both sets
s = my_set | your_set
print(s)

# intersection operator returns a set with only the elements that the sets have in common
c = my_set & your_set
print(c)

# difference operator returns a new set with the elements of the first set not in other sets
d = my_set - your_set
print(d)

# symmetric operator returns a new set with the elements that
# are either in the first or second set, but not in both
sd = my_set ^ your_set
print(sd)

# compound assignment operator 
#|= &= -= ^=

my_set -= your_set
print(my_set)

# in operator checks if an element is in a set or not
print(5 in my_set)

