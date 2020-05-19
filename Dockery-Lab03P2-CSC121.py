#Tyler Dockery for CSC121 5-19-2020 twdockery@waketech.edu
'''
Write a program to find the largest value.  Ask the user to enter three numbers.  Compare them and report the largest one.  [Hint: The user is free to enter any three numbers.  Some or all of them may be the same.  Take this into consideration when you compare the numbers.]
''' 
print("Thank you for using the COMPARE-A-TRON.")
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))
num3 = float(input("Enter the Third Number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")
