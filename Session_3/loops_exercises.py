# # Continuously ask the user to enter a number until they provide a blank input. Outputthe sum of all the numbers.
number = input("Enter a number: ")
total = 0
while number:
      try:
            total+=int(float(number))
            number = input("Enter a number: ")
      except ValueError:
            total+=0
            break
print(total)

# Ask the user to enter a in integer number.
# Print all the odd numbers between 0 and that number (inclusive).
odd_numbers = []
number = int(input("Enter a number: "))+1
count = 0
while count < number:
      if count % 2 == 1:
            odd_numbers.append(count)
            count+=1
      else:
            count+=1
print(odd_numbers)

# Write a guessing game.Select a number, and save it as a variable in your code.
# Ask the user to enter a number, and then output whether their number is less than or greater than the
# selected number. Keep asking until the user guesses the correct number.
# Then print a congratulatatory message.
import random

secret_number = random.randint(0, 101)
while True:
      try:
            number_guess = int(input("Guess the secret number: "))
            break
      except ValueError:
            print("I'm sorry, I do not understand. Please guess an integer. ")
while number_guess != secret_number:
      if number_guess > secret_number:
            try:
                  number_guess = int(input("My number is lower than your guess. Try again! "))
                  break
            except ValueError:
                  print("I'm sorry, I do not understand. Please guess an integer. ")
      else:
            try:
                  number_guess = int(input("My number is higher than your guess. Try again! "))
            except ValueError:
                  print("I'm sorry, I do not understand. Please guess an integer. ")
print(f"Congratulations! You guessed my secret number: {secret_number}!")

# Ask the user for a number. Use a for loop to print the times tables for that number,up to ten
multiplication_number = input("Enter a number: ")
for i in range(1,11):
      print(f"{multiplication_number} * {i} = {int(multiplication_number) * i}")

# Ask the user for an integer. Using a for loop, add up every number from 0 up to that integer, and print the result.
number = int(input("Enter a number: "))
total = 0
for num in range(0,number +1):
      total += num
print(total)

# Save a list of numbers to a variable in your script,
# and then use a for loop to print the sum of all the numbers in the list
numbers = [3,5,8,10,7]
total = 0
for number in numbers:
      total+=number
print(total)


groceries = [
      ["Baby Spinach", 2.78],
      ["Hot Chocolate", 3.70],
      ["BBQ Shapes", 9.00],
      ["Bread", 2.10],
      ["Carrots", 0.56],
      ["Oranges", 3.08],
]
total = 0
for grocery in groceries:
      quantity = int(input(f"Please enter the quanity for {grocery[0]}: ")) * grocery[1] 
      total += quantity
print(round(total,2))

# Let's improve the guessing game you wrote in Q3 of the while loop exercises. 
# Update the code so that when the game ends, the program asks the player if they would 
# like to play again. If they input "no", the game ends, but with any other input the game
# begins again.

# import random

# secret_number = random.randint(0, 101)
# while True:
#       try:
#             number_guess = int(input("Guess the secret number: "))
#             break
#       except ValueError:
#             print("I'm sorry, I do not understand. Please guess an integer. ")
# while number_guess != secret_number:
#       if number_guess > secret_number:
#             try:
#                   number_guess = int(input("My number is lower than your guess. Try again! "))
#                   break
#             except ValueError:
#                   print("I'm sorry, I do not understand. Please guess an integer. ")
#       else:
#             try:
#                   number_guess = int(input("My number is higher than your guess. Try again! "))
#             except ValueError:
#                   print("I'm sorry, I do not understand. Please guess an integer. ")
# print(f"Congratulations! You guessed my secret number: {secret_number}!")