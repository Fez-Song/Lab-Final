import numpy as np
import pandas as pd

index_labels = pd.date_range(start='2022-01-01', periods=5)

date_of_observation1 = pd.DataFrame(np.random.uniform(0, 100, size=(5, 1)), index=index_labels, columns=['data'])
date_of_observation2 = pd.DataFrame(np.random.uniform(0, 100, size=(5, 1)), index=index_labels, columns=['data'])

print(date_of_observation1)
print(date_of_observation2)

add_column = date_of_observation1 + date_of_observation2
print(add_column)
subtract_column = date_of_observation2 - date_of_observation1
print(subtract_column)
