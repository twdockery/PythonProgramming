"""

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
annualBefore = jackpot / 20
annualAfter = (jackpot / 20) * .7
instantBefore = jackpot
instantAfter = jackpot * .7
print("With a jackpot of $%s, you will receive:" % (jackpot, ))
print("$%s a year for 20 years, but $%s a year after taxes" % (annualBefore, annualAfter))
print("$%s instantly, but $%s after taxes" % (instantBefore, instantAfter))
