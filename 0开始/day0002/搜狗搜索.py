import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
kw = {
    'type' : '2',
    'query': '篮球'

}
r = requests.get("https://weixin.sogou.com/weixin",headers=headers,params=kw)
r.encoding = "utf-8"
print(r.text)