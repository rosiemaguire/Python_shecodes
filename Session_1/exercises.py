# Q1: Write a program that takes two numbers from the user,and outputs their sum.
def first_function():
  first_number = float(input("Enter a number: "))
  second_number = float(input("Enter another number: "))
  print(first_number + second_number)

# first_function()

# Q2: Write a program that takes two numbers from the user,and outputs the equation representing the multiplication ofthe two numbers.
def second_function():
  first_number = float(input("Enter a number: "))
  second_number = float(input("Enter another number: "))
  print(f"{first_number} + {second_number} = {first_number + second_number}")

# second_function()

# Q3: Write a program that takes a distance in kilometers fromthe user, and output the distance in meters and centimeters.
def third_function():
  km = float(input("How many kilometres? "))
  print(f"{km}km = {int(km * 1000)}m")
  print(f"{km}km = {int(km * 100000)}cm")

# third_function()

# Q4: Write a program that takes the user's name and height(in centimeters), and outputs a summary sentence.
def fourth_function():
  name = input("What is your name? ")
  height = input("How tall are you (cms)? ")
  print(f"{name} is {height}cms tall.")

# fourth_function()


def your_age():
  import datetime
  get_date = datetime.date.today()
  current_year = get_date.year
  birth_year = input("What year were you born? ")
  print(f"You are (turning) {current_year-int(birth_year)} years old this year.")

your_age()