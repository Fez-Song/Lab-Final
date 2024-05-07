import pandas as pd
import numpy as np

index = pd.MultiIndex.from_product([['A', 'B', 'C'], [1, 2, 3]], names=['Class', 'students'])
columns = ('Math_grades', 'Science_grades')
df = pd.DataFrame(np.random.randint(50, 100, size=(9, 2)), index=index, columns=columns)
print(df)


