import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Step 1: Load the AirPassengers dataset using the pandas library.
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url, index_col='Month', parse_dates=True)
print(df.head())

# Step 2: Convert the index to a datetime format and explore the first few rows of the dataset.
df.index = pd.to_datetime(df.index)
print(df.head())

# Step 3: Create a line plot of the number of passengers over time.
plt.plot(df.index, df['Passengers'])
plt.xlabel('Year')
plt.ylabel('Number of passengers')
plt.title('AirPassengers Dataset')
plt.show()

# Step 4: Perform a decomposition of the time series into trend, seasonal, and residual components,
# and visualize each component separately.
decomposition = seasonal_decompose(df['Passengers'], period=12)

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(211)
ax1.plot(df.index, df['Passengers'], label='Original')
ax1.plot(decomposition.trend, label='Trend')
ax1.legend()

ax2 = fig.add_subplot(212)
ax2.plot(decomposition.seasonal, label='Seasonality')
ax2.legend()

plt.tight_layout()
plt.show()

# Step 5: Compute and visualize the autocorrelation function (ACF) and partial autocorrelation function (PACF)
# of the time series.
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121)
plot_acf(df['Passengers'], ax=ax1)
ax1.set_title('ACF')

ax2 = fig.add_subplot(122)
plot_pacf(df['Passengers'], ax=ax2)
ax2.set_title('PACF')

plt.tight_layout()
plt.show()

