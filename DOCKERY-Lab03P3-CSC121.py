#Tyler Dockery for CSC121 5-19-2020 twdockery@waketech.edu
'''
Write a program to do the following.  Ask the customer to enter “S” for standard shipping or “E” for express shipping.  Also ask the user to enter the weight of the package in pounds.  Calculate and display shipping charge.
''' 
print('Thank you for choosing Dockery Shipping')

# Ask for standard or express shipping
shipment = input("Enter S for standard shipping, E for express ")
if shipment.lower() != "s" and shipment.lower() != "e":  # just to stop bad answers
    print("We don't have that kind of shipping. Please start again.")
    charge = 0

# Calculate the cost based on weight
else:
    weight = float(input("Enter weight (lbs): "))
    if shipment.lower() == "s":
        if weight <= 4:
            charge = weight * 1.05
        elif 4 < weight <= 8:
            charge = weight * 0.95
        elif 8 < weight <= 15:
            charge = weight * 0.85
        else:
            charge = weight * 0.8
    if shipment.lower() == "e":
        if weight <= 2:
            charge = weight * 3.25
        elif 2 < weight <= 5:
            charge = weight * 2.95
        elif 5 < weight <= 10:
            charge = weight * 2.75
        else:
            charge = weight * 2.55
# Output the cost
print(f'Shipping charge: ${charge:.2f}  (${charge})')