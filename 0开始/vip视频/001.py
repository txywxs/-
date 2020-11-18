import requests
import bs4

url = 'https://api.52wyb.com/webcloud/'
url_vip = input("请输入您要下载的vip视频")
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 ',
}
kw = {
    'v': url_vip
}
response = requests.get(url=url, headers=headers, params=kw)
print(response)
