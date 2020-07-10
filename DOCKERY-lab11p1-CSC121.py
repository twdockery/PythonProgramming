#Tyler Dockery for CSC121    twdockery@waketech.edu 7-9-2020
# ----------------------------------------------------------------
# Author: Tyler Dockery
# Date:
#
# This program is about sets.  Write a Python program to do the following:
# (a)	Generate 5 random integers between 1 and 10, inclusive.  Store the random integers in a set named set1.  Display the set. Please note that the set may have less than 5 elements because some of the random integers generated may be redundant.
# (b)	Generate 5 random integers between 1 and 10, inclusive.  Store the random integers in another set named set2.  Display the set. Please note that the set may have less than 5 elements because some of the random integers generated may be redundant.
# (c) Find and display the union of set1 and set2.
# (d) Use set comprehension to select odd numbers from the union and store them in a set.  Display this set.
# (e)	Find and display the intersection of set1 and set2.
# (f)	Find and display the symmetric difference of set1 and set2.
#
# The following is an example.
# set1: {9, 10, 1, 7}
# set2: {8, 1, 7}
# Union of set1 and set2: {1, 7, 8, 9, 10}
# Odd numbers in union of set1 and set2: {1, 9, 7}
# Intersection of set1 and set2: {1, 7}
# Symmetric difference of set1 and set2: {8, 9, 10}
# ----------------------------------------------------------------


from random import randint
set1 = set()
set2 = set()

for everyitem in range(5):
    set1.add(randint(1,10))
    set2.add(randint(1,10))

def odds(a,b):
    odd_set = a | b
    # Using list comprehension on the union
    return [x for x in odd_set if x % 2 == 1]

print("set1:",set1)
print("set2:",set2)
print("Union of set1 and set2:", set1 | set2)
print("Odd numbers in union of set1 and set2:", odds(set1,set2))
print("Intersection of set1 and set2:", set1 & set2)
print("Symmetric difference of set1 and set2:", set1 ^ set2)