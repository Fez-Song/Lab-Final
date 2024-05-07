import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, chi2_contingency


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到。")
        return None

def clean_data(df):
    # 使用“Nothing”填充“Sleep Disorder”列中的缺失值
    df['Sleep Disorder'].fillna("Nothing", inplace=True)
    # 将“BMI Category”中的“Normal Weight”替换为“Normal”
    df['BMI Category'].replace("Normal Weight", "Normal", inplace=True)
    return df

def plot_scatter_with_regression(x, y, xlabel, ylabel, title):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color="skyblue", label='Data Points')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, color='red', label='Regression Line')
    plt.legend()
    plt.show()

def plot_horizontal_bar(df, group_column, value_column, title, figsize=(12, 10)):
    average_values = df.groupby(group_column)[value_column].mean()
    plt.figure(figsize=figsize)
    bars = plt.barh(average_values.index, average_values,
                    color=plt.cm.viridis(np.linspace(0, 1, len(average_values))), edgecolor='grey')
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', ha='left', va='center',
                 fontsize=10, color='black')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.gca().invert_yaxis()
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.xlabel(title)
    plt.ylabel(group_column)
    plt.title(title)
    plt.tight_layout()
    plt.show()

# 加载和清理数据
file_path = 'Sleep_health_and_lifestyle_dataset.csv'
df = load_data(file_path)
if df is not None:
    df = clean_data(df)

    # 绘制带有回归线的散点图
    plot_scatter_with_regression(df['Stress Level'], df['Sleep Duration'], 'Stress Level', 'Sleep Duration', 'Stress Level vs Sleep Duration')
    plot_scatter_with_regression(df['Age'], df['Sleep Duration'], 'Age', 'Sleep Duration', 'Age vs Sleep Duration')
    plot_scatter_with_regression(df['Heart Rate'], df['Sleep Duration'], 'Heart Rate', 'Sleep Duration', 'Heart Rate vs Sleep Duration')
    plot_scatter_with_regression(df['Physical Activity Level'], df['Sleep Duration'], 'Physical Activity Level', 'Sleep Duration', 'Physical Activity Level vs Sleep Duration')

    # 绘制水平条形图
    plot_horizontal_bar(df, 'Occupation', 'Sleep Duration', 'Average sleep duration for each occupation')
    plot_horizontal_bar(df, 'Occupation', 'Quality of Sleep', 'Average Sleep Quality for each occupation')
    plot_horizontal_bar(df, 'BMI Category', 'Quality of Sleep', 'Average sleep quality for each BMI type')
    plot_horizontal_bar(df, 'BMI Category', 'Physical Activity Level', 'Average Physical Activity Level for each BMI type')
    plot_horizontal_bar(df, 'BMI Category', 'Daily Steps', 'Average Daily Steps for each BMI type')
    plot_horizontal_bar(df, 'Occupation', 'Stress Level', 'Average Stress Level for each occupation')

    # 计算和可视化相关矩阵
    corr = df.corr()
    plt.figure(figsize=(12, 11))
    plt.imshow(corr, cmap='coolwarm')
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            plt.text(j, i, round(corr.iloc[i, j], 2), ha='center', va='center')
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.title('Correlation Matrix')
    plt.colorbar()
    plt.tight_layout()
    plt.show()

    # 执行假设检验
    stat, p = pearsonr(df['Sleep Duration'], df['Stress Level'])
    print('\n睡眠时长与压力水平之间的皮尔逊相关系数:')
    print(f'统计值: {stat:.3f}, p-value: {p:.3f}')
    if p > 0.05:
        print('睡眠时长与压力水平之间没有显著关系。')
    else:
        print('睡眠时长与压力水平之间存在显著关系。')

    chi2, p, dof, expected = chi2_contingency(pd.crosstab(df['Age'], df['Sleep Duration']))
    print('\n年龄与睡眠时长之间的卡方检验:')
    print("卡方统计值: ", chi2)
    print("P-value: ", p)
    print("自由度: ", dof)
    print("期望值和实际值: ", expected)
