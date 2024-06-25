# 2.	Write a Python program to display a range of numbers by steps of -2.
# a)	Prompt the user at the keyboard for a positive integer using:
# var = input ("Please enter an integer: ")
# b)	Validate the input (var) to make sure that the user entered an integer using the isdecimal() method.
# If the user entered an invalid value, output a suitable error message and exit the program.
# c)	Use a loop to count down from this integer in steps of 2, displaying each number on the screen until either 1 or 0 is reached.
# For example, if the integer 16 (validated) is entered, the output would be:
# 16
# 14
# 12
# 10
# 8
# 6
# 4
# 2
# 0
# And if 7 is entered, the output would be:
# 7
# 5
# 3
# 1
# You will need to look-up the range() built-in in the online documentation, pay particular attention to the stop parameter.

var = input ("Please enter an integer: ")

if not var.isdecimal():
    print("Invalid value:", var)
    exit(1)

#              starting point, end point, incrementer (+)/decrementer(-)
for var in range(int(var), -1, -2):
    print(var)