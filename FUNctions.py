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


# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)