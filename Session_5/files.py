import csv

with open(file="dogs_are_awesome.csv", mode="r", encoding="utf-8") as my_file:
# with open(file="dogs_are_awesome.csv") as my_file:
#Both lines of code will achieve the same result due to the function's default values
    csv_reader = csv.reader(my_file, delimiter=" ")
    for row in csv_reader:
        print(row)

with open(file="hello.csv", mode="w") as my_file:
    csv_writer = csv.writer(my_file)
    csv_writer.writerow(["Hello", "Hi"])

# with open(file="2016_pilbara.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

population = []
with open(file="2016_pilbara.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        population.append(line)

print(population)

for age_group in population:
    print(f"{age_group[0]} {age_group[1]}")

with open(file="population.csv", mode="w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="-")
    for age_group in population:
        csv_writer.writerow([age_group[0], age_group[1]])

# with open(file="population.csv", mode="w") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     for age_group in population:
#         age_group,frequency = age_group
#         csv_writer.writerow([age_group, frequency])