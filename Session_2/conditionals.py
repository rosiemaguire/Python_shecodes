#Boolean
# name = "Rosie"
# age = 29
# height = 1.63
# is_raining = True
# my_variable2 = False
# print(is_raining)
# print(type(is_raining))

# Boolean Expresions - Expressions that produce a boolean value
# Comparison Operators
# == is equal to
# != is not equal to 
# > greater than
# < less than
# >= greater than or equal to 
# <= less than or equal to 
# print(5 > 3)
# print (3.5 > 6.3)
# print("Rosie" == "rosie")

# Mathematical Operators - Addition, Division, Subtraction, Multiplcation
# Boolean Operators - not, and, or
is_sunny = True
is_warm = True

# print(not is_sunny)
# print(is_sunny and is_warm)
# print(is_sunny != is_warm)
# print(is_sunny or is_warm)


temperature = 18
# syntax / semantics
if temperature <= 18:
    print("Weather is too cold!") 
    print("I want to stay home.")
    # if the first condition/statement false, it will check elif
elif temperature > 28:
    print("Weather is too hot!")
else:
    print("Weather is nice!")


# print("My cat looks cute.")