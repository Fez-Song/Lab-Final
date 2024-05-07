import numpy as np
import pandas as pd

np.random.seed(42)

# Generate plant height data for four fertilizer treatments
fertilizer_A = np.random.normal(loc=50, scale=5, size=50)
fertilizer_B = np.random.normal(loc=55, scale=7, size=50)
fertilizer_C = np.random.normal(loc=60, scale=8, size=50)
fertilizer_D = np.random.normal(loc=65, scale=10, size=50)

# Create DataFrame
data = pd.DataFrame({'Fertilizer': ['A'] * 50 + ['B'] * 50 + ['C'] * 50 + ['D'] * 50,
                     'Plant Height': np.concatenate([fertilizer_A, fertilizer_B, fertilizer_C, fertilizer_D])})

print(data.head())

from scipy.stats import kruskal

static, p_value = kruskal(data[data['Fertilizer'] == 'A']['Plant Height'],
                          data[data['Fertilizer'] == 'B']['Plant Height'],
                          data[data['Fertilizer'] == 'C']['Plant Height'],
                          data[data['Fertilizer'] == 'D']['Plant Height'])
print('Kruskal-Wallis H Test:')
print('H-static:', static)
print("p_value:", p_value)
if p_value < 0.05:
    print('The groups are different.')
else:
    print('The groups are the same.')
