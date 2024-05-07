import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.head())

aveg_total_bill_by = tips.groupby('sex')['total_bill'].mean()
print(aveg_total_bill_by)
