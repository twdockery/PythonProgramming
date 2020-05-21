#Tyler Dockery for CSC121 5-20-2020 twdockery@waketech.edu
'''
Write a program to calculate the number of seconds since midnight.  For example, suppose the time is 1:02:05 AM. Since there are 3600 seconds per hour and 60 seconds per minutes, it has been 3725 seconds since midnight (3600 * 1 + 2 * 60 + 5 = 3725).  The program asks the user to enter 4 pieces of information: hour, minute, second, and AM/PM.  The program will calculate and display the number of seconds since midnight.  [Hint: be very careful when the hour is 12].
In Lab 03 we wrote a program to calculate the number of seconds since midnight.  Modify the program by adding error checking loops.  Hour must be a number from 1 to 12.  Minute and second must be numbers from 0 to 59. Also check whether “AM” or “PM” is entered.  Every time an invalid value is entered, display an error message and ask the user to re-enter a valid value immediately.
'''
print("Welcome to the Midnight Machine!")
hour = int(input("What is the Hour? "))
while hour < 1 or hour > 12: #checking for accurate hour
    print("Hour must be from 1 to 12.")
    hour = int(input("What is the Hour? "))
minute = int(input("What is the Minute? "))
while minute < 1 or minute > 59: #checking for accurate minute
    print("Minute must be from 1 to 59.")
    minute = int(input("What is the Minute? "))
second = int(input("What are the seconds? "))
while second < 1 or second > 59: #checking for accurate seconds
    print("Second must be from 1 to 59.")
    second = int(input("What is the second? "))
am_or_pm = (input("Is it AM or PM? "))
while am_or_pm.lower() != "am" and am_or_pm.lower() != "pm":
    print("Must be either AM or PM.")
    am_or_pm = (input("Is it AM or PM? "))
if am_or_pm.lower() == "am" and hour == 12:
    hour = 0
since_midnight = (hour * (60 ** 2)) + (minute * 60) + second #must check for hours first...
if am_or_pm.lower() == "pm":
    since_midnight += (12 * (60 ** 2)) #so it can add 12 more hours if PM
print(f'It has been {since_midnight} seconds since midnight.')
