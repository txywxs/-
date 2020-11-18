import bs4
import requests

url = "https://weixin.sogou.com/"
a = ""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
responses = requests.get(url=url,headers=headers)

soup = bs4.BeautifulSoup(responses.content.decode(),'lxml')

lists = soup.find_all('ul',class_='news-list')
for i in lists:
    a = i.find_all('h3')
for i in a:
    print(i.text,i.find_all('a')[0]['href'])
    print()