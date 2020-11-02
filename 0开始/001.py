import requests
urls = "https://www.baidu.com"
re = requests.get(urls)
re = re.text
with open('./爬取的源代码/baidu.html','w',encoding='utf-8') as f:
    f.write(re)
print('源代码下载完毕')