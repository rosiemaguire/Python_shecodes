# Store multiple data points
list_name = ["Rosie", 1, 4.5, True, []]
# can take multiple data types - e.g. str, int, float, bool, and other lists
# however it makes sense to store similar data types in a list
# (or at least have some common logic e.g. person =["hair",1.63, 29])
digits = [1, 2, 3, 4, 5]
print(list_name)
print(type(list_name))

# Lists are indexed starting from 0
print(digits[-1])
print(digits[len(digits) - 1])

# slicing a list
# print 1-4
print(digits[0:4])  # Start index (inclusive) and End index (exclusive)
print(digits[:4])

# print 1 and 5
print(digits[::4])
print(digits[0::4])

# print 4 and 5
print(digits[3:])
print(digits[3:5])
print(digits[3::])

# skipping [start index: end index: how many elements to skip]
# setting elements to skip as 1 doesn't skip any
print(digits[0:5:1])

# print a number, skip a number, print a number...
print(digits[0:5:2])

digits = [1, 2, 3, 4, 5]
print(digits)
digits.append(6)
print(digits)
# digits.pop() without adding an index it removes the last item in the list
print(digits)
popped_element = digits.pop(0)
print(popped_element)
print(digits)
digits[1] = 90
print(digits)

letters = ["a", "b", "c", "d", ["Emily", "Julie"]]
print(len(letters))
print(letters[4][0])  # Get the first list, then get the first element

# for you visual learners
names_nested_in_list = letters[4]
print(names_nested_in_list)
print(names_nested_in_list[0])

# Checking if element in list
if "a" in letters:
    print("'a' is in the list.")

if "A" in letters:
    print("'A' is in the list.")

if "Emily" in letters:
    print("it is in the list")

for l in letters:
    if "Emily" in l:
        print("Emily is in the list")
