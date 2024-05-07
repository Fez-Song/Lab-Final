import numpy as np


def shuffle_data(dataset):
    np.random.shuffle(dataset)
    return dataset


Dataset = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12],
                    [13, 14, 15]])

new_Dataset = shuffle_data(Dataset)
print("Random shuffled dataset:")
print(new_Dataset)
