# LISTS
# creation - need [] brackets
fruits = ["apple", "banana", "cherry"]
print(fruits)
# access elements
print(fruits[1]) # output: banana
# modifying elements - mutable
fruits[2] = "blueberry"
print(fruits)
# add elements - use append() method
fruits.append("orange")
print(fruits)
# add multiple elements
# more_fruits = ["orange", "grape", "peach"]
# fruits = fruits + more_fruits
# print(fruits)
# print(fruits + ["orange", "grape", "peach"]) # to do in one line of code
fruits.extend(["orange", "grape", "peach"])
# remove elements
fruits.remove("apple")
print(fruits)

# TUPLE
# create - need () brackets
coordinates = (10, 20)
print(coordinates)
# access elements
print(coordinates[0])
# proof of immutability - cannot update or remove elements
# coordinates[0] = 15 # TypeError

# SET
# creating - {} or set()
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
unum = set([0, 0, 8, 7]) # automatically removes duplicate elements
print(unum)
# add elements - add()
unique_numbers.add(9)
print(unique_numbers)
# remove elements - remove()
unique_numbers.remove(3)
print(unique_numbers)

# DICTIONARY
# create - {}, key-value pairs
person = {"name": "Ash", "address": "london", "age": 25}
print(person)
# access specific elements - use the key
print(person["name"])
# modify elements
person["age"] = 26
print(person)
# add elements
person["country"] = "UK"
print(person)
# delete elements - del
del person["address"]
print(person)
