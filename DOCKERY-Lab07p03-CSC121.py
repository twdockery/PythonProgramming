"""In Lab 07 we wrote a program to calculate energy bill for residential and business customers.
We are going to rewrite that program with value returning functions.
Residential customers pay $0.12 per kWh for the first 500 kWh.  After the first 500 kWh, the rate is $0.15 per kWh.
Business customers pay $0.16 per kWh for the first 800 kWh.  After the first 800 kWh, the rate is $0.20 per kWh.
Write a program to calculate energy charge.  You must write and use the following functions.

• A main function: Call the value returning function get_user_input, which returns kWh used and customer type.
Pass the return values to the value returning function bill_calculator as two arguments.
Display the return value of bill_calculator.

• A get_user_input function: This function has no parameter.  It asks the user to enter number of kWh used.
Use an input validation loop to ensure that kWh used is not negative.
Also ask the user to enter customer type (enter R for residential or B for business).
Convert lowercase letter to uppercase.  Use an input validation loop to ensure that customer is either R or B.
Return kWh used and customer type.

• A bill_calculator function: This function has two parameters to receive number of kWh used and customer type.
Calculate and return the energy charge.

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
    bill_calculator(power=kwh, type=customer)

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