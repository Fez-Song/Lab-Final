students = [
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
    print(f"{name}'s updated average grade: {avg_grade}")