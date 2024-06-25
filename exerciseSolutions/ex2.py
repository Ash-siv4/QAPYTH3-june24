# 1.	This exercise carries out some basic operations on variables.
# a)	Create a new script called ex2.py
# b)	Create two variables, one containing your first name and another containing your last name. Display them using print.
# c)	Now transfer these variable values into a list and display the list.
# d)	Take the variables and now store the values in a dictionary, using keys 'first' and 'last'. Display the dictionary values.
#
# …and execute the script ex2.py.

first_name = "bob"
last_name = "the builder"

print(first_name, last_name)

# [ ] - is a list - index
# lists start with index of 0
# first_name has index of 0
#last_name has index of 1
names = [first_name, last_name]
print(names) # prints everything in the list
print(names[0]) # prints value at index 0
print(names[1]) # prints value at index 1

# { } - a dictionary, key-value pairs
# keys are: first & last
# values are what is stored in these variables: first_name & last_name
dict = {'first': first_name, 'last': last_name}
print(dict) # prints contencts of dictionary including the keys
print(dict['first'], dict['last']) # just prints the values referenced by the keys