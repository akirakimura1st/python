import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import re
import uuid

r = requests.get("https://bandainamco-am.co.jp/chara_shop/girls-und-panzer/")
data = BeautifulSoup(r.text, 'html.parser')
item_list = list()
price_list = list()

item = data.find_all("h4", class_="name")
for t in item:
    string = t.getText()
    string = string.rstrip('\n')
    item_list.append(string)

price = data.find_all("p", class_="price")
for i in price:
    string = i.getText()
    string = string.strip('\n')
    string = string.strip('各')
    string = string.strip('円（税込）')
    string = string.strip(',')
    price_list.append(string)

item_length = len(item_list)
price_length = len(price_list)
print(len(item_list))
print(len(price_list))

while item_length != price_length:
    price_list.append("NaN")
    item_length = len(item_list)
    price_length = len(price_list)


df = pd.DataFrame({
    '商品名': item_list,
    '価格': price_list
})
df.to_csv('Garupan.csv', index=False)