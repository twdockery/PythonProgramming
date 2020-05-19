"""
Step 1: input admission only
Step 2: input 3d only
Step 3: input both
Step 4: calculate total = (admission only * 14) + (3d only * 8) + (both * (22 * 0.75))
Step 5: display total
"""
admissionOnly = int(input("How many Admissions only in the group? "))
threeDOnly = int(input("How many 3D Movie only in the group? "))
both = int(input("How many admission + 3d tickets (25% discount) in the group? "))
total = (admissionOnly * 14) + (threeDOnly * 8) + (both * 22 * 0.75)
print("your total price is: $%s" % (total))