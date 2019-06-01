import urllib.request, urllib.error
from bs4 import BeautifulSoup
from time import sleep

if __name__ == '__main__':
    N = 30 #ページネートの数
    BT = 2

    for i in range(1, N+1): #元for i in range(N)

        sleep(BT)#アクセスが多くなりすぎないように時間を開ける

        #pの値をfor文で変える
        url = 'https://search.rakuten.co.jp/search/mall/inz/?p=' + str(i) + '&sid=261213'
        print(url)


        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
        div = soup.findAll('div' , class_='image')
        for f in div:
            for link in f.findAll('a'):
                print(link.attrs['href'])
