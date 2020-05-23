#Tyler Dockery for CSC121  5-22-2020 twdockery@waketech.edu
"""
Write a program for course registration.  Students can use this program to add and drop courses.  There should be a loop in the program that tells the user to enter A to add course, D to drop course or E to exit.  If A is chosen, ask the user to enter the course to add.  If the user is already registered in that course, display the message “You are already registered in that course”; otherwise, add the course to the user’s course list, display the message “Course added”, sort the list and display the list.  If the user chooses D, ask the user to enter the course to drop.  If the user is not registered in that course, display the message “You are not registered in that course”; otherwise, remove the course from the user’s course list, display the message “Course dropped” and display the list.  The loop will stop when the user enters E
"""
print("Welcome to Man-Chi Tech Registration!")
courses = []
action = "filler variable"

################################################  Main loop
while action.lower() != "e":
    action = input("Would you like to (A)dd a course, (D)rop a course, or (E)nd? ")
    if action.lower() == "a": ################## add loop
        add = input("Add Which course? ")
        if add in courses:
            print("\033[1mYou are already registered in that course \033[0m") #bold just for fun
            print("Currently registered for:")
            for everyitem in courses:
                print(everyitem)
            continue
        else:
            courses.append(add)
            print("Course added")
            print("Currently registered for:")
            courses.sort()  # sort the courses alphanumerically before showing
            for everyitem in courses:
                print(everyitem)
            continue
    if action.lower() == "d":  ################ drop loop
        drop = input("Drop Which course? ")
        if drop in courses:
            courses.remove(drop)
            print("Course dropped")
            print("Currently registered for:")
            courses.sort()  # sort the courses alphanumerically before showing
            for everyitem in courses:
                print(everyitem)
            continue
        else:
            print("\033[1m You are not registered in that course \033[0m") #bold just for fun
            print("Currently registered for:")
            for everyitem in courses:
                print(everyitem)
            continue
print("ending...")
