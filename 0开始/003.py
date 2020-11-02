import requests
import json

word = input('输入你要搜索的东西')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 Safari/537.36 '
}
url = 'https://fanyi.baidu.com/sug'
data = {
    'kw' : word
}
re = requests.post(url=url,data=data,headers=headers)
json_data = re.json()
filName = word+'.json'
f = open('./爬取的字段/%s'%filName,'w',encoding='utf-8')
json.dump(json_data,f,ensure_ascii=False)

