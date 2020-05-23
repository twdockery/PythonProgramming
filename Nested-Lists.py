# Tyler Dockery for CSC121  5-23-2020  twdockery@waketech.edu
"""
Three figure skaters, Jean, Kayla and Connie, compete in a meet.  Each skater receives 4 scores.  Write a program to do the following.
	•	Ask the user to enter 4 scores for Jean. Store the scores in a list named j_list. Display the list.
	•	Ask the user to enter 4 scores for Kayla. Store the scores in a list named k_list. Display the list.
	•	Ask the user to enter 4 scores for Connie. Store the scores in a list named c_list. Display the list.
	•	First, use the following code to create a copy of each list and construct a list of lists from them:

all_scores = [j_list[:], k_list[:], c_list[:]]

Note: We want the elements of all_scores to be a copy of the three score lists but not the three score lists themselves.  Therefore, the following code does not generate what we want:

all_scores = [j_list, k_list, c_list]

Next, use a set of nested for loops to add 1 extra point to every score of every skater in all_scores. Display all_scores.

	•	Sort the scores in ascending order within each skater in all_scores. Display all_scores.

 The following is an example.

Please enter Jean's scores one by one.
Enter a score: 77
Enter a score: 74
Enter a score: 75
Enter a score: 72
Jean's scores: [77.0, 74.0, 75.0, 72.0]

Please enter Kayla's scores one by one.
Enter a score: 81
Enter a score: 77
Enter a score: 80
Enter a score: 79
Kayla's scores: [81.0, 77.0, 80.0, 79.0]

Please enter Connie's scores one by one.
Enter a score: 69
Enter a score: 74
Enter a score: 72
Enter a score: 70
Connie's scores: [69.0, 74.0, 72.0, 70.0]

All scores: [[77.0, 74.0, 75.0, 72.0], [81.0, 77.0, 80.0, 79.0], [69.0, 74.0, 72.0, 70.0]]
All scores after extra point: [[78.0, 75.0, 76.0, 73.0], [82.0, 78.0, 81.0, 80.0], [70.0, 75.0, 73.0, 71.0]]
All scores after sorting: [[73.0, 75.0, 76.0, 78.0], [78.0, 80.0, 81.0, 82.0], [70.0, 71.0, 73.0, 75.0]]
"""
j_list = []
k_list = []
c_list = []
all_scores =[]

# get scores for each person and print them
print("Please enter Jean's scores one by one.") #gets a float instead of integer
for i in range(4): #ask these questions 4 times
    j_list.append(float(input("Enter a score: ")))
print(j_list)
print("Please enter Kayla's scores one by one.")
for i in range(4): #ask these questions 4 times
    k_list.append(float(input("Enter a score: ")))
print(k_list)
print("Please enter Connie's scores one by one.")
for i in range(4): #ask these questions 4 times
    c_list.append(float(input("Enter a score: ")))
print(c_list)

#build a comprehensive list
all_scores = [j_list[:], k_list[:], c_list[:]]
print("All scores: ",all_scores)

###################################
"""This section was super tough!"""
###################################

#add 1pt to all using nested for loops
for r in range(3): # number of skaters
    for c in range(4): # number of scores
        all_scores[r][c] = all_scores[r][c] + 1
print("All scores after extra point: ",all_scores)

#sort all lists
for everyitem in all_scores:
    everyitem.sort()
print("All scores after sorting: ",all_scores)



