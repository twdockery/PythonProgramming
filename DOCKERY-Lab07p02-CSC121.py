"""Rewrite Program 2.  This is you must use keyword arguments to pass number of kWh and customer type to the bill_calculator function when it is called.

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