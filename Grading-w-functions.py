"""
Students in a course need to do lab assignments and take tests.  Course grade is calculated from these scores.
Write a program to calculate course grade.  You must write and use the following two functions.
• A main function:
First, ask the user how many labs there are. Use a loop to enter lab scores and store them in a list. Display the list of lab scores.
Second, ask the user how many tests there are.Use a loop to enter test scores and store them in another list.  Display the list of test scores.
Third, tell the user that the default weights for labs and tests are 50 and 50.
If the user wants to use the default weights, enter D. Otherwise, enter C.
If the user chooses to use default weights, call the grade_calculator function and pass the list of lab scores
and the list of test scores as two arguments. Do not pass any other arguments.
If the user chooses not to use default weights, ask the user to enter the weights for labs and tests, respectively.
Then call the grade_calculator function and pass the list of lab scores, the list of test scores,
lab weight and test weight as four arguments. You are free to use positional or keyword arguments.
• A grade_calculator function: This function has four parameters: lab score list, test score list, lab weight and test weight.
Use default arguments for lab weight and test weight. Default values are 50 and 50.
First, calculate and display average lab score.
Second, calculate and display average test score.
Third, use average lab score, average test score, lab weight and test weight to calculate course grade. Display course grade.

The following is an example. Default weights are used.

How many labs? 3
Enter a lab score: 87
Enter a lab score: 93
Enter a lab score: 90
Lab scores: [87.0, 93.0, 90.0]
How many tests? 2
Enter a test score: 85
Enter a test score: 75
Test scores: [85.0, 75.0]

The default weights for course grade are 50% labs and 50% tests.
Enter C to change the weights or D to use default weights: D
Lab average: 90.00
Test average: 80.00
Course grade: 85.00

The following is another example. Default weights are not used.

How many labs? 3
Enter a lab score: 93
Enter a lab score: 87
Enter a lab score: 90
Lab scores: [93.0, 87.0, 90.0]
How many tests? 2
Enter a test score: 85
Enter a test score: 75
Test scores: [85.0, 75.0]

The default weights for course grade are 50% labs and 50% tests.
Enter C to change the weights or D to use default weights: c
Enter lab percentage (without the % sign): 60
Enter test percentage (without the % sign): 40
Lab average: 90.00
Test average: 80.00
Course grade: 86.00
"""
print("Let's Weigh Those Grades!")
def main():
    labs = []
    num = int(input("How many labs are there? "))
    for x in range(num):
        labs.append(float(input("Enter a lab score: ")))
    print(labs)

    tests = []
    num = int(input("How many tests are there? "))
    for x in range(num):
        tests.append(float(input("Enter a test score: ")))
    print(tests)

    print()
    print("The default weights for labs and tests are 50% and 50%.")
    weight = input("Would you like to use the [D]efault or [C]hange the weights? ")

    if weight == "c":
        l_percent = float(input("Enter lab percentage (without the % sign): "))
        t_percent = float(input(f"Enter Test percentage (without the % sign) [I suggest {100 - l_percent}%] : "))
        grade_calculator(labs, tests, lab_weight=l_percent, test_weight=t_percent)
    else:
        grade_calculator(labs, tests, 50, 50) #default of 50/50 passed

def grade_calculator(lab_score_list, test_score_list, lab_weight, test_weight):
    lab_avg = 0
    test_avg = 0
    lab_weight /= 100  # Turns numbers to percentages for weighting
    test_weight /= 100

    for x in lab_score_list:
        lab_avg += (x / len(lab_score_list))
    print("Lab Average: ",lab_avg)
    for x in test_score_list:
        test_avg += (x / len(test_score_list))
    print("Test Average: ",test_avg)
    print("Course Grade: ",((lab_avg * lab_weight) + (test_avg * test_weight)))

main()