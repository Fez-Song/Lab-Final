
# Exercice 1.1

def is_even(num):
    return num % 2 == 0


number = int(input("Enter a number: "))
print(is_even(number))

# Exercice 1.2

"""score = int(input("Enter a number: "))

def grade_checker(mark):
    if mark >= 50:
        return 'Pass'
    else:
        return 'Fail'


print(grade_checker(score))"""

# Exercice 2

"""even_numbers = []
for i in range(0, 10):
    even_numbers.append(2 * i)

print("a list containing the first 10 even numbers", even_numbers)

print("iterate through the list:")
for num in even_numbers:
    print(num)

sum = 0
for num in even_numbers:
    sum = sum + num

print("Sum of even numbers:", sum)"""

# Exercise3
"""phonebook = {
    "John": "18712936268",
    "Fez": "17627796683",
    "Jack": "15900328682",
}


def lookup_number(name):
    return phonebook[name]


name = input("Enter a name(John, Fez, Jack): ")
print(lookup_number(name))"""

# Exercise 4
"""integers = [12, 2, 37, 4, 5, 6, 7, 80, 9]
print("Numbers greater than 10:")
for num in integers:
    if num > 10:
        print(num)
    else:
        continue

print("Number of elements divisible by 3:")
for num in integers:
    if num % 3 == 0:
        print(num)"""

# Exercise 5


"""def calculate_factorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, there is no factorial for negative numbers")
    elif num == 0:
        print("the factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f"the factorial of {num} is {factorial}")


number = int(input("Enter a number: "))
print(calculate_factorial(number))

print("the factorial of each number from 1 to 5:")
for num in range(1, 6):
    print(calculate_factorial(num))"""

# Exercise 6

"""students = [
    {"name": "John", "age": 20, "grade": 95},
    {"name": "Fez", "age": 19, "grade": 97},
    {"name": "Jack", "age": 19, "grade": 89}
]

print("Name and grade of each student:")
for student in students:
    print(f"Name: {student['name']}, Grade: {student['grade']}")

total_age = 0
for student in students:
    total_age = total_age + student['age']

average_age = total_age / len(students)

print("Average age of all students:", average_age)"""

# Exercise 7


"""def find_max(numbers):
    if not numbers:
        return None
    else:
        return max(numbers)


numbers = [3, 43, 65, 8, 0, -4, 31]
print("The largest number in the list is :", find_max(numbers))

class_scores = [
    [89, 80, 90],
    [85, 88, 92],
    [78, 92, 87]
]
i = 1
for scores in class_scores:
    highest_score = find_max(scores)
    print(f"Highest score in class {i}: {highest_score}")
    i = i + 1"""

# Exercise 8

"""students = [
    {"name": "John", "grade1": 95, "grade2": 98, "grade3": 99},
    {"name": "Fez", "grade1": 98, "grade2": 97, "grade3": 99},
    {"name": "Jack", "grade1": 99, "grade2": 99, "grade3": 99},
]


def average_grade(student):
    average_grades = {}
    for student in students:
        name = student["name"]
        grade = [student["grade1"], student["grade2"], student["grade3"]]
        average_grades[name] = sum(grade) / len(grade)
    return average_grades


average_grades = average_grade(students)
for name, avg_grade in average_grades.items():
    print(f"{name}'s average grade: {avg_grade}")

for key in average_grades:
    if average_grades[key] == max(average_grades.values()):
        print(f"Student with the highest average grade is {name}: {average_grades[key]}")

new_students = {"name": "Jake", "grade1": 95, "grade2": 95, "grade3": 94}
students.append(new_students)
print(students)

average_grades_dict = average_grade(students)
for name, avg_grade in average_grades_dict.items():
    print(f"{name}'s updated average grade: {avg_grade}")"""
