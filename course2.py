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

class Course(course_code, max_size, enrollment):
    def __init__(self, course_code, max_size):
        self.code = "c_code"
        self.max_size = 0
        self.enrollment = 0

    def add_student(self):
        """
        if enrollment = max_size:
            print("Course already full.")
        else:
            self.enrollment += 1
            print("1 student added.")
        """

    def drop_student(self):
        """
        if enrollment == 0:
            print("Course already empty.")
        else:
            self.enrollment -= 1
            print("1 student dropped.")
        """