from scipy.stats import kendalltau

exercise_frequency = ['low', 'moderate', 'high', 'moderate', 'high']
health_status = [3, 4, 2, 5, 3]

correlation_coefficient, p_value = kendalltau(exercise_frequency, health_status)

print("Kendall's Tau 系数:", correlation_coefficient)
