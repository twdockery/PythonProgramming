# Tyler Dockery for CSC121  5-23-2020  twdockery@waketech.edu
"""
Write a Python program to do the following:
	•	Use a for loop and a random integer generator to generate 10 random integers in 1 through 15.  Store the random integers in a tuple.  Display the tuple. [Hint: you may want to store the random integers in a list first and then convert the list to a tuple]
	•	Create a new tuple.  Copy the first three elements of the tuple in part (a) to this tuple.  Display this tuple.
	•	Create a new tuple.  Copy the last three elements of the tuple in part (a) to this tuple.  Display this tuple.
	•	Concatenate the two tuples in part (b) and part (c).  Display the concatenated tuple.
	•	Sort the concatenated tuple.  Display the sorted tuple.

The following is an example. There is no user input in this program.

Tuple of 10 random numbers: (12, 3, 4, 7, 5, 9, 7, 3, 1, 7)
Tuple of first 3 numbers: (12, 3, 4)
Tuple of last 3 numbers: (3, 1, 7)
Two tuples concatenated: (12, 3, 4, 3, 1, 7)
Two tuples concatenated and sorted: (1, 3, 3, 4, 7, 12)
"""
from random import randint
list1 = []
# [Hint: you may want to store the random integers in a list first and then convert the list to a tuple]
for x in range(10): #Use a for loop and a random integer generator to generate 10 random integers in 1 through 15.
    list1.append(randint(1,15))  # Storing in a list because tuples cannot be altered
# print(list1)  # just a debug area

# Store the random integers in a tuple.  Display the tuple.
tuple10 = list1[0:10] # all 10 randoms stored
tuple3 = tuple10[0:3] # list item
tuplel3 = tuple10[7:10] # list item from (length -3 to length)
tuplecon = tuple3 + tuplel3 # tuple first 3 + tuple last 3 concatenated
tupleconsort = sorted(tuplecon) # concatenated tuple sorted

print("Tuple of 10 random numbers:",tuple10)
print("Tuple of first 3 numbers: ",tuple3)
print("Tuple of last 3 numbers: ",tuplel3)
print("Two tuples concatenated: ",tuplecon)
print("Two tuples concatenated and sorted: ",tupleconsort)