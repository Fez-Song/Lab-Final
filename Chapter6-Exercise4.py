import pandas as pd

Employees_infos = (
    {'Employee_ID': 101, 'Name': 'Alice', 'Age': 30, 'Department_ID': 1},
    {'Employee_ID': 102, 'Name': 'Bob', 'Age': 22, 'Department_ID': 2},
    {'Employee_ID': 103, 'Name': 'Charlie', 'Age': 21, 'Department_ID': 1},
    {'Employee_ID': 104, 'Name': 'David', 'Age': 19, 'Department_ID': 2}
)

Employees_dataset = pd.DataFrame(Employees_infos)
print(Employees_dataset)

Departments_infos = (
    {'Department_ID': 1, 'Department_Name': 'Sales'},
    {'Department_ID': 2, 'Department_Name': 'Marketing'},
    {'Department_ID': 3, 'Department_Name': 'Finance'},
)
Departments_dataset = pd.DataFrame(Departments_infos)
print(Departments_dataset)

merged = pd.merge(Employees_dataset, Departments_dataset, on='Department_ID', how='inner')
print(merged)
