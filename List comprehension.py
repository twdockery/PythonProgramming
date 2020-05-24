"""
This program is about list comprehension.

list1 = [2, 5, 7, 8]
list2 = [1, 2]

	•	Use list comprehension with list1 as input sequence to generate this list:

[5, 11, 15, 17]

Display the list.

	•	Use list comprehension with list1 as input sequence to generate this list:

[3, 9]

Display the list.

	•	Use list comprehension with list1 as input sequence to generate this list:

[[2, 3], [5, 6], [7, 8], [8, 9]]

Display the list.

	•	Use list comprehension with list1 and list2 as input sequences to generate this list:

[[2, 1], [2, 2], [5, 1], [5, 2], [7, 1], [7, 2], [8, 1], [8, 2]]

Display the list.

	•	Use nested list comprehension with list1 and list2 as input sequences to generate this list:

[[3, 4], [6, 7], [8, 9], [9, 10]]

Display the list.

	The following is the expected output.

Part a: [5, 11, 15, 17]
Part b: [3, 9]
Part c: [[2, 3], [5, 6], [7, 8], [8, 9]]
Part d: [[2, 1], [2, 2], [5, 1], [5, 2], [7, 1], [7, 2], [8, 1], [8, 2]]
Part e: [[3, 4], [6, 7], [8, 9], [9, 10]]
"""
list1 = [2, 5, 7, 8]
list2 = [1, 2]

newlist = []
newlist = [x + (x + 1) for x in list1]
print(f"Part a: {newlist}")
# print("a: [5, 11, 15, 17]") Debug area

newlist = []
for x in range(2):
    newlist = [x + (x - 1) for x in list1]
  # newlist = [3 ** x for x in list 2] just in case
print(f"Part b: {newlist[0:2]}")
# print("b: [3, 9]") Debug area

newlist = []
for x in list1:
    newlist = [[x,x+1] for x in list1]
print(f"Part c: {newlist}"),
# print("c: [[2, 3], [5, 6], [7, 8], [8, 9]]") #Debug area


newlist = []
for x in list1:
    for y in list2:
        newlist.append([x,y])
print(f"Part d: {newlist}")
# print("d: [[2, 1], [2, 2], [5, 1], [5, 2], [7, 1], [7, 2], [8, 1], [8, 2]]") #Debug area

newlist = []
for x in list1:
    for y in list2:
        newlist.append([x + y, x + y + 1])
print(f"Part e: {newlist}"),
print("e: [[3, 4], [6, 7], [8, 9], [9, 10]]")


"""
list1 = [2, 5, 7, 8]
list2 = [1, 2]
"""
