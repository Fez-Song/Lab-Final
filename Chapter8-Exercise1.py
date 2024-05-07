"""by Julien Maitre"""

"""Matplotlib version"""
# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the Iris dataset using the seaborn library
# Load the iris dataset
iris = sns.load_dataset('iris')

# Step 2: Display the first few rows of the dataset to familiarize with its structure
# Display the first few rows of the dataset
print(iris.head())

# Step 3: Create a scatter plot of sepal length vs. sepal width, with different colors for each species
# Create a scatter plot of sepal length vs. sepal width, with different colors for each species
plt.figure(figsize=(10, 6))
colors = {'setosa': 'r', 'versicolor': 'g', 'virginica': 'b'}
for species in iris['species'].unique():
    plt.scatter(iris[iris['species'] == species]['sepal_length'],
                iris[iris['species'] == species]['sepal_width'],
                c=colors[species],
                label=species)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()

# Step 4: Generate a histogram of petal lengths for each species
# Generate a histogram of petal lengths for each species
plt.figure(figsize=(10, 6))
for species in iris['species'].unique():
    plt.hist(iris[iris['species'] == species]['petal_length'],
             label=species,
             alpha=0.5)
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# Step 5: Compute and visualize the correlation matrix of the dataset
# Select only the numeric columns
numeric_columns = iris.select_dtypes(include=['number']).columns

# Compute the correlation matrix
corr = iris[numeric_columns].corr()

# Visualize the correlation matrix
plt.figure(figsize=(10, 6))
plt.imshow(corr, cmap='coolwarm')
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(j, i, round(corr.iloc[i, j], 2), ha='center', va='center')
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.colorbar()
plt.show()


"""Plotly version"""
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# Step 1: Load the Iris dataset using the seaborn library
# Load the iris dataset
iris = sns.load_dataset('iris')

# Step 2: Display the first few rows of the dataset to familiarize with its structure
# Display the first few rows of the dataset
print(iris.head())

# Step 3: Create a scatter plot of sepal length vs. sepal width, with different colors for each species
fig = px.scatter(iris, x='sepal_length', y='sepal_width', color='species')
fig.show()

# Step 4: Generate a histogram of petal lengths for each species
fig = px.histogram(iris, x='petal_length', color='species', barmode='group')
fig.show()

# Step 5: Compute and visualize the correlation matrix of the dataset
# Select only the numeric columns
numeric_columns = iris.select_dtypes(include=['number']).columns

# Compute the correlation matrix
corr = iris[numeric_columns].corr()

# Visualize the correlation matrix
fig = go.Figure(data=go.Heatmap(z=corr.values, x=corr.columns, y=corr.columns))
fig.show()