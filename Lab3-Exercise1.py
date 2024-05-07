import numpy as np

age = np.array([19, 19, 18, 19, 18, 19])

age_mean = np.mean(age)
age_median = np.median(age)
age_std = np.std(age)

print("Mean age:", age_mean)
print("Median age:", age_median)
print("Standard deviation of ages:", age_std)
