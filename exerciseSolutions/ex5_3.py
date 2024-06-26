# 1.	What’s wrong with this?
# cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# print(cheese)
# cheese.append('Oke') # correct way to add a new item to the List
# # cheese += 'Oke'
# print(cheese)
# How should 'Oke' be added to the end of the cheese list?
#
# 2.	What’s going on here? Can you explain the output?
# tup = 'Hello' # storing the string "Hello" in the variable 'tup'
# print(len(tup)) # printing the length of the string (how many characters are in "Hello"
# # Prints 5
# tup = 'Hello',
# # the comma at end changes tup from a string to a tuple () - if you use a comma but don't put brackets, it will assume ()
# print(len(tup))
# Prints 1
#
# 3. Write a Python script called Ex5_3.py
# that will generate and display 6 unique random lottery numbers between 1 and 50.
# Think about which Python data structure is best suited to store the numbers!
# Use the Python help() function to find out which function to use from the python standard library called random.

import random
numbers = set()
# sets don't allow for duplicates
for num in range(1, 7):
    # do the following to always return 6 values in the set that aren't duplicates
    while True:
        num = random.randint(1, 50)
        if num not in numbers:
            numbers.add(num)
            break
    # numbers.add(random.randint(1, 50)) # problem with this alone is set output may vary since it encounters duplicates
print(numbers),

# or, can improve the above and do this:
while len(numbers) < 6:
    numbers.add(random.randint(1, 50))
print(numbers)
