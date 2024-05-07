import seaborn as sns

diamonds = sns.load_dataset('diamonds')

print("First few rows of the dataset:")
print(diamonds)

missing_values = diamonds.isnull().sum()
print("Number of missing values in each column:")
print(missing_values)

mean_values = diamonds.select_dtypes(include='number').mean()
diamonds_filled = diamonds.fillna(mean_values, inplace=True)
print("Dataset after replacing missing values:")
print(diamonds)
