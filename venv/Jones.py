from random import randint

# Variables area
messages = ["you went scuba diving in La Jolla", "you listed to the talking bear 256 times in a row", "you played stickball and ended up wrenching your back and twisting your ankle","you listened to the newlyweds next door set up their waterbed"]
startMoney = 200
gameover = "n"
#
def weekend_costs(playerCash):
    pay = randint(1,125)
    if pay > playerCash:
        pay = playerCash
    return pay

def got_food(food):


# while gameover != "y":  #this is the main loop?
money = startMoney

# Weekly messages ####################################################
print("This weekend",messages[randint(0,3)])  #weekend cost
itemcost = weekend_costs(money)
if itemcost > money
    itemcost = money
money -= itemcost
print("You spent: $",itemcost)

# Food or not ####################################################
"""
if food over 8 weeks, all food over 8 rots (freezerburn)
This section must know if you have a freezer. 
    If not, all food over 4 rots. sickchance += 25%
This section must know if you have a fridge. 
    If not, all food over 1 rots, sickchance += 25%.
    if so, up to 5 weeks survive.
This section must know if you have food. 
    If not, lost time. If lost twice, sickchance += 25%.
    food loses 1 week
returns food remaining, whether you're sick, time -= time/3
"""

# Sick or not ####################################################
"""
This section must know if you have sick chance
Random integer created to see if you're sick.
5% sickchance normally + Food related sickchance
if randint < sickchance, time -= time/6
"""

# repair or not ####################################################
"""
This section must know if you have appliance repair chance
Random integer created to see if you need repair.
0% repairchance normally + 5% per item owned
if randint < repairchance
itemcost = repair_costs = randint(1,100)
print("Your appliances need repair")
if itemcost > money
    itemcost = money
money -= itemcost
"""

# Lottery or not ####################################################
"""
This section must know if you have lottery chance
if lottery > 0
    while in range(lottery)
      win = randint(1,100)
      if win = 1
        print("you won the lottery")
        money += randint(1,200)
        lottery = 0
        break
      else
        continue

"""

# clothes or not ####################################################
"""
This section must know if you need new clothes
clothes = clothes - 1
if clothes = 0
    print("you need new clothes!")
if clothes < 0 
    image = player_naked (character in a barrel)
"""


# relative or not ####################################################
"""
This section must know if you have gotten money from a relative
if clothes % 3 = 0 and clothes < 0 and money < clothes_min
    print("Your relative feels sorry for you and sends you some money. Get some clothes and get a life")
    clothes = -1

"""