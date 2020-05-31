"""
The energy company in Program 1 now uses different rates for residential and business customers.
Residential customers pay $0.12 per kWh for the first 500 kWh.  After the first 500 kWh, the rate is $0.15 per kWh.
Business customers pay $0.16 per kWh for the first 800 kWh.  After the first 800 kWh, the rate is $0.20 per kWh.
Write a program to calculate energy charge.  You must write and use the following two functions.
•	A main function: Ask the user to enter number of kWh used and customer type (enter R for residential or B for business).
Call the bill_calculator function and pass number of kWh used and customer type to it as arguments.
You must use positional arguments to pass kWh used and customer type.
•	A bill_calculator function: This function has two parameters to receive number of kWh used and customer type.
Calculate and display the energy charge.
The following is an example.

Enter kilowatt hours used: 810
Enter R for residential customer, B for business customer: R
Please pay this amount: 106.50

The following is another example.

Enter kilowatt hours used: 810
Enter R for residential customer, B for business customer: b
Please pay this amount: 130.00

"""
def main():
    print("Welcome to the power company!")
    kwh = float(input("How many kWh have you used? "))
    customer = input("Enter R for residential customer, B for business customer: ")
    bill_calculator(kwh, customer)

def bill_calculator(power, type):
    if type.lower() == "b":
        if power > 800:
            charge = ((power - 800) * 0.20) + (800 * 0.16)  # 0.12 for first 500. 0.15 for others
        else:
            charge = power * 0.16

    if type.lower() == "r":
        if power > 500:
            charge = ((power - 500) * 0.15) + (500 * 0.12) #0.12 for first 500. 0.15 for others
        else:
            charge = power * 0.12
    print(f"Please pay this amount: ${charge:.2f}")

main()