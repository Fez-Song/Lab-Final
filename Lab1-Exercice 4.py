integers = [12, 2, 37, 4, 5, 6, 7, 80, 9]
print("Numbers greater than 10:")
for num in integers:
    if num > 10:
        print(num)
    else:
        continue

print("Number of elements divisible by 3:")
for num in integers:
    if num % 3 == 0:
        print(num)