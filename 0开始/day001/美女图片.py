import bs4
import requests
import re, os

url = 'https://www.souutu.com/mnmm/mote/16925.html'
rest = r"\d/(\d{1,2})"
while True:
    url = url
    res = requests.get(url=url)
    bs = bs4.BeautifulSoup(res.text, 'lxml')
    bs_img = bs.find_all('img', id="showpicsouutuIs2020")  # 查询图片
    bs_page = bs.find('div', class_="showcenter")
    bs_page_max = bs_page.text
    bs_page_max = int(re.findall(rest, bs_page_max)[0])  # 获取到最大页数
    bs_a = bs.find_all('a', class_="Nnext imgpage-right")  # 获取下一张图片的url
    bs_img_src = bs_img[0]['src']
    bs_img_alt = bs_img[0]['alt'][:-2]
    bs_a_right_href = bs_a[0]['href']

    print("图片路径:", bs_img_src)
    print("图片标题:", bs_img_alt)
    print("下一张图:", bs_a_right_href)
    print("最大页数:", bs_page_max)
    print("当前页面:", bs_a_right_href)
    url = bs_a_right_href
