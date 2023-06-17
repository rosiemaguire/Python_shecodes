import sys
sys.path.append("..")

print("Question 1")
# Q1
# The dictionary below represents the cost of individual items in a supermarket. Write a
# program that asks the user how many of each item they would like in turn, and outputs
# the total cost of their groceries
groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Coffee": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}


def grocery_shop(groceries):
    total = 0
    for grocery in groceries.items():
        quantity = (
            int(input(f"Please enter the quanity for {grocery[0]}: ")) * grocery[1]
        )
        total += quantity
    return round(total, 2)

# print(f"Your total shop today comes to ${grocery_shop(groceries)}.")

print("\n Question 2")
# Q2
# In the last lesson, you wrote a program that counted the number of colour names in
# the colours_865.csv file.
# Try rewriting this program so that instead of using separate variables to keep track of
# the number of times each colour name appears, it uses a single dictionary instead.
# Here's a dictionary to get you started:
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}

import csv
def read_csv(file):
    with open(file) as file:
        reader = csv.reader(file)
        csv_data = []
        for row in reader:
            csv_data.append(row)
    return csv_data

def get_item_from_list_by_index(some_list,index):
    item_from_list = []
    for item in some_list:
        if all(isinstance(item, str) for item in some_list):
            item_from_list += (item[index].split())
        else:
            item_from_list.append(item[index])
    return item_from_list

# returns count if string exists as word or partial word
def check_partial_string_exists(file, dictionary):
    lowercase_strings =[]
    for string in file:
        lowercase_strings.append(string.lower()) 
    for key in dictionary:
        dictionary[key] = sum(item.count(key.lower()) for item in lowercase_strings)
    return dictionary

# returns count if string exists as whole word
def check_full_string_exists(file, dictionary):
    lowercase_strings =[]
    for string in file:
        lowercase_strings.append(string.lower()) 
    for key in dictionary:
        dictionary[key] = lowercase_strings.count(key.lower())
    return dictionary

data = read_csv("../Session_5/colours_865.csv")
colour_names = get_item_from_list_by_index(data,2)
print(check_partial_string_exists(colour_names,colour_counts))
print(check_full_string_exists(colour_names,colour_counts))

print("\n Question 3")
# Q3
# Read the colour data from colours_20_simple.csv 
# and save the data in a dictionary where each key is a hex code and each value is the
# corresponding English name
colours_20 = read_csv("../Session_5/colours_20_simple.csv")

def make_hexcode_colour_dictionary(file):
    hex_code_dict ={}
    for row in file:
        if row == file[0]:
            pass
        else:
            hex_code_dict[row[1]] = row[2]
    return hex_code_dict

print(make_hexcode_colour_dictionary(colours_20))

print("\n Question 4")
# Q4
# Modify your code from the previous exercise to save both the English name and RGB
# code in a list as the value for the corresponding hex code.
def make_hexcode_colour_and_RGB_dictionary(file):
    hex_code_dict ={}
    for row in file:
        if row == file[0]:
            pass
        else:
            hex_code_dict[row[1]] = [row[0], row[2]]
    return hex_code_dict

print(make_hexcode_colour_and_RGB_dictionary(colours_20))

print("\n Question 5")
# Q5 (Extra Tricky)
# Modify your code from the previous exercise to save both the English name and RGB
# code in a dictionary as the value for the corresponding hex code

def hexcode_dictionary(file):
    hex_code_dict ={}
    # separate the headers to use as keys for the temporary dictionary
    header_keys = file[0]

    # create a temporary dictionary using 'HEX', 'English' and 'RGB' as the keys and all 
    # subsequent rows as values
    temp_dict = [dict(zip(header_keys, row)) for row in file[1:]]

    # update hex_code_dict to have hex code value as key and corresponding colour data
    # from temp_dict as the values
    for dictionary in temp_dict:
        hex_code_dict[dictionary["HEX"]] = dict(dictionary.items())
    
    # remove hex code key & value pair from dictionary of values for each key value pair
    for key,value in hex_code_dict.items():
        del value["HEX"]
    return(hex_code_dict)

print(hexcode_dictionary(colours_20))
