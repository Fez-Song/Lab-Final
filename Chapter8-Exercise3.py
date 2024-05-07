import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the diamonds dataset
diamonds = sns.load_dataset("diamonds")

# Create a box plot of diamond prices based on their cut
plt.figure(figsize=(10, 6))
sns.boxplot(x="cut", y="price", data=diamonds)
plt.xlabel("Cut")
plt.ylabel("Price")
plt.title("Diamond Prices by Cut")
plt.savefig("diamond_prices_by_cut.png")
plt.show()

# Create a box plot of diamond prices based on their color
plt.figure(figsize=(10, 6))
sns.boxplot(x="color", y="price", data=diamonds)
plt.xlabel("Color")
plt.ylabel("Price")
plt.title("Diamond Prices by Color")
plt.savefig("diamond_prices_by_color.png")
plt.show()
# Create a box plot of diamond prices based on their clarity
plt.figure(figsize=(10, 6))
sns.boxplot(x="clarity", y="price", data=diamonds)
plt.xlabel("Clarity")
plt.ylabel("Price")
plt.title("Diamond Prices by Clarity")
plt.savefig("diamond_prices_by_clarity.png")
plt.show()

# Create a box plot of diamond prices based on their carat weight
plt.figure(figsize=(10, 6))
sns.boxplot(x="carat", y="price", data=diamonds)
plt.xlabel("Carat Weight")
plt.ylabel("Price")
plt.title("Diamond Prices by Carat Weight")
plt.savefig("diamond_prices_by_carat.png")
plt.show()

# Create bins for carat weight
carat_bins = np.linspace(diamonds["carat"].min(), diamonds["carat"].max(), 10)
carat_labels = ["{:.1f}-{:.1f}".format(carat_bins[i], carat_bins[i+1]) for i in range(len(carat_bins)-1)]

# Create a box plot of diamond prices based on their binned carat weight
plt.figure(figsize=(10, 6))
sns.boxplot(x=pd.cut(diamonds["carat"], bins=carat_bins, labels=carat_labels), y="price", data=diamonds)
plt.xlabel("Carat Weight")
plt.ylabel("Price")
plt.title("Diamond Prices by Binned Carat Weight")
plt.savefig("diamond_prices_by_binned_carat.png")
plt.show()