import numpy as np
import pandas as pd

days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = np.random.randint(10, 20, size=7)
temperature = pd.Series(temperatures, index=days_of_the_week)
print(temperature)
