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

""" Functions can call other functions. Deserves another will return 3 from one_good_turn(0)"""

def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2

def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")

def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"
distance_from_zero(input("How far away is it? "))
