# Tyler Dockery for CSC121 7-9-2020 twdockery@waketech.edu
"""
A hotdog stand sells hotdogs, potato chips and sodas.  Hotdogs are $2.50 each.  Potato chips are $1.50 per bag.  Sodas are $1.25 per cans.  Design a program to do the following.  Ask the user to enter number of hotdogs, chips and sodas ordered by the customer.  The program will calculate and display the total amount due.
Step 1: input the number of hotdogs
Step 2: input the number of potato chip bags
Step 3: input the number of soda cans
Step 4: calculate cost = (hotdogs * 2.5) + (potato chip bags * 1.5) + (soda cans * 1.25)
Step 5: display cost
"""
hotdogs = chips = soda = -1

hotdogs = int(input("How many hot dogs did the customer order? "))
try:
    hotdogs = int(input("How many hot dogs did the customer order? "))
except:
    print("Integer cannot have decimal point or comma")

chips = int(input("How many bags of potato chips doid the customer order? "))
soda = int(input("How many cans of soda did the customer order? "))
total = (hotdogs * 2.5) + (chips * 1.5) + (soda * 1.25)
print(f"Your total is: ${total:.2f}") # :.2f floats to 2 decimal places