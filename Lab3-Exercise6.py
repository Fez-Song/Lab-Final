import numpy as np


def select_features(dataset, feature_indices):
    selected_features = dataset[:, feature_indices]
    return selected_features


Dataset = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
Feature_indices = [0, 2]
print(select_features(Dataset, Feature_indices))
