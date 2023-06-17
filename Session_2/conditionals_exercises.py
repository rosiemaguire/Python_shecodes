# Q1:
# Sara is a confident rock climber, but sometimes she forgets her helmet. Rei refuses to
# climb with Sara unless she's wearing a helmet, because That's Just Sensible.
# Write a program that sets the value for a boolean variable called sara_has_helmet, and
# then prints out a string indicating whether or not Rei is down to climb
def does_sara_have_her_helmet(sara_has_helmet):
    if sara_has_helmet:
        print("Let's send it!")
    else:
        print("No way, my brain is my moneymaker!")

# sara_has_helmet = False
# does_sara_have_her_helmet(sara_has_helmet)


# Q2
# Rei is a very careful climber, but sometimes she is forgetful. Even if Sara has a helmet,
# they still can't go climbing unless Rei remembers to bring her rope.
# Amend the previous program to add a check for the rope before you output the result.
def helmet_and_rope_to_climb(sara_has_helmet,rei_has_rope):
    if sara_has_helmet:
        if rei_has_rope:
            print("Let's send it!")
        else:
            print("Who's unprepared now, Rei??")
    elif rei_has_rope:
        print("No way, my brain is my moneymaker!")
    else:
        print("I guess let's just go hiking?")
sara_has_helmet = True
rei_has_rope = True
# helmet_and_rope_to_climb(sara_has_helmet, rei_has_rope)


# Q3
# Write a program that implements the algorithm for red light cameras. The program
# should print the string "Flash!" if (and only if) a car is detected driving while the light
# is red. If the light is green or amber, the program should print "Do nothing.", even
# when a car is detected.
def red_light_camera(light_colour,car_detected):
    if light_colour == "Red" and car_detected == True:
        print("Flash!")
    else:
        print("Do nothing.")      

# Q4
# Write a program that asks the user for their height, and determines whether or not
# they are tall enough to ride the rollercoaster, which has a height requirement of
# 120cms.
def min_rollercoaster_height(height):
    if height < 120:
        print("Sorry, not today.")
    else:
        print("Hop on!")

# Q5
# Write a program that asks the user to enter their username and password and output as
# uccess message if they are correct, or a failure message if they are incorrect. Your
# program has one user, whose username is "lucyg", and whose password is "quartzgleam?1".
def lucy_login(username,password):
    if username == "lucyg" and password == "quartzgleam?1":
        print("Logged in successfully")
    else:
        print("Access denied.")

# Q6
# Write a program that asks the user to enter their email address and checks whether it
# is valid or not. For the purpose of this exercise, you can make the assumption that an
# email address is valid if it contains a “@” symbol and a “.” symbol.
def valid_email (email):
    if "@" in email and "." in email:
        print("Email valid")
    else:
        print("Invalid email detected!")

# Q7
# Will this script print anything to the terminal? Have a think first, decide on your
# answer, and then try running it to see if your intuition was correct
if "False":
    print("A strange game. The only winning move is not to play.")

print(bool(""))
print(bool("Rosie"))