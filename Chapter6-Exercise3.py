import pandas as pd

Students_infos = (
    {'Student_ID': 101, 'Name': 'Alice', 'Age': 20, 'Gender': 'Female'},
    {'Student_ID': 102, 'Name': 'Bob', 'Age': 22, 'Gender': 'Male'},
    {'Student_ID': 103, 'Name': 'Charlie', 'Age': 21, 'Gender': 'Male'},
    {'Student_ID': 104, 'Name': 'David', 'Age': 19, 'Gender': 'Male'}
)
Students_dataset = pd.DataFrame(Students_infos)
print(Students_dataset)

Score_infos = (
    {'Student_ID': 101, 'Math_Score': 85, 'Science_Score': 90},
    {'Student_ID': 102, 'Math_Score': 70, 'Science_Score': 75},
    {'Student_ID': 103, 'Math_Score': 90, 'Science_Score': 88},
    {'Student_ID': 104, 'Math_Score': 65, 'Science_Score': 80}
)
Score_dataset = pd.DataFrame(Score_infos)
print(Score_dataset)

Score_infos_drop = Score_dataset.drop(['Student_ID'], axis=1)
print(Score_infos_drop)

concatenated_rows = pd.concat([Students_dataset, Score_infos_drop], axis=1, join='inner')
concatenated_columns = pd.concat([Students_dataset, Score_dataset], axis=0, join='outer')

print("Concatenated Dataset along Rows:")
print(concatenated_rows)
print("Concatenated Dataset along Columns:")
print(concatenated_columns)
