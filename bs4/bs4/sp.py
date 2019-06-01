import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

r = requests.get(
    'https://www.amazon.co.jp/s?k=%E3%82%AC%E3%83%AB%E3%83%91%E3%83%B3&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss_1')
print(r)
i = 0

data = BeautifulSoup(r.text, 'html.parser')
title_list = list()
price_list = list()
page = 1
amazon = "https://www.amazon.co.jp"
for i in range(1):
    sleep(4)
    i += 1
    title = data.find_all("h2", class_="s-access-title")
    for t in title:
        string = t.getText()
        title_list.append(string)

    price = data.find_all("span", class_="s-price")
    # s-priceを持たない価格表示があるために一部商品の価格が取得できない。この問題を解決したい。
    # 1ページ中に存在する商品は24件である。
    for e in price:
        string = e.getText()
        price_list.append(str(string))

    NextUrl = data.find('span', {"class": "pagnRA"})
    Url = NextUrl.a.get("href")

    url = amazon + Url
    print(url)
    r = requests.get(url)
    data = BeautifulSoup(r.text, 'html.parser')

    page += 1


title_length = len(title_list)
price_length = len(price_list)
print(len(title_list))
print(len(price_list))

while title_length != price_length:
    price_list.append("NaN")
    title_length = len(title_list)
    price_length = len(price_list)


df = pd.DataFrame({
    '商品名': title_list,
    '価格': price_list
})

df.to_csv('output.csv')
