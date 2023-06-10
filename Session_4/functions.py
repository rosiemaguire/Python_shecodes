# Function - an activity that is natural to or the purpose of a person or thing.
# Functions we've already seen
# input(), len(), int(), print() #

# name = input("What is your name?")
# age = input("How old are you?")
# if age >= 18:
#     print("Welcome")
# else:
#     print("You cannot enter.")

# Function definition
# Task Separation
def ask_user_name():
    # print("Now function is entered")
    name = input("What is your name? ")
    print("Hey fam")
    return name
    print("Hello") # doesn't get executed - nothing does after "return"

# print("Hello")
# ask_user_name()
# print("Hi")

# print(ask_user_name())

# answer = ask_user_name()
# print(answer)


def ask_user_age():
    age = input("How old are you?")
    if age >= 18:
        print("Welcome")
    else:
        print("You cannot enter.")
    return age

# Parameters
total = 0 # Global variable
def add(number1,number2): # at this point these two variables are created, but have no value: number1 = , number2 =
    # print(total) # Global variables can be called on inside functions
    # result = number1 + number2 # result is a local variable
    return number1 + number2

print(total) # Global variables can also be called on outside of functions

answer = add(2,3)
print(answer)
# print(result) # Local varaible: Local to the function it's created in and does not exist outside of the function - this will return an error if called outside of the function