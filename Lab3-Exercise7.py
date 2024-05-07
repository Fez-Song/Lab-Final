import numpy as np


def impute_missing_values(dataset, replace):
    fill_value = 0
    if replace == 'mean':
        fill_value = np.nanmean(dataset, axis=0)
        # print(fill_value)
    elif replace == 'median':
        fill_value = np.nanmedian(dataset, axis=0)
        # print(fill_value)
    else:
        print('Replace value must be either "mean" or "median"')

    impute_values = np.where(np.isnan(dataset), fill_value, dataset)
    return impute_values


Dataset = np.array([[1, 2, np.nan, 4],
                    [5, np.nan, 7, 8],
                    [9, 10, 11, np.nan]])

imputed_data_mean = impute_missing_values(Dataset, 'mean')
imputed_data_median = impute_missing_values(Dataset, 'median')

print("用平均值填充后的数据集：")
print(imputed_data_mean)
print("用中位数填充后的数据集：")
print(imputed_data_median)
