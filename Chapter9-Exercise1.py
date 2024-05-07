import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

np.random.seed(42)

# Generate exam scores for group A and group B
group_a_scores = np.random.randint(60, 100, 50)
group_b_scores = np.random.randint(50, 90, 50)

# Create DataFrame
data = pd.DataFrame({'Method': ['A'] * 50 + ['B'] * 50,
                     'Scores': np.concatenate([group_a_scores, group_b_scores])})

print(data)

#statistic, p_value = mannwhitneyu(data[data['Method'] == 'A']['Scores'], data[data['Method'] == 'B']['Scores'])
statistic, p_value = mannwhitneyu(group_a_scores, group_b_scores)
print(statistic, p_value)

if p_value < 0.05:
    print('The groups are different.')
else:
    print('The groups are the same.')
