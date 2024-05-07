import numpy as np

students = 10
students_age = np.random.randint(10, 20, size=students)
average_age = np.mean(students_age)
filtered_ages = students_age[students_age > average_age]

print(f"The ages of students in the class are:{students_age}")
print(f"The average age is {average_age}")
print(f"the ages that are above the mean age:{filtered_ages}")
