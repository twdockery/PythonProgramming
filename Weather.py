"""
Write a Python program to analyze weather data.  Please do the following:

(a) Ask the user to enter the daily high temperature of 5 days. Store the termeratures in a list.
(b) Display the 5 temperatures.
(c) Find and display the lowest and highest temperatures.
(d) Calculate and display the average temperature.
(e) Count and display the number of days that are hotter than the average temperature.

The following is an example:

Enter a temperature: 92
Enter a temperature: 88
Enter a temperature: 91
Enter a temperature: 90
Enter a temperature: 87

Temperatures entered:  [92.0, 88.0, 91.0, 90.0, 87.0]
Lowest temperature: 87.0
Highest temperature: 92.0
Average temperature: 89.6
Number of days hotter than the average: 3
"""
temp = []
avg = 0
hot = 0

for everyday in range(5):
    day_temp = float(input(f"Enter the daily high temperation for day {everyday + 1}: "))
    temp.append(day_temp)
    avg += day_temp

print("Temperatures entered: ",temp)
print("Lowest Temperature recorded: ",min(temp))
print("Highest Temperature recorded: ",max(temp))
print("Average Temperature: ",avg / 5)

for every_item in temp:
    if every_item > avg / 5:
        hot += 1
print("Days Hotter than the average: ",hot)

"""
The following is an example:

Enter a temperature: 92
Enter a temperature: 88
Enter a temperature: 91
Enter a temperature: 90
Enter a temperature: 87

Temperatures entered:  [92.0, 88.0, 91.0, 90.0, 87.0]
Lowest temperature: 87.0
Highest temperature: 92.0
(e) Count and display the number of days that are hotter than the average temperature.
"""
