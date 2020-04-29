"""
This will be a game of rock, paper, scissors
I am watching Animal World, a show about a
High Stakes game of rock paper scissors
so its very appropriate
"""
from random import randrange

print("Welcome to Rock, Paper, Scissors!")
print("You must play until you win")
cpu = ("r","p","s")
# a random number will be created (1-3) and chosen from CPU

cpu_play = cpu[int(randrange(3)) ]
print(cpu_play)

def game(play):
    """
    Player will choose rock, paper, scissors.
    This will then be compared to the computer's play
    The winner will be announced
    Args:
        play:

    Returns:
    """
    if (play) == (cpu_play):
        print("It's a Tie!")
    elif (play) == "r" and (cpu_play) == "s":
        print("You WIN! ")
    elif (play) == "p" and (cpu_play) == "r":
        print("You WIN! ")
    elif (play) == "s" and (cpu_play) == "p":
        print("You WIN! ")

    else:
        print("You LOSE!")
        game(input("What will it be: R, P, S? "))


game(input("What will it be: R, P, S? "))