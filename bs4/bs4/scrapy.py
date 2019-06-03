import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import re
import uuid

r = requests.get("http://google.com")
data = BeautifulSoup(r.text, 'html.parser')
item_list = list()
price_list = list()

# 取得したデータから指定のデータを抽出し、リストに格納する。
item = data.find_all("div", class_="card")
for i in item:
    item_name = i.getText()
    item_name = item_name.strip('\n')
    item_list.append(item_name)

# 取得したデータから指定のデータを抽出し、リストに格納する。
price = data.find_all("h4", class_="card")
for p in price:
    price_name = i.getText()
    price_name = price_name.strip('\n')
    price_list.append(price_name)

item_length = len(item_list)
price_length = len(price_list)
print(len(item_list))
print(len(price_list))
