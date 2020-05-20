# Tyler Dockery for CSC121 5-20-2020 twdockery@waketech.edu
"""
Diabetes is diagnosed by measuring patient’s fasting plasma glucose level (FPG).  If FPG is higher than 125, the patient has diabetes.  If FPG is higher than 100 but not higher than 125, the patient has pre-diabetes.  FPG 100 or lower is considered as a healthy level.  Write a program to do diabetes diagnosis for multiple patients.  For each patient, enter FPG and determine whether the patient has diabetes, pre-diabetes or a healthy FPG level.  Ask the user to answer a yes/no question to indicate whether he/she wants to do diagnosis for another patient.
""" 
print("Welcome to Diabetes Diagnostic Services")
again = "y"
while again.lower() == "y":
    fpg = float(input("Patient’s fasting plasma glucose level (FPG) "))
    if fpg > 125:
        print("This patient has diabetes.")
    elif 100 < fpg <= 125:
        print("This patient is pre-diabetic.")
    else:
        print("This patient has healthy FPG.")
    again = (input("Check diabetes for another patient? [y/n] "))
