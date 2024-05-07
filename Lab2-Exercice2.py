import requests
from bs4 import BeautifulSoup

url = "https://weather.com/zh-CN/weather/today/l/CHXX0008:1:CH?Goto=Redirected"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

temperature_index = soup.find("span", class_="TodayDetailsCard--feelsLikeTempValue--2icPt")

weather_condition = soup.find("div", {"class": "CurrentConditions--phraseValue--mZC_p"})

wind_name = soup.find_all("div", {"class": "WeatherDetailsListItem--label--2ZacS"})[1]
wind = soup.find("span", {"class": "Wind--windWrapper--3Ly7c undefined"})
wind_speed = wind.find_all("span")[1]
Wind_speed_unit = wind.find_all("span")[2]

print(f"Current temperature: {temperature_index.text}")
print(f"Weather condition: {weather_condition.text}")
print(f"Wind speed: {wind_name.text} {wind_speed.text}{Wind_speed_unit.text}")