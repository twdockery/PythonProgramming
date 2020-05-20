#Tyler Dockery for CSC121 5-19-2020 twdockery@waketech.edu
'''
Residential and business customers are paying different rates for water usage.  Residential customers pay $0.005 per gallon for the first 6000 gallons.  If the usage is more than 6000 gallons, the rate will be $0.007 per gallon after the first 6000 gallons.  Business customers pay $0.006 per gallon for the first 8000 gallons.  If the usage is more than 8000 gallons, the rate will be $0.008 per gallon after the first 8000 gallons.  For example, a residential customer who has used 9000 gallons will pay $30 for the first 6000 gallons ($0.005 * 6000), plus $21 for the other 3000 gallons ($0.007 * 3000).  The total bill will be $51.  A business customer who has used 9000 gallons will pay $48 for the first 8000 gallons ($0.006 * 8000), plus $8 for the other 1000 gallons ($0.008 * 1000).  The total bill will be $56.  Write a program to do the following.  Ask the user which type the customer it is and how many gallons of water have been used.  Calculate and display the bill.
''' 
# Ask the user which type the customer it is how many gallons of water have been used.
print("Welcome to the municipal waterworks billing center")
customer_type = input("Enter R for residential customer or B for business customer: ")
bill = 0
if customer_type.lower() != "r" and customer_type != "b":
    print("We don't serve those customers here")

# Calculate costs
else:
    gallons = float(input("How many gallons of water were used? "))
    if customer_type.lower() == "r" and gallons <= 6000:
        bill = gallons * 0.005 # 0.005 for the first 6000 gallons
    elif customer_type.lower() == "r" and gallons > 6000:
        gallons -= 6000 # removes the first 6000 gallons
        bill += 6000 * 0.005 # first 6000 gallons at lower rate added to bill
        bill += gallons * 0.007 # remaining gallons at the higher rate
    elif customer_type.lower() == "e" and gallons <= 8000:
        bill = gallons * 0.006 # 0.006 for the first 8000 gallons
    else: # customer_type.lower() == "e" and gallons > 8000:
        gallons -= 8000  # removes the first 8000 gallons
        bill += 8000 * 0.006  # first 8000 gallons at lower rate added to bill
        bill += gallons * 0.008  # remaining gallons at the higher rate

# Display the bill to the customer
print(f"Please pay this amount: ${bill:.2f} ({bill})") # rounded to 2 places