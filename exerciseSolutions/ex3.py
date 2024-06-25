# 1.	Write a Python program that emulates the high-street bank mechanism for checking a PIN.
# Keep taking input from the keyboard (see below) until it is identical to a password number which is hard-coded by you in the program.
#
# To output a prompt and read from the keyboard:
# supplied_pin = input("Enter your PIN: ")
#
# Restrict the number of attempts to three (be sure to use a variable for that, we may wish to change it later), and output a suitable message for success and failure.
# Be sure to include the number of attempts in the message.

# Optional extension
# Passwords, and PINs, would not normally be displayed (echoed) to the screen for security reasons.
#     So, now we will add the functionality to hide the characters typed. That could be a lot of work, but one of the advantages of using a language like Python is that "there's a module for it".
# You’ll need to import a module called getpass, which is part of the standard library.
# Instead of input use getpass.getpass, in the same place in the program, with the same parameters.
# Note you will have to run your program in pycharm or VSCode.
# You may also have to update the Edit Configuration Templates to ‘Emulate terminal in output Console’ for the getpass module to work correctly in pycharm

import getpass

pass_number = "4356"
limit = 4
# inclusive of 1 but exclusive of "limit"
for tries in range(1, limit):
    # supplied_pin = input("Enter your PIN: ")
    supplied_pin = getpass.getpass("Enter your PIN: ")
    if supplied_pin == pass_number:
        print("success")
        print(tries, "attempts")
        break
    else:
        print("failed after", tries, "attempts")
