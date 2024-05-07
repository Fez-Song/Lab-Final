import numpy as np


def scale_data(data_set):
    data_set_mean = np.mean(data_set, axis=0)
    data_set_std = np.std(data_set, axis=0)
    scale_dataset = (data_set - data_set_mean) / data_set_std
    return scale_dataset


data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
dataset = scale_data(data)
print(dataset)
