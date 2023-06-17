import csv
print("Question 1")
# Q1
# Write a program that reads in colours_20_simple.csv and print each line of the colour
# data one by one as a string. Use spaces to separate the columns insead of commas.
def read_csv(file):
    with open(file) as file:
        reader = csv.reader(file)
        csv_data = []
        for row in reader:
            csv_data.append(row)
        return csv_data

def read_data_line_as_string(data_list):
    data_string = ''
    for data in data_list:
        if data == data_list[-1]:
            data_string += ' '.join(data)
        else:
            data_string += ' '.join(data) +"\n"
    return data_string

data = read_csv("colours_20_simple.csv")
print(read_data_line_as_string(data))


print("\n Question 2")
# Q2
# Write a program that reads in colours_20_simple.csv and outputs the colour data in
# order English, Hex then RGB
# with open(file="colours_20_simple.csv") as file:
#     file = file.readlines()
#     reader = csv.DictReader(file)
#     for row in reader:
#         print (f"{list(row.values())[2]}, {list(row.keys())[1]}: {list(row.values())[1]}, {list(row.keys())[0]}: {list(row.values())[0]}")

def read_csv_as_dict(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        data = [dict(zip(headers, row)) for row in reader]
        return data
    
def order_data(data):
        data = read_csv_as_dict(data)
        desired_order = ['English','HEX','RGB']
        reordered_data = []
        for row in data:
            reordered_dict = {k: row[k] for k in desired_order}
            reordered_data.append(reordered_dict)
        return reordered_data

def format_row_data(data):
    data = order_data(data)
    formatted_data = []
    for row in data:
        formatted_row = ', '.join(f'{header}: {value}' for header, value in row.items())
        remove_first_key = formatted_row[formatted_row.index(':')+1:len(formatted_row)]
        formatted_data.append(remove_first_key)
    return formatted_data

formatted_data = format_row_data('./colours_20_simple.csv')
for row in formatted_data:
    print(row)

print("\n Question 3")
# Q3
# Write a program that takes a csv file describing colours, and outputs the number of
# times each of the following colours appears in the English Name
# red, green, blue, yellow
# first option only grabs full colour name if colour makes up entire string
def solo_colour_string(file, colours):
    with open(file) as file:
        colours_2 = []
        file = csv.reader(file)
        for f in file:
            colours_2+=(f[2].split())
        colour_dict = {colour:0 for colour in colours}
        lowercase_colours =[]
        for colour in colours_2:
            lowercase_colours.append(colour.lower())    
        for colour in colours:
            colour_dict[colour]=lowercase_colours.count(colour.lower())
        return colour_dict
print(solo_colour_string("colours_865.csv",["red","green","blue","yellow"]))

# second option grabs if colour name exists in string in list of colours
def colour_exists_in_string (file,colours):
    with open(file) as file:
        colours_2 = []
        file = csv.reader(file)
        for f in file:
            colours_2+=(f[2].split())
        colour_dict = {colour:0 for colour in colours}
        lowercase_colours =[]
        for colour in colours_2:
            lowercase_colours.append(colour.lower())    
        for colour in colours:
            colour_dict[colour]=sum(s.count(colour.lower()) for s in lowercase_colours)
        return colour_dict
print(colour_exists_in_string("colours_865.csv",["red","green","blue","yellow"]))

print("\n Question 4")
# Q4
# galaxies.csv contains data about 82 different galaxies and their velocities (km/sec).
# Using this data, print a string showing the galaxy with the slowest velocity, and
# another showing the galaxy with the highest velocity

def get_nested_list_by_index(list_of_lists, index):
    nested_list = []
    for items in list_of_lists:
        nested_list.append(int(items[index]))
    return nested_list

def get_galaxy(galaxies_list,velocity):
    for row in range(0, len(galaxies_list)):
        if (int(galaxies_list[row][1])) == velocity:
            galaxy = galaxies_list[row]
        else:
            pass
    return galaxy

galaxies_list = read_csv("galaxies.csv")
slowest = min(get_nested_list_by_index(galaxies_list,1))
fastest = max(get_nested_list_by_index(galaxies_list,1))
slowest_galaxy = get_galaxy(galaxies_list,slowest)
fastest_galaxy = get_galaxy(galaxies_list,fastest)

print(f"Galaxy {slowest_galaxy[0]} has the min velocity of {slowest_galaxy[1]}km/sec.")
print(f"Galaxy {fastest_galaxy[0]} has the max velocity of {fastest_galaxy[1]}km/sec.")