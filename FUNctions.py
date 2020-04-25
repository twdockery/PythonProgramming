"""
Each function has 3 parts:
def which defines the function
name which names the function so it can be called
(): Where it tells us what if anything will be returned

Each function should have a block code using a tuple (three quotes) together to explain it to coders
"""


def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print("%d squared is %d." % (n, squared))
    return squared

## ask for number and checks if its an integer
number = input("Give Me A Whole Number: ")
if number.isnumeric():
    square(int(number))
else:
    print("that wasn't a whole number...")

