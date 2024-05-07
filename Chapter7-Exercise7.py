import pandas as pd
import numpy as np

sales_data = pd.DataFrame({
    'Product': ["computer", "shirt", "phone"],
    'Quantity': [1, 2, 3],
    'Price': [1001, 200, 303]
})
print(sales_data)
sales_data['Total'] = pd.eval(sales_data['Quantity'] * sales_data['Price'])
print(sales_data)

data_filter = sales_data[pd.eval(sales_data.Price * sales_data.Quantity > 1000)]
print(data_filter)
