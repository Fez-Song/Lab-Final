import numpy as np

temp = np.arange(1, 26).reshape(5, 5)

result1 = np.sum(temp)
print(result1)

result2 = np.std(temp)
print(result2)

result3 = sum(temp)
print(result3)

