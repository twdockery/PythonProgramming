student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
course_list = ['CSC101', 'CSC102', 'CSC103']
max_size_list = [3, 2, 1]
roster_list = [['1004', '1003'], ['1001'], ['1002']]

def add_course():
    add = input("Add which course: ")
    if add.upper not in course_list:
        print("Course not available.")
    else:
        print("course is available")



choice = 1
while choice != "0":
    choice = input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: ")
    if choice == "1":
        add_course()
    else:
        print(choice)
