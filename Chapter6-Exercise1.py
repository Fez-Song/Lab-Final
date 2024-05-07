import seaborn as sns

titanic = sns.load_dataset('titanic')

print("First few rows of the dataset:")
print(titanic.head())

missing_values = titanic.isnull().sum()
print("Number of missing values in each column:")
print(missing_values)

titanic_cleaned = titanic.dropna()

print("Dataset after removing rows with missing data:")
print(titanic_cleaned.head())
