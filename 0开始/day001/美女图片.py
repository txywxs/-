import bs4
import os
import requests
import time

url = 'https://www.souutu.com/mnmm/mote/21751.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
rest = r"\d/(\d{1,2})"
count = 0
try:
    while True:
        url = url
        res = requests.get(url=url,headers=headers)
        bs = bs4.BeautifulSoup(res.text, 'lxml')
        bs_img = bs.find_all('img', id="showpicsouutuIs2020")  # 查询图片
        bs_page = bs.find('span', class_="mlw")
        bs_page_max = int(str(bs_page)[-9:-8])# 获取到最大页数
        # bs_page_max = int(re.findall(rest, bs_page_max)[0])
        bs_a = bs.find_all('a', class_="Nnext imgpage-right")  # 获取下一张图片的url
        bs_img_src = bs_img[0]['src']
        bs_img_alt = bs_img[0]['alt'][:6]
        bs_a_right_href = bs_a[0]['href']

        print("图片路径:", bs_img_src)
        print("图片标题:", bs_img_alt)
        print("下一张图:", bs_a_right_href)
        print("最大页数:", bs_page_max)
        print("当前页面:", bs_a_right_href)
        print()
        print()
        if not os.path.exists(bs_img_alt):
            os.mkdir('./%s' % bs_img_alt)
        with open('./%s/%s.jpg' % (bs_img_alt, count), "wb") as f:
            f.write(requests.get(bs_img_src).content)
            count += 1
        url = bs_a_right_href
        time.sleep(0.1)
except Exception as a:
    print(a)

# 本代码只供学习交流
