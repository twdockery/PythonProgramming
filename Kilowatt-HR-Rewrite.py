"""
In Lab 07 we wrote a program to calculate energy bill for households.
A power company charges customers $0.12 per kWh for the first 500 kWh.
After the first 500 kWh, the rate is $0.15 per kWh.
Write a program to calculate energy charge.  You must write and use the following functions.
•	A main function: Call the value returning function get_kWh_used.
Pass the return value to the value returning function bill_calculator as an argument.
Display the return value of bill_calculator.
•	A get_kWh_used function: This function has no parameter.  It asks the user to enter number of kWh used.
Use an input validation loop to ensure that kWh used is not negative. Return kWh used.
•	A bill_calculator function: This function has a parameter to receive number of kWh used.
Calculate and return the energy charge.

The following is an example.

Enter kilowatt hours used: -5
kWh cannot be negative.
Enter kilowatt hours used: -6
kWh cannot be negative.
Enter kilowatt hours used: 510
Please pay this amount: $61.50
"""
def main():
    print(f"Please pay this amount: ${bill_calculator(get_kwh_used()):.2f}")

def get_kwh_used():
    # kwh = 0    #failed debug
    kwh = float(input("Enter number of kWh used: "))
    if kwh >= 0:
        return kwh
    else:
        print("kWh cannot be negative.")
        get_kwh_used()

def bill_calculator(hrs):
    if float(hrs) <= 500:
        charge = hrs * 0.12
        return charge

    else:
        hrs -= 500
        charge = hrs * 0.15
        charge += 500 * 0.12
        return charge

main()