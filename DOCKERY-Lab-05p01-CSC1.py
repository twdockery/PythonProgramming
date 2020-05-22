"""
Write a Python program to do the following:
	•	Ask the user to enter as many integers from 1 to 10 as he/she wants. Store the integers in a list.  Every time after the user has entered an integer, use a yes/no type question to ask whether the user wants to enter another one.  Display the list.
	•	Display the largest element, the smallest element, the sum of all elements and the length of the list.
	•	Calculate and display the average of the elements.
	•	Reverse the order of the elements. Display the reversed list.
	•	Move the last element to the front of the list, i.e., the last element becomes the first element while other elements remain the same.  [Hint: Insert the last element to the front first, then delete the last element]

"""
add = "y"
list = []
#add as many integers as user wants
while add.lower() == "y":
    new_int = int(input("Choose an integer from 1 to 10 "))
    if new_int > 10 or new_int < 1:
        print("Integer out of range")
        add = "y"
        continue
    else:
        list.append(new_int)
        add = (input("Add another [y/n]? "))

# print the list
for every_item in list:
    print(every_item)
print(f"Number list: {list}")

#Largest element: 9
print(f"Largest element: {max(list)}")
#Smallest element: 5
print(f"Smallest element: {min(list)}")

#Sum of all elements: 34
sum = 0
for every_item in list:
    sum += every_item
print(f"Sum of items: {sum}")

#Length of list: 5
print(f"Length of list: {len(list)} items.")

#Average: 6.8
print(f"Average: {sum/len(list)}")

#List reversed: [7, 5, 8, 9, 5]
list.reverse()
print("List reversed: ",list)

#Last element moved to front: [5, 7, 5, 8, 9]
list.insert(0,list[-1])
del list[-1]
print("Last item first: ",list)