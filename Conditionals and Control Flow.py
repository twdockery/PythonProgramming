# So I clearly am missing some learning, such as inputs, and printing with variables and multiplication. So,
# I'll build out this if/else page and then revisit earlier projects to build out some good work

def clinic():  # So this defines the finction
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower() # input is sent to lowercase text
    if answer == "left" or answer == "l": # == is short for equals to? or is an argument? :starts it
        print("This is the Verbal Abuse Room, you heap of parrot droppings!") # 4 spaces indent?
    elif answer == "right" or answer == "r":
        print("Of course this is the Argument Room, I've told you that already!")
    else:
        print("You didn't pick left or right! Try again.")
        clinic() #if you didn't pick a choice, the function is started again

clinic() #this calls the function. All that is needed to execute it.

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "Tis but a scratch!":
        return True
    else:
        return False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False

# it seems that if statments can be on a line by themselves, but usually if, elif, else statements seem to be part of a function

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

# here is a sample grading project:
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 65 and grade <= 69:
        return "D"
    else:
        return "F"


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))

# Here is a slightly better version
def grade_converter(grade):
    if grade >= 90:
        return "Your grade of %s is an A" % (grade)
    elif grade >= 80: # because if it were 90+ it would have already printed and escaped the condition...
        return "Your grade of %s is a B" % (grade)
    elif grade >= 70:
        return "Your grade of %s is a C" % (grade)
    elif grade >= 65:
        return "Your grade of %s is a D" % (grade)
    else:
        return "Your grade of %s is an F" % (grade)


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))
