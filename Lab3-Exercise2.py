import numpy as np

students = 30
tests = 3
students_score = np.random.randint(0, 100, (students, tests))
print(students_score)

average_scores = np.mean(students_score, axis=0)
for i, average_score in enumerate(average_scores):
    print(f"The average score of Test{i + 1}:{average_score}")
