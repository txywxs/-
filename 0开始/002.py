import requests

word = input('输入你要搜索的东西')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 Safari/537.36 '
}
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/69.0.3497.100 Safari/537.36',
url = "https://www.sogou.com/web"
param = {
    'query': word
}
html_txt = requests.get(url=url, headers=headers, params=param)
html_txt = html_txt.text
fild_name = word + '.html'
with open('./爬取的字段/%s' % fild_name, 'w', encoding='utf-8') as f:
    f.write(html_txt)
print('爬取完毕')
