from random import randrange #this allows us to create random numbers
secret = (randrange(10) + 1 # this is a random number from 0-9 + 1
def guess_it():
    """
    User will guess until they have the secret number
    """
    guess = int(input("Guess a number from 1 to 10: "))
    print(secret)
    while guess != secret:
        if guess < secret:
            print("Too small, Try again!")
            guess_it()
        elif guess > secret:
            print("Too big, Try again!")
            guess_it()
        else:
            print("Congratulations!")
            print("Congratulations!")
            print("Congratulations!")
            print("Congratulations!")
            print("Congratulations!")
            print("Congratulations!")
            print("Congratulations!")
            print("Congratulations!")

guess_it()