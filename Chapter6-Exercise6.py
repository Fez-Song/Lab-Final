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
    {'ID': 1, 'Department_Name': 'Sales', 'Manager_ID': 301},
    {'ID': 2, 'Department_Name': 'Marketing', 'Manager_ID': 302},
    {'ID': 3, 'Department_Name': 'Finance', 'Manager_ID': 303},
)
Departments_dataset = pd.DataFrame(Departments_infos)
print(Departments_dataset)

merge_data = pd.merge(Employees_dataset, Departments_dataset, left_on='Department ID', right_on='Department ID',
                      how='inner', suffixes=('_employee', '_Department'))
print(merge_data)
