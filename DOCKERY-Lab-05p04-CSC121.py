#Tyler Dockery for CSC121  5-22-2020 twdockery@waketech.edu
"""

Write a Python program to do the following:
	•	Use a for loop and a random integer generator to generate 5 random integers in 1 to 9.  Store the random integers in a list.  Display the list.
	•	Use a for loop and a random integer generator to generate 5 random integers in 2 to 8.  Store the random integers in a second list.  Display the second list.
	•	Use a for loop to compare elements in the two lists in pairs, i.e., compare the first elements in both lists, compare the second elements in the both lists, etc.  Display the larger number in each comparison.

The following is an example.  There is no user input in this program.

First list: [3, 4, 7, 8, 7]
Second list: [7, 3, 2, 8, 5]
Larger number in each comparison:
7
4
7
8
7
"""
from random import randint
list1 = []
list2 = []
for i in range(5):
    list1.append(randint(1,9)) #creates 5 random int 1-9, 5 times
print("First List: ",list1)

for i in range(5):
    list2.append(randint(2,8)) #creates 5 random int 2-8, 5 times
print("Second List: ",list2)

print("Larger number in each comparison:")
for i in range(5):
    if list1[i] >= list2[i]:
        print(list1[i])
    else:
        print(list2[i])
