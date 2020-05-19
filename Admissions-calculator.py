# Tyler Dockery for CSC121 5-28-2020 twdockery@waketech.edu
"""
Admission to an aquarium is $14 per person.  There is also an IMAX theatre in the building, which charges $8 per ticket for a 3D shark show.  Customers have three choices: admission to the aquarium only without watching 3D show, watch 3D show only with no admission to the aquarium, or do both with a 25% discount.  Design a program for group orders.  Ask the group to enter number of people who want admission only but no 3D show, number of people who want 3D show only but no admission to the aquarium, and number of people who want both.  Calculate and display the total amount due from the group.
Step 1: input admission only
Step 2: input 3d only
Step 3: input both
Step 4: calculate total = (admission only * 14) + (3d only * 8) + (both * (22 * 0.75))
Step 5: display total
"""
admission_only = int(input("How many Admissions only in the group? "))
three_d_only = int(input("How many 3D Movie only in the group? "))
both = int(input("How many admission + 3d tickets (25% discount) in the group? "))
total = (admission_only * 14) + (three_d_only * 8) + (both * 22 * 0.75) #only paying 75% of the full price
print(f"your total price is: ${total:.2f}")