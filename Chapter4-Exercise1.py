import numpy as np

ten_zeros = np.zeros(10)
print(ten_zeros)

ten_ones = np.ones(10)
print(ten_ones)

ten_fives = np.linspace(5, 5, 10)  # np.ones(10) * 5
print(ten_fives)

the_integers_from_10_to_50 = np.arange(10, 51)
print(the_integers_from_10_to_50)

the_even_integers_from_10_to_50 = np.arange(10, 51, 2)
print(the_even_integers_from_10_to_50)

matrix_with_values_ranging_from_0_to_8 = np.arange(9).reshape(3, 3)
print(matrix_with_values_ranging_from_0_to_8)

matrix = np.eye(3)
print(matrix)

rad = np.random.rand(1)
print(rad)

arr = np.random.randn(25)
print(arr)

float_arr = np.linspace(0.01, 1, 100).reshape(10, 10)
print(float_arr)

line_arr = np.linspace(0, 1, 20)
print(line_arr)






