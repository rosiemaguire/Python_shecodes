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
with open(file="colours_20_simple.csv") as file:
    file = file.readlines()
    reader = csv.DictReader(file)
    for row in reader:
        print (f"{list(row.values())[2]}, {list(row.keys())[1]}: {list(row.values())[1]}, {list(row.keys())[0]}: {list(row.values())[0]}")