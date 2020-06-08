#tyler dockery for CSC121  6-8-2020

def add_course(id, c_list, m_list, r_list):
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
    print("Courses registered:")
    classes = []
    size = 0
    # print(r_list) failed debug :(
    for x in range(len(c_list)):
        if id in r_list[x]:
            print(c_list[x])
            size += 1
    print(f"total number: {size}")

