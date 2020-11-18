import requests
import time
from lxml import etree

count = 0
while True:
    try:

        url = 'https://movie.douban.com/subject/1292052/comments?start=%s&limit=20' % count

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 '
                          'Safari/537.36 '
        }

        res = requests.get(url=url, headers=headers, proxies={"https": "http://27.155.223.209:4370"})
        html = etree.HTML(res.text)
        resp = html.xpath('//div[@class="comment"]')

        for i in resp:

            dicts = {}
            dicts['用户名'] = i.xpath(".//span[@class='comment-info']/a/text()")[0]
            dicts['点赞数'] = i.xpath(".//span[@class='votes vote-count']/text()")[0]
            dicts['评论时间'] = i.xpath(".//span[@class='comment-info']/span[@class='comment-time ']/@title")[0]
            try:
                b = i.xpath(".//span[@class='comment-info']/span[2]/@class")[0]
            except:
                b = None
            if b == 'allstar50 rating':
                dicts['评分'] = '⭐⭐⭐⭐⭐'
            elif b == 'allstar40 rating':
                dicts['评分'] = '⭐⭐⭐⭐'
            elif b == 'allstar30 rating':
                dicts['评分'] = '⭐⭐⭐'
            elif b == 'allstar20 rating':
                dicts['评分'] = '⭐⭐'
            elif b == 'allstar10 rating':
                dicts['星'] = '⭐'
            else:
                dicts['星'] = ' '
            dicts['内容'] = i.xpath(".//span[@class='short']/text()")[0]
            print(dicts)
            with open("1.txt", 'a', encoding="utf-8") as l:
                print(1)
                l.write(str(dicts) + '\n'+ '\n')
        count += 20
        print(url)
        time.sleep(0.1)
    except Exception as f:
        print(f)
