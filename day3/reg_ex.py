# REGULAR EXPRESSIONS (REGEX) - tool for matching and manipulating text
# allow you to define patterns that can match sequences of characters within strings
# 're' module in python, has functions & methods that work with regex
# Basic Concepts:
# literal  characters (characters that match themselves, e.g: a-z)
# meta-characters (special characters that have special meanings, e.g: $, *, +, {}, etc)
# Common functions:
import re
# re.match() - checks for a match only at the beginning of the string
pattern = "World"
string = "Hello, World!"
match = re.match(pattern, string)
if match:
    print("found")
else:
    print("nope")
# re.search() - search the string for a match anywhere in it
search = re.search(pattern, string)
if search:
    print("found match")
else:
    print("not found")
# re.findall() - returns a list of all non-overlapping matches in the string
# meta-character to match any character is (.)
pat2 = "do."
string2 = "The dog left the house through the doggy door"
find = re.findall(pat2, string2)
print(find)
# to match any vowels
vowels = "[aeiou]" # use meta-character of [] to check for multiple chars in string
# vowel = ["a", "e", "i", "o", "u"] # can't use this
find_vow = re.findall(vowels, string2)
print(find_vow)
# re.sub() - replaces one or more matches with a string
ptn = r"\d" # looking for all the digits
# (the r is saying the string is a raw string,
# so backslashes in the string are treated as literal backslashes and not escape characters)
num = "My phone number is 0123-456-7890"
res = re.sub(ptn, "#", num) # replace the numbers with a hash
print(res)
# More complex patterns:
# grouping & capturing - extract the phone number from the text
ptn2 = r"(\d{4})-(\d{3})-(\d{4})" # state the pattern we are looking for is in the format of 4digits-3digits-4digits
get = re.search(ptn2, num)
if get:
    print(get.group())
    print(get.group(1)) # output first 4 digits
# using alternation
one_or_other = "cat|dog" # use the | for alternation - matching different patterns
text = "I have one boy dog and one girl dog as well as a cat"
matched = re.findall(one_or_other, text)
print(matched)
# SUMMARY
# - Literal Characters: match themselves
# - Meta-characters: Have special meanings ('.','^','$', etc.)
# - Character classes: represents sets of characters ( '[aeiou]')
# - Quantifiers: specify the number of occurrences ('*','+','?','{}')
# - Grouping: capturing part of the match ('()','\d{4}-\d{3}-\d{4}')
# - Alternation: matching one pattern or another ('cat|dog')
