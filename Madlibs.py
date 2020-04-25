print("Welcome to the madlib generator!")
# here I'll ask for 4 items
familyFriend = input("Who is a family friend? ")
food = input("What is your favorite food? ")
action = input("What's your favorite marial arts move? ")
body = input("What's their best body part? ")
print()
print('%s leaned in and said: "We weren\'t expecting this much company tonight. I\'m sorry but there won\'t be enough '
      '%s for everyone. We\'ll be giving you a smaller portion than usual, and there won\'t be enough for seconds. '
      'In retaliation, I decided to %s %s in the %s!' % (familyFriend, food, action, familyFriend, body))