# Q1
# Write a program that reads in colours_20_simple.csv and print each line of the colour
# data one by one as a string. Use spaces to separate the columns insead of commas.
import csv
with open(file="colours_20_simple.csv") as csv_file:
    csv_file = csv_file.readlines()
    csv_data=[]
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        print(line[0],line[1],line[2])


# Q2
# Write a program that reads in colours_20_simple.csv and outputs the colour data in
# order English, Hex then RGB
# with open(file="colours_20_simple.csv") as file:
#     file = file.readlines()
#     reader = csv.DictReader(file)
#     for row in reader:
#         print (f"{list(row.values())[2]}, {list(row.keys())[1]}: {list(row.values())[1]}, {list(row.keys())[0]}: {list(row.values())[0]}")
# # 
import csv
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row
        data = [dict(zip(headers, row)) for row in reader]
        return data
    
def order_data(data):
        data = read_csv(data)
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
# for row in formatted_data:
#     print(row)


# Q3
# Write a program that takes a csv file describing colours, and outputs the number of
# times each of the following colours appears in the English Name
