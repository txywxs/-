# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

urls = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 Safari/537.36 '
}
page_text = requests.get(urls, headers=headers).text
soup = BeautifulSoup(page_text, 'lxml')
soup_a = soup.find_all("li")
for i in soup_a:
    print(i.a['href'])