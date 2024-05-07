students = [
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

print("Average age of all students:", average_age)