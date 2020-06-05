"""
Create a module currency, which includes the following three functions that do currency conversions:

to_euro(dollar): This function receives US Dollar as an argument and converts it to Euro.  1 US Dollar = 0.81 Euro.  Return Euro.
to_yen(dollar): This function receives US Dollar as an argument and converts it to Japanese Yen.  1 US Dollar = 106.45 Yen.  Return Yen.
to_peso(dollar): This function receives US Dollar as an argument and converts it to Mexican Peso.  1 US Dollar = 18.58 Peso.  Return Peso.
Store these three functions in a file named currency.py.

Create a file for the main module.  Name the file lab08P3.py.

Define a main function in the main module to do the following:
• Ask the user to choose a foreign currency: Euro, Japanese Yen or Mexican Peso.
Write a loop to validate user input. If an invalid choice is made, display an error message and
ask the user to choose a foreign currency again until the choice is valid.
• Ask the user to enter US dollar amount. Write a loop to validate user input.
If the US dollar amount is negative, display an error message and ask the user to reenter it until it is non-negative.
• Call one of the three functions in the currency module to convert US dollar to the foreign currency chosen by the user
• Receive and display the converted foreign currency

  The following is an example.

Converting US Dollar to a foreign currency.
Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: 4
Error: Invalid Choice
Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: 5
Error: Invalid Choice
Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: 2
Enter US Dollar: -100
Error: US Dollar cannot be negative.
Enter US Dollar: -200
Error: US Dollar cannot be negative.
Enter US Dollar: 100
It is converted to 10645.0 Yen
"""

import currency  #this imports currency.py module

def main():
    print("Welcome to the foreigh currency exchange!")
    foreign_currency = input("Please choose a foreign currency: [E]uro, Japanese [Y]en or Mexican [P]eso: ")
    while foreign_currency.lower() != "e" and foreign_currency.lower() != "y" and foreign_currency.lower() != "p":
        print("Invalid Choice.")
        foreign_currency = input("Please choose a foreign currency: [E]uro, Japanese [Y]en or Mexican [P]eso: ")

    exchange = float(input("How much would you like to exchange? "))
    while exchange < 0:
        print("US Dollar amount cannot be negative.")
        exchange = float(input("How much would you like to exchange? "))

    if foreign_currency.lower() == "e":
        print(f"It is converted to {currency.to_euro(exchange)} Euros")
    elif foreign_currency.lower() == "y":
        print(f"It is converted to {currency.to_yen(exchange)} Yen")
    else: #if not Euros or Yen, it must be Pesos
        print(f"It is converted to {currency.to_peso(exchange)} Pesos")

main()