#Tyler Dockery for CSC121 5-22-2020 twdockery@waketech.edu
"""
Write a Python program to do the following:
	•	Use the range function to generate this sequence of integers: 5, 9, 13, 17, 21. Use a for loop to display this sequence.
	•	Use the range function to generate this sequence of integers: 26, 19, 12, 5. Use a for loop to display this sequence.

 The following is the expected output.  There is no user input in this program.

First Sequence:
5
9
13
17
21
Second Sequence:
26
19
12
5

"""
print("First Sequence")
for i in range(5,22,4):
    print(i)
print("Second Sequence")
for i in range(26,4,-7):
    print(i)