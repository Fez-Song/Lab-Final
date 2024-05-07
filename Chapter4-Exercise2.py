import numpy as np

arry1 = np.arange(1, 26).reshape(5, 5)

print(arry1)
print(arry1[2:, 1:])
print(arry1[3, 4])
print(arry1[0:3, 1])
print(arry1[4, :])
print(arry1[3:, :])
print(arry1.size)
