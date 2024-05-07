import seaborn as sns

tips = sns.load_dataset("tips")

grouped_data = tips.groupby('day').agg({'total_bill': 'count', 'tip': 'max'}).reset_index()

grouped_data.columns = ['Day', 'Total Bills', 'Max Tip Amount']
print(grouped_data)






