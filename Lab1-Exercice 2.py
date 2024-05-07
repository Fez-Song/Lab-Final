even_numbers = []
for i in range(0, 10):
    even_numbers.append(2 * i)

print("a list containing the first 10 even numbers", even_numbers)

print("iterate through the list:")
for num in even_numbers:
    print(num)

sum = 0
for num in even_numbers:
    sum = sum + num

print("Sum of even numbers:", sum)