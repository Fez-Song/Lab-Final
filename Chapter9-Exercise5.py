from scipy.stats import pearsonr

study_hours = [10, 8, 5, 12, 15]
exam_scores = [85, 70, 60, 90, 95]

# Calculate Pearson correlation coefficient
correlation_coefficient, p_value = pearsonr(study_hours, exam_scores)

print("Pearson correlation coefficient:", correlation_coefficient)
