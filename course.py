# Tyler Dockery for CSC121  7.12.2020  twdockery@waketech.edu
"""
Define a class Course in this file.  This class has three publicly accessible instance variables to store:
course code, maximum class size and enrollment.  Define the following methods:

•	An __init__ method that accepts course code and maximum class size as arguments.
Write statements in __init__ to store them in instance variables. Also create an instance variable
to store enrollment and initialize it to 0.
•	An add_student method to increase enrollment by one and display “One student added”
if the course is not full.  If the course is already full, make no change to enrollment
and display “Course already full”.  This method has no argument other than self and has no return value.
•	A drop_student method to decrease enrollment by one and display “One student dropped”
if the course is not empty.  If the course is empty, make no change to enrollment and
display “Course is empty”.  This method has no argument other than self and has no return value.

The following class diagram shows the design of this class:

Course
+course_code: String
+max_size: Integer
+enrollment: Integer
+Course(course_code:String, max_size:Integer)
+add_student()
+drop_student()

"""


class Course:

    def __init__(self, c_code, c_max_size):

        """ constructor of class Course """
        self.code = c_code
        self.max_size = c_max_size
        self.enrollment = 0

    def add_student(self):
        # add only if students are less than max size. if full, cannot add students
        if self.enrollment < self.max_size:
            self.enrollment += 1
            print("1 student added.")
            print("Enrollment: ",self.enrollment)
        else:
            print("\033[1mCourse already full.\033[0m") #bold for fun
            print("Enrollment: ",self.enrollment)


    def drop_student(self):
        # drop only if students are in class. if empty, cannot drop students
        print("drop")
        if self.enrollment > 0:
            self.enrollment -= 1
            print("1 student dropped.")
            print("Enrollment: ",self.enrollment)
        else:
            print("\033[1mCourse is empty.\033[0m")  # bold for fun
            print("Enrollment: ",self.enrollment)

