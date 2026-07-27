my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition: ', float_addition) # Float addition

float_multiplication = my_float_1 * my_float_2
print('Float Multiplication: ', float_multiplication) # Float multiplication

float_division = my_float_1 / my_float_2
print('Float division: ', float_division) # Float division

my_int = 56
my_float = 5.4

sum_int_float = my_int + my_float
print(sum_int_float) # Addition of integer and float
print(type(sum_int_float)) # Always a float

my_int_1 = 56
my_int_2 = 12

my_float_1 =5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2 # Modulus
mod_floats = my_float_1 % my_float_2 # Modulus

print('Integer Modulo: ', mod_ints)
print('Float Modulo: ', mod_floats)

floor_div_ints = my_int_1 // my_int_2 # Floor Division
floor_div_floats = my_float_1 // my_float_2 # Floor Division

exp_int = my_int_1 ** my_int_2 # Exponentiation
exp_float = my_float_1 ** my_float_2 # Exponentiation

print('Integer Exponentiation: ', exp_int)
print('Float Exponentiation: ', exp_float)

my_int = 12
my_float = 5.4

my_float = float(my_int) # Type Casting from Integer to Float
print('Type Casting from Integer to Float: ', my_float) 

my_int = 56
my_flaot = float(my_int) # Type Casting from Integer to Float
print('Type Casting from Integer to Float: ', my_float) 

my_str_int = '56'
my_str_float = '7.8'

converted_int = int(my_str_int) # Type Casting from String to Integer
converted_float = float(my_str_float) # Type Casting from String to Float   

my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1) # Rounding off the float to nearest integer
rounded_int_2 = round(my_int_2, 1) # Rounding off the float to nearest integer
print('Rounded Integer 1: ', rounded_int_1)
print('Rounded Integer 2: ', rounded_int_2)

num = -15

absolute_value = abs(num) # Absolute value of a number
print('Absolute Value: ', absolute_value) # 15

result_1 = pow(2, 3) # 2 raised to the power of 3
print('Power Result: ', result_1) # 8

result_2 = pow(2, 3, 5) # 2 raised to the power of 3 and then modulo 5
print('Power Result with Modulo: ', result_2) # 3       