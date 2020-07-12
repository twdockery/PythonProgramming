# Tyler Dockery for CSC121  7.12.2020  twdockery@waketech.edu
"""
Write code to ask the user to enter course code and maximum class size of a course.
Use the data provided by the user to create an instance of Course.  Write a loop to manage this course.
In the loop, ask the user to enter 1 for adding a student, 2 for dropping a student,
3 for displaying course info, or 0 for exit.
If 1 is chosen, call the add_student method of the Course object and use a print statement
o display updated enrollment.  If 2 is chosen, call the drop_student method of the Course object
and use a print statement to display updated enrollment.  If 3 is chosen, display values stored in
the Course object to show course code, maximum class size and enrollment.

The following shows a sample test run:

Enter course code: CSC121
Enter maximum class size: 2
Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: 1
One student added.
Enrollment: 1

Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: 2
One student dropped
Enrollment: 0

Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: 2
Course is empty.
Enrollment: 0

Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: 1
One student added.
Enrollment: 1

Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: 1
One student added.
Enrollment: 2

Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: 1
Course already full.
Enrollment: 2

Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: 3
Course code: CSC121
Maximum class size: 2
Enrollment: 2

Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: 0

"""
from course import Course

def main():
    course_code = input("Enter course code: ")
    try:
        max_size = int(input("Enter maximum class size: "))
    except:
        print("must be an integer")
    else:
        print()
    my_course = Course(course_code,max_size)     # creates an instance of the course

    choice = -1
    while choice != 0:
        try:
            choice = int(input("Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: "))
            if choice < 0 or choice > 3:
                raise
        except:
            print("\033[1minvalid command. \033[0m")
        else:
            if choice == 1:
                my_course.add_student() # call add_student from Course
            elif choice == 2:
                my_course.drop_student()
            elif choice == 3:
                print("Course Code:",my_course.code )
                print("Maximum Class Size:",my_course.max_size )
                print("Enrollment:",my_course.enrollment)
            else:
                break

main()