import student
def login(id, s_list):
    # print("login called") #debug area
    pin = input("Enter PIN: ")
    if (id,pin) in s_list:
        print("ID and PIN verified")
        return True
    else:
        print("ID or PIN incorrect")
        return False


def main():
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101','CSC102','CSC103']
    max_size_list = [3, 2, 1]
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    # print("main called")  # debug area

    student_id = "1"
    while student_id != "0":
        student_id = input("Enter ID to log in, or 0 to quit: ")
        if student_id == "0":
            break
        else:
            if login(student_id, student_list) == True:
                choice = -1
                while choice != 0:
                    choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
                    if choice == 0:
                        print("session ended.")
                        student_id = "0"
                    elif choice == 1:
                        student.add_course(student_id, course_list, max_size_list, roster_list)
                    elif choice == 2:
                        student.drop_course(student_id, course_list, roster_list)
                    else:
                        student.list_courses(student_id, course_list, roster_list)



            """
                choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
                if choice == 0:
                    print("session ended.")
                    student_id = "0"
                while choice != 0:
                    if choice == 1:
                        student.add_course(student_id, course_list, max_size_list, roster_list)
                    elif choice == 2:
                        student.drop_course(student_id, course_list, roster_list)
                    else:
                        student.list_courses(student_id, course_list, roster_list)
"""

print("Welcome to Man Chi Tech Registration!")
main()
