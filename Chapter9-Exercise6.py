from scipy.stats import spearmanr

ages = [25, 30, 35, 40, 45]
happiness_rank = [8, 7, 6, 9, 5]

correlation_coefficient, p_value = spearmanr(ages, happiness_rank)

print("Spearman correlation coefficient:", correlation_coefficient)
