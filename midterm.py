"""A car rental company has three types of cars for customers to choose.
SUV: $55 per day for first 7 days. $47 per day starting from the 8th day.
Minivan: $49 per day for first 7 days. $42 per day starting from the 8th day.
Hybrid: $44 per day for first 7 days. $38 per day starting from the 8th day.

Write a Python program to do the following.
(a) [4 points] Ask user to choose car type. Enter S for SUV, M for minivan or H for hybrid.
User may enter uppercase or lowercase letter. Both S and s should be accepted for SUV.
Both M and m should be accepted for minivan. Both H and h should be accepted for hybrid.
If an invalid car type is entered, display "Invalid car type" and ask the user to reenter repeatedly
until a valid car type is entered.
(b) [4 points] Ask user to enter number of days. Since user is expected to enter a whole number, it is safe to convert
it to an integer.  A minimum of 2 days rental is required.
 If number of days is smaller than 2, display "Must be at least 2 days" and
 ask user to reenter repeatedly until 2 or larger is entered.
(c) [8 points] Calculate and display rental fee.



The following is another example:

Enter S for SUV, M for minivan, H for hybrid: x
Invalid car type.
Enter S for SUV, M for minivan, H for hybrid: F
Invalid car type.
Enter S for SUV, M for minivan, H for hybrid: m

Enter number of days: 1
Must be at least 2 days.
Enter number of days: 0
Must be at least 2 days.
Enter number of days: 8

Rental fee:  385
"""
######################
# Part A : What Kind of Rental?
######################

print("welcome to CSC121 Rental Agency!")
car_type = input("Enter S for SUV, M for minivan, H for hybrid: ")
while car_type.lower() != 's' and car_type.lower() != 'm' and car_type.lower() != 'h':
    print("Invalid car type...")
    car_type = input("Enter S for SUV, M for minivan, H for hybrid: ")

######################
# Part B: How many days?
######################

days = int(input("Enter number of days: "))
while days < 2:
    print("Must be at least 2 days.")
    days = int(input("Enter number of days: "))

######################
# Part C: What is the cost?
######################

if car_type == "s":
    if days > 7:
        cost = (55 * 7) + (47 * (days - 7))
    else:
        cost = 55 * days
elif car_type == "m":
    if days > 7:
        cost = (49 * 7) + (42 * (days - 7))
    else:
        cost = 49 * days
else:
    if days > 7:
        cost = (44 * 7) + (38 * (days - 7))
    else:
        cost = 44 * days
print("Rental Fee: ",cost)
