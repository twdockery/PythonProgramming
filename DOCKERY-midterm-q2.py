"""
Write a Python program to do the following:

(a) [2 points] Generate 5 random integers in the range of 5 to 40, inclusive. Store the random integers in a list.
Name it list1. Display list1.

(b) [2 points] Generate 5 random integers in the range of 10 to 35, inclusive. Store the random integers in a list.
Name it list2. Display list2.

(c) [2 points] Concatenate the first 2 elements of list1 and the last 3 elements of list2 to form a new list.
Name it list3. Display list3.

(d) [2 points] Concatenate the first 2 elements of list2 and the last 3 elements of list1 to form a new list.
Name it list4. Display list4.

(e) [8 points] Compare corresponding elements in list3 and list4
(i.e. compare the first element in both lists, compare the second element in both lists, and so on).
Store the larger number in each comparison in a list named list5. Store the smaller number in each comparison
in a list named list6.  If the two numbers being compared are the same, simply put one in each list.
Display list5 and list6.

(f) [4 points] Use list comprehension to select numbers that are larger than 30 from list5. Display the new list.

(g) [4 points] Use nested list comprehension to create a list of two lists.  Both lists have 5 elements.
The elements in the first list are two times the value of the elements of list6,
while the elements in the second list are three times the value of the elements of list6.
For example,  if list6 is [5, 6, 7, 8, 9], the list of lists will be [[10, 12, 14, 16, 18], [15, 18, 21. 24, 27]].

The following is an example:

List 1: [14, 30, 18, 21, 30]
List 2: [24, 28, 34, 35, 30]
List 3: [14, 30, 34, 35, 30]
List 4: [24, 28, 18, 21, 30]
List 5: [24, 30, 34, 35, 30]
List 6: [14, 28, 18, 21, 30]
Elements in list5 larger than 30: [34, 35]
List of lists: [[28, 56, 36, 42, 60], [42, 84, 54, 63, 90]]
"""
import random
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
comprehension = []
list_of_lists = []

######################
# Part A : Generate 5 random integers in the range of 5 to 40, inclusive
######################
for every_item in range(5):
    x = random.randint(5,40)
    list1.append(x)
print(list1)

######################
# Part B : Generate 5 random integers in the range of 10 to 35, inclusive
######################
for every_item in range(5):
    x = random.randint(10,35)
    list2.append(x)
print(list2)

######################
# Part C : Concatenate the first 2 elements of list1 and the last 3 elements of list2 to form a new list.
######################
list3 = [list1[0],list1[1],list2[2],list2[3],list2[4]]
print(list3)

######################
# Part D : Concatenate the first 2 elements of list2 and the last 3 elements of list1 to form a new list
######################
list4 = [list2[0],list2[1],list1[2],list1[3],list1[4]]
print(list4)

######################
# Part E : compare the first element in both lists, compare the second element in both lists, and so on).
# Store the larger number in each comparison in a list named list5. Store the smaller number in each comparison
# in a list named list6.  If the two numbers being compared are the same, simply put one in each list.
######################

for every_item in range(5):
    if list3[every_item] >= list4[every_item]:
        list5.append(list3[every_item])
        list6.append(list4[every_item])
    else:
        list5.append(list4[every_item])
        list6.append(list3[every_item])
print(list5)
print(list6)

######################
# Part f :Use list comprehension to select numbers that are larger than 30 from list5. Display the new list.
######################
comprehension = [x for x in list5 if x > 30]
print("Elements in list5 larger than 30: ",comprehension)

######################
# Part g : Use nested list comprehension to create a list of two lists.  Both lists have 5 elements.
#The elements in the first list are two times the value of the elements of list6,
#while the elements in the second list are three times the value of the elements of list6.
#For example,  if list6 is [5, 6, 7, 8, 9], the list of lists will be [[10, 12, 14, 16, 18], [15, 18, 21. 24, 27]].
######################
list_of_lists = [x * 2 for x in list6],[x *3 for x in list6]
print("List of lists: ",list_of_lists)