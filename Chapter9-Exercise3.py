import numpy as np
import pandas as pd

np.random.seed(42)

# Generate salary data for three departments
salary_dept1 = np.random.normal(loc=50000, scale=10000, size=50)
salary_dept2 = np.random.normal(loc=55000, scale=12000, size=50)
salary_dept3 = np.random.normal(loc=60000, scale=15000, size=50)

# Create DataFrame
data = pd.DataFrame({'Department': ['Dept 1'] * 50 + ['Dept 2'] * 50 + ['Dept 3'] * 50,
                     'Salary': np.concatenate([salary_dept1, salary_dept2, salary_dept3])})

print(data.head())

from scipy.stats import f_oneway

static, p_value = f_oneway(data[data['Department'] == 'Dept 1']['Salary'], data[data['Department'] == 'Dept 2']['Salary'], data[data['Department'] == 'Dept 3']['Salary'])
print("Kruskal-Wallis H Test:")
print('H-statistic:', static)
print('P_value:', p_value)

if p_value < 0.05:
    print('The departments are different.')
else:
    print('The departments are the same.')
