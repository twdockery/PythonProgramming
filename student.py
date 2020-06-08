#tyler dockery for CSC121  6-8-2020

def add_course(id, c_list, m_list, r_list):

    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    add = input("Add which course: ")
    if add == "0":
        choice = "0"
        student_id = "0"
        # print(add) # debug area
    if add.upper() not in c_list:
        print("This course is not available.")
    else:
        index = c_list.index(add.upper()) #find course position in course list
        if str(id) in (r_list[index]):
            print("You are already registered for this course")
            #choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
        else:
            size = 0
            for everyitem in r_list[index]: #counts SID in list
                size += 1
            if size >= m_list[index]:
                print("This course is already full")
                #choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
            else:
                r_list[index].append(id) #adds student to end of list in index position
                # print(r_list[index]) #debug area to check addition.
                print("Course Added")
                #choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))



def drop_course(id, c_list, r_list):

    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_list is the course list; r_list is the list of class
    # rosters. This function asks user to enter the course he/she
    # wants to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.  This function has no return value.
    # -------------------------------------------------------------

    drop = input("drop which course: ")
    # print(add) # debug area
    if drop.upper() not in c_list:
        print("This course is not available.")
    else:
        index = c_list.index(drop.upper())  # find course position in course list
        if id not in (r_list[index]):
            print("You are not registered for this course")
        else:
            r_list[index].remove(id)  # removes student from list in index position
            print("Course removed")
            #print(r_list[index])  # debug to show removal from roster


def list_courses(id, c_list, r_list):

    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has three parameters: id is the ID of the
    # student; c_list is the course list; r_list is the list of
    # class rosters. This function has no return value.
    # -------------------------------------------------------------

    print("Courses registered:")
    classes = []
    size = 0
    # print(r_list) failed debug :(
    for x in range(len(c_list)):
        if id in r_list[x]:
            print(c_list[x])
            size += 1
    print(f"total number: {size}")

