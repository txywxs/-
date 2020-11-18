import requests

# http代理
ip = "27.151.78.113"
port = 	23564

proxies = {
    "http": "http://%s:%d" % (ip, port),
    "https": "http://%s:%d" % (ip, port)
}

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.183 Safari/537.36 "
}

# URL为通过百度搜索ip，响应内容中包括ip查询信息
url = "https://www.baidu.com/s?wd=ip"
# url = "https://so.com"

r = requests.get(url=url, headers=headers, proxies=proxies, timeout=5)

# print(r.text)

with open("./百度查询ip-proxy.html", "w",encoding="utf-8") as f:
    f.write(r.content.decode())
