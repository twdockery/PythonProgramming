# Tyler Dockery for CSC121 5-18-2020 twdockery@waketech.edu
"""
The jackpot of a lottery is paid in 20 annual installments.  There is also a cash option, which pays the winner 65% of the jackpot instantly.  In either case 30% of the winnings will be withheld for tax. Design a program to do the following.  Ask the user to enter the jackpot amount. Calculate and display how much money the winner will receive annually before tax and after tax if annual installments is chosen. Also calculate and display how much money the winner will receive instantly before and after tax if cash option is chosen.
Step 1: input jackpot
Step 2: calculate annual before = jackpot / 20
Step 3: calculate annual after = (jackpot / 20) * .7
Step 4: calculate instant before = jackpot
Step 5: calculate instant after = jackpot * .7
Step 6: display annual before
Step 7: display annual after
Step 8: display instant before
Step 9: display instant after
"""
jackpot = int(input("How much is the jackpot amount? "))
annual_before = jackpot / 20
annual_after = (jackpot / 20) * .7
instant_before = jackpot
instant_after = jackpot * .7
print(f"With a jackpot of {jackpot} you will receive:")
print(f"${annual_before} a year for 20 years, but it would be ${annual_after:.2f} a year after taxes.")
print(f"OR you could receive ${instant_before} instantly, although it would be ${instant_after:.2f} after taxes")
