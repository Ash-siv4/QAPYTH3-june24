# 2.	Now we’ll try some object methods. Create a Python script (call it ex2_2.py if you like) with the following line:
# var = input("Please enter a value: ")
# This is an easy way of outputting a prompt to the console and getting a reply. The variable var is a reference to that reply, which is a string.
#
# Now print the following:
# a)  The value of var as upper case.
# b)  The number of characters in var (this does not require a method).
# c)   Does it contain numeric characters? (try the isdecimal() method).

var = input("Please enter a value: ")

print(var.upper())
print(len(var))
print(var.isdecimal())