# 3.	If a year is exactly divisible by 4 but not by 100, the year is a leap year. There is an exception to this rule. Years exactly divisible by 400 are leap years.
# The year 2000 is a good example.
# Write a program that asks the user for a year and reports either a leap year or not a leap year. (Hint: x % y is zero if x is exactly divisible by y.) Test with the following data:
# 	1984 	is a leap year 				1981	is NOT a leap year
# 	1904 	is a leap year 				1900	is NOT a leap year
# 	2000	is a leap year				             2010	is NOT a leap year
# 	Use the following to ask the user for a year:
# 	year = int(input('Please enter a year: '))

year = int(input('Please enter a year: '))

if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")