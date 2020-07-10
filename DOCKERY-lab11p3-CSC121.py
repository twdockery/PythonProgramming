#Tyler Dockery for CSC121    twdockery@waketech.edu 7-9-2020
# ----------------------------------------------------------------
# Author: Tyler Dockery
# This program is about exception handling.  Create an empty list.
# Use a loop to ask user to input 5 integers.  In every iteration,
# add user input to the list if it can be converted to an integer.
# Otherwise, display an error message.  Display the list of integers
# after the loop.
# ----------------------------------------------------------------

emptylist = []
for everyitem in range(5):
    try:
        variable = int(input("Enter an integer: "))
    except:
        print("Integer cannot have decimal point or comma")
    else:
        emptylist.append(variable)

print(emptylist)