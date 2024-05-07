import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import scipy.stats as stats

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
print("The initial dataset:\n")
print(df)

# Data cleaning
print("Calculate the number of missing values in the dataset:\n")
print(df.isna().sum())
print("By calculating the missing value of the data set, \n"
      "we can see that the missing data are all in the column of sleep disorder, \n"
      "so it can be inferred that the people corresponding to these missing data have no sleep disorder, \n"
      "so we fill in the missing data as Nothing.\n")
df = df.fillna("Nothing")
df["BMI Category"] = df["BMI Category"].replace("Normal Weight", "Normal")
print(df)

# The features
print("\nThe features are:")
for column in df.columns:
    print("     -" + str(column))

# Calculate summary statistics for numerical variables
numerical_data = df.select_dtypes(include='number')
print("Summary Statistics for Numerical Variables:\n ")
print(numerical_data.info())

# Summarize the mode of the categorical variable
categorical_data = df.select_dtypes(include=['object'])
print("Mode Summary for Categorical Variables:\n")
print(categorical_data.mode().transpose())

# Computes the min-maximum interval for a numerical variable
print("\nThe min-maximum interval for a numerical variable")
numeric_variables = df.select_dtypes(include=['int', 'float']).columns
for col in numeric_variables:
    min_val = df[col].min()
    max_val = df[col].max()
    print(f'\n{col}: Min: {min_val} - Max: {max_val}')


def calculate_statistics(data, variable):
    # Calculate the mean of the variable
    mean_value = data[variable].mean()
    print(f"\nThe average of {variable}:{mean_value}")

    # Calculate the standard deviation of the variable
    std_value = data[variable].std()
    print(f"The standard deviation of {variable}:{std_value}")

    # Calculate the variance of the variable
    variance_value = data[variable].var()
    print(f"The variance of {variable}:{variance_value}")


# Mean, standard deviation and variance of age
calculate_statistics(df, 'Age')

# Mean, standard deviation and variance of sleep duration
calculate_statistics(df, 'Sleep Duration')

# Mean, standard deviation and variance of quality of sleep
calculate_statistics(df, 'Quality of Sleep')

# Mean, standard deviation and variance of Physical Activity Level
calculate_statistics(df, 'Physical Activity Level')

# Mean, standard deviation and variance of Stress Level
calculate_statistics(df, 'Stress Level')

# Mean, standard deviation and variance of Daily Steps
calculate_statistics(df, 'Daily Steps')

# Mean, standard deviation and variance of Heart Rate
calculate_statistics(df, 'Heart Rate')


def plot_horizontal_bar(df_, group_column, value_column, figsize=(12, 10)):
    average_values = df_.groupby(group_column)[value_column].mean()
    plt.figure(figsize=figsize)
    bars = plt.barh(average_values.index, average_values,
                    color=plt.cm.viridis(np.linspace(0, 1, len(average_values))), edgecolor='grey')
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center',
                 fontsize=10, color='black')

    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.gca().invert_yaxis()
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)


