def find_max(numbers):
    if not numbers:
        return None
    else:
        return max(numbers)


numbers = [3, 43, 65, 8, 0, -4, 31]
print("The largest number in the list is :", find_max(numbers))

class_scores = [
    [89, 80, 90],
    [85, 88, 92],
    [78, 92, 87]
]
i = 1
for scores in class_scores:
    highest_score = find_max(scores)
    print(f"Highest score in class {i}: {highest_score}")
    i = i + 1