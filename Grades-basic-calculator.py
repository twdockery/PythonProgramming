# Tyler Dockery for CSC121 5-18-2020 twdockery@waketech.edu
"""
Each student in a course needs to submit 3 lab assignments and take 2 tests.  Design a program to do the following.  Ask the user to enter 3 lab scores and 2 test scores.  Calculate and display the lab average and the test average.  Also calculate and display the course grade, which equals 55% of the lab average plus 45% of the test average.
Step 1: input lab1
Step 2: input lab2
Step 3: input lab3
Step 4: input test1
Step 5: input test2
Step 6: calculate lab average = (lab1 + lab2 +lab3) / 3
Step 7: calculate test average = (test1 + test2) / 2
Step 8: calculate course grade = (lab average * 0.55) + (test average * 0.45)
Step 9: display lab average
Step 10: display test average
Step 11: display course grade
"""

lab1 = float(input("Please enter your Lab 1 score: ")) #just in case a decimal is added
lab2 = float(input("Please enter your Lab 2 score: "))
lab3 = float(input("Please enter your Lab 3 score: "))
test1 = float(input("Please enter your Test 1 score: "))
test2 = float(input("Please enter your Test 2 score: "))
lab_average = (lab1 + lab2 + lab3) / 3
test_average = (test1 + test2) / 2
course_grade = (lab_average * 0.55) + (test_average * 0.45)
print(f"Lab Average: {lab_average:.2f}")
print(f"Test Average: {test_average:.2f}")
print(f"Course Grade: {course_grade:.2f}")