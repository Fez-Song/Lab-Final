import pandas as pd
import numpy as np

index = pd.MultiIndex.from_product([['A', 'B', 'C'], [1, 2, 3]], names=['Class', 'Students'])
columns = ('Math_grades', 'Science_grades')
df = pd.DataFrame(np.random.randint(50, 100, size=(9, 2)), index=index, columns=columns)
print(df)

my_new_students_grades = df.swaplevel('Class', 'Students').sort_index(level='Students', ascending=False)
print(my_new_students_grades)

df_sorted_class_descending = df.sort_index(level='Class', ascending=False)
print(df_sorted_class_descending)
