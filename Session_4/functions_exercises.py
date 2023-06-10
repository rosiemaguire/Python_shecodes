# Q1
# Write a function called get_integer that takes a string as its argument, 
# and uses that string to prompt the user to enter an integer. 
# Your function should return the integer supplied by the user.

def get_integer(string):
    return input(string)
prompt ="Could I please have an integer?: "
# Define your function here
# user_input = get_integer(prompt)
# print(f"So your integer is {user_input}? Thanks!")

# Q2
# Write a function called celcius_convert that takes a number representing the
# temperature in Farenheit as its argument, and returns a float representing the
# temperature in Celcius
degrees_f = 350 # Assign some number as the value here
# Define your function here
def celcius_convert(degrees_f):
    return 5/9 * (degrees_f - 32)

# print(celcius_convert(degrees_f))

# Q3
# Write a function that accepts one argument (an integer) and returns True when that
# argument is odd and False when that argument is even. 
degrees_f = -1
def is_odd(integer):
    return integer % 2 == 1
# print(is_odd(degrees_f))

# Q4
# Write a function that takes two arguments; the unit price of an item, and how many
# units were purchased. Return the total cost as a string.
def total_cost(unit_price, number_of_units):
    return "$" + str(unit_price * number_of_units)

print(total_cost(4.25, 3))