"""
Write a loop to control the speed and height of the drone.  In the loop, ask the user to enter:
1 for acceleration, 2 for deceleration, 3 for ascending, 4 for descending, or 0 for exit.
Call the appropriate method of the Drone object to change the speed or height of the drone.
Every time the speed or height of the drone changes, display the speed and height.
"""
from drone import Drone
speed = 0
height = 0

main()
    choice = 5
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
                speed = speed + 10
            elif choice == 2:
                if speed == 0:
                    print("\033[1mDrone is already stopped.\033[0m") #bold for fun
                else:
                    speed = speed - 10
            elif choice == 3:
                height = height + 10
            elif choice == 4:
                if height == 0:
                    print("\033[1mDrone is already on the ground.\033[0m") #bold for fun
                else:
                    height = height - 10
            else:
                break
        print("Speed: ", speed,"  height: ",height)

main()