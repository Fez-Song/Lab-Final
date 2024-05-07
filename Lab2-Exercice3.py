import csv

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

with open("students_summary.csv", 'w', encoding="utf-8", newline="") as csvfile:
    fieldnames = ["Name", "Grade"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    students = [
        {"Name": "Fez", "Grade": 7},
        {"Name": "john", "Grade": 8},
        {"Name": "bob", "Grade": 8}
    ]
    for student in students:
        writer.writerow({'Name': student['Name'], 'Grade': student['Grade']})

    print("写入数据成功")
    csvfile.close()
