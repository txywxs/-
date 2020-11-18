import bs4
import requests
import re,os
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
url = 'https://www.souutu.com/mnmm/mote/16925.html'
url = url
res = requests.get(url=url,headers=headers)
bs = bs4.BeautifulSoup(res.text, 'lxml')
bs_img = bs.find_all('img', id="showpicsouutuIs2020")  # 查询图片
bs_page = bs.find('span', class_="mlw")
print(str(bs_page)[-9:-8])
