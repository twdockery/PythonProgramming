#Tyler Dockery for CSC121 5-19-2020
'''
Write a program to calculate the number of seconds since midnight.  For example, suppose the time is 1:02:05 AM. Since there are 3600 seconds per hour and 60 seconds per minutes, it has been 3725 seconds since midnight (3600 * 1 + 2 * 60 + 5 = 3725).  The program asks the user to enter 4 pieces of information: hour, minute, second, and AM/PM.  The program will calculate and display the number of seconds since midnight.  [Hint: be very careful when the hour is 12].
'''
hour = int(input("What is the Hour? "))
minute = int(input("What is the Minute? "))
second = int(input("What are the seconds? "))
am_or_pm = (input("Is it AM or PM? "))
since_midnight = (hour * (60 ** 2)) + (minute * 60) + second
if am_or_pm.lower() == "pm":
    since_midnight += (12 * (60 ** 2))
print(f'It has been {since_midnight} seconds since midnight.')