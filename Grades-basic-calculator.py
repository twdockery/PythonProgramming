lab1 = int(input("Lab 1 score: "))
lab2 = int(input("Lab 2 score: "))
lab3 = int(input("Lab 3 score: "))
test1 = int(input("Test 1 score: "))
test2 = int(input("Test 2 score: "))
labAverage = (lab1 + lab2 +lab3) / 3
testAverage = (test1 + test2) / 2
courseGrade = (labAverage * 0.55) + (testAverage * 0.45)
print("Lab Average: %s" % (labAverage))
print("Test Average: %s" % (testAverage))
print("Course Grade: %s" % (courseGrade))