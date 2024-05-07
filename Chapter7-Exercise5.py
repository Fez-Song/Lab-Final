import pandas as pd
import numpy as np

index = pd.MultiIndex.from_product([['A', 'B', 'C'], [1, 2, 3]], names=['Class', 'Students'])
columns = ('Math_grades', 'Science_grades')
df = pd.DataFrame(np.random.randint(50, 100, size=(9, 2)), index=index, columns=columns)
print(df)

class_b = df.loc[('B', pd.IndexSlice[:]), 'Math_grades'][df.loc[('B', pd.IndexSlice[:]), 'Math_grades'] > 80]
print("Grades of all students from class B whose Math score is greater than 80:")
print(class_b)

student_2 = df.loc[(pd.IndexSlice[:], 2), 'Science_grades'][df.loc[(pd.IndexSlice[:], 2), 'Science_grades'] < 85]
print("Grades of Student 2 from all classes whose Science score is less than 85:")
print(student_2)



