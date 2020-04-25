# This is a copy of What-Are-Variables.ipynb
# I am making a copy because not all programs can understand the Satyrn Notebook file
# Comments explain code to designers. Code explains comments to computers.

# This is your standard Hello World Program
# print("...") allows you to output to the program
print("Hello World!")

# This is too simple. Let's try some interactivity!
name = input("What is your name? ")
print("Hello " + name +"!")

# variables can be different items, such as integers (whole numbers)
a = 1
b = 2

# variables can be strings of text
c = "help! I am trappend in a variable!"

# variables can contain decimals if floated, or including a decimal point
d = float(13.125)
e = 13.

# variables can equal other variables, and different variables can have different values
f = e

# variables can contain math equations
g = 10 * 2  # multiplication
h = 10 / 3  # division (returns only integer value)
h2 = 10 / 3. # division (returns floated decimal answer)
h3 = 10 % 3 # remainder (division of terms returns ONLY the remainder value
i = 10 + 2  # addition
j = 10 - 2  # subtraction
k = 1.5e4   # scientific notation
k2 = 10 ** 2 # exponents are created with 2 asterisks

print(h)
print (h2)
print (h3)
print(k)

# variable can also calculate remainders
remainder = 17 % 3
print(remainder)

# variables can change forms
a1 = "100"
b1 = "10"

# this variable will slam the strings together
c = a1 + b1

# this will create a number
d = int(a1) + int(b1)

print(c)
print(d)

# by themselves, variables are split into types, but they can be combined with printing if converted to strings
a = "10"
b = 10

print("today I ran " + a + " miles in " + str(b) + " minutes!")

# Variables are stored at the time they are created or updated, not at the end
a = 10
b = a
a = 5

print(a)
print(b)

# here is an exercise for creating tips
# Tax will be set to 8%
# I will calculate a 15% and 20% tip
entree = 15.25
mealCost = entree * 1.08
tax15 = mealCost * 1.15
tax20 = mealCost * 1.2

print("Today's entree is a burrito the size of your head!")
# I wanted to round the float, and had to look online. So, I skipped ahead and found out how to do this
print("It will cost: $" + str(round(mealCost,2)) + " with tax.")
print("$" + str(round(tax15,2)) +" with a 15% tip. $" + str(int(tax15)) + " would be nicer")
print("$" + str(round(tax20,2)) +" with a 20% tip. $" + str(int(tax20)) + " would be nicer")
