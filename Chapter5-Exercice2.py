import numpy as np
import pandas as pd

students_data = {
    'age': [20, 21, 19],
    'grade': ['A', 'B', 'C'],
    'gender': ['M', 'F', 'M'],
}

student_name = ['Fez', 'Ace', 'Jake']

df = pd.DataFrame(students_data, index=student_name)
print(df)