letters = ['a','b','c']
for letter in letters:
    print(letter)

count = 0
while count < len(letters):
  print(letters[count])
  count+=1

# name = input("What is your name? ")
# while name != "Ashley":
#   print("I don't know you!")
#   name = input("Well, what's the new name? ")

# range() number is very similar to slicing
# in that start int is inclusive and end int is exclusive
for number in range(1,11):
    print(number)

students = [
    ["Cindy", "Emily", "Evgenia"],
    ["Julie","Maddy","Andrea"],
    ["Jenny","Sarah","Yara"]
]

for student in students:
    for name in student:
        print(name)