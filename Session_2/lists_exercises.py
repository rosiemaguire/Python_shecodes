def foods():
    foods = [
        "orange",
        "apple",
        "banana",
        "strawberry",
        "grape",
        "blueberry",
        ["carrot", "cauliflower", "pumpkin"],
        "passionfruit",
        "mango",
        "kiwifruit",
    ]
    # First item in list
    print(foods[0])
    # The third item in the list.
    print(foods[2])
    # The last item in the list.
    print(foods[-1])
    # The first three items in the list.
    print(foods[:3])
    # The last three items in the list.
    print(foods[-3:])
    # The last item in the sublist
    print(foods[-4][-1])


foods()


# Format and print the contents of the following list so that the output appears as depicted:
# A little bit of Monica in my life
# A little bit of Erica by my side;
# A little bit of Rita's all I need;
# A little bit of Tina's what I see;
# A little bit of Sandra in the sun;
# A little bit of Mary having fun;
# A little bit of Jessica, here I am;
# A little bit of you makes me your man (ah!)
# *trumpet solo*
def mambo_number_5():
    mambo_number_5 = [
        ["Monica", "in my life"],
        ["Erica", "by my side"],
        ["Rita's", "all I need"],
        ["Tina's", "what I see"],
        ["Sandra", "in the sun"],
        ["Mary", "having fun"],
        ["Jessica", "here I am"],
    ]
    lyrics = ""
    for mambo in mambo_number_5:
        lyrics += f"A little bit of {mambo[0]} {mambo[1]};\n"
    print(f"{lyrics}A little bit of you makes me your man (ah!)\n*trumpet solo*")


mambo_number_5()

# Ask the user for three names. Add each name to a list, and then print the list.


def names():
    names = []
    while len(names) < 3:
        names.append(input("Please provide a name: "))
    print(names)


names()

# Use the following starter code:
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# d = []
# e = []
# Print the following lists:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


def list_concatenation():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    d = []
    e = []
    d.extend([a, b, c])
    for list in d:
        for l in list:
            e.append(l)
    for list in [a, b, c, d, e]:
        print(list)


list_concatenation()
