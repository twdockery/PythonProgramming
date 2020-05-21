# Tyler Dockery for CSC121  5-20-2020  twdockery@waketech.edu
"""
Write a program for playing a game with the computer.  First, generate a random integer in the range of 6 through 9.  This will be the computer’s pick.  Then generate three random integers for the human player.  These random integers are in the range of 1 through 10. If any of these three random integers is greater than the computer’s pick, the human player wins the game.  Otherwise, the human player loses.  You must use a for loop to generate these three random integers.  In each iteration, generate and display one random integer.  If it is larger than the computer’s pick, display “You have won the game” and break out of the loop.  If the human player cannot get a random integer larger than computer’s pick after three iterations , display “sorry you have lost the game”.
"""
from random import randint
print("The computer has a special number. Can you guess it?")

computer = randint(6,9)
#print(computer) # debug area

for i in range(3): # use a for loop to generate these three random integers.
    human = randint(1,10)  #generate/display one random integer in the range of 1-10.
    print(human)
    if human > computer:
        print("You have won the game")  #human > computer, display “You have won the game” and break out of the loop.
        break
    else:
        if i == 2:
            print("sorry you have lost the game")
        continue