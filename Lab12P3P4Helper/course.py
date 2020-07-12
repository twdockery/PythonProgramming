class Course:

    def __init__(self, c_code, c_max_size):

        # initialize self.__code to c_code

        # initialize self.__max_size to c_max_size

        # initialize self.__enrollment to 0


    def add_student(self):

        # if self.__enrollment is less than self.__max_size, increase self.__enrollment by 1 and display "one student added"

        # else display "Course already full"


    def drop_student(self):

        # if self.__enrollment is greater than 0, decrease self.__enrollment by 1 and display "One student dropped"

        # else display "Course is empty"


    def get_course_code(self):
        # return self.__code

    def get_enrollment(self):
        # return self.__enrollment

    def get_max_size(self):
        # return self.__max_size

    def set_max_size(self, new_max_size):

        # if new_max_size < 0, display "Maximum class size cannot be negative."

        # elif new_max_size < self.__enrollment, display "Maximum class size cannot be lower than current enrollment."

        # else change self.__max_size to new_max_size and display "Maximum class size changed."
