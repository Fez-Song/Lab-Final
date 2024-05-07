import pandas as pd
student_scores = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [85, 70, 90, 65],
    'Science': [55, 75, 40, 80],
})
print(student_scores.query('Math>80'))
print(student_scores.query('Science<60'))
print(student_scores[student_scores['Science'] < 60])
