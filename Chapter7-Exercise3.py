import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.head())


def custom_agg(df):
    ratio = df['total_bill'].sum() / df['tip'].sum()
    return ratio


custom_agg_result = tips.groupby('day').apply(custom_agg).reset_index(name="Bill to tip ratio")
print(custom_agg_result)
