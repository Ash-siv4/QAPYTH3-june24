string = "    Hello, World!    "

stripped_string = string.strip()

print("original:", string)
print("stripped:", stripped_string)

left_strip = string.lstrip()
right_strip = string.rstrip()

print("left:", left_strip)
print("right", right_strip)

sentence = "  this ia  a     sentence  "
no_spaces = sentence.replace(" ", "")
print("with space:", sentence)
print("without space:", no_spaces)

name = input("Enter your name: ")
print("Hello {}".format(name))