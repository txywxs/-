import requests
from lxml import etree

url = 'https://movie.douban.com/subject/1292052/comments'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}

res = requests.get(url=url, headers=headers)

html = etree.HTML(res.text)

resp = html.xpath('//p[@class=" comment-content"]/span/text()')
for i in resp:
    print(i)
