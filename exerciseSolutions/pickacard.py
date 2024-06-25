# 3.	We have a simple module for displaying a playing card, called showcard. It has a function called display_file() which takes one parameter: the name of a gif file. The playing card filenames are of the following format:
# BMPn.GIF
# Where n is a number between 1 and 52, indicating the ordinal number of the card in the pack. Note that on Linux this is case sensitive.
# Write a Python program called pickacard.py which uses this module to display a single card. Prompt the user for a number, as follows:
# 	number = input("Pick a card (1-52): ")
# Then construct a filename from number, and then display the card by passing the filename to showcard.display_file() as a parameter.
# Do not worry about out-of-range numbers for the time being

import showcard

number = input("Pick a card (1-52): ")
filename = f"BMP{number}.GIF" # filename = "BMP" + number + ".GIF"
showcard.display_file(filename)


