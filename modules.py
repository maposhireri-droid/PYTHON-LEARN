''' These are libraries that are like
toolbox for developers in software development.'''

# importing a module
#import module_name

import math

# calling a function from module in your python script
#module_name.function_name()

math.sqrt(36)

# importing the module as an alias
# import module_name as module alias

import math as m

m.sqrt(36)

# Importing specific functions or classes from a module and not everything
# from module import name1, name2
# if you want to use aliases on them
# from module import name1 as alias1, name2 as alias2
# you can call these functions directly in your code without module name prefix.

from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value)
print(cos_value)

# Import everything and no need to use the name of the module as prefix
# from module_name import *

from math import *
print(sqrt(36))
print(pow(5, 2))
print(exp(1))

# accessing constant from math module
import math
print(math.pi)  # pi is a constant from the math module

# Accessing a class from datetime module
import datetime
birthday = datetime.date(1959, 7, 15)
print(birthday.day)
print(birthday.month)
print(birthday.year)