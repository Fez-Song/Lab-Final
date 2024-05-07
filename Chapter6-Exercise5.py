import pandas as pd

Employees_infos = (
    {'Employee_ID': 101, 'Name': 'Alice', 'Age': 30, 'Department_ID': 1, 'Manager_ID': 201},
    {'Employee_ID': 102, 'Name': 'Bob', 'Age': 35, 'Department_ID': 2, 'Manager_ID': 202},
    {'Employee_ID': 103, 'Name': 'Charlie', 'Age': 28, 'Department_ID': 1, 'Manager_ID': 201},
    {'Employee_ID': 104, 'Name': 'David', 'Age': 32, 'Department_ID': 3, 'Manager_ID': 203},
)

Employees_dataset = pd.DataFrame(Employees_infos)
print(Employees_dataset)

Departments_infos = (
    {'ID': 1, 'Department_Name': 'Sales', 'Manager_ID': 201},
    {'ID': 2, 'Department_Name': 'Marketing', 'Manager_ID': 202},
    {'ID': 3, 'Department_Name': 'Finance', 'Manager_ID': 203},
)
Departments_dataset = pd.DataFrame(Departments_infos)
print(Departments_dataset)
merged = pd.merge(Employees_dataset, Departments_dataset, left_on='Department_ID', right_on='ID')
print(merged)
merged.drop(columns='ID', inplace=True)
print(merged)
merged_on = pd.merge(Employees_dataset, Departments_dataset, on='Manager_ID')
print(merged_on)