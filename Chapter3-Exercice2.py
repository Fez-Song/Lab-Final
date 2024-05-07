import requests

from bs4 import BeautifulSoup
with open("C:\\Users\\sz200\\Downloads\\index.html", 'rb') as file:
    soup = BeautifulSoup(file, 'html.parser')


title = soup.title.text
print(title)

h1 = soup.h1.text
print(h1)

product_List = soup.find_all('ul')[0].find_all('li')
product_names = []
product_prices_euros = []
product_descriptions = []

for product in product_List:
    name = product.find('span', class_='product-name').text
    price = product.find('span', class_='product-price').text
    description = product.find('p').text
    product_names.append(name)
    product_prices_euros.append(price)
    product_descriptions.append(description)

product_prices_dollar = []
for price in product_prices_euros:
    price_euro = int(price.replace("price:", "").replace("€", ""))
    price_dollar = int(price_euro * 1.2)
    product_prices_dollar.append(f"{price_dollar}")

print("Products:")
for i in range(len(product_names)):
    print(f"Name: {product_names[i]},"
          f"Price: {product_prices_dollar[i]},"
          f"Description: {product_descriptions[i]}")