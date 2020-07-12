# Tyler Dockery for CSC121 7/12/2020  twdockery@waketech.edu
"""
Write a loop to control the speed and height of the drone.  In the loop, ask the user to enter:
1 for acceleration, 2 for deceleration, 3 for ascending, 4 for descending, or 0 for exit.
Call the appropriate method of the Drone object to change the speed or height of the drone.
Every time the speed or height of the drone changes, display the speed and height.
"""
from drone import Drone

my_drone = Drone() # creates an instance of the drone

def main():
    choice = -1
    while choice != 0:
        try:
            choice = int(input("Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: "))
            if choice < 0 or choice > 4:
                raise()
        except:
            print("\033[1mImproper command.\033[0m") #bold for fun
        else:
            # print("choice: ",choice) #debug
            if choice == 1:
                my_drone.accelerate() #call accelerate from drone.py Drone class
            elif choice == 2:
                my_drone.decelerate()
            elif choice == 3:
                my_drone.ascend()
            elif choice == 4:
                my_drone.descend()
            else:
                print("Goodbye")
                break
        print("Speed: ", my_drone.speed,"  height: ",my_drone.height)

main()