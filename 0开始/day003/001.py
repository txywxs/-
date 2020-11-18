import requests

url = "http://www.360buy.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
response = requests.get(url=url,headers=headers)

re_hi = response.history
for i in re_hi:
    print(i.url,i.headers,i.headers.get('Location'))
    print(i.text)
