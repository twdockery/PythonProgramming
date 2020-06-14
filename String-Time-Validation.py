#Tyler Dockery for CSC121    twdockery@waketech.edu
# ----------------------------------------------------------------
# Author: Tyler Dockery
# Date:
#
# Ask user to enter time in the format of hh:mm:ss. For example, 11:07:28.
# Hour must be a two-digit number between 0 and 23, inclusive.
# Minute and second must be two-digit numbers between 0 and 59, inclusive.
# The program needs to check whether the time entered is valid.
# -----------------------------------------------------------------

time = input("Enter time [hh:mm:ss]: ")

# if not 2 colons, error and stop
if time.count(":") != 2:
    print("Must separate hour, minute and second with colons.")

# elif hour not two-digit number, error and stop
elif time_split[0].isdigit() == False:
    print("Hour must be a 2-digit number.")

# elif minute not two-digit number, error and stop
elif time[3:5].isdigit() == False:
    print("Minute must be a 2-digit number.")

# elif second not two-digit number, error and stop
elif time[7:9].isdigit() == False:
    print("Second must be a 2-digit number.")

# elif hour not between 0 and 23, inclusive, error and stop
elif 0 > int(hour) >= 24:
    print("Hour must be a 2-digit number between 0 and 23.")

# elif minute not between 0 and 59, inclusive, error and stop
elif 0 > int(time[3:5]) >= 60:
    print("Minute must be a 2-digit number between 0 and 59.")

# elif second not between 0 and 59, inclusive, error and stop
elif 0 > int(time[7:8]) >= 60:
    print("Second must be a 2-digit number between 0 and 59.")

# else remove the colons and display the time.
else:
    time2 = time.replace(":", "")
    print(f"Time with colons removed: {time2}")

"""
Write a program to do the following.  Ask user to enter time in the format of hh:mm:ss. For example, 11:07:28. Hour must be a two-digit number between 0 and 23, inclusive.  Minute and second must be two-digit numbers between 0 and 59, inclusive.  The program needs to check whether the time entered is valid. 
 
	•	Check whether there are exactly two colons. Display an error message and stop if the input is invalid.
	•	Check whether hour is a two-digit number. Display an error message and stop if the input is invalid.
	•	Check whether minute is a two-digit number. Display an error message and stop if the input is invalid.
	•	Check whether second is a two-digit number. Display an error message and stop if the input is invalid.
	•	Check whether hour is between 0 and 23, inclusive. Display an error message and stop if the input is invalid.
	•	Check whether minute is between 0 and 59, inclusive. Display an error message and stop if the input is invalid.
	•	Check whether second is between 0 and 59, inclusive. Display an error message and stop if the input is invalid.
	•	If the time entered is valid, remove the colons and display the time.  For example, if the input time is 11:07:28, the program should display 110728.

The following are a few examples:

Enter time [hh:mm:ss]: 10.44.58
Must separate hour, minute and second with colons.

Enter time [hh:mm:ss]: 11:27 28
Must separate hour, minute and second with colons.

Enter time [hh:mm:ss]: 11:16:ss
Second must be a 2-digit number.

Enter time [hh:mm:ss]: 15:4:26
Minute must be a 2-digit number.

Enter time [hh:mm:ss]: 24:05:07
Hour must be a 2-digit number between 0 and 23.

Enter time [hh:mm:ss]: 14:07:28
Time with colons removed: 140728

"""