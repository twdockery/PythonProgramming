# Tyler Dockery for CSC121  6-5-2020  twdockery@waketech.edu
"""
Create a module currency, which includes the following three functions that do currency conversions:

to_euro(dollar): This function receives US Dollar as an argument and converts it to Euro.  1 US Dollar = 0.81 Euro.  Return Euro.
to_yen(dollar): This function receives US Dollar as an argument and converts it to Japanese Yen.  1 US Dollar = 106.45 Yen.  Return Yen.
to_peso(dollar): This function receives US Dollar as an argument and converts it to Mexican Peso.  1 US Dollar = 18.58 Peso.  Return Peso.
Store these three functions in a file named currency.py.
"""
# This module is used to calculate the exchange of US to foreign currency.

def to_euro(dollar):
    euro = dollar * 0.81
    return euro

def to_yen(dollar):
    yen = dollar * 106.45
    return yen

def to_peso(dollar):
    peso = dollar * 18.58
    return peso