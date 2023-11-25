from random import randint # this creates a random integer. 

######################################################
# Create the random numbers. Cannot be zero
######################################################

roll = randint(1,10) - randint(1,6)
if roll <= 0:
    roll = 0


######################################################
# Create the dictionary
######################################################

dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
}



print(roll)
print(dict[str(roll)])