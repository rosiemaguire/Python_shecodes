# Lists
# numbers = [1,2,3]
# numbers[0]
# Dictionary
# Keys are unique 
# Values can be any data type that we've learned so far 
# Keys can only be immutable data types
# Immutable - Strings, integers, floats, booleans
student_phonebook = {
    "Cindy": 111,
    "Tracey":123,
    "Pauline":444
    }

print(student_phonebook)
print(type(student_phonebook))
student_phonebook["Yara"] = 555
print(student_phonebook)

# Key error when key does not exist in dictionary
# print(student_phonebook["Asli"])

student_phonebook["Cindy"] = 555 # as this key already exists, the value will just be updated
print(student_phonebook)
del student_phonebook["Tracey"]
print(student_phonebook)
# student_phonebook.clear() # removes all keys and valuesfrom the dictionary
print(student_phonebook)

# Dictionaries default to refer to the key
for element in student_phonebook:
    print(element)
# Iterate all the key-value pairs 
for key in student_phonebook:
    print(key, student_phonebook[key])

# Iterate all the values in a dictionary     
for value in student_phonebook.values():
    print(value)

# Iterate through the keys and values and return as tuple
for example in student_phonebook.items():
    print(example)

# Iterate through the keys and values
for key,value in student_phonebook.items():
    print(key,value)

# turning tuples into dictionary
test_dict = {}

for example in student_phonebook.items():
    print(example)
    test_dict[example[0]] = example[1]
print(test_dict)    