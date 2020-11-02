import requests
from bs4 import BeautifulSoup

urls = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 '
                  'Safari/537.36 '
}

response = requests.get(url=urls, headers=headers)
html_text = response.text
Butef = BeautifulSoup(html_text,'lxml')
btf = Butef.find('div',class_='book-mulu')
btfs = btf.find_all('a')
for i in range(1,len(btfs)+1):
    print('正在下载第%s章'%i)
    "https://www.shicimingju.com/book/sanguoyanyi/1.html"
    urllb = 'https://www.shicimingju.com/book/sanguoyanyi/%s.html'%i
    with open('')