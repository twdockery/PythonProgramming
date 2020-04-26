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

"""
I don't understand how variables seem to come OUT of a variable.
It seems smart to send complicated processes to variables so that you know where errors occur.
However, if a variable is set, it cannot return the variable back...
"""


def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "No flights there..."


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50  # $50 rebate for long rental
        return cost
    elif days >= 3:
        cost -= 20  # $20 rebate for medium-length rental
        return cost
    else:
        return cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(
        city) + spending_money  # days-1 is because hotels charge by the night


print
trip_cost("Los Angeles", 5, 600)