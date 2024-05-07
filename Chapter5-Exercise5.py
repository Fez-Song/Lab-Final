import numpy as np
import pandas as pd

index_labels = pd.date_range(start='2022-01-01', periods=5)
date_of_observation = pd.DataFrame(np.random.uniform(0, 100, size=(5, 1)), index=index_labels, columns=['data'])
print(date_of_observation)

data_sqrt = np.sqrt(date_of_observation)
print(data_sqrt)
data_round = np.around(date_of_observation)
print(data_round)
