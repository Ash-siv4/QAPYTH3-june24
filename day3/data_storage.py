import json
import csv

# File Handling - open(), read(), write() and close()
file = open("example", "r")  # opens file in read mode
# MODES:
# r - read (default) ; w - write ; a - append ; b - binary mode ; t - text mode ; + - read&write
content = file.read()  # read entire file
single_line = file.readline()  # read a single line
list_lines = file.readlines()  # read all lines into a list
print(content)
print(single_line)
print(list_lines)
file.close()
# writing to a file
file1 = open("example", "a")  # open in write mode so it can be edited
file1.write("\n Hello world")
file1.close()

# JSON - JavaScript Object Notation - lightweight data interchange format
data = {
    'country': "UK",
    'EMAIL': "tbc"
}
# write json data to a file
with open('data.json', 'r') as file:
    up = json.load(file)
# get the contents from json file and add it to the data dictionary
data.update(up)
with open('data.json', 'w') as file:
    # overwrite json with new_data+old_contents
    json.dump(data, file)
with open('data.json', 'r') as file:
    updated = json.load(file)
    print(updated)

# CSV
data = [
    ['animal', 'breed', 'origin'],
    ['dog', 'chi', 'mexico'],
    ['kangaroo', 'unknown', 'aus']
]
# writing to the csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# reading the csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    print('CSV Data:')
    for row in reader:
        print(row)

# Binary
# write to binary file
with open('example.bin', 'wb') as file:
    file.write(b'\x00\xFF\x00\xFF')
# reading binary
with open('example.bin', 'rb') as file:
    dataB = file.read()
    print(dataB)
