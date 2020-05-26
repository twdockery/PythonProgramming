# Tyler Dockery for CSC121  5-23-2020  twdockery@waketech.edu
"""
A teacher wants a program to give extra points to students who fail a test. Write a Python program to do the following:

	•	Ask the user to enter 5 test scores.  Store the scores in a list. Display the list.
	•	Copy all 5 test scores to another list.  Use a loop to examine each test score in the new list.  If the score is below 60, add 10 extra points to the score. Display the list.
	•	Compare the old score and new score of each student.  If the old score and new score are different, display the two scores.

The following is an example.

Enter a test score: 45
Enter a test score: 77
Enter a test score: 88
Enter a test score: 52
Enter a test score: 90
All scores: [45.0, 77.0, 88.0, 52.0, 90.0]
Students who scored below 60 get 10 extra points.
All scores: [55.0, 77.0, 88.0, 62.0, 90.0]
Students whose scores have changed:
Old score: 45.0 New score: 55.0
Old score: 52.0 New score: 62.0
"""
scores =[]
for i in range(5):
    scores.append(float(input("Enter a test score: "))) # ask for 5 scores, store them

print("All scores: ",scores)
print("\033[1mStudents who scored below 60 get 10 extra points. \033[0m") #bold for fun


#copy list and +10 pts if 59 or lower
new_scores = []  #create a new list
for everyitem in scores:
    if everyitem >= 60:
        new_scores.append(everyitem)  # if score 60+ add to new list
    else:
        new_scores.append(everyitem + 10)  # if score < 60, add 10 then add to new list
print("All scores: ",new_scores)

# compare lists
print("\033[1mStudents whose scores have changed: \033[0m") #bold for fun
if scores == new_scores:
    print("No scores have changed")
else:
    for everyitem in range(len(scores)):
        if scores[everyitem] != new_scores[everyitem]:
            print(f"Old Score: {scores[everyitem]}  New Score {new_scores[everyitem]}")
