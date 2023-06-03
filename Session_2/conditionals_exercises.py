def does_sara_have_her_helmet(sara_has_helmet):
    if sara_has_helmet:
        print("Let's send it!")
    else:
        print("No way, my brain is my moneymaker!")

# sara_has_helmet = False
# does_sara_have_her_helmet(sara_has_helmet)

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

def red_light_camera(light_colour,car_detected):
    if light_colour == "Red" and car_detected == True:
      print("Flash!")
    else:
        print("Do nothing.")      

def min_rollercoaster_height(height):
    if height < 120:
        print("Sorry, not today.")
    else:
        print("Hop on!")

def lucy_login(username,password):
    if username == "lucyg" and password == "quartzgleam?1":
        print("Logged in successfully")
    else:
        print("Access denied.")

def valid_email (email):
    if "@" in email and "." in email:
        print("Email valid")
    else:
        print("Invalid email detected!")


if "False":
    print("A strange game. The only winning move is not to play.")

print(bool(""))
print(bool("Rosie"))