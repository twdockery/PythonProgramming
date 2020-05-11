#################
# just a test to figure out about functions
#################
from random import randrange #this allows us to create random numbers
start = 200 # player starts with 200
currentCash = 200  # Test amount

def message():
    """
    This is to grab a message from an exterior file, or choice at random
    """
    #secret = (int(randrange(1)) + 1) # Find a way to return many messages
    weekendMessage = "You went scuba diving in La Jolla" # only one now
    return weekendMessage


def daily(currentCash):
    secret = (int(randrange(60)) + 1) # how much money you spent this weekend

    if secret > currentCash:  # you can't take what you don't have
        secret = currentCash
    currentCash -= (secret) # the secret number is removed from cash
    return secret

##############################################
# Turn Mechanics
##############################################

# initial message
print(message())
print("This turn you spent %s." % (daily(currentCash)))

# food message
Food()
