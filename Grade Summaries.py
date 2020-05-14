def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

# In this program, grades have been added to dictionaries
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])

    total = homework * .1 + quizzes * .3 + tests * .6
    return total


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

# a list is built including all the students names
students = (lloyd, alice, tyler)
class_list = (lloyd, alice, tyler)

for everyItem in students:
    print(everyItem["name"])
    print("Homework Grades: %s" % (everyItem["homework"]))
    print("Quiz Grades: %s" % (everyItem["quizzes"]))
    print("Test Grades: %s" % (everyItem["tests"]))
    print("Final Grade at this time: %s (%s)" % (
    round(get_average(everyItem), 2), get_letter_grade(get_average(everyItem))))  # rounds the variable to 2 places
    print("")

print("Class Average: %s%% (%s)" % (round(get_class_average(class_list), 2), get_letter_grade(get_class_average(
    class_list))) ) #%s substitutes, %s%% add % to the
# substitute