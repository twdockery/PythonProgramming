# Tyler Dockery for CSC121 7/12/2020  twdockery@waketech.edu
"""
Define a class Drone in this file.  This class has the following five methods:
•	__init__ : Create two instance variables to store the speed and the height of the drone.
	Initialize them to 0.0. This method has no parameters other than self and no return value.
•	accelerate : Increase the speed of the drone by 10.
	his method has no parameters other than self and no return value.
•	decelerate : Decrease the speed of the drone by 10.  The new speed cannot be negative.
	This method has no parameters other than self and no return value.
•	ascend : Increase the height of the drone by 10.
	This method has no parameters other than self and no return value.
•	descend : Decrease the height of the drone by 10.  The new height cannot be negative.
	This method has no parameters other than self and no return value.

   The following class diagram shows the design of this class:

Drone
+speed: Float
+height: Float
+Drone()
+accelerate()
+decelerate()
+ascend()
+descend()
"""
class Drone:

    def __init__(self):
        """ constructor of class Student """
        self.__speed = 0.0
        self.__height = 0.0

    def accelerate(self):
        """ input from user """
        self.__speed += 10

    def decelerate(self):
        """ input from user """
        if self.__speed == 0:
            print("\033[1mDrone is already stopped.\033[0m")  # bold for fun
        else:
            self.__speed -= 10

    def ascend(self):
        """ input from user """
        self.__height += 10

    def descend(self):
        """ input from user """
        if self.__height == 0:
            print("\033[1mDrone is already on the ground.\033[0m")  # bold for fun
        else:
            self.__height -= 10

    def __str__(self):
        """ Set String method to access data """
        return "speed:"+str(self.__speed)+" height:"+str(self.__height) # <=== really hard to figure out!
