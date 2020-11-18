import json

import requests

url = 'https://fanyi.baidu.com/sug'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
kw = {
    'kw': '你好'
}
res = requests.post(url=url, data=kw,headers=header)
texts = json.loads(res.text)
k = texts.get("data")[0].get('k')
v = texts.get("data")[0].get('v')
print(k,v)

