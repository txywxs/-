import bs4
import requests
re = r'<img class="pic" *. src="(.*)" .* title="(.*)">'
url = "https://www.huya.com/g/2168"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
response = requests.get(url=url, headers=headers)
bs = bs4.BeautifulSoup(response.text, 'lxml')
tu = bs.find_all(class_='pic')
co = 0
for i in tu:
    f = requests.get(str(i['data-original']),headers=headers)
    print(str(i['data-original']))
    c = open('./虎牙颜值区/%s.jpg'%co,'wb')
    c.write(f.content)
    c.close()
    co+=1