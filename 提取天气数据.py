import requests
from bs4 import BeautifulSoup

# 设置请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# 发送请求并获取响应
url = "https://weather.com/weather/today/l/5d455f55e4a1da83df8f0b30977bc63e1db462c400571585af21b295f7053fbe"
response = requests.get(url, headers=headers)

# 创建Beautiful Soup对象
soup = BeautifulSoup(response.content, "html.parser")

# 获取第一个版块div元素
first_div = soup.find("div", {"id": "WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"})

# 获取第一个版块div元素中的标题
first_header = first_div.find("h2", {"class": "Card--cardHeading--2H1-_"}).text

# 获取第一个版块div元素中的ul下所有li元素
li_list = first_div.find("div", {"class": "TodayWeatherCard--TableWrapper--globn"}).find("ul").find_all("li")

# 打印第一个版块div元素中的标题
print(first_header)

# 遍历li_list中的li元素
for li in li_list:
    # 获取时间段
    time = li.find("a").find("h3").find("span").text
    # 获取温度
    temperature = li.find("a").find("div").find("span").text
    # 打印时间段和温度
    print(time, temperature)

# 添加一个换行，分割内容显示
print()

# 获取第二个版块div元素
second_div = soup.find("div", {"id": "todayDetails"})

# 获取第二个版块div元素中的标题
second_header = second_div.find("h2").text

# 打印第二个版块div元素中的标题
print(second_header)

# 获取第二个版块div元素中的温度
temperature = second_div.find("span", {"class": "TodayDetailsCard--feelsLikeTempValue--2icPt"}).text

# 获取第二个版块div元素中的所有div元素
div_list = second_div.find_all("div", {"class": "ListItem--listItem--25ojW WeatherDetailsListItem--WeatherDetailsListItem--1CnRC"})

# 遍历div_list中的div元素
for div in div_list:
    # 获取描述
    desc = div.find("div").text
    # 获取值 replace("\xa0", "")是因为控制台默认是gbk格式编码，一些特殊的字符必须要utf-8解码才可以看到。
    value = div.find("div", {"class": "WeatherDetailsListItem--wxData--kK35q"}).text.replace("\xa0", "")
    # 打印描述和值
    print(desc, "\t", value)