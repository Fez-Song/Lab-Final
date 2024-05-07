import numpy as np


def normalize_data(dataset):
    dataset_min = np.min(dataset, axis=0)
    dataset_max = np.max(dataset, axis=0)
    normalizes_dataset = (dataset - dataset_min) / (dataset_max - dataset_min)
    return normalizes_dataset


Dataset = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
normalize_Data = normalize_data(Dataset)
print(normalize_Data)
