# Q1.	Open the script sep.py in a text editor. You’ll see a string defined called 'Belgium'. Add code to print:
# 1.	A line of hyphens the same length as the Belgium string, followed by
# 2.	the string with the comma separators replaced by colons ':'., followed by
# 3.	the population of Belgium (the second field) plus the population of the capital city (the forth field). Hint: the answer should be 11183818.
# 4.	A line of hyphens the same length as the Belgium string.

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

#step 1 & 4
line_length = len(Belgium) # 81
print(line_length * "-")
#step 2
colons = Belgium.replace(",", ":")
print(colons)
#step 3
# identify & separate (split) individual elements  in the string
elements = Belgium.split(",")
print(elements)
# find element in the second field - parse into an integer
second_field = elements[1]
print(second_field)
# find element in the forth field - parse to int
forth_field = elements[3]
print(forth_field)
# add the 2nd and 4th field values - or parse to in here
total = int(second_field) + int(forth_field)
print(total)
