import csv
import random

with open('data.csv', 'w', newline='') as file_csv:
    fieldnames = ["ID", "Name", "Score"]
    writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, 101):
        name = f"Name {i}"
        score = random.randint(0, 100)
        writer.writerow({"ID": i, "Name": name, "Score": score})

data = []
with open('data.csv', 'r') as file_csv:
    reader = csv.DictReader(file_csv)
    next(reader)
    for row in reader:
        data.append(row)

for row in data:
    print(row)

with open('data.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)
    next(reader)
    for row in reader:
        data.append(row)

for row in data:
    print(row)
