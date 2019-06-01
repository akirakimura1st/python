import requests
from bs4 import BeautifulSoup

r = requests.get('https://bandainamco-am.co.jp/chara_shop/girls-und-panzer/')
data = BeautifulSoup(r.text, 'html.parser')
with open('garupan_data.html', mode='w', encoding='utf-8') as fw:
    fw.write(data.prettify())