# Stress Level vs Sleep Duration
plt.figure(figsize=(8, 6))
plt.scatter(df['Stress Level'], df['Sleep Duration'], color="skyblue", label='Data Points')
plt.xlabel('Stress Level')
plt.ylabel('Sleep Duration')
plt.title('Stress Level vs Sleep Duration')
m, b = np.polyfit(df['Stress Level'], df['Sleep Duration'], 1)
plt.plot(df['Stress Level'], m*df['Stress Level'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()

# Age vs Sleep Duration
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Sleep Duration'], color="skyblue", label='Data Points')
plt.xlabel('Age')
plt.ylabel('Sleep Duration')
plt.title('Age vs Sleep Duration')
m, b = np.polyfit(df['Age'], df['Sleep Duration'], 1)
plt.plot(df['Age'], m*df['Age'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()

# Heart Rate vs Sleep Duration
plt.figure(figsize=(8, 6))
plt.scatter(df['Heart Rate'], df['Sleep Duration'], color="skyblue", label='Data Points')
plt.xlabel('Heart Rate')
plt.ylabel('Sleep Duration')
plt.title('Heart Rate vs Sleep Duration')
m, b = np.polyfit(df['Heart Rate'], df['Sleep Duration'], 1)
plt.plot(df['Heart Rate'], m*df['Heart Rate'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()

# Physical Activity Level vs Sleep Duration
plt.figure(figsize=(8, 6))
plt.scatter(df['Physical Activity Level'], df['Sleep Duration'], color="skyblue", label='Data Points')
plt.xlabel('Physical Activity Level')
plt.ylabel('Sleep Duration')
plt.title('Physical Activity Level vs Sleep Duration')
m, b = np.polyfit(df['Physical Activity Level'], df['Sleep Duration'], 1)
plt.plot(df['Physical Activity Level'], m*df['Physical Activity Level'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()

# Average sleep duration for each occupation
plot_horizontal_bar(df, 'Occupation', 'Sleep Duration', figsize=(12, 10))
plt.xlabel('The Average of Sleep Duration')
plt.ylabel('Occupation')
plt.title('Average sleep duration for each occupation')
plt.tight_layout()
plt.show()

# Sleep Duration vs Quality of Sleep
plt.figure(figsize=(8, 6))
plt.scatter(df['Sleep Duration'], df['Quality of Sleep'], color="skyblue", label='Data Points')
plt.title('Sleep Duration vs Quality of Sleep')
plt.xlabel('Sleep Duration')
plt.ylabel('Quality of Sleep')
plt.grid(True)
m, b = np.polyfit(df['Sleep Duration'], df['Quality of Sleep'], 1)
plt.plot(df['Sleep Duration'], m*df['Sleep Duration'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()

# Stress Level vs Quality of Sleep
plt.figure(figsize=(8, 6))
plt.scatter(df['Stress Level'], df['Quality of Sleep'], color="skyblue", label='Data Points')
plt.title('Stress Level vs Quality of Sleep')
plt.xlabel('Stress Level')
plt.ylabel('Quality of Sleep')
plt.grid(True)
m, b = np.polyfit(df['Stress Level'], df['Quality of Sleep'], 1)
plt.plot(df['Stress Level'], m*df['Stress Level'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()

# Daily Steps vs Quality of Sleep
plt.figure(figsize=(8, 6))
plt.scatter(df['Daily Steps'], df['Quality of Sleep'], color="skyblue", label='Data Points')
plt.title('Daily Steps vs Quality of Sleep')
plt.xlabel('Daily Steps')
plt.ylabel('Quality of Sleep')
plt.grid(True)
m, b = np.polyfit(df['Daily Steps'], df['Quality of Sleep'], 1)
plt.plot(df['Daily Steps'], m*df['Daily Steps'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()

# Average sleep quality for each occupation
plot_horizontal_bar(df, 'Occupation', 'Quality of Sleep', figsize=(12, 10))
plt.xlabel('The Average of Sleep Quality')
plt.ylabel('Occupation')
plt.title('Average Sleep Quality for each occupation')
plt.tight_layout()
plt.show()

# Average sleep quality for each BMI type
plot_horizontal_bar(df, 'BMI Category', 'Quality of Sleep', figsize=(12, 10))
plt.xlabel('The Average of Quality of Sleep')
plt.ylabel('BMI Category')
plt.title('Average sleep quality for each BMI type')
plt.tight_layout()
plt.show()

# Average Physical Activity Level for each BMI type
plot_horizontal_bar(df, 'BMI Category', 'Physical Activity Level', figsize=(12, 10))
plt.ylabel('BMI Category')
plt.xlabel('The Average of Physical Activity Level')
plt.title('Average Physical Activity Level for each BMI type')
plt.tight_layout()
plt.show()

# Average Daily Steps for each BMI type
plot_horizontal_bar(df, 'BMI Category', 'Daily Steps', figsize=(12, 10))
plt.ylabel('BMI Category')
plt.xlabel('The Average of Daily Steps')
plt.title('Average Daily Steps for each BMI type')
plt.tight_layout()
plt.show()

# Average Stress Level for each occupation
plot_horizontal_bar(df, 'Occupation', 'Stress Level', figsize=(12, 10))
plt.ylabel('Occupation')
plt.xlabel('The Average of Stress Level')
plt.title('Average Stress Level for each occupation')
plt.tight_layout()
plt.show()

# Stress Level vs Physical Activity Level
plt.figure(figsize=(10, 6))
plt.scatter(df['Stress Level'], df['Physical Activity Level'], color="skyblue", label='Data Points')
plt.title('Stress Level vs Physical Activity Level')
plt.xlabel('Stress Level')
plt.ylabel('Physical Activity Level')
plt.grid(True)
m, b = np.polyfit(df['Stress Level'], df['Physical Activity Level'], 1)
plt.plot(df['Stress Level'], m*df['Stress Level'] + b, color='red', label='Regression Line')
plt.legend()
plt.show()

# Heart Rate vs Physical Activity Level
grouped = df.groupby('Physical Activity Level')['Heart Rate'].mean()
plt.figure(figsize=(10, 6))
plt.plot(grouped.index, grouped.values, marker='o', linestyle='-', color='skyblue',
         linewidth=2, markersize=8, label='Average Heart Rate')
for x, y in zip(grouped.index, grouped.values):
    plt.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=10, color='black')

plt.title('Average Heart Rate vs Physical Activity Level', fontsize=16)
plt.xlabel('Physical Activity Level', fontsize=12)
plt.ylabel('Average Heart Rate', fontsize=12)
plt.xticks(grouped.index)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()

# correlation coefficients
numeric_columns = df.select_dtypes(include=['number']).columns
corr = df[numeric_columns].corr()
plt.figure(figsize=(12, 11))
plt.imshow(corr, cmap='coolwarm')
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(j, i, round(corr.iloc[i, j], 2), ha='center', va='center')
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title('Correlation Matrix')
plt.colorbar()
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()

# The hypothesis test, Pearson correlation coefficient, examines the correlation between two features
print('\n================================')


def pearson(df_, value1, value2):
    print(f'The Pearson Correlation Index was used to examine the correlation between {value1} and {value2}')
    stat, p = pearsonr(df_[value1], df_[value2])
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print(f'{value1} and {value2} are not related')
    else:
        print(f'{value1} and {value2} are related')


# chi-square test
def chisquare(df_, value1, value2):
    contingency_table = pd.crosstab(df_[value1], df_[value2])
    # Perform chi-square test
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    # Print the results
    print(f'Here is a Chi-square test that examines the correlation between {value1} and {value2} data')
    print("Chi-square test results:")
    print("Chi-square statistic: ", chi2)
    print("P-value: ", p)
    print("Degrees of freedom: ", dof)
    print("Expected values and actual value: ", expected)


# You can choose any two features for a chi-square check or a hypothetical hypothesis
pearson(df, 'Sleep Duration', 'Stress Level')
print('\n================================')
chisquare(df, 'Sleep Duration', 'Stress Level')
