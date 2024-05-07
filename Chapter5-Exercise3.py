import numpy as np
import pandas as pd

population_data = pd.Series([1439323776, 1380004385, 331002651, 273523615, 220892340],
                            index=['China', 'India', 'United States', 'Indonesia', 'Pakistan'])

print("Population data", population_data["India"])
print(population_data['China':'Indonesia'])
threshold = 2500000
print(population_data[population_data > threshold])
