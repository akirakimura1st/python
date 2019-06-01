import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

r = requests.get("https://paiza.jp/challenges/ranks/s/info")
data = BeautifulSoup(r.text, 'html.parser')
title_list = list()
result_list = list()

title = data.find_all("a", class_="problem-box__header__title")
for t in title:
    string = t.getText()
    string = string.rstrip('\n')
    title_list.append(string)

df = pd.DataFrame({
    '課題名': title_list
})
df.to_csv('paiza_S.csv', index=False)
