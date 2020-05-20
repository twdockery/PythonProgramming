# Tyler Dockery for CSC121 5-20-20 twdockery@waketech.edu
"""
A basketball game has four quarters.  Write a program to do the following.  Use a for loop to input scores of team A and team B in each of the four quarters.  Every time a score is entered, update and display the current total score of that team.  After all four quarters, compare the total scores of the two teams and display the outcome of the game (“Team A has won”, “Team B has won” or “It is a tie”)
"""
print("Welcome to tonight's game!")
a_score = b_score = 0
# create a for loop
for every_quarter in range(4):
    a_score += int(input(f"How many points did Team A "
                         "score in this quarter? "))
    print(f"Team A score so far: {a_score} ")
    b_score += int(input(f"How many points did Team B "
                         "score in this quarter? "))
    print(f"Team B score so far: {b_score} ")

# enter the new scores of team A and B for the quarter
# update and display the score each quarter

# after the game, compare scores and declare a winner
if a_score > b_score:
    print(f"Team A has won! They won {a_score} to {b_score}")
elif b_score > a_score:
    print(f"Team B has won! They won {b_score} to {a_score}")
else:
    print("It is a tie.")
