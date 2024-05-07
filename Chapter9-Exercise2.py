import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

np.random.seed(42)

# Generate blood pressure measurements before and after treatment
before_treatment = np.random.randint(100, 150, 50)
after_treatment = np.random.randint(90, 140, 50)

# Create DataFrame
data = pd.DataFrame({'Before Treatment': before_treatment,
                     'After Treatment': after_treatment})

print(data.head())

statistic, p_value = wilcoxon(before_treatment, after_treatment)

print("\nWilcoxon Signed-Rank Test:")
print("Test Statistic:", statistic)
print("p-value:", p_value)

if p_value < 0.05:
    print("Reject null hypothesis: There is a significant difference in blood pressure levels before and after treatment.")
else:
    print("Fail to reject null hypothesis: There is no significant difference in blood pressure levels before and after treatment.")
