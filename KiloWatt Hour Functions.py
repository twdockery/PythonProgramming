# Tyler Dockery for CSC121  5-26-2020  twdockery@waketech.edu
"""
Energy consumption is measured in units of kilowatt hours (kWh). The more kWh a household use in a month, the higher the energy bill.
A power company charges customers $0.12 per kWh for the first 500 kWh.
After the first 500 kWh, the rate is $0.15 per kWh.  Write a program to calculate energy charge.
You must write and use the following two functions.
	•	A main function: Ask the user to enter number of kWh used.
	Call the bill_calculator function and pass number of kWh used to it as an argument.
	•	A bill_calculator function: This function has a parameter to receive number of kWh used.
	Calculate and display the energy charge.

The following is an example.
Enter kilowatt hours used: 510
Please pay this amount: 61.50
"""
def main():
    print("Welcome to the power company!")
    kwh = float(input("How many kWh have you used? "))
    bill_calculator(kwh)

def bill_calculator(power):
    if power > 500:
        charge = ((power - 500) * 0.15) + (500 * 0.12) #0.12 for first 500. 0.15 for others
    else:
        charge = power * 0.12
    print(f"Please pay this amount: ${charge:.2f}")

main()
