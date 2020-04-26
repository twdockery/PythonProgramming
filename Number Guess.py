from random import randrange #this allows us to create random numbers
secret = (int(randrange(10)) + 1)
def guessing():
    print("Pick a number from 1 to 10: ")
    guess = int(input("Guess which number it is: "))
    if guess > secret:
        print("Too big...")
        guessing()
    elif guess < secret:
        print("Too small...")
        guessing()
    else:
        print("Congratulations!")
        print("Congratulations!")
        print("Congratulations!")
        print("Congratulations!")
        print("Congratulations!")
        print("Congratulations!")
        print("Congratulations!")
        print("Congratulations!")
        print("Your guess of %s was correct!" % (guess))

guessing()